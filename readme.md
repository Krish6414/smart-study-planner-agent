# 🧠 Smart Study Planner Agent

An Agentic AI-based study planner** that helps students create and adapt a daily study plan based on their subject, syllabus, available time, and exam deadline.

This project demonstrates **agentic workflows**, decision-making, and LLM integration using Python.

## 🚀 What This Project Does
- Takes user input from CLI:
  - Subject
  - Syllabus topics
  - Days left until exam
  - Daily study hours
- Uses an **LLM-powered Planner Agent** to:
  - Break syllabus into manageable tasks
  - Create a day-wise study plan
- Simulates **agentic behavior** by:
  - Detecting missed study days
  - Replanning the schedule dynamically
  
## 🧠 Agentic Architecture

###🧩 Planner Agent
- Uses an LLM to generate a structured study plan
- Performs reasoning and task breakdown
- Outputs a day-wise schedule

### 🔁 Feedback Loop (Basic Agent Behavior)
- Checks progress day-by-day
- If a day is missed, the plan is adjusted automatically
> This project is designed as a **starter agentic AI system**, focusing on clarity and real-world usefulness.

## 🛠 Tech Stack
- **Python**
- **OpenAI API (LLM)**
- **CLI-based input/output**
- **Git & GitHub**

## Project Structure
smart-study-planner-agent/
│
├── main.py # Entry point (CLI interaction)
├── agents/
│ └── planner_agent.py # LLM-powered Planner Agent
├── requirements.txt
├── .gitignore
└── README.md

## ▶️ How to Run the Project

### 1️⃣ Clone the repository
```bash
  git clone https://github.com/Krish6414/smart-study-planner-agent.git
cd smart-study-planner-agent
2️⃣ Install dependencies
  pip install -r requirements.txt
3️⃣ Set up environment variables
Create a .env file and add:
  OPENAI_API_KEY=your_api_key_here
4️⃣ Run the agent
  python main.py
🧪 Example Input
Enter subject: Data Structures
Enter syllabus topics (comma separated): Arrays, Linked Lists, Trees, Graphs
Enter total days until exam: 14
Enter daily study hours available: 2

##📌 Learning Outcomes

Understood agentic AI concepts

Built a multi-step reasoning workflow

Integrated LLMs into decision-making

Gained hands-on experience with GitHub & project structuring

##🔮 Future Improvements

Separate Scheduler Agent

Persistent memory using files or database

Notifications or UI-based interface

Progress tracking dashboard

##👨‍🎓 Author

Krishna Mohan
Fresher | Aspiring AI Engineer
