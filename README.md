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

### AI-powered bug triage system that simulates real-world engineering workflows — classify, analyze, and fix bugs with explainable intelligence.

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Hugging_Face-orange?style=for-the-badge)](https://huggingface.co/spaces/Neeraj140805/bug-triage-env)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Gradio](https://img.shields.io/badge/Gradio-UI-FF7C00?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)

</p>

---

## 📌 Overview

**Bug Triage AI** is an intelligent OpenEnv environment designed to replicate how real engineering teams triage bugs.

Given a bug report (title, description, files changed, and code diff), the system:

- ⚠️ Predicts **bug severity**
- 🧩 Identifies the **affected component**
- 🔧 Suggests a **potential fix**
- 💡 Explains **why the decision was made**
- 📊 Evaluates itself using a **reward-based scoring system**

> 🎯 Goal: Reduce manual triage effort, improve developer productivity, and simulate real-world debugging workflows with AI.

---

## 🚀 What Makes This Unique?

Unlike traditional ML demos, this project goes beyond prediction:

- 🧠 **Human-in-the-loop evaluation** — users define expected outputs  
- 📊 **Reward-based scoring system** — AI is evaluated like a real engineer  
- 💬 **Explainable AI decisions** — every prediction includes reasoning  
- 🔁 **Interactive feedback loop** — compare AI vs human judgment  
- 🏗️ **Simulation of real triage pipelines**, not just classification  

> This transforms the project from a static model into a **decision-making system**.

---

## 🖥️ App Preview

### 📝 Input — Submit a Bug Report

<p align="center">
<img src="/assets/images/input.png" alt="Bug Input" width="90%"/>
</p>

> Provide bug details including title, description, affected files, and code diff. Optionally define expected outputs for evaluation.

---

### 🤖 Output — AI Decision Engine

<p align="center">
<img src="/assets/images/output.png" alt="Bug Output" width="90%"/>
</p>

> The system predicts severity, component, and fix — along with explanations and a real-time reward score.

---

## 🎯 Key Features

| Feature | Description |
|---|---|
| 🤖 **AI-powered triage** | Classifies severity, component, and suggests fixes |
| 💡 **Explainability layer** | Transparent reasoning behind every prediction |
| 🎯 **Expected Answer system** | Users define ground truth for evaluation |
| 📊 **Reward scoring engine** | Weighted scoring based on prediction accuracy |
| 🔁 **Interactive feedback loop** | Compare AI vs human decisions instantly |
| 🎨 **Clean developer UI** | Built with Gradio for simplicity and speed |

---

## 🧠 System Architecture
<p align="center">
<img src="/assets/images/architecture.png" width="80%"/>
</p>


---

## ⚙️ Model & Approach

The system uses a **hybrid AI approach** combining rule-based logic and lightweight NLP:

- 🔍 **Severity Prediction**
  - Keyword-based heuristics (e.g., "crash", "failure", "urgent")
  
- 🧩 **Component Classification**
  - Pattern matching on file paths and keywords  
  - Categories: `UI`, `BACKEND`, `DATABASE`, `API`

- 🔧 **Fix Suggestion**
  - Template-based + semantic similarity logic  

- 💬 **Explainability**
  - Each prediction includes reasoning derived from detected signals  

> 🧪 Future Work:  
> - Fine-tuned transformer models (BERT / LLMs)  
> - Learning from real bug datasets  

---

## 📊 Reward System

The system evaluates its own predictions using a weighted scoring model:

| Metric | Weight | Description |
|---|---|---|
| ⚠️ Severity Match | **40%** | Exact match with expected severity |
| 🧩 Component Match | **30%** | Exact match with expected component |
| 🔧 Fix Quality | **30%** | Semantic similarity with expected fix |

> 🎯 Final Score ∈ [0, 1]

---

## 📦 Project Structure

```bash
.
├── app.py              # Gradio UI + FastAPI backend
├── env.py              # OpenEnv environment definition
├── baseline.py         # Rule-based baseline agent
├── inference.py        # Model inference logic
├── evaluate.py         # Evaluation script
├── Dockerfile          # Container setup
├── requirements.txt    # Dependencies
├── assets
│   └── images
│       ├── input.png
│       ├── output.png
│       └── architecture.png
└── README.md
```


---

## ⚙️ Run Locally

```bash
git clone https://huggingface.co/spaces/Neeraj140805/bug-triage-env
cd bug-triage-env

pip install -r requirements.txt
python app.py


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