# A053658 — número de subgrupos cíclicos no isomorfos de GL(n,3) (= número de órdenes de elementos distintos)

- Ficha (oeisdata, clon del 2026-10-20, %I #18 del 23-09-2026): n=1..35 (a(15)-a(35) de Jovovic, sept. 2026), `hard,more`, sin b-file.
- Método (generaliza el de A053651 a q = p^f): orden = p^a·o con p ∤ o. c(o) = mochila 0/1 sobre grados d con los e | q^d−1 de orden exacto d; la parte p^a exige un bloque de Jordan de tamaño p^(a−1)+1, que puede ir en un x−1 aparte o, ahorrando 1, en una componente de grado 1 x−c ya usada por o (c1(o) = coste mínimo con parte de grado 1). Colgarlo de grado ≥ 2 nunca ahorra. GL(n,q) tiene orden N sii coste(N) ≤ n.
- impl1 (`impl1/glq_orders.py`, sesión principal, Python con enteros grandes; también sirve para A053660 con q=4 y reproduce A053651 con q=2). impl2 (`impl2/`, subagente Sonnet sin ver impl1: particiones de potencias de primo + capas con __int128, cota o < q^n ≤ 2^88) y fuerza bruta de GL(n,3) para n ≤ 4 (`impl2/bruteforce.txt`).
- Coinciden en n=1..55 y reproducen n=1..35. impl1: 57 s.
