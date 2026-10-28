import math

def fermat_factorization(n):
    """
    Factoriza un entero impar n mediante el método de Fermat (n = a^2 - b^2).
    Retorna los factores p y q (n = p * q).
    """
    a = math.isqrt(n)
    if a * a < n:
        a += 1
    while True:
        b2 = a * a - n
        b = math.isqrt(b2)
        if b * b == b2:
            p = a - b
            q = a + b
            return p, q
        a += 1

def resolver_rsa(n, e, c=None):
    """
    Rompe la clave pública RSA (n, e) encontrando p, q, phi(n) y la clave privada d.
    Si se provee un mensaje cifrado c, también lo descifra.
    """
    p, q = fermat_factorization(n)
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)  # Inverso multiplicativo de e módulo phi(n)
    
    resultado = {
        "p": p,
        "q": q,
        "phi": phi,
        "d": d
    }
    
    if c is not None:
        m = pow(c, d, n)
        resultado["m"] = m
        resultado["ascii"] = chr(m) if 0 <= m <= 255 else None
        
    return resultado

# --- EJERCICIO 13 ---
res13 = resolver_rsa(n=2291, e=17, c=575)
print("=== EJERCICIO 13 ===")
print(f"Factores primos: p = {res13['p']}, q = {res13['q']}")
print(f"Función de Euler phi(n): {res13['phi']}")
print(f"Clave privada d: {res13['d']}")
print(f"Mensaje descifrado (m): {res13['m']}")
print(f"Letra ASCII correspondiente: '{res13['ascii']}'\n")

# --- EJERCICIO 14 ---
res14 = resolver_rsa(n=536813567, e=3602561)
print("=== EJERCICIO 14 ===")
print(f"Factores primos: p = {res14['p']}, q = {res14['q']}")
print(f"Función de Euler phi(n): {res14['phi']}")
print(f"Clave privada de descifrado d: {res14['d']}")