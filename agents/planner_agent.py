import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_study_plan(subject, syllabus, days_left, daily_hours):
    prompt = f"""
You are a smart study planner AI.

Subject: {subject}
Syllabus topics: {syllabus}
Days left until exam: {days_left}
Daily study time available: {daily_hours} hours

Task:
1. Break the syllabus into small study tasks
2. Distribute tasks across days
3. Ensure workload is realistic
4. Output a clear day-wise plan

Respond in this format:
Day 1: ...
Day 2: ...
...
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

def replan_study(subject, remaining_topics, days_left, daily_hours):
    prompt = f"""
You are a smart study replanning AI.

Subject: {subject}
Remaining topics: {remaining_topics}
Days left: {days_left}
Daily study time: {daily_hours} hours

Create an adjusted day-wise study plan.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

