# ⚡ Smart Energy Optimization System
## VTU Internship — Student Repository

**Organisation:** Emertxe Information Technologies
**Programme:** VTU Internship — IoT and Python

---

## What You Are Building

A Python simulation of an intelligent HVAC control system for a commercial
building. The system reads simulated sensor data (temperature, humidity,
occupancy), decides whether the AC should be ON or OFF using rule-based
logic, tracks energy consumption, and displays everything on a live
Streamlit dashboard.

By the end of the programme you will have built all five components from
scratch and run the complete system in your browser.

---

## Programme Structure

This is a **7-day programme**. The first two days are design and discussion —
no coding. Coding begins on Day 1.

| Day | Activity | What you work on |
|---|---|---|
| R1 | Requirements walkthrough | `Docs/requirements.md` |
| R2 | Design walkthrough | `Docs/hld.md` and `Docs/lld.md` |
| 1 | Codealong | `sessions/day1/src/config.py` + `sensor.py` |
| 2 | Codealong | `sessions/day2/src/engine.py` |
| 3 | Codealong | `sessions/day3/src/calculator.py` + `logger.py` |
| 4 | Codealong | `sessions/day4/src/main.py` |
| 5 | Codealong | `sessions/day5/src/dashboard.py` |

---

## Repository Structure

```
├── Docs/
│   ├── requirements.md   # Software Requirements Specification (SRS)
│   ├── hld.md            # High-Level Design
│   └── lld.md            # Low-Level Design
│
├── sessions/
│   ├── day1/src/         # Day 1 starter files
│   ├── day2/src/         # Day 2 starter files
│   ├── day3/src/         # Day 3 starter files
│   ├── day4/src/         # Day 4 starter files
│   └── day5/src/         # Day 5 starter files
│
├── requirements.txt
└── README.md
```

Each `sessions/dayN/src/` folder contains all seven source files. The file
you are implementing that day has `TODO` and `HINT` comments where your
code goes. All other files are complete and ready to run.

---

## Setup (do this once, before Day 1)

```bash
# 1. Clone the repository
git clone https://github.com/EmertxeInfoTech/smart-energy-optimization-system-student.git
cd smart-energy-optimization-system-student

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

## How to Work Each Day

Each coding day, open the folder for that day and work inside it:

```bash
# Example: Day 2
cd sessions/day2/src
```

The file for that day has `TODO` comments. Fill them in, then run the
system to verify your work:

```bash
# Terminal runner (Days 1–4)
python3 main.py

# Streamlit dashboard (Day 5)
streamlit run dashboard.py
```

Your code is correct when the output matches what the mentor shows.
On Day 5, all 10 acceptance criteria in `Docs/requirements.md` Section 11
must pass.

---

## Documents

Read these before you write any code. They define exactly what you are building.

| Document | Read on | What it covers |
|---|---|---|
| [`Docs/requirements.md`](Docs/requirements.md) | Day R1 | What the system must do, use cases, acceptance criteria |
| [`Docs/hld.md`](Docs/hld.md) | Day R2 | How the system is structured, architecture, data flow |
| [`Docs/lld.md`](Docs/lld.md) | Day R2 | How each class works, attributes, method pseudocode |
