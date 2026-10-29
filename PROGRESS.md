# AI Engineering Learning Progress Tracker

This file syncs your exact progress between your **Home Laptop** and **Office Laptop** via Git/GitHub.
*(Antigravity reads `GEMINI.md` and this `PROGRESS.md` file automatically in every new chat!)*

---

## Current Status
- **Current Phase:** Phase 1 — Python Foundations for AI (Weeks 1–5)
- **Current Week:** Week 1 (Variables, Input, Conditionals, Loops & CLI Mini-Apps)
- **Current Active Step:** **Week 1, Lesson 3 — Deep-Dive Loop Teaching & 3-Question Check** (Continue this Loop Lesson on Home Laptop!)

---

## Completed Milestones
- [x] **Environment Setup:** Installed `uv`, Python 3.12, initialized `pyproject.toml` and `.venv` (Verified & synced on both Home & Office laptops!)
- [x] **Week 1, Lesson 1 (`week01/lesson01.py`):** Variables (`str`, `int`, `float`, `bool`), math expressions, and `f-strings` (Built Agent `Un01` task & cost tracker)
- [x] **Week 1, Lesson 2 (`week01/lesson02.py`):** Live user input (`input()`), type conversion (`int()`, `float()`), and decision logic (`if / elif / else` AI Budget Guardrail)
- [x] **Week 1 Refresher Exam (Lessons 1 & 2):** Passed 5-question refresher exam + mastered the `if / elif / else` "3 Doors / First-Match Wins" waterfall rule!
- [x] **Week 1, Lesson 3 Initial Code (`week01/lesson03.py`):** Wrote `week01/lesson03.py` and now doing a deep-dive into **How Loops Actually Work From Zero** so both `while` and `for` loops feel 100% natural!

---

## Active Lesson: Week 1, Lesson 3 — How Loops Work From Zero (Pick Up Here at Home!)

> **Note for Antigravity on Home Laptop:** When the user says `"lets continue"`, re-present the **3 Loop Building Blocks** below clearly and walk through the **3-Question Loop Check** with them!

### Building Block 1: The `while True:` Track & `break` (Slow-Motion Laps)
A loop tells Python: *"When you reach the bottom of this indented block, jump back up to the top of the loop and run it again!"* Every repetition is one **Lap (or Turn)**.

```python
credits = 10                      # Before the track starts: credits is 10

while True:                       # <-- TOP OF THE TRACK
    credits -= 4                  # Subtract 4 from credits
    if credits < 0:               # Is credits negative (less than 0)?
        print("Out of credits!")
        break                     # <-- EMERGENCY EXIT (stops the loop!)
    print(f"Credits left: {credits}") # <-- BOTTOM OF THE TRACK (jump back to while True!)
```
- **Lap 1:** `10 - 4 = 6` $\rightarrow$ not `< 0` $\rightarrow$ prints `Credits left: 6` $\rightarrow$ jumps back to top!
- **Lap 2:** `6 - 4 = 2` $\rightarrow$ not `< 0` $\rightarrow$ prints `Credits left: 2` $\rightarrow$ jumps back to top!
- **Lap 3:** `2 - 4 = -2` $\rightarrow$ `-2 < 0` is `True`! $\rightarrow$ prints `Out of credits!` and hits `break` (stops loop!).

### Building Block 2: "Outside the Track" vs. "Inside the Track"
- **Outside/Above the loop (`total_tokens = 0` before `while True:`):** Set to `0` **once** before the loop starts, so it remembers and adds up across laps.
- **Inside the loop (`total_tokens = 0` indented inside `while True:`):** Resets back to `0` at the start of every single lap (wiping out memory!).

### Building Block 3: The `for` Loop & `range(start, stop)`
- **`range(start, stop)` Rule:** `start` is **INCLUDED**, `stop` is **EXCLUDED** (Python stops right *before* the `stop` number!).
- Example: `for i in range(1, 5):` counts `1, 2, 3, 4` and stops as soon as it hits the wall at `5` (`5` is not printed).

---

### Pending 3-Question Loop Check (To Answer on Home Laptop):

1. **(`range` check):** What exact numbers will this loop print?
   ```python
   for i in range(1, 4):
       print(i)
   ```
2. **(`range` reverse check):** If you want a `for` loop to print `1, 2, 3, 4, 5, 6` (including `6`), what two numbers should you put inside `range(___, ___)`?
3. **(Slow-motion `while` trace):** Trace every lap of this loop—what exact lines will it print from start to finish?
   ```python
   battery = 50

   while True:
       battery -= 20
       if battery <= 0:
           print("Battery dead!")
           break
       print(f"Battery: {battery}%")
   ```

---

## Upcoming Next Steps (Week 1)
- [ ] **Finish Loop Deep-Dive & 3-Question Check** (above) + practice any extra small loop puzzles if needed
- [ ] **Week 1 Mini-App #1 (`week01/mini_app_token_estimator.py`):**
  - *Stage 1 (Teach):* String methods (`.lower()`, `.strip()`) + multi-option menu routing (`"1"`, `"2"`, `"3"`) + AI token math
  - *Stage 2 (Hands-On):* Build Client LLM API Token & Model Router Calculator
  - *Stage 3 (Exam):* Post-build review & Mini-Exam
- [ ] **Week 1 Main Capstone App (`week01/app_study_expense_tracker.py`):** Interactive CLI Study XP & AI Freelance Expense Tracker

---

## Daily Laptop Sync Cheat Sheet (GitHub Desktop)

### 1. When You Sit Down at Either Laptop (Start of Session)
- Open **GitHub Desktop** $\rightarrow$ click **Fetch origin** (top right) $\rightarrow$ if there are changes from your other laptop, click **Pull origin**.
- *(Or in terminal: `git pull`)*

### 2. When You Finish Studying on Either Laptop (End of Session)
- Open **GitHub Desktop**:
  1. Look at the bottom-left **Summary** box and type a short note (e.g., `"Sync Loop lesson for home"`).
  2. Click the blue **Commit to main** button.
  3. Click **Push origin** (top right) to send it to the cloud!
