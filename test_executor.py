from brain.executor import Executor
from brain.actions import Action

executor = Executor()

print(executor.execute(Action.TEACH))
print(executor.execute(Action.GENERATE_QUIZ))
print(executor.execute(Action.GREET))
print(executor.execute(Action.ASK_AI))