import discord


class QuizQuestionView(discord.ui.View):

    def __init__(self, questions, question_index=0, score=0):

        super().__init__(timeout=180)

        self.questions = questions
        self.question_index = question_index
        self.score = score

        question = questions[question_index]

        options = question["options"]

        self.add_item(
            AnswerButton(
                label="A",
                answer=options[0],
                correct_answer=question["correct_answer"],
                questions=questions,
                question_index=question_index,
                score=score
            )
        )

        self.add_item(
            AnswerButton(
                label="B",
                answer=options[1],
                correct_answer=question["correct_answer"],
                questions=questions,
                question_index=question_index,
                score=score
            )
        )

        self.add_item(
            AnswerButton(
                label="C",
                answer=options[2],
                correct_answer=question["correct_answer"],
                questions=questions,
                question_index=question_index,
                score=score
            )
        )

        self.add_item(
            AnswerButton(
                label="D",
                answer=options[3],
                correct_answer=question["correct_answer"],
                questions=questions,
                question_index=question_index,
                score=score
            )
        )


class AnswerButton(discord.ui.Button):

    def __init__(
        self,
        label,
        answer,
        correct_answer,
        questions,
        question_index,
        score
    ):

        super().__init__(
            label=label,
            style=discord.ButtonStyle.primary
        )

        self.answer = answer
        self.correct_answer = correct_answer
        self.questions = questions
        self.question_index = question_index
        self.score = score


    async def callback(self, interaction: discord.Interaction):

        if self.answer == self.correct_answer:
            self.score += 1

        next_index = self.question_index + 1


        if next_index < len(self.questions):

            question = self.questions[next_index]


            embed = discord.Embed(
                title=f"📝 Question {next_index + 1}",
                description=question["question"],
                color=discord.Color.orange()
            )

            for index, option in enumerate(question["options"]):

                embed.add_field(
                    name=f"Option {chr(65+index)}",
                    value=option,
                    inline=False
                )


            await interaction.response.edit_message(
                embed=embed,
                view=QuizQuestionView(
                    self.questions,
                    next_index,
                    self.score
                )
            )

        else:

            embed = discord.Embed(
                title="🏆 Quiz Completed",
                description=(
                    f"Your Score: **{self.score}/{len(self.questions)}**"
                ),
                color=discord.Color.gold()
            )


            await interaction.response.edit_message(
                embed=embed,
                view=None
            )