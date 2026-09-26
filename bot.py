import os
import time
import random
import sympy as sp

print("🚀 LUMENI STATUS: 24/7 High-Speed Mathematical Core Online.")
print("Stream lining calculation matrix loops... Standby.\n")

# Track total cycles completed in memory
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

        # Output the compiled entry to the server log dashboard stream
        print(f"[ENTRY #{total_calculations} | {time.strftime('%H:%M:%S')}]")
        print(log_text)
        print("-" * 60)
        
        # Pauses for 5 seconds before executing the next math breakthrough
        time.sleep(5)

except KeyboardInterrupt:
    print("Server stopped.")
