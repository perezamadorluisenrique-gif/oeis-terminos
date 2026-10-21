# Cómo enviar A053658 (número de subgrupos cíclicos no isomorfos de GL(n,3))

Lee antes `../NORMAS-OEIS.md`. Envíala después de A086087 (una cada vez, esperando aprobación).

## Qué aportas

La ficha tiene n=1..35 (Jovovic, sept. 2026). Aquí van a(1)..a(55) en `b053658.txt`. "Subgrupos cíclicos no isomorfos" = número de órdenes distintos de elementos del grupo.

## El método, en cuatro líneas

Un orden N = p^a·o (p la característica, o primo con p) aparece en GL(n,3) sii su "coste" es ≤ n. El coste de o es el mínimo de la suma de grados de polinomios irreducibles (uno por grado basta) cuyos órdenes tienen mcm o; la parte p^a necesita un bloque de Jordan de tamaño p^(a−1)+1 (en AGL(n,2) basta 2^(a−1), porque la traslación aporta un factor 2; en GL(n,q) con q > 2 el bloque puede ir sobre un factor x−c ya usado y ahorra 1). Así se cuentan los órdenes sin recorrer el grupo. Dos programas independientes (uno en Python, otro en C++ con otra organización del cálculo) coinciden en todo el rango y reproducen todos los términos publicados; una enumeración exhaustiva de grupos pequeños confirma la caracterización (`verificacion.md`).

## Pasos

1. En oeis.org, abre A053658 y pulsa «edit».
2. Sube `b053658.txt` y enlázalo en LINKS: `Table of n, a(n) for n = 1..55`.
3. DATA: puedes ampliarlo con `datos-propuestos.txt` (hasta a(48)).
4. EXTENSIONS: `a(36)-a(55) from _Tu Nombre_, <fecha>`.
5. PROG (opcional): `programas/impl1-*.py` es corto; ponlo como `(Python)` solo si entiendes la mochila sobre grados que hace.
6. Si la ficha tiene `more` y ya no te parece incompleta, no lo quites tú: lo decide el editor.
7. «ready for review».
