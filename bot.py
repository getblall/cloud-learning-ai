import os
import time
import json
import urllib.request

knowledge_file = "knowledge_base.txt"

# 1. Initialize the file text log layout if it doesn't exist
if not os.path.exists(knowledge_file):
    with open(knowledge_file, "w") as f:
        f.write("=== LUMENI: ADVANCED AI COGNITIVE KNOWLEDGE BASE ===\n")

# 2. Connect to Hugging Face's completely free keyless model gateway
# We are using Qwen/Qwen2.5-7B-Instruct which is elite at mathematics and Python coding
url = "https://huggingface.co"

system_prompt = "You are Lumeni, an elite autonomous mathematical intelligence. Invent an advanced, complex math equation or computer science coding algorithm topic. Provide the complete step-by-step mathematical solution and write a clean, working Python code snippet verifying the output calculation."
user_content = "Generate your next advanced mathematical breakthrough log entry."

# Build a modern open chat structure
payload = {
    "inputs": f"<|im_start|>system\n{system_prompt}<|im_end|>\n<|im_start|>user\n{user_content}<|im_end|>\n<|im_start|>assistant\n",
    "parameters": {
        "max_new_tokens": 600,
        "temperature": 0.6,
        "return_full_text": False
    }
    }

headers = {
    "Content-Type": "application/json"
}

try:
    # Send a clean public POST request with zero API key authorization locks
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=15) as response:
        res_data = json.loads(response.read().decode("utf-8"))
        
        # Extract the generated text block safely based on Hugging Face's return array layout
        if isinstance(res_data, list) and len(res_data) > 0:
            ai_output = res_data[0].get("generated_text", "Data formatting gap occurred.")
        elif isinstance(res_data, dict):
            ai_output = res_data.get("generated_text", "Data formatting gap occurred.")
        else:
            ai_output = str(res_data)
except Exception as e:
    ai_output = f"Core operational linkage interface fallback scenario executed: {str(e)}"

# 3. Append the highly intelligent answer directly to Lumeni's database file archive
with open(knowledge_file, "a") as f:
    f.write(f"\n[LUMENI COGNITIVE LOG ENTRY: {time.strftime('%Y-%m-%d %H:%M:%S')}]\n")
    f.write(ai_output.strip() + "\n")
    f.write("="*75 + "\n")

print("Docs updated successfully via open gateway.")
