# install wikipedia package if not already installed
# pip install wikipedia
import wikipedia

topic = input("Enter a topic to search: ")
print("=" * 40)
print(f"Searching Wikipedia for: {topic}")
print("=" * 40)

res = wikipedia.summary(topic, sentences=5)

print(res)
print("=" * 40)
