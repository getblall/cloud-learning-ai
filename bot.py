import os
import time
import random
import sympy as sp

knowledge_file = "knowledge_base.txt"

# Initialize the file text log layout if it doesn't exist
if not os.path.exists(knowledge_file):
    with open(knowledge_file, "w") as f:
        f.write("=== LUMENI: UN-BLOCKABLE HIGH-REASONING MATHEMATICS DATABASE ===\n")

# --- CHOOSE A COMPREHENSIVE MATH BRANCH DIP ---
math_modes = ["Calculus", "Matrix", "Algebraic_Balance"]
selected_mode = random.choice(math_modes)

log_text = ""

if selected_mode == "Calculus":
    # Autonomously invent a complex calculus expression
    x = sp.Symbol('x')
    power = random.randint(2, 5)
    coeff = random.randint(2, 9)
    constant = random.randint(1, 15)
    
    # Example: 3x^4 + 12
    expression = coeff * x**power + constant
    
    # Calculate the Derivative and the Integral using pure symbolic math logic
    derivative = sp.diff(expression, x)
    integral = sp.integrate(expression, x)
    
    log_text = f"Category: Advanced Calculus (Symbolic Integration & Differentiation)\n"
    log_text += f"Target Function: f(x) = {expression}\n"
    log_text += f"  1. Derivative Log: f'(x) = d/dx [{expression}] -> Answer: {derivative}\n"
    log_text += f"  2. Integral Log: ∫ [{expression}] dx -> Answer: {integral} + C\n"

elif selected_mode == "Matrix":
    # Autonomously invent a 2x2 matrix structure
    a, b, c, d = random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5)
    matrix = sp.Matrix([[a, b], [c, d]])
    
    # Compute the Determinant and Inverse Matrix values
    det = matrix.det()
    try:
        inv = matrix.inv()
        inv_text = str(inv)
    except Exception:
        inv_text = "Matrix is singular (No Inverse exists)"
        
    log_text = f"Category: Linear Algebra (Matrix Array Systems)\n"
    log_text += f"Target Matrix M:\n  [{a}, {b}]\n  [{c}, {d}]\n"
    log_text += f"  1. Determinant Calculation: det(M) = ({a}*{d}) - ({b}*{c}) -> Answer: {det}\n"
    log_text += f"  2. Inverse Matrix Inversion: M^-1 -> Answer: {inv_text}\n"

else:
    # Autonomously invent a multi-step algebraic expansion: (ax + b)(cx + d)
    x = sp.Symbol('x')
    a, b, c, d = random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5)
    
    factored_expr = (a*x + b) * (c*x + d)
    expanded_expr = sp.expand(factored_expr)
    
    log_text = f"Category: Advanced Polynomial Algebra (Structural Expansion)\n"
    log_text += f"Factored Expression: ({a}x + {b})({c}x + {d})\n"
    log_text += f"  1. FOIL Multiplication Execution: Distributing term vectors across scales...\n"
    log_text += f"  2. Complete Structural Expanded Equation -> Answer: {expanded_expr} = 0\n"

# --- WRITE THE LOG ENTRIES PERMANENTLY ---
with open(knowledge_file, "a") as f:
    f.write(f"\n[LUMENI LOCAL CORE REASONING LOG: {time.strftime('%Y-%m-%d %H:%M:%S')}]\n")
    f.write(log_text)
    f.write("="*75 + "\n")

print(f"📝 Lumeni compiled math log successfully via internal compiler.")

