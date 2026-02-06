import json

MEMORY_FILE = "memory/study_state.json"

def load_state():
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_state(state):
    with open(MEMORY_FILE, "w") as f:
        json.dump(state, f, indent=4)

def update_progress(day_completed):
    state = load_state()
    state["completed_days"].append(day_completed)
    state["current_day"] += 1
    save_state(state)

