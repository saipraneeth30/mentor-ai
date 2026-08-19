from datetime import datetime, timedelta


class TimetableAgent:

    DAYS = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
    ]

    # -----------------------------
    # Allocate Study Duration
    # -----------------------------
    def allocate_duration(self, subject, profile):

        weak_subjects = [
            s.strip().lower()
            for s in profile.weak_subjects.split(",")
            if s.strip()
        ]

        if subject.subject_name.lower() in weak_subjects:

            if profile.goal.lower() == "gate":
                return 4

            return 3

        if subject.difficulty == "Hard":
            return 3

        elif subject.difficulty == "Medium":
            return 2

        return 1

    # -----------------------------
    # Subject Priority
    # -----------------------------
    def get_priority(self, subject, profile):

        weak_subjects = [
            s.strip().lower()
            for s in profile.weak_subjects.split(",")
            if s.strip()
        ]

        if subject.subject_name.lower() in weak_subjects:
            return 1

        if subject.difficulty == "Hard":
            return 2

        if subject.difficulty == "Medium":
            return 3

        return 4

    # -----------------------------
    # Starting Time
    # -----------------------------
    def get_start_time(self, preferred_time):

        preferred_time = preferred_time.lower()

        if preferred_time == "morning":
            return datetime.strptime("09:00", "%H:%M")

        elif preferred_time == "afternoon":
            return datetime.strptime("14:00", "%H:%M")

        return datetime.strptime("19:00", "%H:%M")

    # -----------------------------
    # Weekly Schedule
    # -----------------------------
    def generate_weekly_schedule(
        self,
        subjects,
        profile,
        available_hours
    ):

        sorted_subjects = sorted(
            subjects,
            key=lambda subject: self.get_priority(subject, profile)
        )

        weekly_schedule = {}

        subject_index = 0

        for day in self.DAYS:

            if subject_index >= len(sorted_subjects):
                break

            current_time = self.get_start_time(
                profile.preferred_study_time
            )

            used_hours = 0

            day_schedule = []

            while subject_index < len(sorted_subjects):

                subject = sorted_subjects[subject_index]

                duration = self.allocate_duration(
                    subject,
                    profile
                )

                if used_hours + duration > available_hours:
                    break

                start = current_time
                end = start + timedelta(hours=duration)

                day_schedule.append({
                    "subject": subject.subject_name,
                    "difficulty": subject.difficulty,
                    "priority": self.get_priority(subject, profile),
                    "start_time": start.strftime("%I:%M %p"),
                    "end_time": end.strftime("%I:%M %p"),
                    "duration": f"{duration} Hours"
                })

                used_hours += duration
                current_time = end + timedelta(minutes=15)
                subject_index += 1

            weekly_schedule[day] = day_schedule

        # -----------------------------
        # Add Learning Activities
        # -----------------------------
        activities = [
            "Revision",
            "Practice Questions",
            "Mock Test",
            "Project Work"
        ]

        remaining_days = self.DAYS[len(weekly_schedule):]

        for day, activity in zip(remaining_days, activities):
            weekly_schedule[day] = [
                {
                    "activity": activity
                }
            ]

        return weekly_schedule