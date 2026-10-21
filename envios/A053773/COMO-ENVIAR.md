# Cómo enviar A053773 (soluciones de X^8 = I en GL(n,2))

Lee antes `../NORMAS-OEIS.md`.

## Qué aportas

La ficha tiene a(0)..a(11) (2000). Aquí van a(0)..a(40) en `b053773.txt`. DATA ya ocupa tres líneas, así que los términos nuevos van solo en el b-file.

## El método

En característica 2, X^8 − I = (X − I)^8. Por eso X^8 = I equivale a X = I + N con N nilpotente y N^8 = 0. Las clases de conjugación de nilpotentes corresponden a particiones de n (tipo de Jordan), y N^8 = 0 obliga a que todas las partes sean ≤ 8. Se suma el tamaño de cada clase, |GL_n(2)| / |centralizador|, con la fórmula clásica del centralizador. La segunda implementación cuenta por otro camino: recursión sobre la dimensión del núcleo y la imagen, sin tipos de Jordan, y fuerza bruta para n ≤ 4. Las dos coinciden en n ≤ 40.

Comprobación sencilla: para n ≤ 8 sale 2^(n(n−1)), el número total de nilpotentes (Fine–Herstein), igual que en la ficha.

## Pasos

1. Abre A053773 y pulsa «edit». Sube `b053773.txt` y añade en LINKS: `Table of n, a(n) for n = 0..40`.
2. EXTENSIONS: `a(12)-a(40) from _Tu Nombre_, <fecha>` (los términos están en el b-file).
3. PROG (opcional): `programas/impl1-impl1.py`, en Python, con unas 40 líneas, firmado por ti.
4. Pulsa «ready for review».
