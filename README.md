#  Autonomous Enterprise Workflow Engine
### *Next-Gen Multi-Agent Meeting Intelligence & Task Automation*

<p align="center">
  <img src="https://img.shields.io/badge/Agentic%20AI-State%20Machine-blueviolet?style=for-the-badge&logo=ai" />
  <img src="https://img.shields.io/badge/Language-Python%203.9+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/LLM-Llama--3.1-orange?style=for-the-badge&logo=meta" />
  <img src="https://img.shields.io/badge/Inference-Groq_Cloud-f5f5f5?style=for-the-badge&logo=speedtest&logoColor=orange" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge&logo=opensourceinitiative&logoColor=white" />
</p>

---

## Overview

An **Agentic AI system** that converts unstructured meeting transcripts into **intelligent, executable workflows** — with minimal human intervention and full transparency.

* Extracts decisions using LLMs
* Assigns owners & priorities automatically
* Maps task dependencies intelligently
* Simulates autonomous execution cycles
* Maintains a complete audit trail of all actions

---

## Problem Statement

Build a system that can:

* Manage **multi-step enterprise workflows**
* Detect failures and **self-correct dynamically**
* Execute tasks with **minimal manual intervention**
* Maintain a **fully auditable and explainable decision trail**

---

## System Architecture

```mermaid
flowchart LR
    A[Meeting Transcript] --> B[LLM Agent]
    B --> C[Workflow Engine]
    C --> D[Task Registry]
    D --> E[Validator Agent]
    E --> F[Audit Trail]
```

---

## Multi-Agent System

| Agent                          | Responsibility                                         |
| ------------------------------ | ------------------------------------------------------ |
| **LLM**                     | Extracts structured decisions and assigns ownership    |
| **Logic Engine**            | Handles dependencies, state transitions, and execution |
| **Validator**               | Verifies completion and records all system actions     |

---

## Core Capabilities

* AI-powered decision & task extraction
* Dependency-aware workflow execution
* Autonomous task lifecycle management
* Real-time interactive dashboard (Gradio)
* Fully explainable audit logging

---

## Execution Lifecycle

```mermaid
flowchart TD
    A[Pending ⚪] --> B[In Progress 🔵]
    B --> C{Dependency Check}
    C -->|Blocked| D[Stalled 🔴]
    C -->|Clear| E[Continue]
    E --> F[Resolved 🟢]
```

---

## Tech Stack

| Layer      | Technology         |
| ---------- | ------------------ |
| AI Layer   | Llama-3 (Groq API) |
| Backend    | Python             |
| Interface  | Gradio             |
| Data Layer | Pandas             |

---

## Project Structure

```
etimes-ai-workflow/
│
├── src/              # Core system (agents, workflow engine)
├── notebook/         # Interactive Colab demo
├── data/             # Sample inputs
├── outputs/          # Sample outputs
├── images/           # UI & architecture visuals
├── docs/             # Approach & design notes
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Setup & Run

```bash
git clone <your-repo-link>
cd etimes-ai-workflow
pip install -r requirements.txt
python src/main.py
```

### Quick Demo (Colab)

* **Run Demo (Colab)**  
[Open Notebook](https://github.com/<your-username>/<your-repo>/blob/main/notebook/demo.ipynb)

- Add API key via secrets  
- Run all cells

---

## Security & Reliability

* Secure API key handling (no hardcoding)
* No persistent storage of sensitive data
* Input validation for safe processing
* Controlled and minimal dependency usage

---

## Auditability

Every system action is **logged, traceable, and verifiable**, ensuring enterprise-grade transparency.

### Sample Audit Trail

| Time  | Agent       | Event             | Description                    |
| ----- | ----------- | ----------------- | ------------------------------ |
| 05:31 | Planner  | Task Indexed      | Extracted decision → Task #1   |
| 05:31 | Planner  | Task Indexed      | Extracted decision → Task #2   |
| 05:31 | Executor | Execution Started | Task #1 moved to *In Progress* |
| 05:31 | Executor | Execution Started | Task #2 moved to *In Progress* |
| 05:31 | Auditor  | Validation        | Task #1 marked as *Resolved*   |

### Guarantees

* **Full Traceability** → Every action tied to agent & timestamp
* **Explainable Decisions** → Clear path from input → execution
* **Failure Visibility** → Stalled tasks tracked via dependencies
* **Audit-Ready Logs** → Structured for monitoring & debugging

> Full logs are visible in the live dashboard during execution.

---

## Key Challenges & Solutions

| Challenge                             | Solution                                                                    |
| ------------------------------------- | --------------------------------------------------------------------------- |
| Handling non-linear task dependencies | Designed a dependency-aware state engine to dynamically stall/unblock tasks |
| Ensuring structured AI output         | Enforced strict JSON response format from LLM                               |
| Maintaining explainability            | Built a dedicated audit trail tracking every agent action                   |

> These design decisions ensure the system remains reliable, interpretable, and production-ready.

---

## Summary

This system demonstrates how **Agentic AI** evolves from passive assistance to **active, autonomous execution**, combining:

* Intelligence (LLMs)
* Logic (Workflow Engine)
* Transparency (Audit Trail)

---

<p align="center">
  <b>Economic Times Hackathon • Agentic AI Track</b><br>
  <i>Built for autonomous enterprise workflows</i>
</p>
