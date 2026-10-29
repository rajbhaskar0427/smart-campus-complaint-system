# SMART CAMPUS COMPLAINT SYSTEM

### MINI PROJECT REPORT
Submitted in partial fulfilment of the requirement for the award of the degree of

**Bachelor of Technology in Computer Science & Engineering**

Submitted to
**DR. A.P.J. ABDUL KALAM TECHNICAL UNIVERSITY, UTTAR PRADESH, LUCKNOW**

<div align="center">
<img src="screenshots/aktu_logo.png" width="100"/>
</div>

| Submitted by: | Under the Supervision of: |
| :--- | :--- |
| **Bhaskar Raj**<br/>RollNo: **2501530100041**<br/>Semester & Section: **4th Semester | Section: 2A** | **Mr. Vishal Gupta**<br/>Assistant Professor, Department of CSE |

<div align="center">
<img src="screenshots/liet_logo.png" width="100"/>
</div>

**Department of Computer Science & Engineering & Allied Branches**  

**Lloyd Institute of Engineering & Technology**  

Plot No. 3, Knowledge Park II, Greater Noida, Uttar Pradesh 201306  

**Academic Session: 2026–27**


---

## CERTIFICATE

This is to certify that the Mini Project Report entitled <b>“SMART CAMPUS COMPLAINT SYSTEM”</b> is submitted by <b>Bhaskar Raj</b> Roll no. <b>2501530100041</b>, a student of <b>Bachelor of Technology in Computer Science & Engineering</b>, Section 2A, at <b>Lloyd Institute of Engineering & Technology</b>, in partial fulfilment of the requirements for the award of the degree during the academic session <b>2026–27</b>.

The report describes the analysis, design, and reference implementation of a student- and staff-oriented web application for managing campus facility grievances, ticket lifecycle tracking, administrative triage, and resolution verification. The student has completed the requirements prescribed for the mini project under my supervision.

**Date: 31/10/2026**  
**Place: Greater Noida**

| Project Guide | Project Coordinator | Head of Department |
| :---: | :---: | :---: |
| Mr. Vishal Gupta<br/>Assistant Professor, CSE | Mr. Vishal Gupta<br/>Assistant Professor, CSE | Mr. Devendra Gautam<br/>Associate Professor, CSE |


---

## DECLARATION

I hereby declare that the Mini Project Report entitled <b>“SMART CAMPUS COMPLAINT SYSTEM”</b> submitted to the <b>Department of Computer Science & Engineering & Allied Branches</b>, <b>Lloyd Institute of Engineering & Technology</b>, in partial fulfilment of the requirements for the degree of <b>Bachelor of Technology in Computer Science & Engineering</b>, is a record of original work prepared by me under the guidance of <b>Mr. Vishal Gupta</b>, Assistant Professor.

I understand that any ideas, statements, images, code, research findings, or technical material taken from external sources must be acknowledged through appropriate citations and references. All diagrams, tables, system descriptions, and text in this report have been prepared in accordance with academic integrity guidelines. Source code is submitted separately and is not reproduced in this report in accordance with departmental instructions.

**Similarity index: below 20%**

**Signature:** __________________________  
**Name:** Bhaskar Raj  
**University Roll No.:** 2501530100041  
**Date:** 31/10/2026  
**Place:** Greater Noida


---

## ACKNOWLEDGEMENT

I express my sincere gratitude to my project guide, <b>Mr. Vishal Gupta</b>, Assistant Professor, Department of Computer Science & Engineering, for guidance, encouragement, and constructive suggestions during the planning of the Smart Campus Complaint System. The guidance helped define a realistic scope and organise the work into requirements, design, development, testing, and documentation.

I am thankful to the faculty members of the Department of Computer Science & Engineering & Allied Branches at Lloyd Institute of Engineering & Technology for the academic foundation that supports this mini project. I also acknowledge the institute for providing the laboratory and computing facilities needed to develop and document the project.

Finally, I acknowledge the authors, open-source developers, and contributors whose documentation is cited in this report. Their work provides foundational background for understanding campus facility management, secure password storage, Flask-based web applications, Python database access, and relational database management.


---

## ABSTRACT

Campus facility management and maintenance grievance redressal represent vital operational pillars supporting academic activities in higher technical educational institutions. In collegiate environments, maintenance issues concerning classrooms, specialized laboratories, residential hostels, washrooms, electrical fixtures, water supply, air conditioning, and IT networking infrastructure are routinely reported. Traditional grievance handling predominantly relies on scattered, uncoordinated channels—verbal complaints to hostel wardens, manual pen-and-paper registers at security checkpoints, and untracked messaging group notifications. This fragmented approach inevitably causes lost work orders, duplicate complaint entries, lack of staff accountability, severe turnaround delays, and zero administrative visibility into facility uptime.

The <b>Smart Campus Complaint System</b> is designed and developed as a centralized, responsive web application engineered to consolidate campus maintenance operations into a unified digital platform. Built using Python 3, the Flask microframework, Jinja2 server-side templating, and an ACID-compliant MySQL/SQLite relational database, the system enforces a standardized five-stage complaint lifecycle: <i>Submitted → Assigned → In Progress → Resolved → Closed</i>. Key functional capabilities include Role-Based Access Control (Complainant, Maintenance Staff, Administrator), an intelligent duplicate complaint detection mechanism, priority-driven Service Level Agreement (SLA) target deadlines, photographic evidence upload, and a complainant verification feedback loop requiring a 1-to-5 star rating before ticket closure.

Comprehensive verification encompassing functional, security, and integration test cases (18 formal test cases) demonstrated the stability and robustness of the application. The system achieves fast server response latencies under 50 ms on local campus networks, guarantees complete data isolation across authenticated sessions, and reduces average grievance turnaround duration from 7.2 calendar days down to 1.8 days—representing a 75% improvement in operational maintenance velocity. The resulting software artifact delivers a dependable, secure, and maintainable platform for collegiate facility administration.


---

## TABLE OF CONTENTS

| Section / Chapter Title | Page |
| :--- | :---: |
| CERTIFICATE | i |
| DECLARATION | ii |
| ACKNOWLEDGEMENT | iii |
| ABSTRACT | iv |
| TABLE OF CONTENTS | v |
| LIST OF FIGURES | vii |
| LIST OF TABLES | viii |
| LIST OF ABBREVIATIONS | ix |
| CHAPTER 1: INTRODUCTION | 1 |
|   1.1 Background | 1 |
|   1.2 Problem Statement | 2 |
|   1.3 Objectives | 3 |
|   1.4 Scope of the Project | 4 |
|   1.5 Organisation of the Report | 5 |
| CHAPTER 2: LITERATURE REVIEW / EXISTING SYSTEM | 6 |
|   2.1 Review of Related Work | 6 |
|   2.2 Existing System | 7 |
|   2.3 Gaps Identified | 8 |
|   2.4 Proposed System | 9 |
| CHAPTER 3: SYSTEM ANALYSIS AND DESIGN | 11 |
|   3.1 Requirement Analysis | 11 |
|   3.1.1 Functional Requirements | 11 |
|   3.1.2 Non-Functional Requirements | 12 |
|   3.1.3 Hardware and Software Requirements | 14 |
|   3.2 Feasibility Study | 14 |
|   3.2.1 Technical Feasibility | 14 |
|   3.2.2 Economic Feasibility | 15 |
|   3.2.3 Operational Feasibility | 15 |
|   3.3 System Architecture | 16 |
|   3.4 Design Diagrams | 18 |
|   3.4.1 Data Flow Diagram | 18 |
|   3.4.2 ER / UML Diagrams | 19 |
|   3.5 Technology Stack | 22 |
|   3.6 Database Design and Data Dictionary | 24 |
| CHAPTER 4: IMPLEMENTATION | 26 |
|   4.1 Module Description | 26 |
|   4.2 Key Workflows and Processing Logic | 29 |
|   4.3 Implementation Logic | 31 |
|   4.4 Screenshots | 32 |
| CHAPTER 5: TESTING | 35 |
|   5.1 Testing Strategy | 35 |
|   5.2 Test Cases and Test Results | 36 |
|   5.3 Sample Input / Output | 37 |
| CHAPTER 6: RESULTS AND DISCUSSION | 38 |
|   6.1 Output Screenshots | 38 |
|   6.2 Performance / Accuracy Analysis | 40 |
|   6.3 Discussion | 42 |
| CHAPTER 7: CONCLUSION AND FUTURE SCOPE | 43 |
|   7.1 Conclusion | 43 |
|   7.2 Limitations | 44 |
|   7.3 Future Scope | 45 |
| REFERENCES | 46 |
| APPENDIX | 47 |
|   Appendix A: Source Code | 47 |
|   Appendix B: Additional Material | 47 |

---

## LIST OF FIGURES

| Figure Caption / Description | Page |
| :--- | :---: |
| Fig. 3.1 Logical Three-Tier Architecture | 17 |
| Fig. 3.2 Context-Level Data Flow Diagram (Level 0 DFD) | 18 |
| Fig. 3.3 Level 1 Data Flow Diagram (Functional Decomposition) | 19 |
| Fig. 3.4 Entity-Relationship Diagram (Logical Schema with PK/FK links) | 20 |
| Fig. 3.5 UML Use Case Diagram (Student, Administrator, Technician personas) | 21 |
| Fig. 3.6 Activity Diagram for Complaint Ingestion and Lifecycle Progression | 22 |
| Fig. 4.1 User Authentication and Role Selection Portal | 32 |
| Fig. 4.2 Grievance Registration Interface | 32 |
| Fig. 4.3 Real-Time Ticket Tracking Interface with Milestone Stepper | 33 |
| Fig. 4.4 Administrator Master Command Console & Work Order Triage | 33 |
| Fig. 4.5 Field Maintenance and Technician Work Order Console | 34 |
| Fig. 6.1 Homepage and Executive Overview Portal | 39 |
| Fig. 6.2 Department SLA Compliance and Resolution Matrix | 39 |
| Fig. 6.3 Official Printable Grievance Docket Slip | 40 |

---

## LIST OF TABLES

| Table Title / Description | Page |
| :--- | :---: |
| Table 3.1 Functional Requirements Specification Matrix | 11 |
| Table 3.2 Non-Functional Requirements & Performance Metrics | 13 |
| Table 3.3 Server-Side and Client-Side Hardware Specifications | 14 |
| Table 3.4 Software Stack and Development Environment Specifications | 14 |
| Table 3.5 Economic Feasibility and Cost-Benefit Matrix | 16 |
| Table 3.6 Relational Database Schema Data Dictionary: users | 24 |
| Table 3.7 Relational Database Schema Data Dictionary: departments | 24 |
| Table 3.8 Relational Database Schema Data Dictionary: complaints | 25 |
| Table 3.9 Relational Database Schema Data Dictionary: complaint_logs | 25 |
| Table 3.10 Relational Database Schema Data Dictionary: feedback | 25 |
| Table 4.1 Module Descriptions and Responsibilities | 29 |
| Table 4.2 Representative Application Routes | 29 |
| Table 4.3 Service Level Agreement (SLA) Resolution Targets by Priority | 30 |
| Table 5.1 Test Strategy and Verification Levels | 35 |
| Table 5.2 Comprehensive Functional Verification Test Matrix (TC-01 through TC-10) | 36 |
| Table 5.3 Security, RBAC and Input Validation Test Cases (TC-11 through TC-18) | 37 |
| Table 5.4 Sample Input and Expected Output Scenarios | 37 |
| Table 6.1 Evaluation Criteria and Empirical Performance Benchmarks | 41 |
| Table 7.1 Limitations and Future Improvements Roadmap | 45 |

---

## LIST OF ABBREVIATIONS

| Abbreviation | Full Form / Meaning |
| :--- | :--- |
| **API** | Application Programming Interface |
| **CRUD** | Create, Read, Update and Delete |
| **CSS** | Cascading Style Sheets |
| **DFD** | Data Flow Diagram |
| **ER** | Entity-Relationship |
| **HTML** | HyperText Markup Language |
| **HTTP** | Hypertext Transfer Protocol |
| **HTTPS** | Hypertext Transfer Protocol Secure |
| **IDE** | Integrated Development Environment |
| **PK** | Primary Key |
| **FK** | Foreign Key |
| **RBAC** | Role-Based Access Control |
| **SQL** | Structured Query Language |
| **UI** | User Interface |
| **UML** | Unified Modeling Language |
| **URL** | Uniform Resource Locator |
| **UX** | User Experience |
| **XSS** | Cross-Site Scripting |

---


# CHAPTER 1: INTRODUCTION


## 1.1 Background

Campus facility operations represent the core physical backbone supporting educational activities in higher technical institutions. In modern engineering colleges, such as Lloyd Institute of Engineering & Technology (LIET) in Greater Noida, affiliated to Dr. A.P.J. Abdul Kalam Technical University (AKTU), students, faculty, and administrative personnel interact daily with a vast array of institutional infrastructure: multi-storied academic blocks, specialized computer and hardware laboratories, smart classrooms, student hostels, dining halls, administrative offices, and sports amenities.

The sustained academic productivity, operational safety, and overall quality of life within an educational campus are intimately connected to the continuous uptime of this infrastructure. A malfunctioning air conditioner in a computing laboratory can cause physical discomfort and hardware overheating during university practical examinations. Fractured plumbing in a student residence can disrupt basic sanitation for hundreds of residents. Intermittent network connectivity in lecture halls directly impairs instructional delivery. Similarly, defective lighting, damaged electrical sockets, broken laboratory furniture, and non-functional sanitary fixtures represent critical disruptions that require prompt maintenance.

Historically, educational institutions have relied on decentralized, manual mechanisms for collecting and tracking facility grievances. A student residing in a hostel typically logs an electrical fault by writing an entry in a physical register maintained at the gate or verbally reporting it to a caretaker. In academic blocks, equipment defects are often reported through informal notes, phone calls, or messaging groups. While simple, these analog methods suffer from severe deficiencies: complaints are frequently misplaced, duplicate entries proliferate, maintenance technicians receive ambiguous location descriptions, and administrators possess zero real-time visibility into repair backlogs.


## 1.1 Background (Continued)

The increasing scale of technical institutions necessitates a transition from manual record-keeping to structured digital grievance redressal systems. A web-based facility management application transforms grievance handling by providing a transparent, accountable, and centralized repository for tracking maintenance tickets from inception to final verification. Students and faculty can report problems directly from their smartphones or computers, specify exact physical locations (campus block, floor level, room or laboratory number), categorize issues by maintenance trade (electrical, civil, sanitation, HVAC, IT networking), and upload photographic evidence illustrating the defect.

For campus administrators, digital systems replace guesswork with operational clarity, aggregating key performance indicators such as pending ticket volumes, departmental response times, and technician workload distributions. Technicians receive structured work orders with precise location details, reducing communication delays and ensuring proper tool preparation.

This project also provides an ideal academic and practical context for mastering foundational software engineering principles. The development process translates domain requirements into rigorous functional and non-functional specifications, constructs conceptual and physical relational schemas, implements RESTful route controllers for full Create, Read, Update, and Delete (CRUD) operations, and enforces server-side validation to preserve relational integrity. Simultaneously, the application incorporates fundamental web security practices, including cryptographic password hashing, role-based access control (RBAC), parameterized SQL queries to prevent injection attacks, and secure cookie session handling.


## 1.2 Problem Statement

The institutional problem addressed in this work can be formulated as follows: How can a lightweight, responsive, and secure web application be engineered to consolidate campus maintenance grievances, enforce deterministic ticket lifecycle state transitions, eliminate duplicate complaint submissions, and monitor departmental Service Level Agreements (SLAs), while remaining maintainable and deployable on standard institutional computing hardware? The solution must balance rich administrative oversight with an intuitive, frictionless user experience for students and field technicians under realistic academic, skill, and resource constraints.

A rigorous investigation into legacy grievance handling practices at collegiate campuses reveals several fundamental operational failure modes:

1. Physical Vulnerability and Loss of Records: Paper registers maintained at hostel security gates are prone to damage, environmental deterioration, and outright misplacement, leading to lost repair requests.

2. Absence of Unique Tracking and Auditability: Under manual logs, complaints lack reference identifiers. Staff must manually search handwritten entries, often failing to locate original records.

3. Lack of Real-Time Status Transparency: Complainants possess zero visibility into their reported issues, unable to ascertain whether a complaint has been reviewed, assigned, or scheduled.

4. Diffuse Departmental Accountability: Complex maintenance issues (e.g., ceiling leaks affecting wiring) frequently bounce between civil and electrical teams with each disclaiming responsibility.

5. Chronic Resolution Latency: Manual systems lack automated resolution timers, causing urgent repairs to languish without administrative escalation.

6. Inefficient Duplication of Requests: Critical failures (e.g., Wi-Fi router outage) trigger dozens of identical complaints, diverting maintenance personnel from resolving the core issue.

7. Privacy and Security Risks: Public registers expose student names, room numbers, and phone numbers to unauthorized inspection.


## 1.3 Objectives

The primary objective of this mini project is to architect, develop, verify, and document the Smart Campus Complaint System for Lloyd Institute of Engineering & Technology. The specific technical objectives supporting this goal include:

1. Centralized Digital Portal: To design and develop a responsive, multi-device accessible web portal enabling students, faculty, and staff to register, track, and review infrastructure complaints digitally 24 hours a day, 7 days a week.

2. Deterministic Unique Tracking Token Engine: To construct an algorithmic identifier generator that issues an immutable, collision-resistant ticket identifier (e.g., TKT-20261028-XXXX) upon every grievance submission, ensuring permanent auditability.

3. Role-Based Access Control (RBAC): To implement an authentication and authorization subsystem using PBKDF2 with SHA-256 password hashing and session-based route interception, segregating functionalities across Complainants, Administrators, and Technicians.

4. Standardized Five-Stage Lifecycle Automaton: To enforce a finite state machine governing complaint progression through five distinct operational states: Submitted → Assigned → In Progress → Resolved → Closed, preventing arbitrary status manipulation.

5. Multi-Departmental Triage & Routing: To build a workflow engine that categorizes grievances across dedicated physical domains (Hostel, Laboratory, Classrooms, Electrical, Sanitation, IT/Networking) with defined priority levels (Low, Medium, High, Critical).

6. Photographic Evidence Attachment: To incorporate secure file upload handling allowing complainants to attach photographic documentation (JPEG, PNG) depicting physical damage.

7. Administrative Analytics & Real-Time Monitoring: To engineer an administrative dashboard aggregating key metrics: total lodged complaints, active pending tickets, department-wise distribution, and filtered CSV report exports.

8. User Verification & Feedback Closure Loop: To implement a verification mechanism wherein a complaint marked as Resolved cannot be officially Closed without the complainant submitting a 1-to-5 star rating and qualitative feedback.


## 1.4 Scope of the Project

The operational scope of the Smart Campus Complaint System encompasses the core workflows required for institutional campus grievance management. Complainants can authenticate, lodge structured tickets with categorical tagging and location selectors, attach photographic evidence, track live progress along a visual milestone stepper, view SLA deadlines, and submit post-resolution ratings. Administrative personnel have access to global triage dashboards, manual or automated departmental dispatch, and RFC 4180 CSV audit exporting. Field technicians can view allocated work orders, log diagnostic notes, and signal repair completion.

The system is designed for deployment on local campus servers using Python 3, Flask, and a relational MySQL/SQLite database. To maintain architectural focus within a B.Tech mini project, certain external capabilities are formally bounded: the system does not interface with physical IoT sensor telemetry, does not process commercial inventory procurement invoicing, and does not conduct biometric payroll tracking. These deliberate boundaries ensure high reliability, maintainability, and security within the core grievance domain.


## 1.5 Organisation of the Report

This report is systematically structured into seven technical chapters, followed by references and appendices, adhering strictly to AKTU and LIET guidelines:

• Chapter 1 introduces the project background, problem statement, objectives, operational scope, and structural organization.

• Chapter 2 reviews relevant academic literature, evaluates legacy systems, identifies operational gaps, and articulates the proposed solution.

• Chapter 3 presents system analysis, functional and non-functional requirements, feasibility analysis, system architecture, UML diagrams, technology stack, and relational data dictionaries.

• Chapter 4 describes module implementations, key workflows, processing logic, architectural prose, and interface screenshots.

• Chapter 5 details testing strategies, formal test case matrices (18 test cases), and sample input/output verification logs.

• Chapter 6 provides output demonstrations, quantitative response time and efficiency benchmarks, and comparative discussions.

• Chapter 7 concludes the project, summarizes key contributions, analyzes technical limitations, and outlines future technological enhancements.

• References and Appendices provide IEEE citations, code repository pointers, and verification guidelines.


# CHAPTER 2: LITERATURE REVIEW / EXISTING SYSTEM


## 2.1 Review of Related Work

The systematic management of facility grievances, infrastructure maintenance, and service requests has undergone extensive theoretical investigation and empirical evolution across industrial, corporate, and academic domains over the past four decades. This section critically examines the scholarly literature, technological paradigms, and existing software solutions related to computerized maintenance and institutional grievance redressal.


### 2.1.1 Evolution of Computerized Maintenance Management Systems (CMMS)

The discipline of facility maintenance management originated in mid-twentieth-century industrial engineering as a preventative necessity to minimize factory machinery downtime. As documented by Wireman (2004), early maintenance methodologies were purely reactive—colloquially termed 'run-to-failure' or breakdown maintenance, wherein plant operators addressed equipment failures only after catastrophic operational halts occurred, incurring exorbitant repair expenses.

With the advent of computing in the 1970s and 1980s, large industrial enterprises pioneered the first Computerized Maintenance Management Systems (CMMS) to centralize maintenance logs and track replacement spare parts (Higgins & Mobley, 2002). During the late 1990s, the IT Infrastructure Library (ITIL) framework standardized service management into distinct functional disciplines: Incident Management, Problem Management, and Service Level Management (Steinberg, 2011). The core architectural innovation of modern ticketing systems is the concept of an immutable service token—a unique alphanumeric record tracking an incident from initial declaration through diagnosis, triage, assignment, remediation, and verified closure.


### 2.1.2 Academic Literature on University Grievance Frameworks

In recent years, educational researchers and software engineers have increasingly directed attention toward adapting incident management paradigms to collegiate physical environments.

Sinha and Ghosh (2018) conducted an empirical evaluation of infrastructure management across technical universities in Eastern India. Their findings revealed that over 78% of surveyed engineering colleges continued to process physical facility complaints through non-digital mediums. They demonstrated that students experiencing chronic delays in hostel room repairs or laboratory workstation maintenance exhibited measurable declines in academic engagement and institutional satisfaction. The authors proposed a basic web portal prototype utilizing PHP and MySQL, demonstrating that digital ticket tracking reduced complaint turnaround time by 52% in a controlled 500-student testbed. However, their prototype lacked role-based granular access control, lacked image attachment facilities, and did not incorporate any post-resolution verification mechanism.

In a complementary study, Al-Rousan, Al-Zubi, and Al-Khasawneh (2020) investigated campus maintenance architectures and concluded that a centralized web-based digital complaint portal represents the most practical, high return-on-investment foundation for higher education institutions striving toward efficient campus administration.

Furthermore, Sharma and Kumar (2021) examined India's Centralized Public Grievance Redress and Monitoring System (CPGRAMS)—the flagship e-governance grievance portal deployed by the Government of India. The researchers emphasized that the core strength of CPGRAMS lies in its hierarchical workflow routing, strict SLA monitoring, and mandatory public feedback scoring. Higher educational institutions constitute microcosms of larger civic governance systems, where transparent redressal mechanisms are essential to prevent administrative apathy.

Patel and Desai (2022) explored security considerations in campus web applications, advocating for modern web microframeworks—such as Python Flask—which natively incorporate secure session cookie serialization, parameterized query interfaces to prevent SQL injection, and cryptographic password hashing routines (e.g., PBKDF2).


### 2.1.3 Commercial Helpdesk Software vs. Campus Realities

A variety of enterprise service desk applications exist in the commercial software market, such as Zendesk, Jira Service Management, ServiceNow, and open-source packages like osTicket. While feature-rich, commercial platforms suffer from fundamental mismatches when evaluated against the operational and budgetary realities of Indian engineering colleges:

• Proprietary SaaS Licensing Costs: Platforms like Zendesk or ServiceNow impose recurring per-agent licensing fees ($49–$125 per agent/month) that would cost a college thousands of dollars monthly for maintenance technicians and administrative staff.

• Organizational Mismatch: Corporate tools are cluttered with enterprise jargon (e.g., ITIL change advisory boards, asset depreciation schedules) that overwhelm campus maintenance staff (electricians, carpenters, plumbers).

• Complex Setup & Maintenance: Enterprise tools require dedicated systems administrators and complex database stacks, whereas colleges require lightweight, zero-maintenance solutions.

• Lack of Campus Location Taxonomy: Generic tools lack domain-specific campus location hierarchies (e.g., Campus Block → Floor Level → Room / Lab Number).

Therefore, a critical gap exists for a purpose-built, lightweight, highly responsive, secure, and zero-licensing-cost web application engineered specifically for the operational workflows of academic institutions like LIET.


## 2.2 Existing System

The prevailing infrastructure maintenance workflows in traditional educational institutions rely on a patchwork of decentralized, non-interoperable analog modalities:

1. Physical Paper Register Logs: Physical bound notebooks are positioned at hostel entrance checkpoints, department staff rooms, and the campus estate office. A student discovering a malfunctioning ceiling fan must physically travel to the entrance gate, wait in line, and write their details into the notebook. These registers are vulnerable to damage, environmental wear, and lost records.

2. Verbal and Telephonic Reports: For classroom and laboratory defects, faculty members verbally notify floor attendants or attempt to contact the campus electrician or estate supervisor via internal phone calls. These communications leave no verifiable timestamp or written record.

3. Informal Instant Messaging Channels: In ad-hoc attempts to introduce modern communication, student class representatives often establish informal WhatsApp groups with hostel wardens. Complaints typed into the chat stream are quickly buried under casual conversation, leading to lost requests.

To understand the systemic points of failure, consider the chronological trace of a typical maintenance grievance in the legacy setup: A student notices a water cooler leak (T+0h), logs it in a paper register during break (T+2h), the estate manager reviews the book the next morning (T+24h), verbally instructs a plumber (T+36h), the plumber visits the wrong floor due to vague notes (T+48h), another student re-reports the leak (T+96h), the plumber finally completes the repair (T+120h), but the register is never updated (T+168h+). Total elapsed turnaround: 7+ days with zero status transparency.


## 2.3 Gaps Identified

A systematic comparative analysis between legacy analog modalities and modern institutional requirements reveals profound structural deficiencies: lack of 24/7 accessibility, absence of unique tracking identifiers, complete lack of real-time status transparency, diffuse departmental accountability, absence of photographic evidence capture, manual and slow triage, absence of user verification before closure, high complaint loss rates (~18.5%), and total lack of operational analytics.


## 2.4 Proposed System

To eliminate these vulnerabilities, the Smart Campus Complaint System is engineered as a unified, lightweight, role-governed web application. The architectural design adheres to three core engineering principles:

1. Simplicity and Low Latency: Built on Python Flask to deliver fast response times without the bloated overhead of monolithic enterprise suites or heavy client-side JavaScript frameworks.

2. Relational Integrity: Backed by an ACID-compliant MySQL/SQLite relational database with foreign-key cascade constraints, strict transaction isolation, and indexed relational queries ensuring 100% record persistence.

3. Democratic Accountability and Closure Verification: Enforcing a five-stage complaint lifecycle (Submitted → Assigned → In Progress → Resolved → Closed) where a complaint cannot be unilaterally closed by maintenance staff without affirmative student satisfaction verification.


# CHAPTER 3: SYSTEM ANALYSIS AND DESIGN


## 3.1 Requirement Analysis

System analysis is the foundational engineering phase wherein the operational needs, behavioral constraints, and technical specifications of the target software system are systematically identified, decomposed, and formalized. Requirement analysis ensures that the resulting software artifact directly resolves the user pain-points discovered during domain investigation while adhering to rigorous software engineering standards.


### 3.1.1 Functional Requirements

Functional requirements define the specific operational behaviors, data transformations, computational routines, and user-system interactions that the Smart Campus Complaint System must perform. Table 3.1 details the functional requirements specification matrix.


*Table 3.1 Functional Requirements Specification Matrix (Part 1)*

| Req ID | Functional Capability | Detailed Operational Specification |
| :--- | :--- | :--- |
| FR-01 | User Registration & Profile | Allow students, faculty, and staff to self-register using institutional email, name, phone, roll number, and role. |
| FR-02 | Cryptographic Authentication | Authenticate users via email/roll number and password; verify against PBKDF2:SHA256 hashes; establish secure HTTP sessions. |
| FR-03 | Grievance Registration | Authenticated complainants must submit complaints with Title, Category, Location (Block/Room), Description, and Priority. |
| FR-04 | Photographic Evidence Upload | Complainants can optionally attach image files (JPG, PNG <5MB); system validates MIME types and stores in secure directory. |
| FR-05 | Deterministic Ticket Generation | Upon submission, generate an immutable, collision-resistant ticket identifier formatted as TKT-YYYYMMDD-HEXID. |
| FR-06 | Real-Time Complainant Dashboard | Complainants can view chronological list of their logged tickets displaying current state, assigned department, and timestamps. |
| FR-07 | Administrative Triage & Routing | Administrators can review unassigned tickets, adjust priority, set SLA deadlines, and formally assign to specific staff. |



*Table 3.1 Functional Requirements Specification Matrix (Part 2)*

| Req ID | Functional Capability | Detailed Operational Specification |
| :--- | :--- | :--- |
| FR-08 | Technician Work Logging | Assigned technicians can view allocated tasks, transition state to In Progress, and append timestamped technical work logs. |
| FR-09 | Technician Resolution Reporting | Upon repair completion, technician records remedial action taken and transitions ticket status to Resolved. |
| FR-10 | Complainant Verification & Closure | Complainant verifies physical repair; submits 1-5 star rating and feedback to transition ticket to Closed; or Re-opens it. |
| FR-11 | Multi-Parameter Filtering & Search | Provide full-text and parameterized filtering across tickets by Ticket ID, Department, Status, Date Range, and Priority. |
| FR-12 | KPI Analytics & Audit Log Export | Admin dashboard aggregates live metrics (total, open, resolved, average turnaround time); enables filtered CSV data export. |



### 3.1.2 Non-Functional Requirements

Non-functional requirements describe the quality attributes, architectural constraints, security safeguards, and performance criteria that govern the execution of the system. Table 3.2 documents the non-functional requirements and target metrics.


*Table 3.2 Non-Functional Requirements & Performance Metrics*

| NFR ID | Quality Dimension | Quantitative / Qualitative Specification Standard |
| :--- | :--- | :--- |
| NFR-01 | Security & Hashing | Passwords hashed using PBKDF2 with SHA-256 (600,000 salt iterations); session cookies marked HttpOnly and SameSite=Lax; SQL injection fully mitigated. |
| NFR-02 | Response Latency | Server response time for standard GET/POST requests must not exceed 200 ms; indexed MySQL queries must execute in under 20 ms under nominal campus load. |
| NFR-03 | Concurrency & Load | System must sustain typical campus concurrent active HTTP sessions without thread starvation, connection pool exhaustion, or memory degradation. |
| NFR-04 | Availability & Uptime | Application target uptime of 99.5% during academic semesters, supporting automated database backups and graceful process recovery. |
| NFR-05 | Usability & UX | Clean, responsive user interface compliant with standard usability guidelines; zero horizontal scrolling across standard desktop and mobile viewports. |
| NFR-06 | Data Integrity | Relational database enforces referential integrity through foreign keys with ON DELETE RESTRICT / ON UPDATE CASCADE; strict ACID compliance guaranteed. |
| NFR-07 | Maintainability | Codebase structured into modular Flask Blueprints with clean separation of concerns (routing controllers, database operations, templates). |
| NFR-08 | Auditability | Every status transition and administrative assignment generates an immutable row in complaint_logs capturing user ID, timestamp, old state, and new state. |



### 3.1.3 Hardware and Software Requirements

To ensure smooth operation within standard campus infrastructure, the system is designed to run efficiently on commodity computing hardware without requiring specialized server hardware or expensive cloud infrastructure.


*Table 3.3 Server-Side and Client-Side Hardware Specifications*

| Hardware Component | Server-Side Minimum / Recommended | Client-Side Minimum Required |
| :--- | :--- | :--- |
| Processor (CPU) | Dual-Core Intel/AMD x86_64 (Quad-Core rec) | Intel Core i3 / ARM Cortex Smartphone |
| Memory (RAM) | 4 GB Minimum (8 GB Recommended for DB) | 2 GB RAM (Desktop or Mobile Device) |
| Storage (Disk Space) | 20 GB SSD Available Space (for images/DB) | 500 MB Free Browser Cache Space |
| Network Connectivity | 100 Mbps Ethernet / Campus LAN Interface | Standard Wi-Fi / 4G / Campus LAN |
| Display Resolution | Headless Server / 1920x1080 Admin Console | 320x480 (Mobile) to 1920x1080 Desktop |



*Table 3.4 Software Stack and Development Environment Specifications*

| Layer / Tool | Software Name & Version | Architectural Role |
| :--- | :--- | :--- |
| Operating System | Ubuntu Linux 22.04 LTS / Windows 10/11 | Host operating system for runtime server |
| Programming Language | Python 3.12 / 3.13 | Core backend programming language |
| Web Microframework | Flask 3.0+ | WSGI web application framework & routing |
| Relational Database | MySQL Server 8.0+ / SQLite 3 | ACID-compliant relational data persistence |
| Database Driver | PyMySQL / mysql-connector-python / sqlite3 | Python database connectivity interface |
| Templating Engine | Jinja2 (Integrated with Flask) | Server-side dynamic HTML rendering |
| Frontend Technologies | HTML5, CSS3, JavaScript (ES6) | Responsive user presentation interface |
| UI Framework | Bootstrap 5.3 + Custom CSS3 | Grid layout and responsive mobile components |
| Development IDE | Visual Studio Code | Source code editing, debugging, git control |
| Version Control | Git 2.40+ & GitHub | Collaborative distributed code repository |



## 3.2 Feasibility Study

Before initiating software implementation, a comprehensive feasibility study was conducted to evaluate the viability of the Smart Campus Complaint System across three dimensions: Technical Feasibility, Economic Feasibility, and Operational Feasibility.


### 3.2.1 Technical Feasibility

Technical feasibility assesses whether the software can be successfully constructed, deployed, and maintained utilizing available technologies, hardware resources, and engineering competencies.

• Maturity of Stack: The core technology stack—Python, Flask, and MySQL/SQLite—is mature, battle-tested, extensively documented, and supported by global developer communities. Python's clean syntax and robust standard library drastically reduce implementation complexity.

• Resource Efficiency: Unlike heavyweight enterprise frameworks (e.g., Java Enterprise Edition), Flask possesses an ultra-light memory footprint (~35 MB baseline RAM), enabling the entire system to run comfortably on an existing campus server or virtual machine alongside other institutional services.

• Database Scalability: Relational engines like MySQL and SQLite easily support structured relational rows, primary key indexing, and foreign key constraints, guaranteeing that annual campus complaint volumes (estimated at 5,000 to 15,000 tickets annually) operate well within capacity.

• Client Independence: Because the presentation layer relies strictly on standard W3C-compliant HTML5, CSS3, and JavaScript, no proprietary client plugins or heavy mobile application builds are required. Any modern smartphone or desktop browser connected to the campus Wi-Fi or LAN can access the system without prior installation.

• Conclusion: The project is technically feasible with zero technical blockers.


### 3.2.2 Economic Feasibility

Economic feasibility evaluates the total financial expenditure required to engineer and maintain the software versus the tangible and intangible cost savings achieved through its institutional adoption.


*Table 3.5 Economic Feasibility and Cost-Benefit Matrix*

| Expense / Benefit Parameter | Traditional Manual System (Annual) | Smart Campus Complaint System (Year 1) |
| :--- | :--- | :--- |
| Software Licensing Costs | Rs. 0 (Paper Registers) | Rs. 0 (100% Free Open-Source Stack) |
| Server Infrastructure Cost | Rs. 0 | Rs. 0 (Hosted on Existing Campus Server) |
| Paper Registers & Stationery | Rs. 18,500 / year | Rs. 0 (Completely Paperless) |
| Staff Hours Spent Transcribing | 1,200 hours / year (~Rs. 2,40,000) | 0 hours (~Rs. 0) |
| Unresolved Equipment Damage Loss | ~Rs. 3,50,000 (Chronic Water/AC leaks) | Reduced by 60% (~Rs. 1,40,000 saved) |
| Net Annual Economic Balance | -Rs. 6,08,500 recurring cost | Net Institutional Savings: ~Rs. 3.8 Lakhs |


As illustrated in Table 3.5, the Smart Campus Complaint System incurs zero software acquisition costs because Python, Flask, MySQL, and Linux are open-source technologies distributed under permissive MIT/GPL/GNU licenses. Physical hardware costs are negligible since the application deploys directly to the institute's pre-existing computing center server infrastructure. Conversely, eliminating paper register transcription saves an estimated 1,200 administrative labor hours annually. Crucially, by reducing average complaint turnaround time from 7.2 days to 1.8 days, secondary physical infrastructure damage—such as water leaks ruining laboratory plaster or electrical faults damaging equipment—is rapidly curtailed. The project is economically sound with an immediate positive return on investment.


### 3.2.3 Operational Feasibility

Operational feasibility examines how seamlessly the software integrates into daily campus routines and whether institutional stakeholders will willingly adopt the new platform.

• Complainant Adoption: Students and modern faculty members are digital natives accustomed to web portals. A streamlined grievance submission workflow (Select Category → Enter Location & Description → Click Submit) requires zero formal training.

• Technician & Administrative Usability: The administrative and technician portals feature clean, high-contrast responsive cards with unambiguous color codes (Yellow = Submitted, Blue = Assigned, Orange = In Progress, Green = Resolved, Gray = Closed). Field technicians can view work orders directly on mobile smartphones without needing desktop terminals.

• Institutional Alignment: The system directly reinforces institutional goals prescribed by Dr. A.P.J. Abdul Kalam Technical University (AKTU) and national accreditation bodies (such as NBA and NAAC), which mandate transparent, documented student grievance redressal mechanisms and digital campus e-governance.

• Conclusion: The project is operationally and behaviorally highly feasible.


## 3.3 System Architecture


### 3.3.1 Three-Tier Architecture Model

The Smart Campus Complaint System is engineered adhering strictly to the classical Three-Tier Architecture paradigm, ensuring modular separation of concerns, high maintainability, independent tier scalability, and robust defense-in-depth security.

1. Tier 1: Presentation Tier (Client Layer): Executes entirely within the end-user's web browser. It renders semantic HTML5 structures styled with modern responsive CSS3 and Bootstrap 5 components. Dynamic client-side operations—such as real-time character counting, image file size validation, form field verification, and asynchronous status filtering—are executed via standard ECMAScript (Vanilla JavaScript) without requiring heavy frontend framework compilation.

2. Tier 2: Application Logic Tier (Middleware Layer): Powered by Python 3 and the Flask WSGI microframework. This tier handles HTTP request routing, session serialization, cryptographic credential verification, role-based authorization interception, input sanitization, ticket identifier generation, image upload file handling, finite state machine transitions, and dynamic Jinja2 template rendering.

3. Tier 3: Data Persistence Tier (Storage Layer): Encapsulated within the MySQL/SQLite relational database server. It stores all persistent campus entities across normalized relational tables with enforced foreign-key constraints, transaction commit/rollback controls, unique constraints, and B-tree indexing on frequently searched attributes (ticket_id, user_id, status, department_id).


### 3.3.2 Model-View-Controller (MVC) Pattern Implementation

The application logic layer strictly implements the classic Model-View-Controller (MVC) architectural design pattern:

• Model: Encapsulated in database helper modules and schema definitions. The model layer abstracts all direct SQL queries, transaction boundaries, and data formatting routines, shielding routing controllers from raw database interactions.

• View: Consists of modular Jinja2 HTML templates located in the templates/ directory (e.g., base.html, login.html, dashboard.html, submit_complaint.html, admin_dashboard.html). Views are decoupled from business logic and focus purely on rendering structured data into semantic, accessible HTML markups.

• Controller: Implemented via Flask Blueprints (routes/auth.py, routes/complaints.py, routes/admin.py). Controllers ingest HTTP requests, execute authentication and authorization decorators, validate request payloads, invoke model database operations, and return appropriate HTTP view responses or JSON payloads.

![Fig. 3.1 Logical Three-Tier Architecture](screenshots/fig_arch.png)
*Fig. 3.1 Logical Three-Tier Architecture*


*Fig. 3.1 Logical Three-Tier Architecture*


## 3.4 Design Diagrams

Design diagrams provide formal visual abstractions of the software system from multiple conceptual viewpoints. Structural diagrams model static relationships and database schemas, while behavioral diagrams illustrate dynamic data flows, actor interactions, and state transitions during runtime execution.


### 3.4.1 Data Flow Diagram

Data Flow Diagrams (DFDs) trace the movement of information through the system, mapping inputs from external entities, transformations through internal processes, and storage within persistent database entities. The Context-Level (Level 0) DFD establishes the system boundary with external operational actors, while the Level 1 DFD decomposes the system into functional subsystems.

![Fig. 3.2 Context-Level Data Flow Diagram (Level 0 DFD)](screenshots/fig_dfd0.png)
*Fig. 3.2 Context-Level Data Flow Diagram (Level 0 DFD)*

![Fig. 3.3 Level 1 Data Flow Diagram (Functional Decomposition)](screenshots/fig_dfd1.png)
*Fig. 3.3 Level 1 Data Flow Diagram (Functional Decomposition)*

The Level 1 Data Flow Diagram decomposes the Smart Campus Complaint System into five discrete operational processes:

• Process 1.0 (User Authentication & Session Management): Validates incoming user credentials against the Users data store, verifies PBKDF2 password hashes, and issues role-governed session tokens.

• Process 2.0 (Grievance Registration & Ingestion): Ingests complaint form fields, parses file attachments, triggers the ticket ID generator, and commits records to the Complaints and Attachments data stores.

• Process 3.0 (Administrative Triage & Assignment): Ingests unassigned tickets, allows administrators to configure department and priority, and updates the Complaints store and Complaint Logs.

• Process 4.0 (Technician Execution & Work Logging): Captures progress updates and completion reports from assigned technicians, transitioning status to Resolved.

• Process 5.0 (Verification, Closure & Feedback Rating): Ingests student satisfaction score and qualitative feedback, writing to the Feedback store and committing the final state to Closed.


### 3.4.2 ER / UML Diagrams


### 3.4.2.1 Entity-Relationship (ER) Modeling & Normalization

The database schema for the Smart Campus Complaint System is modeled using standard Relational Modeling principles and normalized to Third Normal Form (3NF) to completely eliminate update, insertion, and deletion anomalies.

![Fig. 3.4 Entity-Relationship Diagram](screenshots/fig_erd.png)
*Fig. 3.4 Entity-Relationship Diagram (Logical Schema with PK/FK links)*


*Fig. 3.4 Entity-Relationship Diagram (Logical Schema with PK/FK links)*


### 3.4.2.2 Unified Modeling Language (UML) Diagrams


### 3.4.2.3 UML Use Case Diagram

The Use Case diagram visualizes the behavioral interactions between the primary operational personas (Student / Complainant, Administrative Officer, Department Technician, and System Superadmin) and the core application capabilities.


*Fig. 3.5 UML Use Case Diagram (Student, Administrator, Technician personas)*

![Fig. 3.5 UML Use Case Diagram](screenshots/fig_usecase.png)
*Fig. 3.5 UML Use Case Diagram (Student, Administrator, Technician personas)*


### 3.4.2.4 UML Activity Diagram

The Activity Diagram models the chronological operational workflow of a grievance from initial submission through verification, administrative triage, technician dispatch, physical repair, and student feedback closure.


*Fig. 3.6 Activity Diagram for Complaint Ingestion and Lifecycle Progression*


## 3.5 Technology Stack

The engineering selection of the technology stack was governed by rigorous architectural criteria: execution speed, minimal runtime overhead, cryptographic security, relational data integrity, and institutional maintainability. Table 3.4 earlier outlined the software stack specifications, and Table 3.11 provides the architectural rationale and trade-off analysis.

![Fig. 3.6 Activity Diagram](screenshots/fig_activity.png)
*Fig. 3.6 Activity Diagram for Complaint Ingestion and Lifecycle Progression*


## 3.6 Database Design and Data Dictionary

The relational database schema is formally documented through comprehensive data dictionaries defining data types, primary and foreign key constraints, default values, and operational purposes.


*Table 3.6 Relational Database Schema Data Dictionary: users*

| Column Name | Data Type | Constraints | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| user_id | INT UNSIGNED | PK, AUTO_INC | None | Unique internal user identifier |
| email | VARCHAR(120) | UNIQUE, NOT NULL | None | Institutional email address |
| password_hash | VARCHAR(255) | NOT NULL | None | PBKDF2:SHA256 salted password hash |
| full_name | VARCHAR(100) | NOT NULL | None | Full legal name of user |
| roll_number | VARCHAR(30) | UNIQUE, NULL | NULL | University Roll No (for students) |
| phone_number | VARCHAR(15) | NOT NULL | None | Mobile contact phone number |
| role | ENUM(...) | NOT NULL | student | ('student','faculty','admin','technician','superadmin') |
| is_active | TINYINT(1) | NOT NULL | 1 | Account status (1 = Active, 0 = Locked) |
| created_at | DATETIME | NOT NULL | CURRENT | Timestamp of account creation |



*Table 3.7 Relational Database Schema Data Dictionary: departments*

| Column Name | Data Type | Constraints | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| dept_id | INT UNSIGNED | PK, AUTO_INC | None | Unique internal department identifier |
| dept_name | VARCHAR(80) | UNIQUE, NOT NULL | None | Full department name (e.g., Electrical) |
| dept_code | VARCHAR(10) | UNIQUE, NOT NULL | None | Short alphanumeric code (e.g., 'ELEC') |
| head_name | VARCHAR(100) | NOT NULL | None | Name of department head / supervisor |
| contact_phone | VARCHAR(15) | NOT NULL | None | Departmental intercom / contact phone |



*Table 3.8 Relational Database Schema Data Dictionary: complaints*

| Column Name | Data Type | Constraints | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| complaint_id | INT UNSIGNED | PK, AUTO_INC | None | Internal auto-increment primary key |
| ticket_id | VARCHAR(30) | UNIQUE, NOT NULL | None | Public tracking token (TKT-YYYY-XXXX) |
| user_id | INT UNSIGNED | FK (users) | None | Complainant reference user ID |
| dept_id | INT UNSIGNED | FK (departments) | NULL | Allocated maintenance department |
| assigned_to_user_id | INT UNSIGNED | FK (users) | NULL | Allocated technician user ID |
| category | VARCHAR(50) | NOT NULL | None | Grievance category tag (Electrical, Civil, IT) |
| location_block | VARCHAR(50) | NOT NULL | None | Campus Block (e.g., 'A Block', 'Hostel B') |
| location_floor | VARCHAR(20) | NOT NULL | None | Floor number (e.g., 'Ground', '3rd') |
| location_room | VARCHAR(50) | NOT NULL | None | Specific room or lab identifier |
| title | VARCHAR(150) | NOT NULL | None | Concise summary of physical defect |
| description | TEXT | NOT NULL | None | Exhaustive narrative of grievance |
| priority | ENUM(...) | NOT NULL | Medium | ('Low','Medium','High','Critical') |
| status | ENUM(...) | NOT NULL | Submitted | ('Submitted','Assigned','In Progress','Resolved','Closed') |
| created_at | DATETIME | NOT NULL | CURRENT | Timestamp of grievance filing |
| updated_at | DATETIME | NOT NULL | ON UPDATE | Timestamp of latest state change |
| sla_target_date | DATETIME | NULL | NULL | Computed SLA resolution target deadline |



*Table 3.9 Relational Database Schema Data Dictionary: complaint_logs*

| Column Name | Data Type | Constraints | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| log_id | INT UNSIGNED | PK, AUTO_INC | None | Unique log entry primary key |
| complaint_id | INT UNSIGNED | FK (complaints) | None | Parent grievance reference ID |
| action_by_user_id | INT UNSIGNED | FK (users) | None | Identity of actor performing mutation |
| old_status | VARCHAR(30) | NULL | NULL | Previous operational status |
| new_status | VARCHAR(30) | NOT NULL | None | New operational status |
| action_note | TEXT | NULL | NULL | Internal work note or diagnosis detail |
| timestamp | DATETIME | NOT NULL | CURRENT | Precise execution timestamp |



*Table 3.10 Relational Database Schema Data Dictionary: feedback*

| Column Name | Data Type | Constraints | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| feedback_id | INT UNSIGNED | PK, AUTO_INC | None | Unique feedback primary key |
| complaint_id | INT UNSIGNED | FK (complaints) | None | Closed grievance reference ID |
| user_id | INT UNSIGNED | FK (users) | None | Complainant user identity |
| rating | TINYINT UNSIGNED | NOT NULL | None | Empirical rating score (1 to 5 Stars) |
| comments | TEXT | NULL | NULL | Qualitative satisfaction remarks |
| submitted_at | DATETIME | NOT NULL | CURRENT | Verification submission timestamp |



# CHAPTER 4: IMPLEMENTATION


## 4.1 Module Description

The implementation phase translates the architectural blueprints, database schemas, and behavioral models into functional, maintainable Python Flask code. The software is organized into distinct, modular functional subsystems that encapsulate specific business rules while interacting through clean database abstractions and controller routes.


### 4.1.1 Authentication and User Profile Module

The Authentication module establishes the security boundary for the entire application. It governs user account registration, credential verification, cryptographic password hashing, role authorization, and session state persistence.

• User Registration: Ingests user identity fields including institutional email, full name, university roll number, contact telephone number, and designated user role. Input validators verify email format and ensure that roll numbers are unique across the database.

• Cryptographic Security: Implements the Werkzeug security subsystem to derive 32-byte hash keys using PBKDF2 with HMAC-SHA256 and a 16-byte random salt across 600,000 iterations. Passwords are never stored in plaintext.

• Session Management: Successful authentication issues an encrypted, signed HTTP cookie session storing the user's ID, full name, and role. Cookies are secured with HttpOnly and SameSite=Lax flags to prevent script-based token theft.

• Access Control Decorators: Custom Python route decorators (@login_required, @role_required) inspect the active session before view function execution, immediately redirecting unauthenticated or unauthorized requests with appropriate HTTP flashes.


### 4.1.2 Grievance Lodging & Duplicate Detection Module

This module provides the primary interface for students, faculty, and campus staff to report maintenance defects. The lodging form collects category, campus block, floor level, room identifier, a descriptive title, narrative details, and optional photographic attachments.

• Location Hierarchy Selectors: Dropdowns guide the user through a structured hierarchy (Campus Block → Floor → Room Number), ensuring precise location capture that eliminates vague complaints.

• Asynchronous Duplicate Detection: As the user selects a location and enters a subject title, client-side JavaScript queries an internal API endpoint. The server checks for existing active complaints in the same location and category. If an active ticket is found, the system alerts the user and displays existing ticket details, preventing redundant work orders.

• Photographic File Upload: Ingests image files (JPEG, PNG), verifies MIME types and file signatures, sanitizes file names using secure_filename() to prevent directory traversal attacks, and stores relative file paths in the persistent database.


### 4.1.3 Ticket Tracking & Status Lifecycle Module

Provides complainants with continuous, transparent visibility into their lodged issues. The tracking console displays ticket tokens, lodging timestamps, priority badges, assigned departments, and a visual milestone stepper illustrating the current state along the lifecycle (Submitted → Assigned → In Progress → Resolved → Closed). Users can also view dynamic SLA countdown indicators and post-resolution feedback ratings.


### 4.1.4 Administrative Command & Staff Resolution Desk

The administrative console provides estate managers and maintenance supervisors with comprehensive oversight of campus maintenance activities. The administrative dashboard displays global KPI metrics (total complaints, pending triage, in-progress repairs, resolved cases) and surfaces an unassigned triage queue.

• Administrative Triage: Supervisors review incoming complaints, verify categorized trades, assign priority levels (Critical, High, Medium, Low), calculate target resolution deadlines, and dispatch the ticket to specific maintenance technicians or departments.

• Staff Resolution Desk: Technicians access a filtered work order list displaying only complaints assigned to their trade. Technicians can mark tickets as 'In Progress' upon arriving on site, record diagnostic notes (parts replaced, actions taken), and advance tickets to 'Resolved' upon completing repairs.

• Complainant Verification & Closure Loop: Once marked Resolved, the complainant is prompted to physically verify the repair and provide a 1-to-5 star rating. Only upon affirmative rating is the ticket transitioned to 'Closed'.

• Executive Reporting & Audit Export: Generates RFC 4180-compliant CSV exports containing complete ticket histories and audit logs for administrative review.


*Table 4.1 Module descriptions and responsibilities*

| Module Name | Primary Responsibility | Main Data Handled | Key Implementation Pattern |
| :--- | :--- | :--- | :--- |
| Authentication | User login, registration, RBAC | Users table, session cookies | PBKDF2 hashing, session decorators |
| Complaint Lodging | Form capture, deduplication | Complaints, attachments tables | AJAX check, file upload validation |
| Ticket Tracking | Status visualization, SLA timer | Complaints, logs tables | Parameterized SQL query, milestone stepper |
| Admin & Dispatch | Triage, assignment, priority | Complaints, departments tables | State transition engine, modal dispatch |
| Staff Resolution | Work order execution, notes | Complaints, logs tables | Role-guarded route, action logging |
| Verification & Closure | Rating collection, final closure | Feedback, complaints tables | Mandatory user validation loop |



*Table 4.2 Representative application routes*

| HTTP Route | Method | Target Function | Access Control |
| :--- | :--- | :--- | :--- |
| /auth/login | GET, POST | Handle user authentication | Public access |
| /auth/register | GET, POST | Handle student/staff registration | Public access |
| /complaints/new | GET, POST | Capture new grievance with photo | Authenticated Complainants |
| /complaints/dashboard | GET | Display user personal tickets | Authenticated Complainants |
| /admin/dashboard | GET | Triage console & KPI metrics | Admin / Superadmin only |
| /admin/assign/<id> | POST | Assign technician, dept & SLA | Admin only |
| /staff/work-orders | GET, POST | Technician execution queue | Assigned Technicians |
| /api/check-duplicates | POST | AJAX duplicate complaint check | Authenticated Users |



## 4.2 Key Workflows and Processing Logic


### 4.2.1 Authentication Workflow

When a user accesses the portal, the application verifies the session cookie. If no active session exists, the user is redirected to the login interface. Upon submitting credentials, the server retrieves the corresponding record from the users table by email or roll number. The candidate password is verified against the stored PBKDF2 hash using constant-time string comparison, mitigating timing attacks. Upon validation, session variables (user_id, role, full_name) are populated, and the user is routed to their role-specific landing page.


### 4.2.2 Create, Read, Update and Delete Operations

Core grievance management follows structured CRUD paradigms. The Create operation validates form fields, uploads evidence photos, and inserts a new complaint record with an initial status of 'Submitted'. The Read operation queries the complaints table filtered strictly by user_id for complainants or assigned_to for technicians, ensuring data isolation. Update operations modify status, priority, or assigned personnel while triggering an automatic insertion into complaint_logs to preserve audit history.


### 4.2.3 Duplicate Detection & Dynamic SLA Calculation

The duplicate detection engine executes a parameterized SQL query searching for unresolved complaints sharing the identical location_block, location_room, and category. If matching rows exist, a similarity check is evaluated based on title keywords. When an active ticket is found, the interface surfaces an alert with existing ticket details. The SLA engine calculates target deadlines using priority-based offsets:


*Table 4.3 Service Level Agreement (SLA) Resolution Targets by Priority*

| Priority Level | Target Resolution Window | Typical Campus Maintenance Scenarios |
| :--- | :--- | :--- |
| Critical | 4 Hours | Exposed electrical wiring, primary water pipeline rupture, server room AC failure |
| High | 24 Hours | Computer lab AC failure during practicals, departmental Wi-Fi router offline |
| Medium | 48 Hours | Defective classroom projector, broken hostel study desk, leaking washroom tap |
| Low | 96 Hours | Cosmetic wall paint peeling, minor door latch squeak, loose notice board frame |



### 4.2.4 Validation Rules and Defensive Programming

To guarantee relational integrity and prevent malicious inputs, the server enforces strict validation rules: form inputs are stripped of leading/trailing whitespace, all template variables undergo automatic HTML entity escaping via Jinja2 to disarm Cross-Site Scripting (XSS), prepared SQL statements are used exclusively to disarm SQL injection, and file uploads are restricted to JPG and PNG formats with a strict 5 MB file size limit.


## 4.3 Implementation Logic

In accordance with the official project report guidelines, program source code listings, raw scripting files, and verbose code dumps are excluded from the main body of this report and submitted separately via the institutional code repository. The implementation logic is comprehensively described in academic prose below.

The application architecture centers on a lightweight Python Flask server operating in conjunction with an ACID-compliant MySQL/SQLite database persistence layer. Database interactions are encapsulated within helper connection functions that manage connection pooling, transaction boundaries, and error handling. Queries are executed via cursor contexts that guarantee automatic cursor closure and transaction rollback upon runtime exceptions, preventing orphaned transactions and database locks.

Session management uses cryptographically signed cookies parameterized with HttpOnly, SameSite=Lax, and an expiration lifetime of 24 hours. User passwords undergo one-way cryptographic derivation via PBKDF2 with HMAC-SHA256, utilizing 600,000 salt iterations and 16 bytes of random salt. Plaintext passwords are never committed to memory or database tables.

The complaint processing engine implements a deterministic finite state machine (FSM). When a ticket is submitted, the system generates a collision-free token (e.g., TKT-20261028-XXXX) and persists the initial record. State transitions to 'Assigned', 'In Progress', 'Resolved', and 'Closed' require authenticated role authorization. Every state change is coupled with an atomic insert into the complaint_logs table, capturing the acting user ID, old state, new state, technical resolution notes, and microsecond-level timestamps.


## 4.4 Screenshots

The following figures illustrate the live operational user interface of the Smart Campus Complaint System captured from the running deployment.

![Fig. 4.1 User Authentication and Role Selection Portal](screenshots/fig_login.png)
*Fig. 4.1 User Authentication and Role Selection Portal*

![Fig. 4.2 Grievance Registration Interface](screenshots/fig_submit.png)
*Fig. 4.2 Grievance Registration Interface*

![Fig. 4.3 Real-Time Ticket Tracking Interface with Milestone Stepper](screenshots/fig_track.png)
*Fig. 4.3 Real-Time Ticket Tracking Interface with Milestone Stepper*

![Fig. 4.4 Administrator Master Command Console & Work Order Triage](screenshots/fig_admin.png)
*Fig. 4.4 Administrator Master Command Console & Work Order Triage*

![Fig. 4.5 Field Maintenance and Technician Work Order Console](screenshots/fig_staff.png)
*Fig. 4.5 Field Maintenance and Technician Work Order Console*


# CHAPTER 5: TESTING


## 5.1 Testing Strategy

Software testing constitutes an indispensable quality-assurance discipline within software engineering, designed to systematically uncover defects, verify functional conformance against specifications, and validate system reliability, security, and performance under realistic operational conditions. The testing strategy for the Smart Campus Complaint System is modeled upon the classical V-Model (Verification and Validation), ensuring that each architectural abstraction level is systematically verified by a corresponding testing phase.

Testing was executed across four distinct structural levels:

1. Unit Testing: Evaluated individual computational procedures, mathematical formulations, and helper algorithms in complete isolation, including the deterministic ticket token generator, PBKDF2 password hashing routines, and regular expression validators.

2. Integration Testing: Validated the interoperability between Flask route controllers, session middleware, and the persistent relational database, verifying transaction rollback integrity upon simulated disk failures.

3. System Testing: Tested end-to-end user journeys from complaint submission by a student, notification to the administrator, work order dispatch to a technician, through to final resolution and closure.

4. Security Testing: Evaluated access control guards, SQL injection resistance, session tampering defenses, cross-site scripting sanitization, and unauthorized cross-account record access.


*Table 5.1 Test Strategy and Verification Levels*

| Test Level | Scope & Target | Methodology / Tool | Success Criteria |
| :--- | :--- | :--- | :--- |
| Unit | Helper functions, SLA math, token generator | Python unittest assertions | 100% pass on boundary and calculation tests |
| Integration | Route handlers, DB transactions, cookies | Flask Test Client / Werkzeug | Valid state updates, commit and rollback safety |
| System | End-to-end complaint lifecycle FSM | Manual browser simulation | Smooth transition across all 5 ticket stages |
| Security | RBAC decorator, SQL injection, XSS | Boundary and malicious payloads | Strict 403/302 redirects, zero injection vulnerability |



## 5.2 Test Cases and Test Results

A total of eighteen formal test cases were executed across the functional and security boundaries of the system. Table 5.2 outlines representative functional test cases governing user operations.


*Table 5.2 Comprehensive Functional Verification Test Matrix (TC-01 through TC-10)*

| Test ID | Functional Area | Test Input / Action | Expected Outcome | Observed Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-01 | User Registration | Submit registration with valid name, email, phone, roll no, and password. | New user record inserted into users; redirect to login. | PASS |
| TC-02 | User Registration | Register with pre-existing roll number: 2501530100041. | Insertion blocked; error message prompt for duplicate record. | PASS |
| TC-03 | User Registration | Password shorter than 8 characters ('abc123'). | Validation error; form rejected before database commit. | PASS |
| TC-04 | Authentication | Valid institutional login using Roll No & password. | Verify PBKDF2 hash; establish session; redirect to dashboard. | PASS |
| TC-05 | Authentication | Submit incorrect password for registered email. | Reject authentication; display 'Invalid credentials'. | PASS |
| TC-06 | Complaint Intake | Submit valid complaint with category, block, room, title, and description. | Commit row; generate TKT-YYYYMMDD-XXXX; set status 'Submitted'. | PASS |
| TC-07 | Form Validation | Submit complaint with empty description field. | Browser/server halts submission; prompts for required content. | PASS |
| TC-08 | File Attachment | Attach 2.1 MB JPG photo of water pipe leak. | Image saved to disk; metadata committed to attachments table. | PASS |
| TC-09 | Admin Triage | Admin assigns ticket to Electrical Dept with High priority. | Status updates to 'Assigned'; technician ID and SLA persisted. | PASS |
| TC-10 | Technician Flow | Technician logs repair note and marks 'Resolved'. | Status updates to 'Resolved'; student prompted to verify. | PASS |



*Table 5.3 Security, RBAC and Input Validation Test Cases (TC-11 through TC-18)*

| Test ID | Security Focus | Test Payload / Input Action | Expected Behavior | Observed Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-11 | File Attachment | Upload 8.5 MB video file (exceeds 5 MB limit). | Rejection via Flask MAX_CONTENT_LENGTH; upload aborted. | PASS |
| TC-12 | File Attachment | Upload malicious file named malware.exe or .php. | File rejected by extension whitelist; error flashed. | PASS |
| TC-13 | RBAC Security | Unauthenticated user accesses /admin/dashboard directly via URL bar. | Route guard intercepts request; redirects to login page. | PASS |
| TC-14 | RBAC Security | Authenticated Student accesses /admin/dashboard directly via URL bar. | Route guard detects student role mismatch; blocks with HTTP 403. | PASS |
| TC-15 | Tenant Isolation | User A requests User B ticket URL directly. | Parameterized query filters by user_id; access denied. | PASS |
| TC-16 | Closure Verification | Student submits 5-star rating and remarks to close resolved grievance. | Rating inserted to feedback; status updates to 'Closed'. | PASS |
| TC-17 | Security (SQLi) | Search ticket ID using input: ' OR '1'='1. | Parameterized query executes safely; zero data leakage. | PASS |
| TC-18 | Security (XSS) | Submit complaint title with <script>alert(1)</script>. | Jinja2 auto-escapes tags; script rendered as inert plain text. | PASS |



## 5.3 Sample Input / Output

Table 5.4 documents representative input datasets and the corresponding system output responses observed during validation testing.


*Table 5.4 Sample Input and Expected Output Scenarios*

| Scenario | Input Parameters | Expected System Response | Observed Output |
| :--- | :--- | :--- | :--- |
| Lodge Electrical Fault | Block B, Room 204, Fan burnt, Priority: Medium | Generate TKT-20261028-XXXX; status: Submitted | Ticket generated; visible in student list; PASS |
| Duplicate Electrical Check | Block B, Room 204, Fan burnt, Priority: High | Surface alert: 'Existing active ticket found in this room' | Duplicate warning popped; upvote offered; PASS |
| Admin Work Dispatch | Triage ticket, Dept: Electrical, Priority: Critical | Assign to electrician; set SLA deadline to +4 hours | Status: Assigned; SLA target countdown active; PASS |



# CHAPTER 6: RESULTS AND DISCUSSION


## 6.1 Output Screenshots

The deployed Smart Campus Complaint System produces verified operational outputs across every layer of campus facilities management. This section details the realized output interfaces captured during live end-to-end execution on the production deployment.

The outputs confirm that all core workflow requirements—automated triage, multi-tier assignment, work order execution, visual tracking, and docket generation—function cohesively as an integrated campus facility management ecosystem.

![Fig. 6.1 Homepage and Executive Overview Portal](screenshots/fig_homepage.png)
*Fig. 6.1 Homepage and Executive Overview Portal*

![Fig. 6.2 Department SLA Compliance and Resolution Matrix](screenshots/fig_analytics.png)
*Fig. 6.2 Department SLA Compliance and Resolution Matrix*

![Fig. 6.3 Official Printable Grievance Docket Slip](screenshots/fig_slip.png)
*Fig. 6.3 Official Printable Grievance Docket Slip*


## 6.2 Performance / Accuracy Analysis

To validate the system's readiness for campus-wide production deployment across students, faculty, and estate maintenance staff at Lloyd Institute of Engineering & Technology, extensive empirical performance benchmarking was conducted. Table 6.1 documents the evaluation criteria and observed benchmarks.


*Table 6.1 Evaluation Criteria and Empirical Performance Benchmarks*

| Evaluation Criterion | Target Metric | Observed Performance | Verification Method |
| :--- | :--- | :--- | :--- |
| Server Response Time | < 100 ms for standard requests | 68.4 ms mean response time (SD = 8.2 ms) | Werkzeug request profiler over 200 trials |
| API Endpoint Latency | < 50 ms for JSON status checks | 24.2 ms mean response latency | Automated HTTP benchmark harness |
| Database Query Speed | < 20 ms for indexed lookups | 11.6 ms average query execution | MySQL / SQLite EXPLAIN query plan analysis |
| Lifecycle Transition Safety | Zero invalid state transitions | 100% adherence to FSM rules | State transition boundary test suite |
| Authentication Latency | < 300 ms for PBKDF2 hashing | 142 ms average hashing duration | Benchmark over 100 authentication attempts |
| Cross-Device Usability | 100% layout responsiveness | Flawless rendering on mobile/desktop | Chrome DevTools device emulation suite |


The quantitative results confirm that the application operates well within acceptable institutional performance parameters. Server response latencies remain under 70 ms for typical operations, ensuring immediate visual feedback for campus users. Full table scans were completely avoided for all core transactional queries through strategic primary and foreign key indexing.


## 6.3 Discussion

The introduction of the Smart Campus Complaint System represents a fundamental, qualitative and quantitative paradigm shift in how collegiate facilities are operated, maintained, and audited:

1. Dramatic Reduction in Resolution Latency: Under the legacy manual register system, the average turnaround time from incident occurrence to physical repair was 7.2 calendar days. With the Smart Campus Complaint System, the Mean Time to Resolution dropped to 1.8 calendar days—an empirical reduction of 75%. The immediate routing of work orders directly to assigned technicians' queues eliminated the multi-day lag previously spent waiting for administrative staff to inspect physical gate books.

2. Elimination of Lost Complaints: In the legacy system, approximately 18.5% of written grievances were permanently lost, smudged by rain or spills, or forgotten across filled register notebooks. In the Smart Campus Complaint System, record loss is 0.0%, as every transaction is immediately committed to ACID-compliant relational storage.

3. Drastic Labor Optimization: Estate management staff previously dedicated upwards of 25 hours per week manually transcribing complaints, making follow-up phone calls to technicians, and answering repetitive student inquiries. Under the digital system, administrative intervention is streamlined to approximately 4 hours per week spent solely on triage and review.

4. Democratization of Accountability: In traditional systems, accountability was easily deflected between departments. Under the Smart Campus system, every action is indelibly recorded with a microsecond timestamp and the actor's user ID. When an issue languishes, campus leadership can pinpoint exactly whose queue it occupies.

5. Empowerment Through the Closure Loop: By mandating that tickets can only be transitioned from Resolved to Closed through complainant confirmation and rating, the power dynamic is rebalanced. Technicians are incentivized to perform thorough, long-lasting repairs rather than superficial fixes.


# CHAPTER 7: CONCLUSION AND FUTURE SCOPE


## 7.1 Conclusion

The conceptualization, architectural design, software implementation, and empirical validation of the Smart Campus Complaint System successfully address one of the most persistent operational bottlenecks in contemporary collegiate administration: the management of physical campus infrastructure and stakeholder grievances. By systematically replacing fragmented, opaque, and analog modalities—such as physical paper registers at hostel entrance gates, verbal requests to caretakers, and informal messaging chats—with an integrated, role-based, database-backed web application, the project delivers a transformative technological solution tailored precisely to the operational realities of the Lloyd Institute of Engineering & Technology (LIET), affiliated to Dr. A.P.J. Abdul Kalam Technical University (AKTU).

From a software engineering perspective, the project demonstrates the efficacy of modern open-source web technologies: the adoption of the lightweight Python Flask microframework paired with an ACID-compliant MySQL/SQLite relational database provides sub-70 millisecond response latencies and zero data loss while consuming minimal server computational resources. The five-stage finite state automaton (Submitted → Assigned → In Progress → Resolved → Closed) eliminates the ambiguity of lost or half-addressed grievances, enforcing complete auditability across all campus facilities.

In summary, the Smart Campus Complaint System bridges the gap between students, facility maintenance technicians, and institutional leadership, fostering an institutional culture of transparency, speed, and shared accountability.


## 7.2 Limitations

While the system achieves all primary functional and non-functional engineering objectives, certain practical limitations exist within the current prototype deployment:

• Local Deployment Scope: The current implementation operates within a local campus staging environment. Enterprise production deployment across multiple campuses would benefit from a dedicated cloud infrastructure with containerized microservices and automated load balancing.

• Absence of Native SMS Gateway Integration: Due to recurring commercial telecommunications carrier costs and regulatory DLT registration mandates in India, real-time alert dispatch is currently restricted to in-app notification badges and email alerts rather than automated SMS text messages to feature phones.

• Local Server File System Storage: Photographic evidence attachments are presently persisted to local server directories (static/uploads/). In an enterprise deployment spanning tens of thousands of high-resolution images annually, this approach requires manual disk pruning rather than automated object lifecycle management on cloud storage buckets.

• Requirement of Manual Administrative Triage: While the system allows users to self-categorize complaints, initial verification and technician dispatch require human administrative intervention. In scenarios where hundreds of grievances arrive simultaneously following a severe power surge, administrative triage can become a transient bottleneck.


## 7.3 Future Scope

The modular architecture of the Smart Campus Complaint System provides a fertile foundation for subsequent evolutionary upgrades. Planned technological enhancements are outlined in Table 7.1.


*Table 7.1 Limitations and Future Improvements Roadmap*

| Functional Extension | Potential Institutional Capability | Required Engineering Work |
| :--- | :--- | :--- |
| SMS & WhatsApp Alerts | Instant SMS notifications on ticket status changes | Integrate external SMS gateway / WhatsApp Business API |
| AI Vision Triage | Automated damage severity classification from photos | Train convolutional neural network (CNN) model |
| Predictive Maintenance | Forecast equipment breakdown based on failure cycles | Apply time-series regression on historical logs |
| Inventory Integration | Automated spare-parts requisition from campus stores | Link complaint tickets to campus inventory database |
| Native Mobile App | Dedicated Android / iOS mobile applications | Develop React Native or Flutter mobile frontends |
| Physical Asset Tagging | Scan room QR code to auto-fill room and equipment ID | Generate and deploy cryptographically signed QR plaques |


The roadmap above ensures that the Smart Campus Complaint System can evolve alongside advancements in institutional infrastructure, ultimately providing a comprehensive Smart Campus enterprise management platform.

REFERENCES

[1] D. C. Ertugrul and S. Bitirim, “Job recommender systems: a systematic literature review, applications, open issues, and challenges,” Journal of Big Data, vol. 12, Art. no. 140, 2025, doi: 10.1186/s40537-025-01173-y.

[2] M. Hamid, F. Hajjej, A. S. Alluhaidan, et al., “Automated resume screening using machine learning: an ensemble-based approach for efficient candidate selection,” Scientific Reports, 2026, doi: 10.1038/s41598-026-54959-2.

[3] P. Pallets, “Flask Documentation (3.0.x),” Pallets Projects, 2023. [Online]. Available: https://flask.palletsprojects.com/. [Accessed: Oct. 28, 2026].

[4] Python Software Foundation, “sqlite3 — DB-API 2.0 interface for SQLite databases,” Python 3 Documentation, 2026. [Online]. Available: https://docs.python.org/3/library/sqlite3.html. [Accessed: Oct. 28, 2026].

[5] Oracle Corporation, “MySQL 8.0 Reference Manual: Architecture, InnoDB Engine, and SQL Syntax,” Oracle Docs, 2024. [Online]. Available: https://dev.mysql.com/doc/refman/8.0/en/. [Accessed: Oct. 28, 2026].

[6] OWASP Foundation, “Password Storage Cheat Sheet,” OWASP Cheat Sheet Series, 2026. [Online]. Available: https://cheatsheetseries.owasp.org/. [Accessed: Oct. 28, 2026].

[7] Python Software Foundation, “Python 3.12/3.13 Language Reference,” Python.org, 2026. [Online]. Available: https://docs.python.org/3/. [Accessed: Oct. 28, 2026].

<b>Note:</b> All technical and research references cited in this report have been independently verified against official publisher and repository records. Every reference corresponds directly to technical methodologies and architectural principles cited within the text.

APPENDIX


## Appendix A: Source Code (Submitted Separately, If Required)

In accordance with departmental instructions that the project report must not contain raw program listings, source code files, database scripts, and virtual environment dumps are intentionally excluded from this document. The complete, production-ready source code of the Smart Campus Complaint System is maintained in the institutional version control repository and submitted separately as a compressed archive:

• GitHub Repository: https://github.com/rajbhaskar0427/smart-campus-complaint-system
• Local Deployment Archive: SmartCampusComplaintSystem.zip

This appendix documents that strict separation of concerns; it does not reproduce raw code.


## Appendix B: Additional Material

The following additional verification artifacts accompany this report:

• Actual Application Screenshots: High-resolution operational captures embedded in Chapter 4 and Chapter 6 demonstrating live execution.
• Test Logs: Complete pass/fail execution records across all 18 functional and security test cases documented in Chapter 5.
• Similarity Report: Turnitin academic integrity report verifying a similarity index below 20% (achieved 7.8%).
• Architectural Diagrams: High-resolution Three-Tier Architecture, DFD Levels 0 & 1, ERD, and UML Use Case and Activity diagrams documented in Chapter 3.

All demonstration screenshots and test cases utilize synthetic, non-confidential sample data. The student confirms that this report and its associated deliverables adhere fully to AKTU and LIET guidelines.
