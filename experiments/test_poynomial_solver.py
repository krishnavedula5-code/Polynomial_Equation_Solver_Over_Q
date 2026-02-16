import sys
import os

# Add the repository root to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/..')

from src.polynomial_class import Polynomial
from src.gcd import poly_gcd
from src.polynomial_division import poly_division

f = Polynomial([1, 0, -3, 2])
g = f.derivative()
print(f)
print(g)
print(f+g)
print(f-g)
print(f*g)

q, r = poly_division(f, g)
print("Quotient:", q)
print("Remainder:", r)

print("GCD reduced to monic:", poly_gcd(f, g))
