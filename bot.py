import os
import time
import random
import threading
import sympy as sp
from flask import Flask

# 1. Initialize a tiny, lightweight web application framework for Render's port check scanner
app = Flask(__name__)

@app.route('/')
def home():
    return "LUMENI ACTIVE: 24/7 High-Speed Mathematical Core Operational Core Online."

# 2. Package your infinite high-speed math engine loops into an independent background thread tracker
def infinite_math_loop():
    print("🚀 LUMENI STATUS: 24/7 High-Speed Mathematical Core Online.")
    print("Streamlining calculation matrix loops... Standby.\n")
    
    total_calculations = 0
    math_modes = ["Calculus", "Matrix", "Algebraic_Balance"]

    try:
        while True:
            selected_mode = random.choice(math_modes)
            total_calculations += 1
            log_text = ""

            if selected_mode == "Calculus":
                x = sp.Symbol('x')
                power, coeff, constant = random.randint(2, 5), random.randint(2, 9), random.randint(1, 15)
                expression = coeff * x**power + constant
                derivative = sp.diff(expression, x)
                integral = sp.integrate(expression, x)
                
                log_text = f"🧪 Calculus Log | Target: f(x) = {expression}\n"
                log_text += f"  -> Derivative: f'(x) = {derivative}\n  -> Integral: ∫ = {integral} + C"

            elif selected_mode == "Matrix":
                a, b, c, d = random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5)
                matrix = sp.Matrix([[a, b], [c, d]])
                det = matrix.det()
                try:
                    inv = matrix.inv()
                    inv_text = str(inv)
                except Exception:
                    inv_text = "Singular Matrix (No Inverse)"
                    
                log_text = f"📊 Matrix Log | Target Array M: [[{a}, {b}], [{c}, {d}]]\n"
                log_text += f"  -> Determinant: {det}\n  -> Inverse: {inv_text}"

            else:
                x = sp.Symbol('x')
                a, b, c, d = random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5)
                factored_expr = (a*x + b) * (c*x + d)
                expanded_expr = sp.expand(factored_expr)
                
                log_text = f"📐 Algebra Log | Target: ({a}x + {b})({c}x + {d})\n"
                log_text += f"  -> FOIL Expanded Polynomial Expression: {expanded_expr} = 0"

            # Print explicitly to Render terminal console stream logs
            print(f"[ENTRY #{total_calculations} | {time.strftime('%H:%M:%S')}]", flush=True)
            print(log_text, flush=True)
            print("-" * 60, flush=True)
            
            time.sleep(5)
    except Exception as e:
        print(f"Loop error: {str(e)}", flush=True)

if __name__ == "__main__":
    # Start your infinite math loops on its own thread channel so it never stalls out the system
    threading.Thread(target=infinite_math_loop, daemon=True).start()
    
    # Grab the port number Render assigned to our free account automatically
    port = int(os.environ.get("PORT", 10000))
    
    # Start web channel listener interface framework block
    app.run(host="0.0.0.0", port=port)
