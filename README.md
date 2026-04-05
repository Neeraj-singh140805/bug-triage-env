# 🐞 Bug Triage & Code Review Environment (OpenEnv)

## 🚀 Overview

This project implements a real-world OpenEnv environment where an AI agent performs bug triage and code review tasks, similar to what software engineers do in real development pipelines.

The agent is trained to:

* Classify bug severity
* Identify affected system components
* Suggest fixes for bugs

---

## 🎯 Objective

Simulate a realistic workflow where an AI agent processes bug reports and code changes to assist in software maintenance and debugging.

---

## 👀 Observation Space

At each step, the agent receives:

* `issue_title`: Short summary of the bug
* `issue_description`: Detailed explanation
* `files_changed`: List of modified files
* `code_diff`: Code snippet showing changes

---

## 🎮 Action Space

The agent must output:

* `severity`: LOW / MEDIUM / HIGH
* `component`: UI / BACKEND / DATABASE / API
* `fix_suggestion`: Text describing how to fix the bug

---

## 🧩 Tasks

### 🟢 Easy — Severity Classification

Classify how critical the bug is.

### 🟡 Medium — Component Detection

Identify which part of the system is affected.

### 🔴 Hard — Code Review & Fix Suggestion

Analyze code and suggest a fix.

---

## 🧠 Reward Design

The agent is rewarded based on:

* Severity correctness (40%)
* Component correctness (30%)
* Fix quality (30%)

Partial rewards are given for partially correct answers.

---

## ⚙️ Environment API

* `reset()` → Returns initial observation
* `step(action)` → Returns (observation, reward, done, info)
* `state()` → Returns current state

---

## 🏆 Why This Matters

Bug triage and code review are essential in real-world software development. Automating these tasks can significantly improve developer productivity.

---

## 🛠️ Setup (To be added)

Instructions for running environment and baseline agent.

---

## 📊 Baseline (To be added)

Performance of a simple AI agent using OpenAI API.


## ⚙️ How It Works

1. The environment provides a bug report (observation).
2. The agent analyzes the issue and predicts:

   * Severity
   * Component
   * Fix suggestion
3. The environment evaluates the response using a weighted reward system.
4. A score between 0 and 1 is returned.

---

## 🔍 Example Run

Observation:
Button color mismatch

Agent Output:

* Severity: LOW
* Component: UI
* Fix: Check code and fix the issue

Reward:
0.7

Explanation:
The agent correctly identified severity and component but gave a generic fix, so partial reward was given.

---

## 🚀 Real-World Use

This environment can be used to train AI agents that assist developers in:

* Debugging code
* Prioritizing bugs
* Suggesting fixes

---

## 📊 Evaluation

Run evaluation across all tasks:

```bash
python evaluate.py
```

Example Output:

Sample 1: Reward = 0.70
Sample 2: Reward = 0.30

Average Reward: 0.52

This shows how well the agent performs across different difficulty levels.


## 🧪 Run Project

```bash
python baseline.py
```

