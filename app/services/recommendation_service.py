from app.repositories import (
    progress_repository,
    topic_repository,
    subject_repository,
    quiz_repository,
    quiz_attempt_repository,
    recommendation_repository
)


def generate_recommendations(
    db,
    student_id: int
):
    recommendations = []

    # --------------------------------
    # Get student's progress
    # --------------------------------
    progress_records = (
        progress_repository.get_progress_by_student(
            db,
            student_id
        )
    )

    # --------------------------------
    # Get student's quiz attempts
    # --------------------------------
    quiz_attempts = (
        quiz_attempt_repository.get_attempts_by_student(
            db,
            student_id
        )
    )

    # --------------------------------
    # Calculate average quiz score
    # --------------------------------
    if quiz_attempts:
        average_quiz_score = (
            sum(
                attempt.score
                for attempt in quiz_attempts
            )
            / len(quiz_attempts)
        )
    else:
        average_quiz_score = None

    # --------------------------------
    # Find weak topics
    # --------------------------------
    weak_topics = []

    for progress in progress_records:

        if progress.completion_percentage >= 40:
            continue

        topic = topic_repository.get_topic_by_id(
            db,
            progress.topic_id
        )

        if topic is None:
            continue

        subject = subject_repository.get_subject_by_id(
            db,
            topic.subject_id
        )

        if subject is None:
            continue

        weak_topics.append({
            "topic_id": topic.topic_id,
            "topic_name": topic.topic_name,
            "subject_id": subject.subject_id,
            "subject_name": subject.subject_name,
            "completion": progress.completion_percentage
        })

    # --------------------------------
    # Generate topic recommendations
    # --------------------------------
    for weak_topic in weak_topics:

        topic_id = weak_topic["topic_id"]
        topic_name = weak_topic["topic_name"]
        subject_id = weak_topic["subject_id"]
        subject_name = weak_topic["subject_name"]
        completion = weak_topic["completion"]

        if average_quiz_score is not None:

            if average_quiz_score < 40:

                recommendation_text = (
                    f"Your {subject_name} progress is "
                    f"{completion}% and your average quiz "
                    f"score is {round(average_quiz_score, 2)}%. "
                    f"Focus specifically on {topic_name}, "
                    f"review the basic concepts, and practice "
                    f"more questions before attempting the "
                    f"next quiz."
                )

                priority = "HIGH"

            elif average_quiz_score < 70:

                recommendation_text = (
                    f"Your {subject_name} progress is "
                    f"{completion}% and your average quiz "
                    f"score is {round(average_quiz_score, 2)}%. "
                    f"Spend more time on {topic_name} and "
                    f"practice additional questions."
                )

                priority = "MEDIUM"

            else:

                recommendation_text = (
                    f"Your quiz performance is good, but your "
                    f"{subject_name} progress is only "
                    f"{completion}%. Continue studying "
                    f"{topic_name} to strengthen your knowledge."
                )

                priority = "MEDIUM"

        else:

            recommendation_text = (
                f"Your {subject_name} progress is "
                f"{completion}%. Focus specifically on "
                f"{topic_name} and complete more practice "
                f"questions."
            )

            priority = "HIGH"

        # --------------------------------
        # Check duplicate using repository
        # --------------------------------
        existing = (
            recommendation_repository
            .get_existing_recommendation(
                db,
                student_id,
                subject_id,
                topic_id,
                recommendation_text
            )
        )

        if existing is not None:
            continue

        # --------------------------------
        # Create recommendation
        # --------------------------------
        recommendation_data = type(
            "RecommendationData",
            (),
            {
                "student_id": student_id,
                "subject_id": subject_id,
                "topic_id": topic_id,
                "recommendation_text": recommendation_text,
                "priority": priority
            }
        )()

        recommendation = (
            recommendation_repository
            .create_recommendation(
                db,
                recommendation_data
            )
        )

        recommendations.append(recommendation)

    # --------------------------------
    # Quiz-only recommendations
    # --------------------------------
    if quiz_attempts and not weak_topics:

        for attempt in quiz_attempts:

            quiz = quiz_repository.get_quiz_by_id(
                db,
                attempt.quiz_id
            )

            if quiz is None:
                continue

            if average_quiz_score < 40:

                recommendation_text = (
                    f"Your average quiz score is "
                    f"{round(average_quiz_score, 2)}%. "
                    f"Review the concepts from "
                    f"{quiz.quiz_name} and practice "
                    f"more questions."
                )

                priority = "HIGH"

            elif average_quiz_score < 70:

                recommendation_text = (
                    f"Your average quiz score is "
                    f"{round(average_quiz_score, 2)}%. "
                    f"Practice more questions from "
                    f"{quiz.quiz_name} to improve your score."
                )

                priority = "MEDIUM"

            else:
                continue

            existing = (
                recommendation_repository
                .get_existing_recommendation(
                    db,
                    student_id,
                    quiz.subject_id,
                    None,
                    recommendation_text
                )
            )

            if existing is not None:
                continue

            recommendation_data = type(
                "RecommendationData",
                (),
                {
                    "student_id": student_id,
                    "subject_id": quiz.subject_id,
                    "topic_id": None,
                    "recommendation_text": recommendation_text,
                    "priority": priority
                }
            )()

            recommendation = (
                recommendation_repository
                .create_recommendation(
                    db,
                    recommendation_data
                )
            )

            recommendations.append(recommendation)

    return recommendations