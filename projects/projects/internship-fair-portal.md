---
title: Internship Fair Portal
date: 2021-02-01
description: A web-based portal that digitized Delhi University's annual internship fair during COVID-19, enabling 50+ companies and 650+ students to connect virtually over a two-day event.
tags:
  - React
  - Firebase
  - Cloud Functions
  - Event Management
  - Education Technology
slug: internship-fair-portal
thumbnail: projects/assets/internship-fair-portal/thumbnail.png
published: true
canonical_url: https://www.abhin.dev/projects/internship-fair-portal
web_url: https://www.linkedin.com/posts/abhinrustagi_internship-fair-2021-portal-screenshots-activity-6766469207342297088-foKw
---

## TL;DR

In February 2021, during the height of COVID-19 lockdowns, I built an end-to-end web portal that transformed a Delhi University college's traditional in-person internship fair into a fully digital event. The platform successfully connected 50+ companies with 650+ students over a two-day virtual event, achieving the highest student participation in the college's history.

## Problem Statement

My undergraduate college at Delhi University was technically regressive—they didn't even have a website. The placement cell, a student-run community, organized an annual internship fair where 30-40 companies would set up physical stalls on campus, and students could submit resumes in person for on-the-spot interviews and hiring processes.

When COVID-19 hit, the college faced a critical challenge: how to organize this essential event remotely. The traditional in-person format was impossible under lockdown restrictions, but students still needed access to internship opportunities. The college had no technical infrastructure and needed a solution that was both quick to deploy and cost-effective.

## Solution

I volunteered to build a complete digital portal that would replicate and enhance the physical fair experience. Working intensively over two weeks—coding up to 10 hours daily—I developed a full-stack web application using React, Firebase, and Cloud Functions. The solution was architected to be zero-cost for the college, even after handling the entire event load.

The platform featured:

**Student Experience:**

- Registration system with comprehensive profile creation
- Document upload workflow (resume, admission certificates, proof documents)
- Real-time application status tracking
- E-commerce-style company and role browsing interface
- One-click application submission to multiple companies

**Admin Portal:**

- Profile review dashboard for placement cell team
- Document verification system with approve/reject/hold workflow
- Bulk profile management capabilities
- Automated email notification system

**Approval Workflow:**
When profiles were put on hold, students automatically received emails explaining which documents needed correction. They could re-upload the required documents, triggering a re-review cycle. Only approved students could access the main portal and apply to companies. Once applications were submitted, all student details were forwarded to companies to manage their hiring processes independently.

## Tech Stack

- **Frontend:** React
- **Backend:** Firebase Cloud Functions
- **Database & Authentication:** Firebase Firestore & Firebase Auth
- **Storage:** Firebase Storage (for document uploads)
- **Hosting:** Firebase Hosting
- **Email Service:** Cloud Functions with email integration

## Key Features

- Complete user authentication and authorization system
- Multi-step registration form with validation
- Document upload and cloud storage management
- Admin dashboard with review and approval workflows
- Automated email notification system for application status updates
- Company and role catalog with search and filter capabilities
- Application tracking and management system
- Real-time data synchronization across all users
- Scalable architecture supporting 655+ concurrent users
- Zero-downtime operation during two-day event

## Challenges & Learnings

**Time Constraint:** Building a production-ready platform in just two weeks required ruthless prioritization. I focused on core functionality first—authentication, registration, document upload, and admin review—before adding polish.

**Scale Considerations:** The system needed to handle 655 students and 50 companies simultaneously during the two-day event. Firebase's real-time database and serverless Cloud Functions proved ideal for this unpredictable load without requiring complex infrastructure management.

**Document Verification Workflow:** Designing a smooth approval process that handled edge cases (missing documents, incorrect formats, re-uploads) while maintaining security was critical. The hold-and-resubmit workflow significantly reduced admin burden.

**Cost Optimization:** By leveraging Firebase's free tier and efficient Cloud Functions, I kept infrastructure costs at zero despite substantial usage. This was crucial for a college with limited technical resources.

**User Experience:** Many students were not tech-savvy, so the interface needed to be intuitive. Drawing inspiration from e-commerce platforms for the company selection flow made the experience familiar and accessible.

## Outcome

The Internship Fair Portal was a resounding success. The platform ran smoothly across the entire two-day event without downtime. There were zero infrastructure costs for the college, even post-event. The digital format enabled better tracking, documentation, and follow-up compared to the previous in-person model
