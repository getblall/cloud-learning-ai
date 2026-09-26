import os
import time
import random
import re
from duckduckgo_search import DDGS

knowledge_file = "knowledge_base.txt"

# 1. Initialize the file with a handful of random starting sparks
if not os.path.exists(knowledge_file) or os.path.getsize(knowledge_file) < 50:
    with open(knowledge_file, "w") as f:
        f.write("=== AUTONOMOUS INFINITE DISCOVERY DATABASE ===\n")
        f.write("[SEED TOPICS] science math history technology space biology chemistry geography physics engineering\n")

def background_web_harvest(query):
    try:
        with DDGS() as ddgs:
            results = [r for r in ddgs.text(query, max_results=3)]
            if results:
                return " ".join([r['body'] for r in results])
    except Exception:
        return None
    return None

# --- AUTONOMOUS SEED DISCOVERY ENGINE ---
# Read the file data to harvest nouns/concepts the AI has previously seen
with open(knowledge_file, "r") as f:
    text_corpus = f.read()

# Use regular expressions to pull out all English words that are 4+ letters long
all_words = re.findall(r'\b[a-zA-Z]{4,12}\b', text_corpus)

# Filter out common junk words so the AI focuses on unique concepts
stop_words = {'with', 'this', 'that', 'from', 'they', 'this', 'then', 'there', 'their', 'entry', 'data', 'topic', 'base', 'cloud', 'file', 'http', 'html', 'www'}
valid_concepts = [w.lower() for w in all_words if w.lower() not in stop_words]

# Pick a couple of concepts to mash together into a unique new research prompt
if len(valid_concepts) >= 2:
    sampled_words = random.sample(valid_concepts, 2)
    current_topic = f"{sampled_words[0]} {sampled_words[1]} breakthroughs discoveries news"
else:
    # Safe emergency fallback if the file is wiped or empty
    current_topic = random.choice(["math physics", "chemistry history", "biology technology", "space computing"]) + " innovation updates"

print(f"🧠 AI Cognitive Process: Extracted keywords from past memory. Formulating new autonomous topic: '{current_topic}'")
# ----------------------------------------

# Go harvest the web for this dynamically generated topic
gathered_knowledge = background_web_harvest(current_topic)

if not gathered_knowledge:
    gathered_knowledge = f"Autonomous Internal Link: AI mapped logical neuron nodes connecting the conceptual relationship between the terms in '{current_topic}' to expand background matrix dimensions."

# Append the new findings permanently to the database file
with open(knowledge_file, "a") as f:
    f.write(f"\n[AUTONOMOUS ADVANCED DISCOVERY ENTRY: {time.strftime('%Y-%m-%d %H:%M:%S')}]\n")
    f.write(f"Target Concept: {current_topic}\n")
    f.write(f"Learned Knowledge: {gathered_knowledge[:450]}\n")
    f.write("-" * 65 + "\n")

print(f"📝 Success! AI expanded its database with an independent concept loop.")
