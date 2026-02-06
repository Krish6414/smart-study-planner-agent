from agents.planner_agent import create_study_plan, replan_study
from agents.memory_agent import load_state, save_state, update_progress

# Initial inputs (later we’ll make this CLI)
print("🎓 SMART STUDY PLANNER AGENT\n")

subject = input("Enter subject: ")

syllabus_input = input("Enter syllabus topics (comma separated): ")
syllabus = [topic.strip() for topic in syllabus_input.split(",")]

total_days = int(input("Enter total days until exam: "))
daily_hours = int(input("Enter daily study hours available: "))

state = load_state()

# FIRST TIME: generate plan
if not state["study_plan"]:
    print("📘 Generating initial study plan...\n")
    plan_text = create_study_plan(
        subject,
        ", ".join(syllabus),
        total_days,
        daily_hours
    )

    state["study_plan"] = {
        f"Day {i+1}": topic
        for i, topic in enumerate(plan_text.splitlines())
    }
    save_state(state)

# Simulate today
current_day = state["current_day"]
print(f"\n📅 Today is Day {current_day}")

# 🚨 Simulate missed day
MISSED_DAY = True   # change to False later

if MISSED_DAY:
    print("⚠️ You missed a study day. Replanning...\n")

    remaining_topics = syllabus[current_day - 1:]
    days_left = total_days - current_day + 1

    new_plan = replan_study(
        subject,
        ", ".join(remaining_topics),
        days_left,
        daily_hours
    )

    print("🔄 NEW ADJUSTED PLAN:\n")
    print(new_plan)

else:
    print("✅ Study completed for today!")
    update_progress(current_day)

