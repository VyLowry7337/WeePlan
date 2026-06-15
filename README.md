# CS50x Final Project


## VyTask (Name TBC)

**A system that doesn't just store tasks, it decides them** (Again, TBC)

###### Description

VyTask* is a tool for the people who, like myself, struggle to remember
important tasks and details.
Even when they do manage to remember, they then struggle to actually set time
aside to complete said things.
Through the use of algorithms, databases and an accessible, intuitive UI/UX.
This Web Application will help you not only remember what you should be doing,
but actually give you a headstart by organising and planning when you should be
doing them.

#### Features

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

***Basic Persistence using a Database (SQLite)***

###### Project Structure

```txt
vytask/
├── app.py
├── helpers.py
├── schema.sql
├── vytask.db            # created after you run init_db
│
├── templates/
│   ├── layout.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── add_task.html
│   └── plan.html
│
├── static/
│   ├── styles.css
│   └── scripts.js
│
├── docs/
│   ├── implementation.md
│   └── README.md
│
└── .gitignore
```
