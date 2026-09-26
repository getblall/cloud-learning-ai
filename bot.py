import os
import time
import random
import json
import urllib.request

knowledge_file = "knowledge_base.txt"

# Initialize with core algebraic seeds for isolating variables
if not os.path.exists(knowledge_file) or os.path.getsize(knowledge_file) < 50:
    with open(knowledge_file, "w") as f:
        f.write("=== ALGEBRA CORE: VARIABLES ON BOTH SIDES ===\n")
        f.write("[CORE SEEDS] Linear_equation Algebraic_equation Variable_isolation Inverse_operations Balancing_equations\n")

def wiki_algebra_search(title):
    """Direct API lookup for academic algebraic core structures."""
    try:
        formatted_title = urllib.parse.quote(title.strip().replace(" ", "_"))
        url = f"https://wikipedia.org{formatted_title}"
        req = urllib.request.Request(url, headers={'User-Agent': 'AlgebraAI_Bot/1.0 (algebra@example.com)'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode('utf-8'))
            return data.get("extract", None)
    except Exception:
        return None

# --- VARIABLE BALANCE SCOUTING LIST ---
# A targeted core pool focusing heavily on equation manipulation principles
algebra_targets = [
    "Linear_equation",
    "Algebraic_equation",
    "Elementary_algebra",
    "Equation_solving",
    "Variable_(mathematics)",
    "Operation_(mathematics)",
    "Inverse_operation",
    "Distributive_property",
    "Like_terms",
    "Equality_(mathematics)"
]

# Pick a core concept to explore balance mechanics
current_topic = random.choice(algebra_targets)

print(f"📐 Algebra Core: Targeting variable balance concept -> '{current_topic}'")

# --- EXECUTE LOGIC FETCH ---
start_time = time.time()
learned_facts = wiki_algebra_search(current_topic)
elapsed_time = time.time() - start_time

# Fallback block to maintain integrity if a specific pathway drops
if not learned_facts:
    current_topic = "Linear_equation"
    learned_facts = wiki_algebra_search(current_topic)

# --- SAVE TO THE PERMANENT DATABASE FILE ---
with open(knowledge_file, "a") as f:
    f.write(f"\n[ALGEBRA LOG ENTRY: {time.strftime('%Y-%m-%d %H:%M:%S')} | Latency: {elapsed_time:.3f}s]\n")
    f.write(f"Focus Concept: {current_topic.replace('_', ' ')}\n")
    f.write(f"Equation Balancing Core Data: {learned_facts}\n")
    f.write("=" * 70 + "\n")

print(f"📝 Algebraic log entry successfully committed in {elapsed_time:.3f}s.")
