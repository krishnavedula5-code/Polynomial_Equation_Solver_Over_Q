from src.polynomial_class import Polynomial

def poly_division(f, g):

    if g.coeffs == [0]:
        raise ZeroDivisionError("Division by zero polynomial")

    f_coeffs = f.coeffs[:]
    g_coeffs = g.coeffs[:]

    deg_f = len(f_coeffs) - 1
    deg_g = len(g_coeffs) - 1

    if deg_f < deg_g:
        return Polynomial([0]), f

    quotient = [0] * (deg_f - deg_g + 1)

    while deg_f >= deg_g and any(c != 0 for c in f_coeffs):

        lead_ratio = f_coeffs[0] / g_coeffs[0]
        shift = deg_f - deg_g

        quotient[len(quotient) - shift - 1] = lead_ratio

        # subtract with alignment
        for i in range(len(g_coeffs)):
            f_coeffs[i] -= lead_ratio * g_coeffs[i]

        # CRITICAL: remove leading zero
        while len(f_coeffs) > 1 and f_coeffs[0] == 0:
            f_coeffs.pop(0)

        deg_f = len(f_coeffs) - 1

    return Polynomial(quotient), Polynomial(f_coeffs)
