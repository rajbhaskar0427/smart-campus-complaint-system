import sqlite3
import os
from datetime import datetime, timedelta
import hashlib

DB_PATH = os.path.join(os.path.dirname(__file__), 'campus_complaints.db')

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()

    # Users Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        role TEXT NOT NULL DEFAULT 'student',
        roll_no TEXT,
        department TEXT,
        phone TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Departments Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS departments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        code TEXT UNIQUE NOT NULL,
        head_name TEXT,
        head_email TEXT,
        sla_hours INTEGER DEFAULT 24,
        icon TEXT
    )
    """)

    # Complaints Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS complaints (
        ticket_id TEXT PRIMARY KEY,
        user_id INTEGER,
        user_name TEXT,
        user_email TEXT,
        user_roll TEXT,
        category TEXT NOT NULL,
        subcategory TEXT,
        building_block TEXT NOT NULL,
        room_location TEXT NOT NULL,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        priority TEXT NOT NULL DEFAULT 'Medium',
        status TEXT NOT NULL DEFAULT 'Submitted',
        assigned_dept_id INTEGER,
        assigned_staff_name TEXT,
        image_path TEXT,
        resolution_remarks TEXT,
        resolution_image TEXT,
        sla_deadline TEXT,
        is_escalated INTEGER DEFAULT 0,
        escalated_to TEXT,
        escalated_at TEXT,
        upvotes INTEGER DEFAULT 0,
        created_at TEXT,
        updated_at TEXT,
        FOREIGN KEY (user_id) REFERENCES users (id),
        FOREIGN KEY (assigned_dept_id) REFERENCES departments (id)
    )
    """)

    # Audit Trail / Complaint Logs
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS complaint_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ticket_id TEXT NOT NULL,
        action TEXT NOT NULL,
        performed_by TEXT NOT NULL,
        role TEXT NOT NULL,
        notes TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (ticket_id) REFERENCES complaints (ticket_id)
    )
    """)

    # Feedback / Rating Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ticket_id TEXT UNIQUE NOT NULL,
        user_id INTEGER NOT NULL,
        rating INTEGER NOT NULL,
        comment TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (ticket_id) REFERENCES complaints (ticket_id),
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    """)

    # Campus IoT Sensors for Simulation
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS iot_sensors (
        sensor_id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        building_block TEXT NOT NULL,
        location TEXT NOT NULL,
        type TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'Normal',
        last_reading TEXT,
        last_checked TEXT
    )
    """)

    conn.commit()
    conn.close()

def seed_db():
    conn = get_db()
    cursor = conn.cursor()

    # Check if data exists
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] > 0:
        conn.close()
        return

    # 1. Seed Users (Students, Faculty, Staff, Admin)
    # Default password for all demo accounts: 'admin123' or 'student123'
    pw_admin = hash_password('admin123')
    pw_student = hash_password('student123')
    pw_staff = hash_password('staff123')

    users_data = [
        # Admin / Supervisor from Synopsis
        ('Prof. Vishal Gupta', 'vishal.gupta@lloyd.ac.in', pw_admin, 'admin', 'EMP-CSE-104', 'Computer Science & Engineering', '+91 98765 43210'),
        # Student Author from Synopsis
        ('Bhaskar Raj', 'bhaskar@lloyd.ac.in', pw_student, 'student', '2501530100041', 'Computer Science & Engineering (2A)', '+91 91234 56780'),
        # Maintenance Staff
        ('Rajesh Kumar (Network Admin)', 'rajesh.it@lloyd.ac.in', pw_staff, 'staff', 'EMP-IT-008', 'IT & Network Infrastructure', '+91 98111 22334'),
        ('Ramesh Sharma (Senior Electrician)', 'ramesh.elec@lloyd.ac.in', pw_staff, 'staff', 'EMP-MAINT-015', 'Electrical Maintenance', '+91 98222 33445'),
        ('Sunita Devi (Housekeeping Supervisor)', 'sunita.hk@lloyd.ac.in', pw_staff, 'staff', 'EMP-HK-003', 'Sanitation & Housekeeping', '+91 98333 44556'),
        ('Manoj Yadav (Plumber In-charge)', 'manoj.plumb@lloyd.ac.in', pw_staff, 'staff', 'EMP-PLUMB-007', 'Water Supply & Plumbing', '+91 98444 55667'),
        # Another Student
        ('Priya Verma', 'priya.verma@lloyd.ac.in', pw_student, 'student', '2501530100088', 'Information Technology (2B)', '+91 98555 66778'),
    ]

    cursor.executemany("""
    INSERT INTO users (name, email, password_hash, role, roll_no, department, phone)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, users_data)

    # 2. Seed Departments
    departments_data = [
        ('Electrical Maintenance', 'ELEC', 'Er. Ramesh Sharma', 'elec.help@lloyd.ac.in', 12, 'zap'),
        ('IT & Network Infrastructure', 'ITNET', 'Rajesh Kumar', 'it.support@lloyd.ac.in', 6, 'wifi'),
        ('Sanitation & Housekeeping', 'HOUSE', 'Sunita Devi', 'housekeeping@lloyd.ac.in', 8, 'trash-2'),
        ('Civil & Infrastructure', 'CIVIL', 'Er. Akhilesh Mishra', 'civil.maint@lloyd.ac.in', 24, 'tool'),
        ('Water Supply & Plumbing', 'PLUMB', 'Manoj Yadav', 'plumbing@lloyd.ac.in', 8, 'droplet'),
        ('Hostel Administration', 'HOSTEL', 'Dr. S. K. Verma', 'hostel.warden@lloyd.ac.in', 12, 'home'),
        ('Security & Campus Safety', 'SEC', 'Capt. V. P. Singh', 'security@lloyd.ac.in', 4, 'shield-alert'),
        ('Library Facilities', 'LIB', 'Dr. Alka Sharma', 'library@lloyd.ac.in', 12, 'book-open')
    ]

    cursor.executemany("""
    INSERT INTO departments (name, code, head_name, head_email, sla_hours, icon)
    VALUES (?, ?, ?, ?, ?, ?)
    """, departments_data)

    # 3. Seed Realistic Complaints
    now = datetime.now()
    def ts(delta_hours):
        return (now - timedelta(hours=delta_hours)).strftime("%Y-%m-%d %H:%M:%S")

    def future_ts(delta_hours):
        return (now + timedelta(hours=delta_hours)).strftime("%Y-%m-%d %H:%M:%S")

    complaints_data = [
        (
            'LIET-2026-1001', 2, 'Bhaskar Raj', 'bhaskar@lloyd.ac.in', '2501530100041',
            'Internet & WiFi', 'Access Point Offline', 'Block B - CS Labs', 'Room 304 - High Performance Lab',
            'Campus Wi-Fi AP disconnected during Data Mining lab session',
            'Students are unable to connect to the campus proxy server in CS Lab 3. The access point LED indicator shows constant red blinking.',
            'High', 'In Progress', 2, 'Rajesh Kumar (Network Admin)', None,
            None, None, future_ts(2), 0, None, None, 4, ts(4), ts(1)
        ),
        (
            'LIET-2026-1002', 2, 'Bhaskar Raj', 'bhaskar@lloyd.ac.in', '2501530100041',
            'Electricity & Lighting', 'Ceiling Fan Defect', 'Block A - Academic', 'Room 204 - Lecture Hall',
            'Overhead ceiling fan vibrating abnormally with burning odor',
            'During the Operating Systems lecture, the center ceiling fan started emitting smoke smell and high vibration. Currently switched off for safety.',
            'Critical', 'Assigned', 1, 'Ramesh Sharma (Senior Electrician)', None,
            None, None, future_ts(1), 0, None, None, 8, ts(3), ts(2)
        ),
        (
            'LIET-2026-1003', 7, 'Priya Verma', 'priya.verma@lloyd.ac.in', '2501530100088',
            'Cleanliness & Sanitation', 'Dustbin Overflow & Litter', 'Student Cafeteria', 'Ground Floor Food Court',
            'Cafeteria wet waste dustbin overflowing causing hygiene hazard',
            'The waste disposal bins outside the juice stall are overflowing since morning. Needs immediate clearing and sanitization.',
            'Medium', 'Resolved', 3, 'Sunita Devi (Housekeeping Supervisor)', None,
            'Cleaned and disinfected cafeteria bins. Placed extra 60L bin to prevent overflow.', None, ts(1), 0, None, None, 2, ts(12), ts(2)
        ),
        (
            'LIET-2026-1004', 2, 'Bhaskar Raj', 'bhaskar@lloyd.ac.in', '2501530100041',
            'Water Supply', 'Pipe Leakage', 'Boys Hostel 1', '2nd Floor Common Washroom',
            'Continuous freshwater pipe leakage near Basin 3',
            'The inlet pipe underneath the hand wash basin has a crack, wasting water continuously and flooding the corridor floor.',
            'High', 'Closed', 5, 'Manoj Yadav (Plumber In-charge)', None,
            'Replaced defective PVC elbow joint with new brass fitting and tested under full pressure.', None, ts(20), 0, None, None, 5, ts(28), ts(8)
        ),
        (
            'LIET-2026-1005', 7, 'Priya Verma', 'priya.verma@lloyd.ac.in', '2501530100088',
            'Library Facilities', 'AC Not Cooling', 'Central Library', '1st Floor Digital Reading Section',
            'Split AC 2 not cooling, reading room getting suffocating',
            'The digital reading section is crowded and unit 2 only blows room-temperature air. Compressor seems tripped.',
            'Medium', 'Submitted', 1, None, None,
            None, None, future_ts(8), 0, None, None, 3, ts(1), ts(1)
        ),
        (
            'LIET-2026-1006', 2, 'Bhaskar Raj', 'bhaskar@lloyd.ac.in', '2501530100041',
            'Civil & Infrastructure', 'Broken Desk Bench', 'Block A - Academic', 'Room 105 - Tutorial Room',
            'Three front-row wooden benches have sharp broken nails',
            'Nails protruding from wooden bench edge, already tore a student bag. Needs carpentry repair or bench replacement.',
            'Low', 'In Progress', 4, 'Er. Akhilesh Mishra', None,
            'Carpentry staff inspected. New replacement desktop ply ordered for delivery.', None, future_ts(18), 0, None, None, 1, ts(14), ts(5)
        ),
        (
            'LIET-2026-1007', 7, 'Priya Verma', 'priya.verma@lloyd.ac.in', '2501530100088',
            'Security & Safety', 'Staircase Emergency Light Out', 'Girls Hostel', 'Wing B Fire Exit Staircase',
            'Emergency exit lights not functioning during night power shift',
            'The emergency lighting at the stairwell between floors 2 and 3 fails to kick in when mains trip.',
            'Critical', 'Assigned', 7, 'Capt. V. P. Singh', None,
            None, None, future_ts(1), 1, 'Prof. Vishal Gupta (Dean Academics / Chief Proctor)', ts(1), 7, ts(6), ts(1)
        )
    ]

    cursor.executemany("""
    INSERT INTO complaints (
        ticket_id, user_id, user_name, user_email, user_roll,
        category, subcategory, building_block, room_location,
        title, description,
        priority, status, assigned_dept_id, assigned_staff_name, image_path,
        resolution_remarks, resolution_image, sla_deadline, is_escalated, escalated_to, escalated_at, upvotes, created_at, updated_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, complaints_data)

    # 4. Seed Audit Logs for Complaints
    logs_data = [
        ('LIET-2026-1001', 'Submitted', 'Bhaskar Raj', 'Student', 'Complaint lodged through student portal.', ts(4)),
        ('LIET-2026-1001', 'Assigned', 'Prof. Vishal Gupta', 'Admin', 'Assigned to IT & Network Department with priority High.', ts(3)),
        ('LIET-2026-1001', 'In Progress', 'Rajesh Kumar (Network Admin)', 'Staff', 'Diagnosed switch port timeout; replacing POE adapter on AP.', ts(1)),

        ('LIET-2026-1002', 'Submitted', 'Bhaskar Raj', 'Student', 'Critical electrical fault reported.', ts(3)),
        ('LIET-2026-1002', 'Assigned', 'Prof. Vishal Gupta', 'Admin', 'Priority tagged Critical (SLA: 4 hours). Dispatched Ramesh Sharma.', ts(2)),

        ('LIET-2026-1003', 'Submitted', 'Priya Verma', 'Student', 'Housekeeping cleanliness ticket raised.', ts(12)),
        ('LIET-2026-1003', 'Assigned', 'Auto-System', 'System', 'Auto-routed to Sanitation & Housekeeping.', ts(11)),
        ('LIET-2026-1003', 'In Progress', 'Sunita Devi (Housekeeping Supervisor)', 'Staff', 'Cleaning crew deployed to food court area.', ts(6)),
        ('LIET-2026-1003', 'Resolved', 'Sunita Devi (Housekeeping Supervisor)', 'Staff', 'Waste cleared and bins sterilized.', ts(2)),

        ('LIET-2026-1004', 'Submitted', 'Bhaskar Raj', 'Student', 'Water leakage ticket lodged.', ts(28)),
        ('LIET-2026-1004', 'Assigned', 'Prof. Vishal Gupta', 'Admin', 'Assigned to Manoj Yadav.', ts(26)),
        ('LIET-2026-1004', 'In Progress', 'Manoj Yadav (Plumber In-charge)', 'Staff', 'Main valve shut off, pipe dismantled.', ts(18)),
        ('LIET-2026-1004', 'Resolved', 'Manoj Yadav (Plumber In-charge)', 'Staff', 'New brass elbow valve fitted. Leak stopped.', ts(10)),
        ('LIET-2026-1004', 'Feedback Submitted', 'Bhaskar Raj', 'Student', 'Rated 5 stars: Very prompt service and clean finish.', ts(8)),
        ('LIET-2026-1004', 'Closed', 'Prof. Vishal Gupta', 'Admin', 'Ticket verified and marked closed.', ts(8)),

        ('LIET-2026-1005', 'Submitted', 'Priya Verma', 'Student', 'Library AC breakdown ticket logged.', ts(1)),

        ('LIET-2026-1007', 'Submitted', 'Priya Verma', 'Student', 'Safety issue reported.', ts(6)),
        ('LIET-2026-1007', 'Assigned', 'Prof. Vishal Gupta', 'Admin', 'Assigned to Security Dept.', ts(5)),
        ('LIET-2026-1007', 'Escalated', 'Smart Campus SLA Engine', 'System', 'Auto-escalated to Dean / Chief Proctor due to critical safety SLA.', ts(1)),
    ]

    cursor.executemany("""
    INSERT INTO complaint_logs (ticket_id, action, performed_by, role, notes, created_at)
    VALUES (?, ?, ?, ?, ?, ?)
    """, logs_data)

    # 5. Seed Feedback for Resolved/Closed complaints
    feedback_data = [
        ('LIET-2026-1004', 2, 5, 'Plumber arrived within 2 hours. Excellent and polite work!', ts(8)),
        ('LIET-2026-1003', 7, 4, 'Resolved on the same day. Much cleaner now.', ts(2))
    ]

    cursor.executemany("""
    INSERT INTO feedback (ticket_id, user_id, rating, comment, created_at)
    VALUES (?, ?, ?, ?, ?)
    """, feedback_data)

    # 6. Seed Campus IoT Sensors for Simulation
    sensors_data = [
        ('IOT-WTR-01', 'Overhead Tank A1 Water Level', 'Block A - Academic', 'Rooftop Water Reservoir', 'Water Tank Level', 'Normal', '87% Capacity', ts(0)),
        ('IOT-WTR-02', 'Hostel Block 1 Sump Sensor', 'Boys Hostel 1', 'Basement Pump House', 'Water Tank Level', 'Warning', '96% - Overflow Risk', ts(0)),
        ('IOT-NET-01', 'Core Gateway Router Ping', 'Block B - CS Labs', 'Server Room 301', 'WiFi Router Ping', 'Normal', '1.2ms latency', ts(0)),
        ('IOT-NET-02', 'Library Wi-Fi Mesh AP', 'Central Library', '1st Floor Reading Hall', 'WiFi Router Ping', 'Warning', 'Packet loss 18%', ts(0)),
        ('IOT-PWR-01', 'Main 11kV Substation Transformer', 'Campus Substation', 'Yard Primary Incomer', 'Power Voltage', 'Normal', '415V stable', ts(0)),
        ('IOT-SEC-01', 'Fire Exit Alarm Node 3', 'Girls Hostel', 'Wing B Staircase', 'Smoke/Fire Monitor', 'Critical', 'Battery low / Sensor fault', ts(0)),
    ]

    cursor.executemany("""
    INSERT INTO iot_sensors (sensor_id, name, building_block, location, type, status, last_reading, last_checked)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, sensors_data)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    seed_db()
    print("Database initialized and seeded successfully!")
