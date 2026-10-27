# AI Engineering Learning Progress Tracker

This file syncs your exact progress between your **Home Laptop** and **Office Laptop** via Git/GitHub.
*(Antigravity reads `GEMINI.md` and this `PROGRESS.md` file automatically in every new chat!)*

---

## Current Status
- **Current Phase:** Phase 1 — Python Foundations for AI (Weeks 1–5)
- **Current Week:** Week 1 (Variables, Input, Conditionals, Loops & CLI Mini-Apps)
- **Current Active Step:** **Week 1, Lesson 3 — Loops (`while` & `for`)**

---

## Completed Milestones
- [x] **Environment Setup:** Installed `uv`, Python 3.12, initialized `pyproject.toml` and `.venv`
- [x] **Week 1, Lesson 1 (`week01/lesson01.py`):** Variables (`str`, `int`, `float`, `bool`), math expressions, and `f-strings` (Built Agent `Un01` task & cost tracker)
- [x] **Week 1, Lesson 2 (`week01/lesson02.py`):** Live user input (`input()`), type conversion (`int()`, `float()`), and decision logic (`if / elif / else` AI Budget Guardrail)

---

## Active Challenge: Week 1, Lesson 3 (`week01/lesson03.py`)
**Topic:** Loops (`while` & `for`) — How AI Agents Stay Alive

### Quick Concept Recap
1. **`while True:` + `break`** keeps an agent running in a loop until the user types `"exit"`:
   ```python
   while True:
       command = input("Type a command (or 'exit'): ")
       if command == "exit":
           break
   ```
2. **Memory Variables (`+=` and `-=`):** Create tracker variables *outside* (above) the `while` loop (`budget`, `total_tasks_completed`) and update them *inside* the loop (`budget -= batch_cost`, `total_tasks_completed += tasks`).
3. **`for` Loop with `range(start, stop)`:** Repeats for a specific count (`range(1, tasks + 1)` counts from `1` up to `tasks`).

### Coding Puzzle #3 Specification (`week01/lesson03.py`)
Create `week01/lesson03.py` (`New-Item week01/lesson03.py`) and build an interactive **Live Session AI Task Runner**:
1. **Before the loop:**
   - Ask the user for starting `budget = float(input("Enter starting budget ($): "))`
   - Create `total_tasks_completed = 0`
2. **Start `while True:` loop:**
   - Print current balance and total tasks done (`f"\nCurrent Balance: ${budget:.2f} | Total Tasks Done: {total_tasks_completed}"`)
   - Ask: `command = input("How many tasks to run next? (or type 'exit'): ")`
   - **If** `command == "exit"`: print final summary (`total_tasks_completed` and remaining `budget`) and `break`.
   - **Otherwise:** convert `tasks = int(command)` and calculate `batch_cost = tasks * 0.05`.
   - **If** `batch_cost > budget`: print an error that there isn't enough balance (do not subtract from `budget`).
   - **Else:** subtract `batch_cost` from `budget`, add `tasks` to `total_tasks_completed`, and print a success message!
   - *(Optional Bonus)*: Inside `else`, use `for i in range(1, tasks + 1):` to print `"  -> Running task #..."`.
3. **Run with:** `uv run python week01/lesson03.py`

---

## Upcoming Next Steps (Week 1)
- [ ] **Week 1, Lesson 3 (`week01/lesson03.py`):** Loops (`while` & `for`) — Live Session AI Task Runner
- [ ] **Week 1 Mini-App #1 (`week01/mini_app_token_estimator.py`):** Client LLM API Token & Model Router Calculator (comparing Local GPU vs. Gemini Flash vs. Frontier Models)
- [ ] **Week 1 Main Capstone App (`week01/app_study_expense_tracker.py`):** Interactive CLI Study XP & AI Freelance Expense Tracker

---

## Daily Laptop Sync Cheat Sheet (GitHub Desktop)

### 1. When You Sit Down at Either Laptop (Start of Session)
- Open **GitHub Desktop** $\rightarrow$ click **Fetch origin** (top right) $\rightarrow$ if there are changes from your other laptop, click **Pull origin**.
- *(Or in terminal: `git pull`)*

### 2. When You Finish Studying on Either Laptop (End of Session)
- Open **GitHub Desktop**:
  1. Look at the bottom-left **Summary** box and type a short note (e.g., `"Finish Week 1 Lesson 3"`).
  2. Click the blue **Commit to main** button.
  3. Click **Push origin** (top right) to send it to the cloud!
