from brain.action_planner import ActionPlanner
from brain.intents import Intent

planner = ActionPlanner()

print(planner.plan(Intent.STUDY))
print(planner.plan(Intent.QUIZ))
print(planner.plan(Intent.GENERAL_CHAT))
print(planner.plan(Intent.UNKNOWN))