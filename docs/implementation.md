# Implementation Outline

## Tools

### Backend
- Python
- Flask
- CS50's SQL (After fighting SQLAlchemy)
- Sqlite3

### Frontend
- HTML/CSS
- Beer CSS Framework (Material Design)
- Flask Templates
- JavaScript

#### Logic
*A rough outline of core logic* 

1. User inputs tasks into WebApp
2. Requests sent to Python to then be sorted
3. Algorithm determines scoring for each task
4. Data stored in Sqlite3 Database with relevant information (Title, Deadline,
   Priority, *Score*)
5. Dashboard shows all tasks with information so it is readily available
6. User then pushes button to send request to Python on how to spread tasks
   throughout day
7. Daily plan sent back to WebApp to be shown on users page

###### Algorithm for Task Scoring

**Variables:**
- urgency:
  int = Days until deadline
- priority:
  int = User set priority
- effort:
  int|float = Estimated time to complete

**Scoring Algorithm** 

```python
score: int = (urgency * weight) +
               (priority * weight) -
               (effort_penalty)
```

**Sorting Tasks**

- User will input how much time they can spare
- Plan will be a List[Dict[]]
- Each Dict[] will represent an hour of their FREE_HOURS
- Dict will consist of:
  Title, Duration, Start, Finish, (Break?)
- This can then be used to populate WebApp

```python
FREE_HOURS: int|float = 0

def plan_day() -> List[Dict[]]
    return dict(plan)
```
