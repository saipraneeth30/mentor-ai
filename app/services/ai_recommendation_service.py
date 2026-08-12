import os

from openai import OpenAI


def generate_ai_recommendation(
    student_name: str,
    overall_progress: float,
    weak_topics: list,
    average_quiz_score: float | None
):

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is not configured"
        )

    client = OpenAI(api_key=api_key)

    if weak_topics:
        topics_text = ", ".join(
            topic["topic_name"]
            for topic in weak_topics
        )
    else:
        topics_text = "No major weak topics identified"

    if average_quiz_score is not None:
        quiz_text = f"{average_quiz_score:.2f}%"
    else:
        quiz_text = "No quiz attempts yet"

    prompt = f"""
You are MentorAI, an AI learning mentor.

Student:
{student_name}

Overall progress:
{overall_progress}%

Weak topics:
{topics_text}

Average quiz score:
{quiz_text}

Create a short, practical personalized study recommendation.

Include:

1. Main weakness
2. Topics to study
3. Specific action to take
4. Priority: HIGH, MEDIUM, or LOW

Use only the information provided.
Do not invent topics.
Keep the response concise and suitable for a student.
"""

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    return response.output_text