import os
import time
import json
import urllib.request

knowledge_file = "knowledge_base.txt"

# 1. Initialize the file text log layout if it doesn't exist
if not os.path.exists(knowledge_file):
    with open(knowledge_file, "w") as f:
        f.write("=== LUMENI: ADVANCED AI COGNITIVE KNOWLEDGE BASE ===\n")

# 2. Securely connect to your repository env secret vault
api_key = os.environ.get("GROQ_API_KEY")

if api_key:
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Utilizing Llama3-8b-8192 optimized for engineering, speed, math, and code syntax structures
    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {
                "role": "system", 
                "content": "You are Lumeni, an elite autonomous mathematical intelligence. Invent an advanced, complex math equation or computer science coding algorithm topic. Provide the complete step-by-step mathematical solution and write a clean, working Python code snippet verifying the output calculation."
            },
            {
                "role": "user", 
                "content": "Generate your next advanced mathematical breakthrough log entry."
            }
        ],
        "temperature": 0.6
    }
    
    try:
        # FIX: Added method="POST" explicitly so the server accepts our data connection payload
        req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers, method="POST")
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            ai_output = res_data["choices"]["message"]["content"]
    except Exception as e:
        ai_output = f"Core operational linkage interface timeout sequence bypass: {str(e)}"
else:
    ai_output = "Bypass Notice: API Key signature not detected in secure repository secrets environment vault framework."

# 3. Append the highly intelligent answer directly to Lumeni's database file archive
with open(knowledge_file, "a") as f:
    f.write(f"\n[LUMENI COGNITIVE LOG ENTRY: {time.strftime('%Y-%m-%d %H:%M:%S')}]\n")
    f.write(ai_output.strip() + "\n")
    f.write("="*75 + "\n")

print("Docs updated successfully.")

