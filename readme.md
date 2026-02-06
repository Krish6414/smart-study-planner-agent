# 🧠 Smart Study Planner – Agentic AI

An Agentic AI system that creates personalized study plans using LLMs, tracks user progress with memory, and automatically replans when a study day is missed.

## 🚀 Features
- LLM-powered study plan generation
- Agent-based architecture (Planner + Memory)
- Persistent state using JSON memory
- Automatic replanning via feedback loop
- CLI-based user input
- Secure API key handling using `.env`

## 🏗 Architecture
- **Planner Agent**: Generates and replans study schedules using an LLM
- **Memory Agent**: Stores progress, current day, and completed tasks
- **Main Controller**: Orchestrates agents and decision-making

## 🛠 Tech Stack
- Python
- OpenAI API
- dotenv
- JSON-based persistence

## ▶️ How to Run
```bash
git clone <repo-url>
cd smart-study-planner-agent
pip install -r requirements.txt
python3 main.py

