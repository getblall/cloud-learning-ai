import os
import time
import random
import math

knowledge_file = "knowledge_base.txt"

# 1. Initialize file if deleted
if not os.path.exists(knowledge_file):
    with open(knowledge_file, "w") as f:
        f.write("=== UNIVERSAL AUTOMATED MATHEMATICS KNOWLEDGE BASE ===\n")

# --- MATHEMATICAL TYPE GENERATORS ---
def solve_linear_both_sides():
    """Generates and solves: ax + b = cx + d"""
    x = random.randint(-10, 10)
    a = random.randint(2, 10)
    c = random.randint(-10, 10)
    while a == c: c = random.randint(-10, 10)
    b = random.randint(-20, 20)
    d = (a * x) + b - (c * x)
    
    steps = f"Category: Linear Equations (Variables Both Sides)\n"
    steps += f"Equation: {a}x + ({b}) = {c}x + ({d})\n"
    steps += f"  Step 1: Subtract {c}x from both sides -> ({a - c})x + ({b}) = {d}\n"
    steps += f"  Step 2: Subtract {b} from both sides -> ({a - c})x = {d - b}\n"
    steps += f"  Step 3: Divide both sides by {a - c} -> x = {x}\n"
    return steps

def solve_quadratic():
    """Generates and solves solvable quadratic structures using factoring: (x - m)(x - n) = 0"""
    m = random.randint(-8, 8)
    n = random.randint(-8, 8)
    # x^2 - (m+n)x + mn = 0 -> x^2 + bx + c = 0
    b = -(m + n)
    c = m * n
    
    steps = f"Category: Quadratic Equations (Factoring Branch)\n"
    steps += f"Equation: x^2 + ({b})x + ({c}) = 0\n"
    steps += f"  Step 1: Identify numbers that multiply to {c} and add to {b} -> ({m}) and ({n})\n"
    steps += f"  Step 2: Rewrite in factored structural form -> (x - {m})(x - {n}) = 0\n"
    steps += f"  Step 3: Set each factor component to zero to discover solutions -> x = {m} or x = {n}\n"
    return steps

def solve_system_linear():
    """Generates and solves a system of 2 linear equations using elimination"""
    x, y = random.randint(-5, 5), random.randint(-5, 5)
    a1, b1 = random.randint(1, 5), random.randint(1, 5)
    a2, b2 = random.randint(1, 5), random.randint(1, 5)
    while (a1/a2) == (b1/b2): a2 = random.randint(1, 5) # ensure unique solution
    c1 = a1*x + b1*y
    c2 = a2*x + b2*y
    
    steps = f"Category: Systems of Linear Equations (Elimination Method)\n"
    steps += f"System:\n  [1] {a1}x + {b1}y = {c1}\n  [2] {a2}x + {b2}y = {c2}\n"
    steps += f"  Resolution Matrix: Computed variables mathematically via substitution -> x = {x}, y = {y}\n"
    return steps

def solve_fraction_proportion():
    """Generates and solves fractional proportions: a/b = x/d"""
    b = random.choice([2, 3, 4, 5, 10])
    d = b * random.randint(2, 6)
    a = random.randint(1, 10)
    x = (a * d) // b
    
    steps = f"Category: Fractional Ratios & Proportions\n"
    steps += f"Equation: ({a} / {b}) = (x / {d})\n"
    steps += f"  Step 1: Cross-multiply opposite components -> {a} * {d} = {b} * x -> {a*d} = {b}x\n"
    steps += f"  Step 2: Isolate variable by dividing by {b} -> x = {a*d} / {b} -> x = {x}\n"
    return steps

def solve_pythagorean():
    """Generates right angle triangle geometries using Pythagorean theorem"""
    a = random.randint(3, 12)
    b = random.randint(4, 15)
    c_squared = (a**2) + (b**2)
    c = round(math.sqrt(c_squared), 2)
    
    steps = f"Category: Geometry (Pythagorean Theorem)\n"
    steps += f"Problem: Find hypotenuse 'c' given legs a = {a} and b = {b}\n"
    steps += f"  Step 1: Use core formula a^2 + b^2 = c^2 -> {a}^2 + {b}^2 = c^2\n"
    steps += f"  Step 2: Calculate squares -> {a**2} + {b**2} = {c_squared}\n"
    steps += f"  Step 3: Take square root -> c = √{c_squared} -> c ≈ {c}\n"
    return steps

# --- EXECUTION MATRICES ---
math_engines = [solve_linear_both_sides, solve_quadratic, solve_system_linear, solve_fraction_proportion, solve_pythagorean]
chosen_engine = random.choice(math_engines)

# Run logic calculation step
math_log_entry = chosen_engine()

# --- APPEND DATA TO LOG FOREVER ---
with open(knowledge_file, "a") as f:
    f.write(f"\n[UNIVERSAL MATH LOG ENTRY: {time.strftime('%Y-%m-%d %H:%M:%S')}]\n")
    f.write(math_log_entry)
    f.write("=" * 70 + "\n")

print("📝 Math log engine run successful. Appended solution matrix step to knowledge_base.txt")
