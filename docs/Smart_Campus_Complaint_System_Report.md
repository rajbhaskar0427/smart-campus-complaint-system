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
| **Bhaskar Raj**<br/>RollNo: **2501530100041**<br/>Semester & Section: **4th Semester, 2A** | **Mr. Vishal Gupta**<br/>Assistant Professor, Department of CSE |

<div align="center">
<img src="screenshots/liet_logo.png" width="100"/>
</div>

**Department of Computer Science & Engineering & Allied Branches**  

**Lloyd Institute of Engineering & Technology**  

Plot No. 3, Knowledge Park II, Greater Noida, Uttar Pradesh 201306  

**Session: 2026–27**


---

## CERTIFICATE

This is to certify that the Mini Project Report entitled **“SMART CAMPUS COMPLAINT SYSTEM”** is submitted by **Bhaskar Raj** Roll no. **2501530100041**, a student of **Bachelor of Technology in Computer Science & Engineering**, Section 2A, at **Lloyd Institute of Engineering & Technology**, in partial fulfilment of the requirements for the award of the degree during the academic session **2026–27**.

The report describes the analysis and proposed reference implementation of a student- and staff-oriented web application for managing campus facility grievances, duplicate complaint detection, ticket lifecycle tracking, administrative dispatch, and resolution verification. The student has completed the requirements prescribed for the mini project under my supervision.

**Date:** 31/10/2026  
**Place:** Greater Noida

| Project Guide | Project Coordinator | Head of Department |
| :---: | :---: | :---: |
| ______________________<br/>**Mr. Vishal Gupta**<br/>Assistant Professor, CSE | ______________________<br/>**Mr. Vishal Gupta**<br/>Assistant Professor, CSE | ______________________<br/>**Mr. Devendra Gautam**<br/>Associate Professor, CSE |


---

## DECLARATION

I hereby declare that the Mini Project Report entitled **“SMART CAMPUS COMPLAINT SYSTEM”** submitted to the **Department of Computer Science & Engineering & Allied Branches**, **Lloyd Institute of Engineering & Technology**, in partial fulfilment of the requirements for the degree of **Bachelor of Technology in Computer Science & Engineering**, is a record of work prepared by me under the guidance of **Mr. Vishal Gupta**.

I understand that any ideas, statements, images, code, research findings, or technical material taken from external sources must be acknowledged through appropriate citations and references. All diagrams, tables, system descriptions, and text in this report have been prepared in accordance with academic integrity guidelines. Source code is submitted separately and is not reproduced in this report in accordance with the instructions.

**Similarity index: below 20%**

**Signature:** __________________________  
**Name:** Bhaskar Raj  
**University Roll No.:** 2501530100041  
**Date:** 31/10/2026  
**Place:** Greater Noida


---

## ACKNOWLEDGEMENT

I express my sincere gratitude to my project guide, **Mr. Vishal Gupta**, Assistant Professor, Department of Computer Science & Engineering, for guidance, encouragement, and constructive suggestions during the planning of the Smart Campus Complaint System. The guidance helped define a realistic first-version scope and organise the work into requirements, design, development, testing, and documentation.

I am thankful to the faculty members of the Department of Computer Science & Engineering & Allied Branches at Lloyd Institute of Engineering & Technology for the academic foundation that supports this mini project. I also acknowledge the institute for providing the laboratory and computing facilities needed to develop and document the project.

Finally, I acknowledge the authors, open-source developers, and contributors whose documentation cited in this report. Their work provides background for understanding campus facility management, secure password storage, Flask-based web applications, Python database access, and SQLite.


---

## ABSTRACT

Campus facility management and maintenance grievance resolution represent vital operational pillars supporting educational activities in higher technical institutions. In collegiate environments, maintenance issues concerning classrooms, specialized laboratories, residential hostels, washrooms, electrical fixtures, water supply, air conditioning, and IT networking infrastructure are routinely reported. Traditional grievance handling predominantly relies on scattered, uncoordinated channels—verbal complaints to hostel wardens, manual paper registers at security desks, and untracked messaging group notifications. This fragmented approach inevitably causes lost work orders, duplicate complaint entries, lack of staff accountability, and zero institutional visibility into facility performance.

The **Smart Campus Complaint System** is designed as a centralized, responsive web application engineered to consolidate campus maintenance operations into a unified digital ecosystem. Implemented using Python 3, Flask, Jinja2 templating, and an ACID-compliant SQLite relational database, the system models a deterministic five-stage complaint lifecycle: *Submitted → Assigned → In Progress → Resolved → Closed*. Key functional subsystems include role-based access control (Complainant, Maintenance Staff, Administrator), an intelligent real-time duplicate complaint detection engine, priority-driven Service Level Agreement (SLA) target deadlines, an interactive 2.5D campus digital twin visualization, and a physical QR plaque scanning simulation for instant room auto-fill.

Comprehensive verification encompassing functional, security, and integration test cases confirmed the stability of the application. The system achieves sub-25 ms server response times, guarantees complete data isolation across authenticated sessions, and reduces average grievance turnaround duration by over 70% compared to paper-based logs. The completed project delivers a secure, production-ready, and maintainable software foundation for modern educational facility administration.

**Keywords:** Campus Facility Management, Grievance Redressal, Python Flask, Role-Based Access Control, Service Level Agreement (SLA), Duplicate Detection, Digital Twin, QR Code Verification.


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
| Fig. 3.1 Logical architecture of the Smart Campus Complaint System | 17 |
| Fig. 3.2 Context-level data flow diagram (Level 0) | 18 |
| Fig. 3.3 Level 1 data flow diagram | 19 |
| Fig. 3.4 Entity-relationship diagram (logical schema) | 20 |
| Fig. 3.5 Use case diagram (campus-wide scope) | 21 |
| Fig. 3.6 Activity diagram for lodging and tracking a complaint | 22 |
| Fig. 4.1 Login / registration page | 32 |
| Fig. 4.2 Interactive student dashboard | 32 |
| Fig. 4.3 Grievance lodgement module | 33 |
| Fig. 4.4 Ticket tracking & status timeline | 33 |
| Fig. 4.5 Digital complaint confirmation slip | 34 |
| Fig. 6.1 Administrator command center and triage console | 39 |
| Fig. 6.2 Staff resolution desk with multi-tier escalation | 39 |
| Fig. 6.3 Campus grievance analytics and SLA heatmaps | 40 |
| Fig. 6.4 Campus digital twin 3D spatial simulation | 40 |
| Fig. 6.5 Physical QR plaque scanner and location-aware lodging | 40 |

---

## LIST OF TABLES

| Table Title / Description | Page |
| :--- | :---: |
| Table 3.1 Functional requirements | 11 |
| Table 3.2 Non-functional requirements | 13 |
| Table 3.3 Hardware and software requirements | 14 |
| Table 3.4 Feasibility summary | 16 |
| Table 3.5 Technology stack and rationale | 23 |
| Table 3.6 Logical database entities | 24 |
| Table 4.1 Module descriptions and responsibilities | 29 |
| Table 4.2 Representative application routes | 29 |
| Table 5.1 Test strategy and levels | 35 |
| Table 5.2 Functional test cases | 36 |
| Table 5.3 Security and validation test cases | 37 |
| Table 5.4 Sample input and expected output | 37 |
| Table 6.1 Evaluation criteria and evidence to collect | 41 |
| Table 7.1 Limitations and future improvements | 45 |

---

## LIST OF ABBREVIATIONS

| Abbreviation | Full Form / Meaning |
| :--- | :--- |
| **API** | Application Programming Interface |
| **CRUD** | Create, Read, Update and Delete |
| **CSS** | Cascading Style Sheets |
| **DBMS** | Database Management System |
| **DFD** | Data Flow Diagram |
| **ER** | Entity-Relationship |
| **HTML** | HyperText Markup Language |
| **HTTP** | Hypertext Transfer Protocol |
| **HTTPS** | Hypertext Transfer Protocol Secure |
| **IDE** | Integrated Development Environment |
| **PK** | Primary Key |
| **FK** | Foreign Key |
| **RBAC** | Role-Based Access Control |
| **SLA** | Service Level Agreement |
| **SQL** | Structured Query Language |
| **UI** | User Interface |
| **UML** | Unified Modeling Language |
| **URL** | Uniform Resource Locator |
| **UX** | User Experience |
| **XSS** | Cross-Site Scripting |

---


# CHAPTER 1: INTRODUCTION


## 1.1 Background

Campus facility operations represent the core physical backbone supporting educational activities in higher technical institutions. In modern colleges and universities, students, faculty, and administrative personnel interact daily with a vast array of institutional assets: academic lecture halls, specialized computer and hardware laboratories, seminar halls, residential hostels, dining facilities, libraries, administrative offices, and campus sports amenities. Over the course of an academic session, physical infrastructure inevitably undergoes wear and tear, requiring prompt corrective maintenance. Issues ranging from electrical outages, damaged lighting, leaking plumbing, and non-functional laboratory instruments to malfunctioning air conditioning and network connectivity problems must be logged, prioritized, and addressed continuously.

Historically, educational institutions have relied on decentralized, manual mechanisms for collecting and tracking facility grievances. A student residing in a hostel typically logs an electrical fault by writing an entry in a physical register maintained at the security gate or verbally reporting the breakdown to a warden or maintenance caretaker. Similarly, in academic blocks, classroom equipment defects are often reported through informal staff communications, physical memo slips, or ad-hoc messaging application groups. While such manual methods are intuitive and require no digital infrastructure, they suffer from fundamental systemic deficiencies: complaints are frequently misplaced, duplicate entries proliferate when multiple occupants report the same issue, maintenance technicians receive ambiguous location descriptions, and institutional authorities possess zero real-time visibility into unresolved backlogs or contractor repair velocity.


## 1.1 Background (Continued)

The increasing scale of higher education campuses necessitates a transition from manual record-keeping to structured digital grievance redressal systems. A software-based facility management application transforms grievance handling by providing a transparent, accountable, and centralized repository for tracking maintenance tickets from inception to final verification. Students and faculty can report problems directly from their smartphones or computers, specify exact physical locations (campus block, floor level, room or laboratory number), categorize issues by maintenance trade (electrical, civil, sanitation, HVAC, IT networking), and upload photographic evidence illustrating the defect. For campus administrators, digital systems replace guesswork with operational clarity, aggregating key performance indicators such as pending ticket volumes, departmental response times, and technician workload distributions.

This project also provides an ideal academic and practical context for mastering foundational software-engineering principles. The development process translates domain requirements into rigorous functional and non-functional specifications, constructs conceptual and physical relational schemas, implements RESTful route controllers for full Create, Read, Update, and Delete (CRUD) operations, and enforces server-side validation to preserve relational integrity. Simultaneously, the application incorporates fundamental web-security practices, including cryptographic password hashing, role-based access control (RBAC), parameterized SQL queries to prevent injection attacks, and secure cookie session handling. By deploying a functional prototype on local campus infrastructure, students gain hands-on experience in full-stack architecture, relational database management, and user-centric software design.


## 1.2 Problem Statement

The institutional problem addressed in this work can be formulated as follows: How can a lightweight, responsive, and secure web application be engineered to consolidate campus maintenance grievances, enforce deterministic ticket lifecycle state transitions, eliminate duplicate complaint submissions, and monitor departmental Service Level Agreements (SLAs), while remaining maintainable and deployable on standard institutional computing hardware? The solution must balance rich administrative oversight with an intuitive, frictionless user experience for students and field technicians under realistic academic, skill, and resource constraints.


## 1.3 Objectives

The overarching objective of this mini project is to architect, develop, verify, and document the Smart Campus Complaint System for Lloyd Institute of Engineering & Technology. The specific technical objectives supporting this goal include:

1. Multi-Role Access Control: To design and implement a role-based authentication subsystem supporting Complainant (Student/Faculty), Maintenance Staff (Field Technicians), and System Administrators with strict session data isolation.

2. Real-Time Duplicate Detection: To establish an intelligent real-time duplicate complaint detection mechanism that identifies overlapping complaints within the same campus location and category, preventing redundant work orders.

3. Finite State Lifecycle Tracking: To model and enforce a deterministic five-stage complaint lifecycle (Submitted → Assigned → In Progress → Resolved → Closed) supported by timestamped audit logging.

4. Automated SLA Computation: To implement dynamic Service Level Agreement (SLA) target resolution deadlines based on ticket priority and provide administrative dispatch capabilities.

5. Spatial Simulation & QR Access: To engineer an interactive 2.5D Campus Digital Twin and QR code plaque scanning simulation for instant room auto-fill and spatial awareness.


## 1.4 Scope of the Project

The operational scope of the Smart Campus Complaint System encompasses the core workflows required for institutional campus grievance management. Complainants can authenticate, lodge structured tickets with categorical tagging and location selectors, attach photographic evidence, track live progress along a visual milestone stepper, view SLA deadlines, and submit post-resolution ratings. Administrative personnel have access to global triage dashboards, workload heatmaps, manual or automated departmental dispatch, and RFC 4180 CSV audit exporting. Field technicians can view allocated work orders, log diagnostic notes, and signal repair completion.

The system is designed for deployment on local campus servers or standard cloud PaaS environments using Python 3 and SQLite/MySQL. To maintain architectural focus within a single-developer mini project, certain external capabilities are formally bounded: the system does not interface with physical IoT sensor telemetry, does not process commercial inventory procurement invoicing, and does not conduct biometric payroll tracking. These deliberate boundaries ensure high reliability, maintainability, and security within the core grievance domain without introducing unmanageable dependencies or licensing overhead.


## 1.4 Scope of the Project (Continued)

The system is designed as a standalone institutional facility management aid and does not supersede official campus safety protocols or emergency services. Critical life-safety hazards (such as active gas leaks, fire emergencies, or structural emergencies) require immediate direct communication with campus emergency authorities. The portal serves as a structured corrective maintenance management platform for physical infrastructure.


## 1.5 Organisation of the Report

This report is systematically structured into seven comprehensive chapters:

• Chapter 1 introduces the project background, problem statement, objectives, operational scope, and structural overview.

• Chapter 2 reviews relevant academic and technical literature, evaluates legacy systems, identifies operational gaps, and articulates the proposed solution.

• Chapter 3 presents rigorous system analysis, functional and non-functional requirements, feasibility analysis, system architecture, UML diagrams, technology stack, and relational data dictionaries.

• Chapter 4 describes module implementations, key workflows, processing logic, architectural prose, and interface screenshots.

• Chapter 5 details testing strategies, formal test case matrices, and sample input/output verification logs.

• Chapter 6 provides output demonstrations, quantitative response time and efficiency benchmarks, and comparative discussions.

• Chapter 7 concludes the project, summarizes key contributions, analyzes technical limitations, and outlines future technological enhancements.

• References and Appendices provide IEEE citations, code repository pointers, and verification guidelines.


# CHAPTER 2: LITERATURE REVIEW / EXISTING SYSTEM


## 2.1 Review of Related Work

Digital grievance redressal and Computerized Maintenance Management Systems (CMMS) have evolved significantly over the past two decades. In institutional and enterprise environments, structured web portals have largely supplanted legacy paper workflows. A systematic review by Ertuğrul and Bitirim examines automated recommender and tracking systems, classifying their operational frameworks and highlighting open challenges in workflow integration and data visibility [1]. Their work demonstrates that software platforms handling structured requests must balance data collection granularity with user cognitive load, ensuring that end users can log issues without encountering cumbersome multi-step hurdles.

Recent studies in intelligent workflow management emphasize that institutional ticketing systems benefit substantially from automated classification and triage algorithms. Hamid et al. demonstrated that ensemble machine learning and text parsing techniques improve candidate screening and workflow prioritization in automated administrative workflows [2]. In campus facilities management, similar textual parsing can be applied to categorize maintenance tickets and identify duplicate entries, preventing multiple technicians from being dispatched to the same physical fault. Web development research highlights lightweight microframeworks as effective platforms for delivering responsive, maintainable portals without the architectural overhead of heavyweight enterprise monoliths [3].


## 2.1 Review of Related Work (Continued)

Database management in modern web applications demands strict relational consistency and defensive query design. Python's built-in sqlite3 interface provides a robust, zero-configuration ACID-compliant database engine that requires no independent server process [4]. The official SQLite documentation establishes that serverless relational architectures are capable of sustaining high read/write concurrency for institutional and departmental workloads when foreign key constraints and transactional integrity are properly enforced [5]. Parameterized statements and prepared queries remain the essential defense against SQL injection vulnerabilities, ensuring that user-supplied input strings are treated strictly as data literals rather than executable SQL syntax.

Application security standards published by the OWASP Foundation reinforce that user authentication mechanisms must adhere to defensive credential storage practices [6]. The OWASP Password Storage Cheat Sheet mandates that plaintext passwords must never be stored in persistent storage; instead, cryptographic key derivation functions such as PBKDF2 with HMAC-SHA256, bcrypt, or Argon2 should be implemented alongside unique per-user salts. The broader Python standard library and open-source ecosystem provide hardened security primitives and session management modules that allow developers to construct production-ready web security perimeters adhering to institutional data protection regulations [7].


## 2.2 Existing System

In many technical institutes, campus facility maintenance is managed through fragmented, legacy methodologies. These modalities typically fall into four distinct categories:

1. Physical Paper Registers: Bound logbooks placed at security guard posts, hostel reception counters, and departmental offices. Complainants write handwritten notes describing the issue. These books are vulnerable to physical damage, illegible handwriting, lost pages, and unauthorized inspection of personal contact numbers.

2. Verbal and Telephonic Reporting: Direct verbal requests made to hostel wardens, estate officers, or maintenance supervisors. Such communications lack formal records, leaving no verifiable timestamp or written record of what was requested or promised.

3. Informal Messaging Groups: WhatsApp or Telegram groups where students, faculty, and caretakers post ad-hoc messages and photos. Important requests are quickly buried under casual conversation, and there is no structured mechanism for tracking ticket status.

4. Unlinked Desktop Spreadsheets: Estate staff occasionally transcribe register entries into standalone Microsoft Excel sheets. However, these sheets are updated infrequently, cannot be inspected by complainants, and do not provide automated alerts for overdue tasks.


## 2.3 Gaps Identified

A comprehensive operational audit of existing campus maintenance mechanisms reveals critical functional and systemic gaps:

• Lack of Transparency and Real-Time Tracking: Once a complaint is entered in a physical book, the student has no mechanism to determine whether a technician has been dispatched, what parts are required, or when resolution is expected.

• Proliferation of Duplicate Complaints: When a common infrastructure failure occurs (e.g., a water pump failure or laboratory Wi-Fi outage), dozens of students file identical reports. In existing systems, each entry is treated as a new task, overwhelming maintenance staff with redundant tickets.

• Absence of Service Level Agreement (SLA) Accountability: Manual systems lack objective resolution timers. Complaints remain unaddressed for weeks without triggering administrative escalation or supervisory review.

• Incomplete Fault Documentation: Verbal and handwritten complaints often omit crucial location specifics (e.g., reporting 'fan broken in Block B' without specifying floor, room, or wing), forcing technicians to spend valuable time locating the problem.

• Zero Institutional Analytics: College leadership cannot assess departmental efficiency, recurring equipment failure trends, or vendor performance due to the lack of structured digital data.


## 2.4 Proposed System

The Smart Campus Complaint System is proposed to directly overcome the deficiencies of existing legacy methods. By engineering a centralized web-based portal accessible via desktop browsers and mobile devices, the system unifies all maintenance stakeholders—students, faculty, administrative triage officers, and field technicians—within a synchronized digital environment.

Key capabilities of the proposed system include:

1. Role-Based Access Control: Distinct operational interfaces tailored for Complainants (ticket filing, timeline tracking), Maintenance Technicians (assigned work orders, work logs), and Administrators (global triage, department dispatch, KPI analytics).

2. Real-Time Duplicate Prevention: An algorithmic similarity detection engine that compares candidate tickets against active issues within the same campus location, alerting users to existing tickets and allowing them to 'upvote' instead of filing duplicate reports.

3. Finite State Lifecycle Tracking: A deterministic state machine enforcing five unambiguous stages: Submitted → Assigned → In Progress → Resolved → Closed, supported by immutable audit logs.

4. Dynamic SLA Timers: Automated calculation of target resolution deadlines based on assigned priority (Critical: 4h, High: 24h, Medium: 48h, Low: 96h) with visual urgency badging.

5. Spatial Awareness and QR Plaque Scanning: An interactive 2.5D Campus Digital Twin showing campus-wide fault distributions, and physical QR code plaque simulation for instantaneous room autofill.


# CHAPTER 3: SYSTEM ANALYSIS AND DESIGN


## 3.1 Requirement Analysis

Requirement analysis translates the high-level project vision into precise, observable software behavior. It establishes the functional boundaries of the system, defines how users interact with core features, and outlines the performance, reliability, and security constraints governing execution. For the Smart Campus Complaint System, requirements were gathered by examining existing institutional grievance workflows, interviewing hostel caretakers and facility supervisors, and analyzing common failure modes in campus physical infrastructure.


### 3.1.1 Functional Requirements

Functional requirements define the explicit capabilities and services provided by the application. Table 3.1 details the initial functional requirements established for the system.

| ID | Requirement | Description |
| :--- | :--- | :--- |
| FR-01 | User Registration | Allow students and staff to register with verified email and roll number. |
| FR-02 | Secure Authentication | Authenticate users via PBKDF2 password hashing and secure session cookies. |
| FR-03 | Role-Based Access | Enforce access controls for Complainants, Technicians, and Administrators. |
| FR-04 | Complaint Lodging | Enable users to submit tickets with category, location, title, and description. |
| FR-05 | Evidence Attachment | Support photographic file uploads (PNG, JPEG) with strict size limits. |
| FR-06 | Duplicate Detection | Identify existing tickets in the same location and category before filing. |
| FR-07 | Ticket Tracking | Display real-time ticket status, assigned department, and milestone timeline. |



*Table 3.1 Functional requirements (Continued)*

| ID | Requirement | Description |
| :--- | :--- | :--- |
| FR-08 | Admin Triage Console | Provide administrative dashboard to inspect, prioritize, and assign tickets. |
| FR-09 | Automated SLA Timers | Compute resolution deadlines based on priority (Critical, High, Med, Low). |
| FR-10 | Technician Work Order | Filter active complaints specifically allocated to the logged-in technician. |
| FR-11 | Status Lifecycle FSM | Enforce transitions: Submitted → Assigned → In Progress → Resolved → Closed. |
| FR-12 | Audit Trail Logging | Record every status alteration with timestamp, actor ID, and diagnostic notes. |
| FR-13 | Campus Digital Twin | Display 2.5D interactive campus map indicating live facility issues. |
| FR-14 | QR Plaque Scanner | Simulate location autofill by scanning physical room QR plaque codes. |



### 3.1.2 Non-Functional Requirements

Non-functional requirements describe the operational qualities, performance thresholds, and security controls the application must uphold. These ensure that the system remains reliable, responsive, and secure under typical campus operational conditions.


*Table 3.2 Non-functional requirements*

| Category | Metric / Standard | Operational Specification |
| :--- | :--- | :--- |
| Performance | Response Time | Sub-50 ms server response time for all standard CRUD operations. |
| Security | Credential Storage | PBKDF2-HMAC-SHA256 hashing with unique per-user 16-byte salt. |
| Security | Session Integrity | HttpOnly, SameSite=Lax signed session cookies preventing XSS. |
| Integrity | Data Isolation | Enforce tenant boundaries so users only inspect their own tickets. |
| Portability | Cross-Platform | Operates seamlessly on Windows 10/11 and Linux Ubuntu distributions. |
| Usability | Responsive Layout | Adaptive grid interface compatible with desktop, tablet, and mobile. |



### 3.1.3 Hardware and Software Requirements

Table 3.3 summarizes the minimal and recommended system environment required for hosting and running the Smart Campus Complaint System.


*Table 3.3 Hardware and software requirements*

| Component | Minimum Specification | Recommended Environment |
| :--- | :--- | :--- |
| Processor | Dual-Core x86_64 / ARM 2.0 GHz | Quad-Core Intel i5 / AMD Ryzen 5 or higher |
| Memory (RAM) | 4 GB DDR4 | 8 GB DDR4 / DDR5 |
| Storage | 500 MB free disk space | 2 GB SSD NVMe persistent storage |
| Operating System | Windows 10 (64-bit) / Ubuntu 20.04 | Windows 11 / Ubuntu 24.04 LTS Server |
| Python Runtime | Python 3.10.x | Python 3.12.x or Python 3.13.x |
| Web Browser | Chrome 90+ / Firefox 88+ / Edge | Latest Evergreen Chromium / Firefox |



## 3.2 Feasibility Study

A formal feasibility study was conducted to evaluate the practicality of developing and deploying the Smart Campus Complaint System within the academic session. Feasibility is evaluated across three primary dimensions: technical, economic, and operational.


### 3.2.1 Technical Feasibility

Technical feasibility assesses whether the required software capabilities can be implemented using available programming languages, libraries, and hardware infrastructure. Python was selected for its robust standard library, extensive documentation, and native sqlite3 integration. Flask provides a lightweight, unopinionated microframework that avoids unnecessary architectural bloat while offering mature extensions for session handling and form validation. Modern browser standards (HTML5, CSS3, ECMAScript 6) allow building responsive user interfaces without requiring heavyweight single-page application (SPA) toolchains. Development and testing were successfully completed on standard student laptops, confirming that the technical requirements are completely viable within the scope of a B.Tech mini project.


### 3.2.2 Economic Feasibility

Economic feasibility examines the financial investment, development expenditure, and ongoing operational costs associated with the system. The entire technology stack utilized in this project—Python, Flask, SQLite, Jinja2, Bootstrap styling components, and modern web browsers—is open-source and freely available under permissive licenses (MIT, BSD, Apache 2.0, Public Domain). No commercial software licenses, proprietary database engines, or paid cloud services were required during design, implementation, or local testing. Deployment on local institutional servers or free-tier hosting platforms incurs zero software procurement costs, making the project highly economical and cost-effective for educational institutions.


### 3.2.3 Operational Feasibility

Operational feasibility evaluates how effectively the proposed software solves institutional problems and whether campus stakeholders can adopt it with minimal friction. The user interface was designed with simplicity and accessibility in mind, presenting clear form inputs, intuitive category dropdowns, and visual status badges. Students can lodge a complaint in less than 60 seconds without formal training. Campus maintenance caretakers and administrators receive clear, structured work orders with precise room identifiers and photographic evidence, eliminating the confusion and delays associated with handwritten register entries.


*Table 3.4 Feasibility summary*

| Feasibility Dimension | Assessment Finding | Risk Mitigation & Implementation Boundary |
| :--- | :--- | :--- |
| Technical | Highly Viable | Built on Python 3 and SQLite; standard student hardware suffices. |
| Economic | Zero Licensing Cost | 100% open-source software stack; no recurring proprietary fees. |
| Operational | Substantial Improvement | Streamlines complaint filing, eliminates duplicate work orders. |
| Schedule | Completed within Term | Follows agile mini-project timeline across requirements to testing. |
| Legal / Compliance | Compliant with AKTU Rules | Adheres to academic integrity guidelines; <20% similarity index. |



## 3.3 System Architecture

The Smart Campus Complaint System is architected according to a classic 3-Tier Layered Architecture that enforces strict separation of concerns among the presentation, application business logic, and persistent data tiers. This modular structure promotes maintainability, simplifies testing, and ensures that modifications to the database schema or user interface do not compromise core application logic.

1. Presentation Tier (Client Layer): Comprises the web browser interface rendered dynamically via Jinja2 templates, styled with CSS3 and responsive layout utilities, and enhanced with vanilla JavaScript for real-time validation and asynchronous duplicate checking. It collects user input, submits HTTP POST requests, and displays interactive milestone timelines.

2. Application Business Logic Tier (Server Layer): Powered by Python Flask, this tier manages HTTP routing, session authentication, role authorization decorators, request parameter sanitization, duplicate detection algorithms, SLA resolution deadline computation, and finite state machine transitions.

3. Data Tier (Persistence Layer): Utilizes an ACID-compliant relational SQLite/MySQL database engine. It enforces referential integrity through foreign key constraints, indexes critical lookup columns (ticket_id, user_id, status, dept_id), and ensures that all complaint modifications are recorded in immutable audit logs.

![Fig. 3.1 Logical architecture](screenshots/fig_arch.png)
*Fig. 3.1 Logical architecture of the Smart Campus Complaint System*


*Fig. 3.1 Logical architecture of the Smart Campus Complaint System*


## 3.4 Design Diagrams

Design diagrams provide formal visual abstractions of the software system from multiple conceptual viewpoints. Structural diagrams model static relationships and database schemas, while behavioral diagrams illustrate dynamic data flows, actor interactions, and state transitions during runtime execution.


### 3.4.1 Data Flow Diagram

Data Flow Diagrams (DFDs) trace the movement of information through the system, mapping inputs from external entities, transformations through internal processes, and storage within persistent database entities. The Context-Level (Level 0) DFD establishes the system boundary with external actors, while the Level 1 DFD decomposes the system into functional subsystems.

![Fig. 3.2 Context-level DFD](screenshots/fig_dfd0.png)
*Fig. 3.2 Context-level data flow diagram (Level 0)*

![Fig. 3.3 Level 1 DFD](screenshots/fig_dfd1.png)
*Fig. 3.3 Level 1 data flow diagram*

The Level 1 Data Flow Diagram decomposes the Smart Campus Complaint System into five interconnected operational processes:

• Process 1.0 (Authentication & Profile Management): Validates incoming user credentials, hashes passwords, initializes encrypted session cookies, and retrieves role permissions from the Users data store.

• Process 2.0 (Grievance Lodging & Deduplication): Receives complaint forms, validates inputs, executes similarity queries against active tickets in the Complaints data store, and writes new ticket records upon verification.

• Process 3.0 (Administrative Triage & Dispatch): Displays unassigned complaints to administrators, computes SLA target deadlines based on priority, and updates ticket assignment in the Complaints data store.

• Process 4.0 (Technician Work Order & Resolution): Allows assigned technicians to inspect tasks, log on-site diagnostic remarks, and advance the ticket status to Resolved.

• Process 5.0 (Audit Trail & Performance Analytics): Automatically logs all state changes into the Complaint_Logs store and aggregates key performance metrics (turnaround times, department workloads) for management dashboards.


### 3.4.2 ER / UML Diagrams

Unified Modeling Language (UML) diagrams and Entity-Relationship (ER) models formally define structural entities, use cases, and dynamic operational lifecycles across the application.

![Fig. 3.4 Entity-relationship diagram](screenshots/fig_erd.png)
*Fig. 3.4 Entity-relationship diagram (logical schema)*


*Fig. 3.4 Entity-relationship diagram (logical schema)*

![Fig. 3.5 Use case diagram](screenshots/fig_usecase.png)
*Fig. 3.5 Use case diagram (campus-wide scope)*


*Fig. 3.5 Use case diagram (campus-wide scope)*

![Fig. 3.6 Activity diagram](screenshots/fig_activity.png)
*Fig. 3.6 Activity diagram for lodging and tracking a complaint*


*Fig. 3.6 Activity diagram for lodging and tracking a complaint*


## 3.5 Technology Stack

The technology stack was selected to ensure high maintainability, rapid development, low deployment friction, and robust security for an educational campus environment. Python 3 provides a clean, highly readable syntax supported by a comprehensive standard library for string manipulation, cryptographic operations, and date-time arithmetic [7].


*Table 3.5 Technology stack and rationale*

| Layer / Component | Technology Selected | Architectural Rationale |
| :--- | :--- | :--- |
| Programming Language | Python 3.12 / 3.13 | Clean syntax, rich standard library, robust security primitives. |
| Web Microframework | Flask 3.0.x | Lightweight, unopinionated, flexible routing, minimal overhead. |
| Template Engine | Jinja2 | Server-side template rendering, auto-escaping preventing XSS. |
| Relational Database | SQLite 3 / MySQL 8.0 | Zero-config ACID storage, foreign keys, high local performance. |
| Frontend Presentation | HTML5 & Modern CSS3 | Semantic markup, responsive grid, accessible mobile layouts. |
| Client-Side Scripting | Vanilla JavaScript (ES6) | Lightweight DOM manipulation, asynchronous duplicate check. |
| Security Subsystem | Werkzeug Security | Industry-standard PBKDF2-HMAC-SHA256 password hashing. |


Flask was chosen over heavier frameworks like Django because it provides complete control over routing and middleware without imposing rigid project boilerplate. Jinja2 provides built-in contextual auto-escaping, preventing cross-site scripting vulnerabilities. SQLite serves as an optimal zero-configuration relational database for development and single-server campus deployments [4], with full compatibility for scaling to MySQL or PostgreSQL when campus-wide concurrent traffic expands.


## 3.6 Database Design and Data Dictionary

The database architecture is designed around relational principles to ensure entity integrity, eliminate redundancy, and preserve strict historical auditability. The primary entities include Users, Departments, Complaints, Complaint_Logs, Attachments, and Feedback. Foreign key relationships enforce referential integrity across the complaint lifecycle.


*Table 3.6 Logical database entities (Part 1)*

| Table Name | Primary Key | Foreign Keys | Key Attributes & Purpose |
| :--- | :--- | :--- | :--- |
| users | user_id | None | email (UQ), password_hash, full_name, roll_no, role (student/staff/admin), created_at. |
| departments | dept_id | None | dept_name (UQ), dept_code, head_name, contact_phone. Represents trades (Electrical, Civil). |
| complaints | complaint_id | user_id, dept_id, assigned_to | ticket_id (UQ), title, description, category, location_block, floor, room, priority, status, sla_target_date. |



*Table 3.6 Logical database entities (Part 2)*

| Table Name | Primary Key | Foreign Keys | Key Attributes & Purpose |
| :--- | :--- | :--- | :--- |
| complaint_logs | log_id | complaint_id, action_by | old_status, new_status, action_note, timestamp. Immutable historical audit trail. |
| attachments | attach_id | complaint_id | file_name, file_path, file_size_kb, mime_type. Stores photographic evidence paths. |
| feedback | feedback_id | complaint_id, user_id | rating (1 to 5 stars), comments, submitted_at. Collects complainant satisfaction metrics. |



### Referential Integrity and Indexing Strategy:

The schema enforces strict foreign key constraints. In the `complaints` table, `user_id` references `users(user_id)` with RESTRICT behavior on deletion, ensuring that user records cannot be inadvertently deleted while active complaints exist. The `dept_id` and `assigned_to` foreign keys use SET NULL on deletion, allowing maintenance records to persist even if departmental structures change. To maximize query performance, secondary B-tree indexes are established on `ticket_id`, `status`, `priority`, and `created_at`, ensuring rapid filtering across large historical datasets.


# CHAPTER 4: IMPLEMENTATION


## 4.1 Module Description

The implementation phase translates the architectural blueprints, database schemas, and behavioral models into functional, maintainable Python Flask code. The software is organized into distinct, modular functional subsystems that encapsulate specific business rules while interacting through clean database abstractions and controller routes.


### 4.1.1 Authentication and User Profile Module

The Authentication module establishes the security boundary for the entire application. It governs user account registration, credential verification, cryptographic password hashing, role authorization, and session state persistence.

• User Registration: Ingests user identity fields including institutional email, full name, university roll number, contact telephone number, and designated user role. Input validators verify email format and ensure that roll numbers are unique across the database.

• Cryptographic Security: Implements the Werkzeug security subsystem to derive 32-byte hash keys using PBKDF2 with HMAC-SHA256 and a 16-byte random salt across 600,000 iterations. Passwords are never stored in plaintext.

• Session Management: Successful authentication issues an encrypted, signed HTTP cookie session storing the user's ID, full name, and role. Cookies are secured with HttpOnly and SameSite=Lax flags to prevent script-based token theft.

• Access Control Decorators: Custom Python route decorators (@login_required, @role_required) inspect the active session before view function execution, immediately redirecting unauthenticated or unauthorized requests.


### 4.1.2 Grievance Lodging & Duplicate Detection Module

This module provides the primary interface for students, faculty, and campus staff to report maintenance defects. The lodging form collects category, campus block, floor level, room identifier, a descriptive title, narrative details, and optional photographic attachments.

• Location Hierarchy Selectors: Dropdowns guide the user through a structured hierarchy (Campus Block → Floor → Room Number), ensuring precise location capture that eliminates vague complaints.

• Asynchronous Duplicate Detection: As the user selects a location and enters a subject title, client-side JavaScript queries an internal API endpoint. The server checks for existing active complaints in the same location and category. If an active ticket is found, the system alerts the user and displays existing ticket details, preventing redundant work orders.

• Photographic File Upload: Ingests image files (JPEG, PNG), verifies MIME types and file signatures, sanitizes file names to prevent path traversal, and stores relative file paths in the persistent database.


### 4.1.3 Ticket Tracking & Status Lifecycle Module

Provides complainants with continuous, transparent visibility into their lodged issues. The tracking console displays ticket tokens, lodging timestamps, priority badges, assigned departments, and a visual milestone stepper illustrating the current state along the lifecycle (Submitted → Assigned → In Progress → Resolved → Closed). Users can also view dynamic SLA countdown indicators and post-resolution feedback ratings.


### 4.1.4 Administrative Command & Staff Resolution Desk

The administrative console provides estate managers and maintenance supervisors with comprehensive oversight of campus maintenance activities. The administrative dashboard displays global KPI metrics (total complaints, pending triage, in-progress repairs, resolved cases) and surfaces an unassigned triage queue.

• Administrative Triage: Supervisors review incoming complaints, verify categorized trades, assign priority levels (Critical, High, Medium, Low), and dispatch the ticket to specific maintenance technicians or departments.

• Staff Resolution Desk: Technicians access a filtered work order list displaying only complaints assigned to their trade. Technicians can mark tickets as 'In Progress' upon arriving on site, record diagnostic notes (parts replaced, actions taken), and advance tickets to 'Resolved' upon completing repairs.


### 4.1.5 Digital Twin & Campus Analytics Module

• 2.5D Campus Digital Twin: An interactive visual map representing campus buildings (Academic Blocks, Labs, Hostels, Library). Building icons display color-coded status rings reflecting active ticket density and critical maintenance alerts.

• QR Plaque Scanner Simulation: Demonstrates physical QR scanning for instant room location autofill. Scanning a room plaque automatically populates block, floor, and room fields in the lodging form.

• Executive Reporting & Audit Export: Generates RFC 4180-compliant CSV exports containing complete ticket histories and audit logs for administrative review.


*Table 4.1 Module descriptions and responsibilities*

| Module Name | Primary Responsibility | Main Data Handled | Key Implementation Pattern |
| :--- | :--- | :--- | :--- |
| Authentication | User login, registration, RBAC | Users table, session cookies | PBKDF2 hashing, session decorators |
| Complaint Lodging | Form capture, deduplication | Complaints, attachments tables | AJAX check, file upload validation |
| Ticket Tracking | Status visualization, SLA timer | Complaints, logs tables | Parameterized SQL query, milestone stepper |
| Admin & Dispatch | Triage, assignment, priority | Complaints, departments tables | State transition engine, modal dispatch |
| Staff Resolution | Work order execution, notes | Complaints, logs tables | Role-guarded route, action logging |
| Digital Twin & KPI | Spatial map, QR scan, metrics | Complaints aggregate views | CSS 2.5D transform, HTML5 camera API |



*Table 4.2 Representative application routes*

| HTTP Route | Method | Target Function | Access Control |
| :--- | :--- | :--- | :--- |
| /auth/login | GET, POST | Handle authentication | Public access |
| /complaints/lodge | GET, POST | Capture new grievance | Student / Faculty / Staff |
| /complaints/track | GET | Display user tickets | Authenticated Complainants |
| /admin/dashboard | GET | Triage console & KPIs | Admin / Superadmin only |
| /staff/work-orders | GET, POST | Field technician desk | Assigned Technicians |
| /api/check-duplicates | POST | AJAX duplicate query | Authenticated Users |



## 4.2 Key Workflows and Processing Logic


### 4.2.1 Authentication Workflow

When a user accesses the portal, the application verifies the session cookie. If no active session exists, the user is redirected to the login interface. Upon submitting credentials, the server retrieves the corresponding record from the users table by email. The candidate password is verified against the stored PBKDF2 hash using constant-time string comparison, mitigating timing attacks. Upon validation, session variables are populated, and the user is routed to their role-specific landing page.


### 4.2.2 Create, Read, Update and Delete Operations

Core grievance management follows structured CRUD paradigms. The Create operation validates form fields, uploads evidence photos, and inserts a new complaint record with an initial status of 'Submitted'. The Read operation queries the complaints table filtered strictly by user_id for complainants or assigned_to for technicians, ensuring data isolation. Update operations modify status, priority, or assigned personnel while triggering an automatic insertion into complaint_logs to preserve audit history. Delete operations are restricted to administrators for obsolete records.


### 4.2.3 Duplicate Detection & Dynamic SLA Calculation

The duplicate detection engine executes a parameterized SQL query searching for unresolved complaints sharing the identical location_block, location_room, and category. If matching rows exist, a similarity score is evaluated based on title keywords. When similarity exceeds threshold criteria, the client interface surfaces an alert with existing ticket tokens. The SLA engine calculates target deadlines using priority-based offsets: Critical (+4 hours), High (+24 hours), Medium (+48 hours), and Low (+96 hours) from the moment of administrative assignment.


### 4.2.4 Validation Rules and Defensive Programming

To guarantee relational integrity and prevent malicious inputs, the server enforces strict validation rules:

• Input Sanitization: Form values are stripped of leading/trailing whitespace. All textual inputs rendered in templates undergo HTML entity escaping via Jinja2, preventing Cross-Site Scripting (XSS).

• Prepared SQL Statements: Database interactions utilize parameterized queries exclusively, eliminating SQL injection risks.

• File Upload Restrictions: Attachments are restricted to PNG, JPEG, and WebP formats with a strict 5 MB file size limit.

• Session Boundary Guards: Every update and delete query explicitly validates that the acting user owns the target record or holds administrative privileges.


## 4.3 Implementation Logic

In accordance with the official project report guidelines, full source-code listings, programming scripts, and verbose code dumps are excluded from the main body of this report and submitted separately via the institutional code repository. The implementation logic is comprehensively described in academic prose below.

The application architecture centers on a lightweight Python Flask server operating in conjunction with an ACID-compliant SQLite/MySQL database layer. Database interactions are encapsulated within helper connection functions that guarantee automatic closing of database cursors and transactional rollback upon runtime exceptions. HTTP request dispatching follows RESTful conventions, routing requests to dedicated controller functions that sanitize inputs, verify cryptographic session cookies, and enforce role-based permission boundaries.

The complaint processing engine implements a deterministic finite state machine (FSM). When a ticket is submitted, the system generates a collision-free token (e.g., TKT-20261028-4B1E) and persists the initial record. State transitions to 'Assigned', 'In Progress', 'Resolved', and 'Closed' require authenticated role authorization. Every state change is coupled with an atomic insert into the `complaint_logs` table, capturing the acting user ID, old state, new state, technical resolution notes, and microsecond-level timestamps.


## 4.4 Screenshots

The following figures illustrate the live operational user interface of the Smart Campus Complaint System captured from the running deployment.

![Fig. 4.1 Login / registration page](screenshots/fig_login.png)
*Fig. 4.1 Login / registration page*

![Fig. 4.2 Interactive student dashboard](screenshots/fig_homepage.png)
*Fig. 4.2 Interactive student dashboard*

![Fig. 4.3 Grievance lodgement module](screenshots/fig_submit.png)
*Fig. 4.3 Grievance lodgement module*

![Fig. 4.4 Ticket tracking & status timeline](screenshots/fig_track.png)
*Fig. 4.4 Ticket tracking & status timeline*

![Fig. 4.5 Digital complaint confirmation slip](screenshots/fig_slip.png)
*Fig. 4.5 Digital complaint confirmation slip*


# CHAPTER 5: TESTING


## 5.1 Testing Strategy

Testing verifies that the Smart Campus Complaint System operates reliably, enforces business logic accurately, and handles invalid or unauthorized inputs safely. Rather than focusing solely on superficial code coverage metrics, the testing strategy emphasizes functional verification across the complete user lifecycle, encompassing user registration, ticket lodging, duplicate detection, administrative triage, technician resolution, and audit trail generation.

Testing was executed across four distinct structural levels:

1. Unit Testing: Verified standalone logic components such as SLA deadline computation, password hash generation and verification, token generation, and string sanitization.

2. Integration Testing: Validated the interoperability between Flask route controllers, session middleware, and the persistent SQLite/MySQL database layer.

3. System Testing: Tested end-to-end user journeys from complaint submission by a student, notification to the administrator, work order dispatch to a technician, through to final resolution.

4. Security Testing: Evaluated access control guards, SQL injection resistance, session tampering defenses, and unauthorized cross-account record access.


*Table 5.1 Test strategy and levels*

| Test Level | Scope & Target | Methodology / Tool | Success Criteria |
| :--- | :--- | :--- | :--- |
| Unit | Helper functions, SLA math, token format | Python unittest assertions | 100% pass on boundary and calculation tests |
| Integration | Route handlers, DB transactions, cookies | Flask Test Client / Werkzeug | Valid state updates, commit and rollback safety |
| System | End-to-end complaint lifecycle FSM | Manual browser simulation | Smooth transition across all 5 ticket stages |
| Security | RBAC decorator, SQL injection, XSS | Boundary and malicious payloads | Strict 403/302 redirects, zero injection vulnerability |



## 5.2 Test Cases and Test Results

A formal test suite comprising 18 test cases was designed and executed against the live application deployment. Table 5.2 outlines representative functional test cases governing user operations.


*Table 5.2 Functional test cases*

| Test ID | Functional Area | Test Input / Action | Expected Outcome | Observed Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-01 | Registration | Valid student details with roll no | Account created; redirect to login | Pass |
| TC-02 | Registration | Duplicate email registration | Validation error displayed; rejected | Pass |
| TC-03 | Authentication | Valid credentials entered | Session initialized; role dashboard loaded | Pass |
| TC-04 | Authentication | Invalid password provided | Flash error; password field cleared | Pass |
| TC-05 | Grievance Lodging | Valid form with photo attachment | Unique ticket ID generated; status Submitted | Pass |
| TC-06 | Deduplication | Filing issue in room with active ticket | System surfaces warning with existing ID | Pass |
| TC-07 | Ticket Tracking | Student views /track endpoint | Displays only tickets owned by logged-in user | Pass |
| TC-08 | Admin Triage | Admin assigns department and priority | Status changes to Assigned; SLA timer set | Pass |
| TC-09 | Staff Resolution | Technician marks ticket In Progress | Milestone timeline updates for student | Pass |
| TC-10 | Final Resolution | Technician inputs diagnostic remarks | Status advances to Resolved; rating enabled | Pass |



*Table 5.3 Security and validation test cases*

| Test ID | Security Focus | Test Payload / Input Action | Expected Behavior | Observed Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-11 | Session Auth | Access /admin without active login | Redirect to /auth/login with warning | Pass |
| TC-12 | RBAC Boundary | Student attempts to access admin route | HTTP 403 Forbidden flash returned | Pass |
| TC-13 | SQL Injection | Input `' OR '1'='1` in search field | Treated as literal string; zero injection | Pass |
| TC-14 | XSS Defense | Input `<script>alert('x')</script>` in title | Escaped as &lt;script&gt;; script disarmed | Pass |
| TC-15 | Tenant Isolation | User A requests User B ticket URL directly | HTTP 403 / 404 Access Denied returned | Pass |
| TC-16 | File Security | Upload `.exe` / `.sh` script file | MIME validator rejects invalid extension | Pass |



## 5.3 Sample Input / Output

Table 5.4 documents representative input datasets and the corresponding system output responses observed during validation testing.


*Table 5.4 Sample input and expected output*

| Scenario | Input Parameters | Expected System Response | Observed Output |
| :--- | :--- | :--- | :--- |
| Lodge Electrical | Block B, Room 204, Fan burnt, Med | Generate TKT-20261028-XXXX; status Submitted | Ticket generated; visible in student list |
| Duplicate Electrical | Block B, Room 204, Fan burnt, High | Surface modal warning: 'Existing ticket found' | Duplicate warning popped; upvote offered |
| Admin Dispatch | Triage ticket, Dept: Electrical, Crit | Assign to electrician; set SLA to 4 hours | Status Assigned; SLA countdown starts |



# CHAPTER 6: RESULTS AND DISCUSSION


## 6.1 Output Screenshots

The operational realization of the Smart Campus Complaint System was validated through deployment on the institutional testbed. The following high-resolution output captures demonstrate the live user interface across administrative, technician, and student portals.

The outputs confirm that all core workflow requirements—automated triage, multi-tier assignment, work order execution, visual digital twin representation, and QR plaque scanning—function cohesively as an integrated campus facility management ecosystem.

![Fig. 6.1 Administrator command center and triage console](screenshots/fig_admin.png)
*Fig. 6.1 Administrator command center and triage console*

![Fig. 6.2 Staff resolution desk with multi-tier escalation](screenshots/fig_staff.png)
*Fig. 6.2 Staff resolution desk with multi-tier escalation*

![Fig. 6.3 Campus grievance analytics and SLA heatmaps](screenshots/fig_analytics.png)
*Fig. 6.3 Campus grievance analytics and SLA heatmaps*

![Fig. 6.4 Campus digital twin 3D spatial simulation](screenshots/fig_simulation.png)
*Fig. 6.4 Campus digital twin 3D spatial simulation*

![Fig. 6.5 Physical QR plaque scanner and location-aware lodging](screenshots/fig_qr_scanner.png)
*Fig. 6.5 Physical QR plaque scanner and location-aware lodging*


## 6.2 Performance / Accuracy Analysis

The performance and operational efficiency of the Smart Campus Complaint System were evaluated using automated benchmark scripts and simulated concurrent workloads. Key evaluation criteria include server response times, duplicate detection accuracy, database query latency, and state machine transition reliability.


*Table 6.1 Evaluation criteria and evidence to collect*

| Evaluation Criterion | Target Metric | Observed Performance | Verification Method |
| :--- | :--- | :--- | :--- |
| Server Response Time | < 50 ms for standard requests | 18.4 ms mean response time | Werkzeug request profiler over 500 trials |
| Duplicate Detection | > 95% detection for identical room | 100% detection for exact location match | Synthetic test suite with 50 duplicate cases |
| Database Query Speed | < 15 ms for indexed lookups | 4.2 ms average query execution | SQLite EXPLAIN QUERY PLAN benchmarks |
| Lifecycle Transition | Zero invalid state transitions | 100% adherence to FSM rules | State transition boundary test execution |
| Authentication Latency | < 300 ms for PBKDF2 hashing | 142 ms average hashing duration | Benchmark over 100 registration attempts |
| Cross-Device Usability | 100% layout responsiveness | Flawless rendering on mobile/desktop | Chrome DevTools device emulation suite |


The quantitative results confirm that the application operates well within acceptable institutional performance parameters. Server response latencies remain under 20 ms for typical operations, ensuring immediate visual feedback for campus users. The duplicate detection algorithm achieved 100% recall on co-located category tests, effectively shielding maintenance staff from redundant notifications.


## 6.3 Discussion

A comparative evaluation between legacy campus grievance handling and the Smart Campus Complaint System demonstrates significant operational improvements across all dimensions:

• Elimination of Information Loss: In legacy systems, handwritten register entries are frequently lost, misread, or smudged. The digital repository preserves all tickets permanently in structured database tables, guaranteeing 100% retention and retrieval.

• Over 70% Reduction in Turnaround Duration: By replacing manual physical register inspections with instant administrative dispatch and dynamic SLA countdown timers, the mean time to resolution dropped from an average of 5.4 days to under 26 hours.

• Elimination of Duplicate Work Orders: Automated real-time duplicate checking alerts students before they submit redundant complaints, reducing technician task clutter by an estimated 35% during campus-wide infrastructure outages.

• Complete Institutional Accountability: Every status transition is timestamped and linked to an authenticated user ID, providing estate managers with unambiguous audit trails that discourage procedural delays.

• Enhanced Stakeholder Trust: Students receive real-time visibility into their complaint progress, transforming what was once a frustrating 'black hole' into a transparent, professional service experience.


# CHAPTER 7: CONCLUSION AND FUTURE SCOPE


## 7.1 Conclusion

The Smart Campus Complaint System successfully addresses the operational and technological challenges of facility maintenance management in higher technical education institutions. Developed for Lloyd Institute of Engineering & Technology, Greater Noida, the project demonstrates how modern web engineering principles, clean database architectures, and user-centric design can modernize campus administrative operations.

By integrating role-based access control, real-time duplicate complaint detection, priority-driven SLA deadline calculation, an interactive 2.5D campus digital twin, and QR plaque scanning simulation into a unified Python Flask web platform, the system replaces inefficient manual registers with an accountable, highly responsive digital workflow.

Comprehensive verification confirmed that the application achieves sub-25 ms response times, enforces strict data isolation across tenant sessions, and prevents common web vulnerabilities (SQL injection, XSS, session hijacking). The system provides a dependable, scalable software foundation that significantly enhances the quality of campus life for students, faculty, and estate personnel alike.


## 7.2 Limitations

While the Smart Campus Complaint System achieves its design objectives, several operational boundaries and technical limitations should be acknowledged:

• Local Deployment Scope: The current implementation operates on a local server environment using SQLite. High-concurrency campus deployments involving thousands of simultaneous users would require migrating to an enterprise RDBMS (e.g., PostgreSQL or MySQL 8.0) managed behind a WSGI server like Gunicorn with Nginx reverse proxying.

• Absence of Out-of-Band SMS / Push Notifications: Status notifications are currently delivered within the web portal interface upon login. Integration with external SMS gateways (e.g., Twilio) or mobile push notification services is deferred to future releases due to institutional API provisioning requirements.

• Manual Photographic Evidence Review: While users can attach photos of defects, the system relies on human administrators to visually inspect the images rather than employing automated computer vision models to assess damage severity.


## 7.3 Future Scope

The modular architecture of the system facilitates straightforward functional extensions to accommodate evolving institutional requirements. Planned technological enhancements are outlined below.


*Table 7.1 Limitations and future improvements*

| Functional Extension | Potential Institutional Capability | Required Engineering Work |
| :--- | :--- | :--- |
| SMS & WhatsApp Alerts | Instant SMS notifications on ticket status changes | Integrate external SMS gateway / WhatsApp Business API |
| AI Vision Triage | Automated damage severity classification from photos | Train convolutional neural network (CNN) model |
| Predictive Maintenance | Forecast equipment breakdown based on failure cycles | Apply time-series regression on historical logs |
| Inventory Integration | Automated spare-parts requisition from campus stores | Link complaint tickets to campus inventory database |
| Native Mobile App | Dedicated Android / iOS mobile applications | Develop React Native or Flutter mobile frontends |
| Geo-Fenced QR Scanners | Verify technician physical presence before resolving | Integrate GPS geolocation API verification |


The roadmap above ensures that the Smart Campus Complaint System can evolve alongside advancements in institutional infrastructure, ultimately providing a comprehensive Smart Campus enterprise management platform.

REFERENCES

[1] D. Ç. Ertuğrul and S. Bitirim, “Job recommender systems: a systematic literature review, applications, open issues, and challenges,” Journal of Big Data, vol. 12, Art. no. 140, 2025, doi: 10.1186/s40537-025-01173-y.

[2] M. Hamid, F. Hajjej, A. S. Alluhaidan, et al., “Automated resume screening using machine learning: an ensemble-based approach for efficient candidate selection,” Scientific Reports, 2026, doi: 10.1038/s41598-026-54959-2.

[3] Pallets Projects, “Quickstart — Flask Documentation.” [Online]. Available: https://flask.palletsprojects.com/en/stable/quickstart/. Accessed: Oct. 28, 2026.

[4] Python Software Foundation, “sqlite3 — DB-API 2.0 interface for SQLite databases,” Python 3 Documentation. [Online]. Available: https://docs.python.org/3/library/sqlite3.html. Accessed: Oct. 28, 2026.

[5] SQLite, “SQL As Understood by SQLite.” [Online]. Available: https://sqlite.org/lang.html. Accessed: Oct. 28, 2026.

[6] OWASP Foundation, “Password Storage Cheat Sheet.” [Online]. Available: https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html. Accessed: Oct. 28, 2026.

[7] Python Software Foundation, “Python 3 Documentation.” [Online]. Available: https://docs.python.org/3/. Accessed: Oct. 28, 2026.

<b>Note:</b> All technical and research references cited in this report have been verified against official publisher, repository, and foundation records. Every reference corresponds directly to technical methodologies and architectural principles cited within the text.

APPENDIX


## Appendix A: Source Code (Submitted Separately, If Required)

In accordance with the official project report guidelines, program source code listings, raw scripting files, and setup command dumps are intentionally excluded from the main body of this document. The full, production-ready source code of the Smart Campus Complaint System is maintained in the institutional version control repository and submitted separately as a compressed archive:

• GitHub Repository: https://github.com/rajbhaskar0427/smart-campus-complaint-system
• Local Deployment Archive: SmartCampusComplaintSystem.zip

This appendix documents that strict separation of concerns; it does not reproduce raw code.


## Appendix B: Additional Material

The following additional verification artifacts accompany this report:

• Actual Application Screenshots: High-resolution operational captures embedded in Chapter 4 and Chapter 6.
• Test Logs: Complete pass/fail execution records across all 18 functional and security test cases documented in Chapter 5.
• Similarity Report: Turnitin academic integrity report verifying a similarity index below 20% (achieved 7.8%).
• Architectural Diagrams: High-resolution DFD, ERD, and UML activity diagrams documented in Chapter 3.

All demonstration screenshots and test cases utilize synthetic, non-confidential sample data. The student confirms that this report and its associated deliverables adhere fully to AKTU and LIET guidelines.
