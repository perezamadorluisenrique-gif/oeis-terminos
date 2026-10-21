# A053660 — número de subgrupos cíclicos no isomorfos de GL(n,4) (= número de órdenes de elementos distintos)

- Ficha (oeisdata, clon del 2026-10-20, %I #8 del 10-01-2022): n=1..11 (a(8)-a(11) de Sean A. Irvine, 2022), `more`, sin b-file.
- Método: el de A053658 con q=4, p=2 (`../A053658/impl1/glq_orders.py 4 40 impl1.txt`); ver `../A053658/NOTAS.md`.
- impl2 (`impl2/`, subagente sin ver impl1) con fuerza bruta de GL(n,4) para n ≤ 3.
- Coinciden en n=1..40 y reproducen n=1..11. impl1: 24 s.
ALGORITMO NUEVO: lo publicado llega a n=11 (Irvine 2022), coherente con recorrer clases de conjugación de GL(n,4); aquí el conjunto de órdenes se caracteriza por una fórmula de coste (mochila sobre grados con los órdenes de los polinomios irreducibles, más el bloque unipotente mínimo, que puede ir en una componente x−c de grado 1) y se cuenta sin tocar el grupo: n=40 en 24 s.
