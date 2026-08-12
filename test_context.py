from brain.context_manager import ContextManager

context = ContextManager()

user1 = 101
user2 = 202

context.set(user1, "current_topic", "Binary Search")
context.set(user1, "last_intent", "STUDY")

context.set(user2, "current_topic", "Trees")

print("User1 Topic :", context.get(user1, "current_topic"))
print("User1 Intent:", context.get(user1, "last_intent"))

print("User2 Topic :", context.get(user2, "current_topic"))

print("\nAll User1 Context")
print(context.get_all(user1))

context.clear(user1)

print("\nAfter Clear")
print(context.get_all(user1))
