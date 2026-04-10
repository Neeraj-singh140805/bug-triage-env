---
title: bug-triage-env
emoji: 🐛
colorFrom: purple
colorTo: blue
sdk: docker
pinned: false
---

<p align="center">

# 🐞 Bug Triage AI

### An AI agent that classifies bugs, detects affected components, and suggests fixes — with explainable decisions and real-time scoring.

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Hugging_Face-orange?style=for-the-badge)](https://huggingface.co/spaces/Neeraj140805/bug-triage-env)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Gradio](https://img.shields.io/badge/Gradio-UI-FF7C00?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)

</p>

---

## 📌 Overview

**Bug Triage AI** is an [OpenEnv](https://openenv.dev) environment where an AI agent simulates real-world software engineering triage tasks. Given a bug report — title, description, changed files, and a code diff — the agent predicts severity, identifies the affected component, and proposes a fix. A built-in reward system lets users score the AI's decisions against their own expected answers.

---

## 🖥️ App Screenshots

### Input — Submit a Bug Report

<p align="center">
<img src="/assets/images/input.png" alt="Bug Triage AI — Input Form" width="90%"/>
</p>

> Enter a bug title, description, affected files, and a code diff. Set your expected severity and component to enable scoring.

---

### Output — AI Analysis Results

<p align="center">
<img src="/assets/images/output.png" alt="Bug Triage AI — Output Panel" width="90%"/>
</p>

> The AI Decision Engine returns the predicted severity, component, and a fix suggestion. The reward score is calculated instantly against your expected answers.

---

## 🎯 Key Features

| Feature | Description |
|---|---|
| 🤖 **AI-powered bug analysis** | Predicts severity, component, and fix from raw bug reports |
| 💡 **Explainable decisions** | Every prediction comes with a "Why?" rationale |
| 🎯 **Expected Answer system** | Users set ground truth — the system scores AI accuracy |
| 📊 **Real-time reward scoring** | Weighted score computed instantly on submission |
| 🎨 **Clean Gradio UI** | Dark-themed, developer-friendly interface |

---

## 🧠 How It Works

```
User Input ──► AI Agent ──► Predictions ──► Scoring
  (bug info)    (triage)    (severity,       (vs expected
                            component,        answers)
                            fix)
```

**Step-by-step:**

1. **User inputs** — bug title, description, files changed, code diff
2. **AI predicts** — severity (`LOW` / `MEDIUM` / `HIGH`), component (`UI` / `BACKEND` / `DATABASE` / `API`), fix suggestion
3. **User provides** — expected severity, component, and optionally an expected fix
4. **System scores** — a weighted reward ∈ [0, 1] is calculated

---

## 📊 Reward System

The final score is a weighted combination of three metrics:

| Metric | Weight | How it's measured |
|---|---|---|
| ⚠️ Severity match | **40%** | Exact match between predicted and expected severity |
| 🧩 Component match | **30%** | Exact match between predicted and expected component |
| 🔧 Fix quality | **30%** | Semantic similarity between predicted and expected fix |

> **Final score ∈ [0, 1]** — higher is better.

---

## 📦 Project Structure

```
.
├── app.py              # Gradio UI + FastAPI server
├── env.py              # OpenEnv environment definition
├── baseline.py         # Rule-based baseline agent
├── inference.py        # Submission entry point
├── evaluate.py         # Offline evaluation script
├── Dockerfile          # Docker build configuration
├── requirements.txt    # Python dependencies
└── README.md
```

---

## ⚙️ Setup & Run Locally

**1. Clone the repo**
```bash
git clone https://huggingface.co/spaces/Neeraj140805/bug-triage-env
cd bug-triage-env
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
python app.py
```

The Gradio UI will be available at `http://localhost:7860`.

---

## 🐳 Run with Docker

```bash
docker build -t bug-triage-ai .
docker run -p 7860:7860 bug-triage-ai
```

---

## 👨‍💻 Author

<p align="center">

**Neeraj Singh** — Builder of Bug Triage AI

[![Hugging Face](https://img.shields.io/badge/Hugging_Face-Neeraj140805-FFD21E?style=flat&logo=huggingface&logoColor=black)](https://huggingface.co/Neeraj140805)

</p>

---

<p align="center">
Built with ❤️ for intelligent bug triage systems
</p>