from src.polynomial_division import poly_division
def poly_gcd(f, g):

    while g.degree() >= 0:
        _, r = poly_division(f, g)
        f, g = g, r

    return f.monic()
