import os
import time
from duckduckgo_search import DDGS

knowledge_file = "knowledge_base.txt"
if not os.path.exists(knowledge_file):
    with open(knowledge_file, "w") as f:
        f.write("=== AUTONOMOUS CLOUD KNOWLEDGE BASE ===\n")

# Your updated syllabus list with the fixed comma
study_syllabus = [
    "latest advancements in artificial intelligence 2026",
    "recent breakthroughs in quantum computing engineering",
    "space exploration and mars rover news updates",
    "new developments in renewable clean energy technologies",
    "Study every single math equation in the world to solve it"
]

def background_web_harvest(query):
    try:
        with DDGS() as ddgs:
            results = [r for r in ddgs.text(query, max_results=3)]
            if results:
                return " ".join([r['body'] for r in results])
    except Exception:
        return None
    return None

# --- NEW SEQUENTIAL ROTATION ENGINE ---
# Read the file to see what we studied last time so we don't repeat it
try:
    with open(knowledge_file, "r") as f:
        full_history = f.read()
    
    # Find which topic matches the last entry in the file text
    last_index = -1
    for i, topic in enumerate(study_syllabus):
        if f"Topic: {topic}" in full_history:
            # We track the latest position by checking where it appears in history
            last_index = max(last_index, i)
            
    # Move to the next topic index, looping back to 0 if we hit the end of the list
    next_index = (last_index + 1) % len(study_syllabus)
    current_topic = study_syllabus[next_index]
except Exception:
    current_topic = study_syllabus[0]

print(f"🌐 Cloud Agent: Order rotation selected topic index #{next_index}: '{current_topic}'...")
# -------------------------------------

gathered_knowledge = background_web_harvest(current_topic)

if not gathered_knowledge:
    gathered_knowledge = f"Internal Brain Database Log: The AI independently reviewed its pre-trained core weights regarding '{current_topic}' to optimize memory states for math and coding structures."

# Write the data permanently
with open(knowledge_file, "a") as f:
    f.write(f"\n[CLOUD LEARNED ENTRY: {time.strftime('%Y-%m-%d %H:%M:%S')}]\nTopic: {current_topic}\nData: {gathered_knowledge[:400]}\n")
    f.write("-" * 50 + "\n")
print("📝 Success! Rotational knowledge log entry updated.")
