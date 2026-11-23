# School Daily Diary App — Specification

Version 1 · Week 3 · Author: Asad Raza

## Purpose
[YOU WRITE — two sentences in your own words. Sentence 1: who it is for and what it does. Sentence 2: the problem it fixes today.]

## Stakeholder
[YOU WRITE — a real person or organisation other than you who cares whether this is solved, e.g. a teacher, principal or tuition centre you know, and why they care.]

## Success criteria (set before building)
[YOU WRITE — 3 to 5 measurable statements you will test against at the end. Examples of the style, not to copy:
- A teacher can post a day's homework for a class in under 1 minute.
- A parent can see today's homework and attendance for their child in 2 clicks or fewer after logging in.
- A parent cannot see any other child's diary.]

## Users and roles
| Role | Can do |
|---|---|
| Teacher | Post homework for a class; record daily attendance; see their classes |
| Parent | View the daily diary (homework + attendance) for their own child only |

Students do not have logins.

## Scope for the whole project (Weeks 3–11)
1. Teachers post homework for a class, optionally with an attached file (file upload from Week 6).
2. Teachers record daily attendance (present / absent / late) for each student.
3. Parents log in and see a daily diary for their own child: that day's homework and attendance.
4. Teacher and parent logins with different permissions (added in a later week).

## Scope for this week (Week 3)
Homework only, with no login, no file upload and no attendance yet.

## Entities (this week)
### Homework
- id (integer, primary key)
- class_name (text, required, max 50 characters, e.g. "3rd Class B")
- subject (text, required, max 100 characters)
- title (text, required, max 200 characters)
- details (text, optional, max 2000 characters)
- date_set (date, required, YYYY-MM-DD, default today)
- due_date (date, optional, YYYY-MM-DD, must not be before date_set)
- status (one of: draft, published — default draft; parents will only ever see published)
- created_at (timestamp, set automatically)

Entities planned for Week 5 (not built this week): Class, Student, Parent, AttendanceRecord.

## Routes (this week)
| Method | Path | Does |
|---|---|---|
| GET | / | List all homework, newest date_set first, showing class, subject, title, due date and status |
| GET | /homework/new | Form to create a homework entry |
| POST | /homework | Validate and create a homework entry, then redirect to / |
| GET | /homework/<id> | Show one homework entry; 404 if it does not exist |
| POST | /homework/<id>/status | Change status to draft or published, then redirect back |
| GET | /diary?class_name=...&date=YYYY-MM-DD | Daily diary preview: published homework for that class on that date |
| GET | /about | Existing route — keep it unchanged |

## Validation rules
- class_name, subject and title must not be empty or whitespace-only.
- Lengths must not exceed the maximums above.
- Dates must be real dates in YYYY-MM-DD form; due_date must not be before date_set.
- status must be draft or published; anything else returns 400.
- On a validation error, re-show the form with a visible message and keep what the user typed.

## Security and privacy requirements
- A parent must only ever see their own child's diary (enforced when logins are added).
- Only teachers can create or change homework and attendance (enforced when logins are added).
- Only made-up test data. No real student, parent or staff information.

## Technical constraints
- Python 3.11+, Flask 3.x
- SQLite through the standard-library sqlite3 module (no ORM)
- Database file path read from an environment variable, defaulting to app.db
- Jinja2 templates in templates/, one base template
- Plain HTML and CSS; no JavaScript framework
- Multi-file structure: app.py, db.py, schema.sql, templates/
- No debug=True, no hard-coded secrets; SECRET_KEY read from an environment variable
- All SQL uses ? placeholders, never string formatting
- No authentication this week

## Out of scope (whole project)
- Online fee payments (fees are handled by a CA1 automation instead)
- Grades, report cards and timetables
- Student logins
- Messaging between parents and teachers
- A mobile app