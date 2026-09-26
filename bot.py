import os
import time
import random
import re
import json
import urllib.request

knowledge_file = "knowledge_base.txt"

# Initialize with deep mathematical core seeds
if not os.path.exists(knowledge_file) or os.path.getsize(knowledge_file) < 50:
    with open(knowledge_file, "w") as f:
        f.write("=== INFINITE PURE MATHEMATICS CORE DATABASE ===\n")
        f.write("[CORE SEEDS] Calculus Algebra Topology Combinatorics Geometry Algorithm Cryptography Trig\n")

def wiki_math_search(title):
    """Instant lookup inside Wikipedia's academic core."""
    try:
        formatted_title = urllib.parse.quote(title.strip().replace(" ", "_"))
        url = f"https://wikipedia.org{formatted_title}"
        req = urllib.request.Request(url, headers={'User-Agent': 'MathAI_Bot/1.0 (math@example.com)'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode('utf-8'))
            return data.get("extract", None)
    except Exception:
        return None

# --- MATHEMATICAL CONCEPT HARVESTER ---
with open(knowledge_file, "r") as f:
    text_corpus = f.read()

# Isolate all capitalized terms that are likely advanced mathematical keywords
all_words = re.findall(r'\b[A-Z][a-z]{4,14}\b', text_corpus)

# Strict math-only filter terms to keep the AI from drifting away into history/biography
math_anchors = [
    "Equation", "Theorem", "Calculus", "Matrix", "Algebra", "Vector", "Integral",
    "Derivative", "Topology", "Geometry", "Fraction", "Algorithm", "Tensor", "Function",
    "Logarithm", "Polynomial", "Asymptote", "Coordinate", "Differential", "Manifold",
    "Arithmetic", "Combinatorics", "Cryptography", "Probability", "Graph_theory", "Statistic"
]

banned_words = {"High", "Speed", "Fast", "Core", "Target", "Concept", "Entry", "Extract", "Database", "Knowledge"}
valid_math_terms = [w for w in all_words if w not in banned_words]

# 70% chance to jump down a discovered math branch, 30% chance to reinforce core pillars
if valid_math_terms and random.random() > 0.3:
    raw_pick = random.choice(valid_math_terms)
    # Hyper-focus the term by structurally linking it directly to math logic rules
    current_topic = random.choice([raw_pick, f"{raw_pick}_(mathematics)", f"{raw_pick}_theorem", f"{raw_pick}_equation"])
else:
    current_topic = random.choice(math_anchors)

print(f"📐 Math Core: Locking target sequence onto -> '{current_topic}'")

# --- EXECUTE CALCULATION & INGESTION ---
start_time = time.time()
learned_facts = wiki_math_search(current_topic)
elapsed_time = time.time() - start_time

# If a hyper-focused sub-link is too narrow, fall back directly onto a stable core mathematical pillar
if not learned_facts:
    current_topic = random.choice(math_anchors)
    learned_facts = wiki_math_search(current_topic)

# --- SAVE TO PERMANENT MATH JOURNAL ---
with open(knowledge_file, "a") as f:
    f.write(f"\n[MATHEMATICAL DISCOVERY LOG: {time.strftime('%Y-%m-%d %H:%M:%S')} | Latency: {elapsed_time:.3f}s]\n")
    f.write(f"Equation/Concept Target: {current_topic.replace('_', ' ')}\n")
    f.write(f"Analyzed Core Logic: {learned_facts}\n")
    f.write("=" * 70 + "\n")

print(f"📝 Math log entry committed in {elapsed_time:.3f}s.")
