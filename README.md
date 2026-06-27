# WeePlan

***So you don't have to...*** 

----------

### Description

WeePlan is a User Dashboard for the people who, like myself, struggle to
remember important tasks and details.
Even when they do manage to remember, they then struggle to actually set time
aside to complete said things.
Through the use of algorithms, databases and an accessible, intuitive UI/UX.
This Web Application will help you not only remember what you should be doing,
but actually give you a headstart by organising and planning when you should be
doing them.

### Features

- A user-friendly Dashboard containing...

    - Tasks
        - Title
        - Deadline
        - Estimated time
        - Priority

    - Daily Planner
        - Score tasks with algorithm
        - Output realistic plan for the day

    - Features time permitted
        - Habit Tracker
        - Rescheduling missed tasks
        - Charts to visualise time/tasks
        - Tagging (Study, Personal, etc.)

    - *Basic Persistence using a Database (SQLite)*

### Project Structure

```txt
weeplan/
├── app.py
├── helpers.py
├── schema.sql
├── dashboard.db            
├── util.py            
│
├── templates/
│   ├── dashboard.html
│   ├── index.html
│   ├── layout.html
│   ├── login.html
│   ├── planner.html
│   ├── register.html
│   └── tasks.html
│
├── static/
│   ├── styles.css
│   └── scripts.js
│
└── docs/
    └── implementation.md
```
