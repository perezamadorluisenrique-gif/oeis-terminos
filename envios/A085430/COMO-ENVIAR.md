# Cómo enviar A085430 (mínimo m con un elemento de orden n en GL(m,2))

Lee antes `../NORMAS-OEIS.md`. Es la hermana de A086087 (mismo método con 2 en vez de 3): si A086087 ya se aprobó, esta es fácil.

## Qué aportas

1. **Una corrección:** la ficha publica a(49) = 12 (de la extensión de Bill McEachen, oct. 2025); lo correcto es **21**. Un elemento de orden 49 (impar) es diagonalizable sobre una extensión y tiene un autovalor de orden 49, que vive en GF(2^k) solo si 49 | 2^k − 1, es decir, k ≥ ord_49(2) = 21. La matriz compañera de un factor irreducible de grado 21 de x^49 − 1 da el ejemplo en GL(21,2). Seguramente es una errata (21 → 12).
2. a(58)..a(10000) en `b085430.txt` (sustituye al b-file actual, que llega a 57).

## El método, en cuatro líneas

n = 2^a·o con o impar. Para la parte impar se reparten las potencias de primo de o en grupos; cada grupo es un polinomio irreducible cuyo grado es el orden de 2 módulo el producto del grupo; c(o) es el mínimo de la suma de grados. La parte 2^a pide un bloque de Jordan de tamaño 2^(a−1)+1 sobre x+1. a(n) = c(o) + (2^(a−1)+1 si a > 0). Dos programas independientes coinciden en n ≤ 10000, y una enumeración completa de GL(m,2) para m ≤ 5 lo confirma.

## Pasos

1. En oeis.org, abre A085430 y pulsa «edit».
2. DATA: cambia el 48.º término (a(49)) de 12 a 21; si quieres, amplía con `datos-propuestos.txt` (llega a a(99)).
3. Sustituye el b-file por `b085430.txt` (LINKS: `Table of n, a(n) for n = 2..10000`).
4. EXTENSIONS: `a(49) corrected and a(58)-a(10000) from _Tu Nombre_, <fecha>`.
5. En la caja de comentarios para el editor, escribe tú, en dos frases, el argumento de a(49) de arriba.
6. «ready for review».
