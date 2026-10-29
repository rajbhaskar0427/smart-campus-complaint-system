# Smart Campus Complaint System (Mini Project)

**Institution:** Lloyd Institute of Engineering & Technology, Greater Noida  
**Affiliation:** Dr. A.P.J. Abdul Kalam Technical University (AKTU), Lucknow  
**Student:** Bhaskar Raj (Roll No: 2501530100041, Section: 2A)  
**Supervisor:** Prof. Vishal Gupta, Assistant Professor, Department of CSE  
**Session:** 2026-27  

---

## 🌟 Overview & Key Capabilities

A production-ready, full-fledged web application implementing the exact software engineering specifications of the Mini Project Synopsis:

1. **Role-Based Access Control (RBAC):**
   - **Student / Ordinary User** (Bhaskar Raj, Priya Verma, or newly registered students)
   - **Administrator / Chief Proctor** (Prof. Vishal Gupta)
   - **Maintenance Field Staff** (Senior Electrician Ramesh, Network Admin Rajesh, Plumber Manoj, Housekeeper Sunita)
2. **Standard Complaint Handling Flow:**
   `Login` ➔ `Submit` ➔ `Ticket` ➔ `Assign` ➔ `Track` ➔ `Resolve` ➔ `Close & Feedback`
3. **Value-Added Features (Synopsis Page 5):**
   - **Priority & SLA Matrix:** Dynamic 4h (Critical), 8h (High), 24h (Medium), 48h (Low) targets.
   - **Intelligent Duplicate Detection:** Real-time similarity checking preventing duplicate tickets; allows users to upvote active issues.
   - **Full Audit Trail:** Time-stamped history of every status update, note, and actor.
   - **Student Satisfaction Rating:** 1 to 5 star rating with feedback commentary upon ticket resolution.
   - **Printable Grievance Docket Slip:** Print-ready official slips with barcode representations.
   - **Data Export:** Export all records to CSV for administrative reports and AKTU inspection.
4. **Interactive Simulations & Digital Twin:**
   - **2.5D Campus Digital Twin Map:** Vector interactive map of Lloyd Institute (Academic Block A, CS Labs Block B, Central Library, Hostels, Cafeteria, Sports Arena). Pulsing pins show active issues by severity.
   - **Campus IoT Sensor Telemetry:** Real-time monitoring of wireless sensor nodes (Overhead Water Tank, Wi-Fi AP ping, 11kV Substation, Smoke detector).
   - **One-Click Event Simulator:** Trigger automated IoT anomaly ingestion, fast-forward SLA auto-escalation, or simulate technician dispatch and resolution.
   - **Campus Facility QR Plaque Scanner Simulator:** Simulates camera scanning of classroom/lab door QR codes for 1-click complaint autofill.

---

## 🚀 Quick Start Guide

### 1. Run Web Server
The server runs on Python 3 with zero external package installation:
```bash
cd "C:\Users\Hello\.gemini\antigravity\scratch\SmartCampusComplaintSystem"
python app.py
```
Open your browser and navigate to:
**[http://127.0.0.1:5000](http://127.0.0.1:5000)**

### 2. Demo Accounts & 1-Click Role Switcher
A convenient top-bar switcher allows examiners to instantly switch roles without re-logging:
- **Student View:** `bhaskar@lloyd.ac.in` (Password: `student123`)
- **Admin View:** `vishal.gupta@lloyd.ac.in` (Password: `admin123`)
- **Electrician View:** `ramesh.elec@lloyd.ac.in` (Password: `staff123`)
- **Network Admin View:** `rajesh.it@lloyd.ac.in` (Password: `staff123`)

---

## 📂 Project Directory Structure

```
SmartCampusComplaintSystem/
├── app.py                     # Main Flask web application & REST API
├── database.py                # SQLite relational schema, seed data, & models
├── campus_complaints.db       # Persistent SQLite database file
├── test_app.py                # Automated unit tests covering all routes & APIs
├── static/
│   ├── css/
│   │   ├── style.css          # Modern UI, design system, cards, tables, steppers
│   │   └── simulation.css     # Digital Twin map, laser QR scanner, cyber console
│   ├── js/
│   │   ├── main.js            # Duplicate checker, modals, star ratings, search
│   │   ├── campus_map.js      # Interactive 2.5D Campus Map controller
│   │   ├── simulator.js       # Live SLA auto-escalation & IoT telemetry simulator
│   │   └── charts.js          # Pure offline SVG/Canvas analytics charts
│   └── uploads/               # Uploaded evidence and grievance photos
└── templates/
    ├── base.html              # Responsive base layout with 1-click role switcher
    ├── index.html             # Homepage, KPI cards, flow stepper, recent feed
    ├── submit_complaint.html  # Enhanced grievance lodging with duplicate detection
    ├── track.html             # Real-time ticket tracking, milestone stepper, audit trail
    ├── user_dashboard.html    # Student portal (My complaints, quick lodging)
    ├── admin_dashboard.html   # Administrator console (Assigning, escalations, KPI)
    ├── staff_dashboard.html   # Field technician work order execution
    ├── analytics.html         # Rich offline charts, SLA compliance matrix
    ├── simulation.html        # Interactive Digital Twin & SLA incident sandbox
    ├── qr_scanner.html        # Facility QR plaque scanner simulation
    ├── login.html             # User authentication
    ├── register.html          # New student & faculty registration
    └── print_slip.html        # Official printable grievance docket slip
```
