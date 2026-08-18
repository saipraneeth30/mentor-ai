from database.connection import cursor


def get_student():

    cursor.execute("""
        SELECT
            name,
            goal,
            today_topic,
            questions,
            quiz_time,
            streak
        FROM students
        LIMIT 1
    """)

    row = cursor.fetchone()

    return {
        "name": row[0],
        "goal": row[1],
        "today_topic": row[2],
        "questions": row[3],
        "quiz_time": row[4],
        "streak": row[5]
    }