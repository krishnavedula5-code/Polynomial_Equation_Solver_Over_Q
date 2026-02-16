#This class defines how to find addition, subtraction,Derivative, Evaluation of polynomials
from fractions import Fraction

# any other imports

class Polynomial:
    
    def __init__(self, coeffs):
        self.coeffs = self._trim([Fraction(c) for c in coeffs])


    def __str__(self):
        coeffs = self.coeffs
        deg = len(coeffs) - 1
    
        if coeffs == [0]:
            return "0"
    
        terms = []
    
        for i, c in enumerate(coeffs):
            power = deg - i
            if c == 0:
                continue
    
            sign = "+" if c > 0 else "-"
            c_abs = abs(c)
    
            if power == 0:
                term = f"{c_abs}"
            elif power == 1:
                term = f"{'' if c_abs == 1 else c_abs}x"
            else:
                term = f"{'' if c_abs == 1 else c_abs}x^{power}"
    
            terms.append((sign, term))
    
        first_sign, first_term = terms[0]
        result = ("" if first_sign == "+" else "-") + first_term
    
        for sign, term in terms[1:]:
            result += f" {sign} {term}"
    
        return result



    def degree(self):
        if self.coeffs == [0]:
            return -1
        return len(self.coeffs) - 1

    def __add__(self, other):
        a = self.coeffs[:]
        b = other.coeffs[:]

        # pad shorter one
        if len(a) < len(b):
            a = [0]*(len(b)-len(a)) + a
        else:
            b = [0]*(len(a)-len(b)) + b

        return Polynomial([x + y for x, y in zip(a, b)])

    def __sub__(self, other):
        return self + Polynomial([-c for c in other.coeffs])

    def __mul__(self, other):
        result = [0]*(len(self.coeffs)+len(other.coeffs)-1)

        for i, a in enumerate(self.coeffs):
            for j, b in enumerate(other.coeffs):
                result[i+j] += a*b

        return Polynomial(result)


    def derivative(self):
        deg = self.degree()
        
        if deg <= 0:
            return Polynomial([0])
        
        return Polynomial([
            self.coeffs[i] * (deg - i)
            for i in range(len(self.coeffs) - 1)
        ])


    def evaluate(self, x):
        result = 0
        for c in self.coeffs:
            result = result * x + c
        return result

    def __repr__(self):
        return f"Polynomial({self.coeffs})"

    def monic(self):
        if not self.coeffs:
            return self
        
        lead = self.coeffs[0]
        if lead == 0:
            return self
        
        return Polynomial([c / lead for c in self.coeffs])

    def _trim(self, coeffs):
        while len(coeffs) > 1 and coeffs[0] == 0:
            coeffs.pop(0)
        return coeffs
