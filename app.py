from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, send_file, g
import os
import sqlite3
import random
from datetime import datetime, timedelta
import io
import csv
from werkzeug.utils import secure_filename
from database import get_db, init_db, seed_db, hash_password, DB_PATH

app = Flask(__name__)
app.secret_key = 'smart-campus-complaint-secret-key-2026'

# Configure upload folder
if os.environ.get('VERCEL') == '1':
    UPLOAD_FOLDER = '/tmp/uploads'
else:
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp', 'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Ensure DB initialized on startup
if not os.path.exists(DB_PATH):
    init_db()
    seed_db()

@app.before_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        g.user = cursor.fetchone()
        db.close()

# Context processor for global helpers and stats
@app.context_processor
def inject_global_data():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM complaints WHERE status != 'Closed' AND status != 'Resolved'")
    active_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM complaints WHERE is_escalated = 1")
    escalated_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM complaints WHERE status = 'Resolved' OR status = 'Closed'")
    resolved_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM complaints")
    total_count = cursor.fetchone()[0]
    db.close()
    return {
        'now': datetime.now(),
        'system_title': 'Smart Campus Complaint System',
        'institution_name': 'Lloyd Institute of Engineering & Technology',
        'aktu_affil': 'Affiliated to Dr. A.P.J. Abdul Kalam Technical University (AKTU)',
        'global_active_count': active_count,
        'global_escalated_count': escalated_count,
        'global_resolved_count': resolved_count,
        'global_total_count': total_count
    }

# -----------------
# AUTHENTICATION
# -----------------

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Check for 1-click demo user switch
    demo_role = request.args.get('demo')
    if demo_role:
        db = get_db()
        cursor = db.cursor()
        if demo_role == 'student':
            cursor.execute("SELECT * FROM users WHERE email = 'bhaskar@lloyd.ac.in'")
        elif demo_role == 'admin':
            cursor.execute("SELECT * FROM users WHERE email = 'vishal.gupta@lloyd.ac.in'")
        elif demo_role == 'staff_elec':
            cursor.execute("SELECT * FROM users WHERE email = 'ramesh.elec@lloyd.ac.in'")
        elif demo_role == 'staff_it':
            cursor.execute("SELECT * FROM users WHERE email = 'rajesh.it@lloyd.ac.in'")
        else:
            cursor.execute("SELECT * FROM users LIMIT 1")
        
        user = cursor.fetchone()
        db.close()
        if user:
            session.clear()
            session['user_id'] = user['id']
            session['user_name'] = user['name']
            session['user_role'] = user['role']
            session['user_email'] = user['email']
            flash(f"Switched role to {user['name']} ({user['role'].title()})", "success")
            
            if user['role'] == 'admin':
                return redirect(url_for('admin_dashboard'))
            elif user['role'] == 'staff':
                return redirect(url_for('staff_dashboard'))
            else:
                return redirect(url_for('user_dashboard'))

    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')

        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE LOWER(email) = ?", (email,))
        user = cursor.fetchone()
        db.close()

        if user and user['password_hash'] == hash_password(password):
            session.clear()
            session['user_id'] = user['id']
            session['user_name'] = user['name']
            session['user_role'] = user['role']
            session['user_email'] = user['email']
            flash(f"Welcome back, {user['name']}!", "success")

            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            if user['role'] == 'admin':
                return redirect(url_for('admin_dashboard'))
            elif user['role'] == 'staff':
                return redirect(url_for('staff_dashboard'))
            return redirect(url_for('user_dashboard'))
        else:
            flash("Invalid email or password. You can also use the 1-click Demo buttons below.", "danger")

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        role = request.form.get('role', 'student')
        roll_no = request.form.get('roll_no', '').strip()
        department = request.form.get('department', '').strip()
        phone = request.form.get('phone', '').strip()

        if not name or not email or not password:
            flash("Please fill in all required fields.", "warning")
            return render_template('register.html')

        db = get_db()
        cursor = db.cursor()
        try:
            cursor.execute("""
            INSERT INTO users (name, email, password_hash, role, roll_no, department, phone)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (name, email, hash_password(password), role, roll_no, department, phone))
            db.commit()
            new_id = cursor.lastrowid
            session.clear()
            session['user_id'] = new_id
            session['user_name'] = name
            session['user_role'] = role
            session['user_email'] = email
            db.close()
            flash("Registration successful! Welcome to the Smart Campus Complaint Portal.", "success")
            return redirect(url_for('user_dashboard'))
        except sqlite3.IntegrityError:
            db.close()
            flash("An account with that email already exists. Please login instead.", "danger")

    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    flash("You have been securely logged out.", "info")
    return redirect(url_for('index'))

# -----------------
# PUBLIC PAGES & HOME
# -----------------

@app.route('/')
def index():
    db = get_db()
    cursor = db.cursor()
    # Recent resolved complaints for transparency
    cursor.execute("""
    SELECT c.*, d.name as dept_name, f.rating, f.comment as feedback_comment
    FROM complaints c
    LEFT JOIN departments d ON c.assigned_dept_id = d.id
    LEFT JOIN feedback f ON c.ticket_id = f.ticket_id
    ORDER BY c.created_at DESC LIMIT 6
    """)
    recent_complaints = cursor.fetchall()

    # Active building issues count for Campus Map preview
    cursor.execute("""
    SELECT building_block, COUNT(*) as count, 
           SUM(CASE WHEN priority = 'Critical' THEN 1 ELSE 0 END) as critical_count
    FROM complaints
    WHERE status != 'Closed' AND status != 'Resolved'
    GROUP BY building_block
    """)
    building_stats = {row['building_block']: {'count': row['count'], 'critical': row['critical_count']} for row in cursor.fetchall()}

    db.close()
    return render_template('index.html', recent_complaints=recent_complaints, building_stats=building_stats)

# -----------------
# COMPLAINT SUBMISSION & DUPLICATE DETECTION
# -----------------

@app.route('/submit', methods=['GET', 'POST'])
def submit_complaint():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM departments ORDER BY name ASC")
    departments = cursor.fetchall()

    if request.method == 'POST':
        user_name = request.form.get('user_name', '').strip()
        user_email = request.form.get('user_email', '').strip()
        user_roll = request.form.get('user_roll', '').strip()
        category = request.form.get('category', '').strip()
        subcategory = request.form.get('subcategory', '').strip()
        building_block = request.form.get('building_block', '').strip()
        room_location = request.form.get('room_location', '').strip()
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        priority = request.form.get('priority', 'Medium').capitalize()

        if not title or not description or not category or not building_block:
            flash("Please fill in all required complaint details.", "warning")
            db.close()
            return render_template('submit_complaint.html', departments=departments)

        # Handle image upload
        image_path = None
        if 'image' in request.files:
            file = request.files['image']
            if file and file.filename != '' and allowed_file(file.filename):
                filename = secure_filename(f"{int(datetime.now().timestamp())}_{file.filename}")
                file_dest = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_dest)
                image_path = f"uploads/{filename}"

        # Generate unique Ticket ID: LIET-2026-XXXX
        random_suffix = random.randint(1010, 9999)
        ticket_id = f"LIET-2026-{random_suffix}"

        # Calculate SLA deadline based on priority
        now = datetime.now()
        sla_hours = 24
        if priority == 'Critical':
            sla_hours = 4
        elif priority == 'High':
            sla_hours = 8
        elif priority == 'Low':
            sla_hours = 48
        sla_deadline = (now + timedelta(hours=sla_hours)).strftime("%Y-%m-%d %H:%M:%S")

        # Auto-match department based on category
        dept_mapping = {
            'Electricity & Lighting': 'ELEC',
            'Internet & WiFi': 'ITNET',
            'Cleanliness & Sanitation': 'HOUSE',
            'Civil & Infrastructure': 'CIVIL',
            'Water Supply': 'PLUMB',
            'Hostel Administration': 'HOSTEL',
            'Security & Safety': 'SEC',
            'Library Facilities': 'LIB'
        }
        dept_code = dept_mapping.get(category)
        assigned_dept_id = None
        if dept_code:
            cursor.execute("SELECT id FROM departments WHERE code = ?", (dept_code,))
            res = cursor.fetchone()
            if res:
                assigned_dept_id = res['id']

        user_id = session.get('user_id')

        cursor.execute("""
        INSERT INTO complaints (
            ticket_id, user_id, user_name, user_email, user_roll,
            category, subcategory, building_block, room_location,
            title, description, priority, status, assigned_dept_id,
            image_path, sla_deadline, created_at, updated_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'Submitted', ?, ?, ?, ?, ?)
        """, (
            ticket_id, user_id, user_name, user_email, user_roll,
            category, subcategory, building_block, room_location,
            title, description, priority, assigned_dept_id,
            image_path, sla_deadline, now.strftime("%Y-%m-%d %H:%M:%S"), now.strftime("%Y-%m-%d %H:%M:%S")
        ))

        # Add initial audit log
        cursor.execute("""
        INSERT INTO complaint_logs (ticket_id, action, performed_by, role, notes, created_at)
        VALUES (?, 'Submitted', ?, ?, 'Complaint registered in the system with SLA target.', ?)
        """, (ticket_id, user_name or 'Complainant', 'Student' if user_roll else 'User', now.strftime("%Y-%m-%d %H:%M:%S")))

        db.commit()
        db.close()

        flash(f"Complaint registered successfully! Your Ticket ID is {ticket_id}", "success")
        return redirect(url_for('track_complaint', ticket_id=ticket_id))

    # Pre-populate if query params provided (e.g., from QR scan or Campus Map)
    prefill = {
        'building': request.args.get('building', ''),
        'room': request.args.get('room', ''),
        'category': request.args.get('category', ''),
        'priority': request.args.get('priority', 'Medium'),
        'title': request.args.get('title', '')
    }
    db.close()
    return render_template('submit_complaint.html', departments=departments, prefill=prefill)

@app.route('/api/check-duplicates', methods=['POST'])
def check_duplicates():
    """Smart Duplicate Detection endpoint: flags active complaints in same building or with similar title"""
    data = request.get_json() or {}
    building = data.get('building_block', '').strip()
    category = data.get('category', '').strip()
    title = data.get('title', '').strip().lower()

    if not building or not category:
        return jsonify({'duplicates': []})

    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
    SELECT ticket_id, title, category, building_block, room_location, status, priority, created_at, upvotes
    FROM complaints
    WHERE building_block = ? AND category = ? AND status NOT IN ('Resolved', 'Closed')
    LIMIT 5
    """, (building, category))
    rows = cursor.fetchall()
    db.close()

    duplicates = []
    keywords = set([w for w in title.split() if len(w) > 3])
    for row in rows:
        match_score = 50  # same building & category
        row_title_words = set(row['title'].lower().split())
        common = keywords.intersection(row_title_words)
        if common:
            match_score += 35
        
        duplicates.append({
            'ticket_id': row['ticket_id'],
            'title': row['title'],
            'status': row['status'],
            'priority': row['priority'],
            'room': row['room_location'],
            'upvotes': row['upvotes'],
            'confidence': min(match_score, 95)
        })

    # Sort by match confidence descending
    duplicates.sort(key=lambda x: x['confidence'], reverse=True)
    return jsonify({'duplicates': duplicates})

@app.route('/api/upvote/<ticket_id>', methods=['POST'])
def upvote_complaint(ticket_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE complaints SET upvotes = upvotes + 1 WHERE ticket_id = ?", (ticket_id,))
    cursor.execute("SELECT upvotes FROM complaints WHERE ticket_id = ?", (ticket_id,))
    res = cursor.fetchone()
    db.commit()
    db.close()
    if res:
        return jsonify({'success': True, 'upvotes': res['upvotes']})
    return jsonify({'success': False, 'message': 'Ticket not found'}), 404

# -----------------
# TRACKING & AUDIT TRAIL
# -----------------

@app.route('/track')
def track_index():
    ticket_id = request.args.get('ticket_id', '').strip()
    if ticket_id:
        return redirect(url_for('track_complaint', ticket_id=ticket_id))
    return render_template('track.html', ticket=None)

@app.route('/track/<ticket_id>')
def track_complaint(ticket_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
    SELECT c.*, d.name as dept_name, d.head_name as dept_head, d.head_email as dept_email,
           f.rating as feedback_rating, f.comment as feedback_comment, f.created_at as feedback_time
    FROM complaints c
    LEFT JOIN departments d ON c.assigned_dept_id = d.id
    LEFT JOIN feedback f ON c.ticket_id = f.ticket_id
    WHERE c.ticket_id = ?
    """, (ticket_id,))
    ticket = cursor.fetchone()

    if not ticket:
        db.close()
        flash(f"No complaint found with ticket ID '{ticket_id}'. Please check the number and try again.", "warning")
        return render_template('track.html', ticket=None, search_id=ticket_id)

    cursor.execute("""
    SELECT * FROM complaint_logs
    WHERE ticket_id = ?
    ORDER BY created_at ASC
    """, (ticket_id,))
    logs = cursor.fetchall()
    db.close()

    return render_template('track.html', ticket=ticket, logs=logs)

# -----------------
# USER DASHBOARD
# -----------------

@app.route('/dashboard')
def user_dashboard():
    if not g.user:
        flash("Please log in to view your dashboard.", "info")
        return redirect(url_for('login', next=request.path))

    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
    SELECT c.*, d.name as dept_name, f.rating as feedback_rating
    FROM complaints c
    LEFT JOIN departments d ON c.assigned_dept_id = d.id
    LEFT JOIN feedback f ON c.ticket_id = f.ticket_id
    WHERE c.user_id = ? OR c.user_email = ?
    ORDER BY c.created_at DESC
    """, (g.user['id'], g.user['email']))
    user_complaints = cursor.fetchall()

    # User personal statistics
    cursor.execute("""
    SELECT 
        COUNT(*) as total,
        SUM(CASE WHEN status IN ('Submitted', 'Assigned', 'In Progress') THEN 1 ELSE 0 END) as active,
        SUM(CASE WHEN status IN ('Resolved', 'Closed') THEN 1 ELSE 0 END) as resolved,
        SUM(CASE WHEN is_escalated = 1 THEN 1 ELSE 0 END) as escalated
    FROM complaints
    WHERE user_id = ? OR user_email = ?
    """, (g.user['id'], g.user['email']))
    stats = cursor.fetchone()

    db.close()
    return render_template('user_dashboard.html', complaints=user_complaints, stats=stats)

# -----------------
# ADMIN DASHBOARD
# -----------------

@app.route('/admin')
def admin_dashboard():
    # Allow admins, or provide demo override
    if not g.user or g.user['role'] != 'admin':
        flash("You are previewing the Admin Console. Use the Quick Switcher above to act as Prof. Vishal Gupta.", "warning")

    db = get_db()
    cursor = db.cursor()

    # Filters
    status_filter = request.args.get('status', '')
    category_filter = request.args.get('category', '')
    priority_filter = request.args.get('priority', '')
    search_q = request.args.get('q', '').strip()

    query = """
    SELECT c.*, d.name as dept_name, d.code as dept_code, f.rating as feedback_rating
    FROM complaints c
    LEFT JOIN departments d ON c.assigned_dept_id = d.id
    LEFT JOIN feedback f ON c.ticket_id = f.ticket_id
    WHERE 1=1
    """
    params = []
    if status_filter:
        query += " AND c.status = ?"
        params.append(status_filter)
    if category_filter:
        query += " AND c.category = ?"
        params.append(category_filter)
    if priority_filter:
        query += " AND c.priority = ?"
        params.append(priority_filter)
    if search_q:
        query += " AND (c.ticket_id LIKE ? OR c.title LIKE ? OR c.user_name LIKE ? OR c.building_block LIKE ?)"
        wild = f"%{search_q}%"
        params.extend([wild, wild, wild, wild])

    query += " ORDER BY CASE WHEN c.priority = 'Critical' THEN 1 WHEN c.priority = 'High' THEN 2 ELSE 3 END, c.created_at DESC"
    cursor.execute(query, params)
    all_complaints = cursor.fetchall()

    # Admin KPI stats
    cursor.execute("""
    SELECT 
        COUNT(*) as total,
        SUM(CASE WHEN status = 'Submitted' THEN 1 ELSE 0 END) as pending_assignment,
        SUM(CASE WHEN status = 'Assigned' THEN 1 ELSE 0 END) as assigned,
        SUM(CASE WHEN status = 'In Progress' THEN 1 ELSE 0 END) as in_progress,
        SUM(CASE WHEN status = 'Resolved' THEN 1 ELSE 0 END) as resolved,
        SUM(CASE WHEN status = 'Closed' THEN 1 ELSE 0 END) as closed,
        SUM(CASE WHEN is_escalated = 1 THEN 1 ELSE 0 END) as escalated
    FROM complaints
    """)
    kpis = cursor.fetchone()

    cursor.execute("SELECT * FROM departments ORDER BY name ASC")
    departments = cursor.fetchall()

    # Maintenance Staff list for assignment modal
    cursor.execute("SELECT * FROM users WHERE role = 'staff'")
    staff_members = cursor.fetchall()

    db.close()
    return render_template(
        'admin_dashboard.html',
        complaints=all_complaints,
        kpis=kpis,
        departments=departments,
        staff_members=staff_members,
        filters={'status': status_filter, 'category': category_filter, 'priority': priority_filter, 'q': search_q}
    )

@app.route('/admin/assign', methods=['POST'])
def admin_assign():
    ticket_id = request.form.get('ticket_id')
    dept_id = request.form.get('department_id')
    staff_name = request.form.get('staff_name', '').strip()
    priority = request.form.get('priority')
    admin_notes = request.form.get('notes', 'Assigned by Administrator')

    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
    UPDATE complaints
    SET assigned_dept_id = ?, assigned_staff_name = ?, priority = ?, status = 'Assigned', updated_at = ?
    WHERE ticket_id = ?
    """, (dept_id, staff_name, priority, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ticket_id))

    actor = g.user['name'] if g.user else 'Prof. Vishal Gupta (Admin)'
    cursor.execute("""
    INSERT INTO complaint_logs (ticket_id, action, performed_by, role, notes, created_at)
    VALUES (?, 'Assigned', ?, 'Admin', ?, ?)
    """, (ticket_id, actor, f"Assigned to {staff_name}. Notes: {admin_notes}", datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    db.commit()
    db.close()
    flash(f"Ticket {ticket_id} successfully assigned to {staff_name}!", "success")
    return redirect(request.referrer or url_for('admin_dashboard'))

@app.route('/admin/escalate/<ticket_id>', methods=['POST'])
def admin_escalate(ticket_id):
    escalate_to = request.form.get('escalate_to', 'Prof. Vishal Gupta (Chief Proctor / HOD CSE)')
    notes = request.form.get('notes', 'Escalated due to SLA threshold breach')

    db = get_db()
    cursor = db.cursor()
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    UPDATE complaints
    SET is_escalated = 1, escalated_to = ?, escalated_at = ?, priority = 'Critical', updated_at = ?
    WHERE ticket_id = ?
    """, (escalate_to, now_str, now_str, ticket_id))

    actor = g.user['name'] if g.user else 'System / Admin'
    cursor.execute("""
    INSERT INTO complaint_logs (ticket_id, action, performed_by, role, notes, created_at)
    VALUES (?, 'Escalated', ?, 'Admin', ?, ?)
    """, (ticket_id, actor, f"Ticket Escalated to {escalate_to}. Reason: {notes}", now_str))

    db.commit()
    db.close()
    flash(f"Ticket {ticket_id} escalated to {escalate_to}.", "danger")
    return redirect(request.referrer or url_for('admin_dashboard'))

@app.route('/admin/close/<ticket_id>', methods=['POST'])
def admin_close(ticket_id):
    db = get_db()
    cursor = db.cursor()
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    UPDATE complaints
    SET status = 'Closed', updated_at = ?
    WHERE ticket_id = ?
    """, (now_str, ticket_id))

    actor = g.user['name'] if g.user else 'Prof. Vishal Gupta (Admin)'
    cursor.execute("""
    INSERT INTO complaint_logs (ticket_id, action, performed_by, role, notes, created_at)
    VALUES (?, 'Closed', ?, 'Admin', 'Ticket verified by administration and closed.', ?)
    """, (ticket_id, actor, now_str))

    db.commit()
    db.close()
    flash(f"Ticket {ticket_id} verified and officially closed.", "success")
    return redirect(request.referrer or url_for('admin_dashboard'))

# -----------------
# STAFF / TECHNICIAN DASHBOARD
# -----------------

@app.route('/staff')
def staff_dashboard():
    if not g.user or g.user['role'] not in ('staff', 'admin'):
        flash("Previewing Staff / Maintenance Dashboard. Click below to act as Senior Electrician Ramesh or IT Admin Rajesh.", "info")

    staff_name = g.user['name'] if g.user and g.user['role'] == 'staff' else None

    db = get_db()
    cursor = db.cursor()

    if staff_name:
        cursor.execute("""
        SELECT c.*, d.name as dept_name
        FROM complaints c
        LEFT JOIN departments d ON c.assigned_dept_id = d.id
        WHERE c.assigned_staff_name LIKE ?
        ORDER BY CASE WHEN c.priority = 'Critical' THEN 1 ELSE 2 END, c.created_at DESC
        """, (f"%{staff_name.split()[0]}%",))
    else:
        cursor.execute("""
        SELECT c.*, d.name as dept_name
        FROM complaints c
        LEFT JOIN departments d ON c.assigned_dept_id = d.id
        WHERE c.status IN ('Assigned', 'In Progress', 'Resolved')
        ORDER BY c.created_at DESC
        """)

    assigned_tasks = cursor.fetchall()
    db.close()
    return render_template('staff_dashboard.html', tasks=assigned_tasks, staff_name=staff_name)

@app.route('/staff/update-status', methods=['POST'])
def staff_update_status():
    ticket_id = request.form.get('ticket_id')
    new_status = request.form.get('status')
    remarks = request.form.get('remarks', '').strip()

    if not ticket_id or new_status not in ('In Progress', 'Resolved'):
        flash("Invalid status update requested.", "warning")
        return redirect(url_for('staff_dashboard'))

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db = get_db()
    cursor = db.cursor()

    if new_status == 'Resolved':
        cursor.execute("""
        UPDATE complaints
        SET status = 'Resolved', resolution_remarks = ?, updated_at = ?
        WHERE ticket_id = ?
        """, (remarks, now_str, ticket_id))
    else:
        cursor.execute("""
        UPDATE complaints
        SET status = 'In Progress', updated_at = ?
        WHERE ticket_id = ?
        """, (now_str, ticket_id))

    staff_name = g.user['name'] if g.user else 'Maintenance Technician'
    cursor.execute("""
    INSERT INTO complaint_logs (ticket_id, action, performed_by, role, notes, created_at)
    VALUES (?, ?, ?, 'Staff', ?, ?)
    """, (ticket_id, new_status, staff_name, remarks or f"Status changed to {new_status}", now_str))

    db.commit()
    db.close()
    flash(f"Ticket {ticket_id} updated to '{new_status}' successfully!", "success")
    return redirect(request.referrer or url_for('staff_dashboard'))

# -----------------
# FEEDBACK & RATING
# -----------------

@app.route('/feedback/submit', methods=['POST'])
def submit_feedback():
    ticket_id = request.form.get('ticket_id')
    rating = int(request.form.get('rating', 5))
    comment = request.form.get('comment', '').strip()
    user_id = session.get('user_id') or 2

    db = get_db()
    cursor = db.cursor()
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        cursor.execute("""
        INSERT INTO feedback (ticket_id, user_id, rating, comment, created_at)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(ticket_id) DO UPDATE SET rating = excluded.rating, comment = excluded.comment
        """, (ticket_id, user_id, rating, comment, now_str))

        cursor.execute("""
        INSERT INTO complaint_logs (ticket_id, action, performed_by, role, notes, created_at)
        VALUES (?, 'Feedback Submitted', ?, 'Student', ?, ?)
        """, (ticket_id, g.user['name'] if g.user else 'Student', f"Submitted {rating}-star rating: {comment}", now_str))

        db.commit()
        flash("Thank you for your valuable feedback! It helps improve campus facilities.", "success")
    except Exception as e:
        flash(f"Error saving feedback: {str(e)}", "danger")

    db.close()
    return redirect(url_for('track_complaint', ticket_id=ticket_id))

# -----------------
# ANALYTICS
# -----------------

@app.route('/analytics')
def analytics():
    db = get_db()
    cursor = db.cursor()

    # 1. By Category
    cursor.execute("""
    SELECT category, COUNT(*) as count
    FROM complaints
    GROUP BY category
    ORDER BY count DESC
    """)
    cat_rows = cursor.fetchall()
    categories_data = [{'category': r['category'], 'count': r['count']} for r in cat_rows]

    # 2. By Status
    cursor.execute("""
    SELECT status, COUNT(*) as count
    FROM complaints
    GROUP BY status
    """)
    status_rows = cursor.fetchall()
    status_data = {r['status']: r['count'] for r in status_rows}

    # 3. By Building Block
    cursor.execute("""
    SELECT building_block, COUNT(*) as count
    FROM complaints
    GROUP BY building_block
    ORDER BY count DESC
    """)
    building_rows = cursor.fetchall()
    building_data = [{'building': r['building_block'], 'count': r['count']} for r in building_rows]

    # 4. Department Performance & SLA compliance
    cursor.execute("""
    SELECT d.name, d.code, d.sla_hours,
           COUNT(c.ticket_id) as total_tickets,
           SUM(CASE WHEN c.status IN ('Resolved', 'Closed') THEN 1 ELSE 0 END) as resolved_tickets,
           SUM(CASE WHEN c.is_escalated = 1 THEN 1 ELSE 0 END) as escalated_tickets,
           AVG(f.rating) as avg_rating
    FROM departments d
    LEFT JOIN complaints c ON d.id = c.assigned_dept_id
    LEFT JOIN feedback f ON c.ticket_id = f.ticket_id
    GROUP BY d.id
    ORDER BY total_tickets DESC
    """)
    dept_performance = cursor.fetchall()

    # 5. Average resolution time calculation (simulated/actual in hours)
    db.close()
    return render_template(
        'analytics.html',
        categories_data=categories_data,
        status_data=status_data,
        building_data=building_data,
        dept_performance=dept_performance
    )

# -----------------
# INTERACTIVE SIMULATION & DIGITAL TWIN
# -----------------

@app.route('/simulation')
def simulation_view():
    db = get_db()
    cursor = db.cursor()

    # IoT Sensors
    cursor.execute("SELECT * FROM iot_sensors ORDER BY status DESC, name ASC")
    sensors = cursor.fetchall()

    # Active complaints for map pins
    cursor.execute("""
    SELECT ticket_id, title, category, building_block, room_location, priority, status, is_escalated
    FROM complaints
    WHERE status NOT IN ('Closed')
    ORDER BY CASE WHEN priority = 'Critical' THEN 1 ELSE 2 END
    """)
    active_complaints = cursor.fetchall()

    db.close()
    return render_template('simulation.html', sensors=sensors, active_complaints=active_complaints)

@app.route('/api/simulation/trigger-iot', methods=['POST'])
def simulation_trigger_iot():
    data = request.get_json() or {}
    sensor_id = data.get('sensor_id')

    db = get_db()
    cursor = db.cursor()

    if sensor_id:
        cursor.execute("SELECT * FROM iot_sensors WHERE sensor_id = ?", (sensor_id,))
        sensor = cursor.fetchone()
    else:
        cursor.execute("SELECT * FROM iot_sensors WHERE status != 'Normal' ORDER BY RANDOM() LIMIT 1")
        sensor = cursor.fetchone()

    if not sensor:
        cursor.execute("SELECT * FROM iot_sensors ORDER BY RANDOM() LIMIT 1")
        sensor = cursor.fetchone()

    # Generate an automated ticket for this IoT anomaly
    ticket_id = f"LIET-2026-{random.randint(6000, 8999)}"
    now = datetime.now()
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")
    deadline = (now + timedelta(hours=4)).strftime("%Y-%m-%d %H:%M:%S")

    # Determine dept
    dept_code = 'ELEC'
    if 'Water' in sensor['type']:
        dept_code = 'PLUMB'
    elif 'WiFi' in sensor['type'] or 'Network' in sensor['type']:
        dept_code = 'ITNET'
    elif 'Smoke' in sensor['type'] or 'Fire' in sensor['type']:
        dept_code = 'SEC'

    cursor.execute("SELECT id FROM departments WHERE code = ?", (dept_code,))
    dept = cursor.fetchone()
    dept_id = dept['id'] if dept else 1

    cursor.execute("""
    INSERT INTO complaints (
        ticket_id, user_id, user_name, user_email, user_roll,
        category, subcategory, building_block, room_location,
        title, description, priority, status, assigned_dept_id,
        sla_deadline, created_at, updated_at
    ) VALUES (?, 1, 'Campus IoT Telemetry System', 'iot.sensors@lloyd.ac.in', 'AI-IOT-DAEMON',
        ?, 'Automated Telemetry Incident', ?, ?,
        ?, ?, 'Critical', 'Assigned', ?,
        ?, ?, ?)
    """, (
        ticket_id, sensor['type'], sensor['building_block'], sensor['location'],
        f"[IoT Alert] Automated Fault: {sensor['name']}",
        f"Real-time sensor telemetry anomaly detected: {sensor['last_reading']}. Auto-dispatching emergency response crew.",
        dept_id, deadline, now_str, now_str
    ))

    cursor.execute("""
    INSERT INTO complaint_logs (ticket_id, action, performed_by, role, notes, created_at)
    VALUES (?, 'Automated Telemetry Ingestion', 'Campus IoT Telemetry Engine', 'System', ?, ?)
    """, (ticket_id, f"Threshold breach: {sensor['last_reading']}. Ticket auto-generated and dispatched.", now_str))

    db.commit()
    db.close()

    return jsonify({
        'success': True,
        'ticket_id': ticket_id,
        'sensor': dict(sensor),
        'message': f"Telemetry incident logged! Ticket {ticket_id} created with Critical SLA."
    })

@app.route('/api/simulation/auto-escalate', methods=['POST'])
def simulation_auto_escalate():
    """Runs automated SLA check and escalates tickets that breach resolution window"""
    db = get_db()
    cursor = db.cursor()

    # Find candidate ticket for escalation
    cursor.execute("""
    SELECT * FROM complaints
    WHERE status IN ('Submitted', 'Assigned', 'In Progress') AND is_escalated = 0
    ORDER BY created_at ASC LIMIT 1
    """)
    ticket = cursor.fetchone()

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if ticket:
        ticket_id = ticket['ticket_id']
        cursor.execute("""
        UPDATE complaints
        SET is_escalated = 1, escalated_to = 'Prof. Vishal Gupta (Chief Proctor / HOD CSE)',
            priority = 'Critical', updated_at = ?
        WHERE ticket_id = ?
        """, (now_str, ticket_id))

        cursor.execute("""
        INSERT INTO complaint_logs (ticket_id, action, performed_by, role, notes, created_at)
        VALUES (?, 'Auto-Escalated', 'Smart Campus SLA Engine', 'System', 'SLA threshold reached. Auto-escalated to Dean / Chief Proctor.', ?)
        """, (ticket_id, now_str))
        db.commit()
        db.close()
        return jsonify({
            'success': True,
            'ticket_id': ticket_id,
            'title': ticket['title'],
            'escalated_to': 'Prof. Vishal Gupta (Chief Proctor / HOD CSE)',
            'message': f"Ticket {ticket_id} automatically escalated to Dean/Chief Proctor."
        })
    else:
        db.close()
        return jsonify({
            'success': False,
            'message': "All active tickets are within current SLA windows or already escalated!"
        })

@app.route('/api/simulation/resolve-demo', methods=['POST'])
def simulation_resolve_demo():
    """Simulates technician field dispatch, progress update, and resolution with remarks"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
    SELECT c.*, d.name as dept_name
    FROM complaints c
    LEFT JOIN departments d ON c.assigned_dept_id = d.id
    WHERE c.status IN ('Submitted', 'Assigned', 'In Progress')
    ORDER BY c.created_at ASC LIMIT 1
    """)
    ticket = cursor.fetchone()

    if not ticket:
        db.close()
        return jsonify({'success': False, 'message': 'No open tickets available to resolve.'})

    ticket_id = ticket['ticket_id']
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sample_resolutions = [
        "Technician replaced the burned capacitor and restored primary power lines. Tested with digital multimeter.",
        "Network switch rebooted and Cat6 patch cord re-terminated. Wi-Fi signal verified at 866 Mbps.",
        "Plumbing gasket replaced and water pressure calibrated. Zero leakage observed.",
        "Sanitation crew completed deep cleaning, disinfection, and trash disposal.",
        "Carpentry work completed. Replaced cracked bench plank with polished hardwood."
    ]
    resolution_text = random.choice(sample_resolutions)

    cursor.execute("""
    UPDATE complaints
    SET status = 'Resolved', resolution_remarks = ?, updated_at = ?
    WHERE ticket_id = ?
    """, (resolution_text, now_str, ticket_id))

    cursor.execute("""
    INSERT INTO complaint_logs (ticket_id, action, performed_by, role, notes, created_at)
    VALUES (?, 'Resolved', 'Field Technician (Simulated)', 'Staff', ?, ?)
    """, (ticket_id, resolution_text, now_str))

    db.commit()
    db.close()

    return jsonify({
        'success': True,
        'ticket_id': ticket_id,
        'title': ticket['title'],
        'remarks': resolution_text,
        'message': f"Ticket {ticket_id} has been marked Resolved by the field technician."
    })

# -----------------
# QR CODE SCANNER SIMULATOR
# -----------------

@app.route('/qr-scanner')
def qr_scanner():
    # Predefined campus QR facility plaques for quick testing
    qr_presets = [
        {
            'code': 'LIET-QR-BLKB-304',
            'building': 'Block B - CS Labs',
            'room': 'Room 304 - High Performance Lab',
            'category': 'Internet & WiFi',
            'suggested_title': 'Wi-Fi Access Point connectivity issue in Lab 304'
        },
        {
            'code': 'LIET-QR-BLKA-204',
            'building': 'Block A - Academic',
            'room': 'Room 204 - Lecture Hall',
            'category': 'Electricity & Lighting',
            'suggested_title': 'Projector display flickering / Power socket dead in Room 204'
        },
        {
            'code': 'LIET-QR-HSTL-WASH2',
            'building': 'Boys Hostel 1',
            'room': '2nd Floor Common Washroom',
            'category': 'Water Supply',
            'suggested_title': 'Water tap valve dripping / Basin leakage in 2nd floor'
        },
        {
            'code': 'LIET-QR-LIB-DIGI',
            'building': 'Central Library',
            'room': '1st Floor Digital Reading Section',
            'category': 'Library Facilities',
            'suggested_title': 'AC cooling failure / digital section lighting issue'
        },
        {
            'code': 'LIET-QR-CAFE-FC',
            'building': 'Student Cafeteria',
            'room': 'Ground Floor Food Court',
            'category': 'Cleanliness & Sanitation',
            'suggested_title': 'Spill cleanup / waste bin clearance required'
        }
    ]
    return render_template('qr_scanner.html', qr_presets=qr_presets)

# -----------------
# DATA EXPORT & PRINTABLE RECEIPT
# -----------------

@app.route('/export/csv')
def export_csv():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
    SELECT c.ticket_id, c.user_name, c.user_email, c.user_roll, c.category, c.subcategory,
           c.building_block, c.room_location, c.title, c.priority, c.status,
           d.name as department_name, c.assigned_staff_name, c.is_escalated,
           c.created_at, c.updated_at, c.resolution_remarks, f.rating as feedback_rating
    FROM complaints c
    LEFT JOIN departments d ON c.assigned_dept_id = d.id
    LEFT JOIN feedback f ON c.ticket_id = f.ticket_id
    ORDER BY c.created_at DESC
    """)
    rows = cursor.fetchall()
    db.close()

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow([
        'Ticket ID', 'Complainant Name', 'Email', 'Roll / ID', 'Category', 'Subcategory',
        'Campus Building', 'Room/Location', 'Title', 'Priority', 'Status',
        'Assigned Department', 'Staff Assigned', 'Is Escalated', 'Created At', 'Updated At',
        'Resolution Remarks', 'Student Rating (1-5)'
    ])

    for r in rows:
        writer.writerow([
            r['ticket_id'], r['user_name'], r['user_email'], r['user_roll'], r['category'], r['subcategory'] or '',
            r['building_block'], r['room_location'], r['title'], r['priority'], r['status'],
            r['department_name'] or 'Unassigned', r['assigned_staff_name'] or '', 'Yes' if r['is_escalated'] else 'No',
            r['created_at'], r['updated_at'], r['resolution_remarks'] or '', r['feedback_rating'] or 'Not Rated'
        ])

    output.seek(0)
    filename = f"LIET_Campus_Complaints_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    return send_file(
        io.BytesIO(output.getvalue().encode('utf-8')),
        mimetype='text/csv',
        as_attachment=True,
        download_name=filename
    )

@app.route('/print-slip/<ticket_id>')
def print_slip(ticket_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
    SELECT c.*, d.name as dept_name, d.head_name as dept_head
    FROM complaints c
    LEFT JOIN departments d ON c.assigned_dept_id = d.id
    WHERE c.ticket_id = ?
    """, (ticket_id,))
    ticket = cursor.fetchone()
    if not ticket:
        db.close()
        flash("Ticket not found for print slip.", "danger")
        return redirect(url_for('track_index'))

    cursor.execute("SELECT * FROM complaint_logs WHERE ticket_id = ? ORDER BY created_at ASC", (ticket_id,))
    logs = cursor.fetchall()
    db.close()

    return render_template('print_slip.html', ticket=ticket, logs=logs)

if __name__ == '__main__':
    print("Starting Smart Campus Complaint System on http://127.0.0.1:5000")
    app.run(host='127.0.0.1', port=5000, debug=False)
