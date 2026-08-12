from brain.workflow import Workflow

workflow = Workflow()

user_id = 101

workflow.run(
    user_id,
    "Explain Binary Search"
)

print(workflow.context.get_all(user_id))