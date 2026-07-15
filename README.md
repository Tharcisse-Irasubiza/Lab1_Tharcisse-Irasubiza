# Grade Evaluator & Archiver Workspace

An automated suite designed to process student performance records, check category dependencies (Formative vs. Summative distributions), track cumulative Grade Point Averages (GPA), and perform workspace sanitizations securely.

## Components
1. **`grade-evaluator.py`**: Validates structural distributions, evaluates grade margins against core limits, computes final metrics, and tags potential formative recoveries.
2. **`organizer.sh`**: Relocates operational runtime data arrays out of baseline context namespaces into timeline logs.

---

## Getting Started

### Prerequisites
* Python 3.x environment
* Bash execution environment (Linux/macOS terminal or Git Bash on Windows)

---

## Usage Instructions

### 1. Execute the Python Evaluator
To safely calculate standard standings on structured performance lists:

```bash
python grade-evaluator.py
