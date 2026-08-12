from brain.topic_extractor import TopicExtractor

extractor = TopicExtractor()

messages = [
    "Explain Binary Search",
    "Teach Linked List",
    "What is Dynamic Programming",
    "Learn Graphs",
    "Understand Recursion",
    "Hello"
]

for msg in messages:

    topic = extractor.extract(msg)

    print(f"Message : {msg}")
    print(f"Topic   : {topic}")
    print("-" * 40)