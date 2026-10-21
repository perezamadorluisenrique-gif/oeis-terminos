# Verificación de A218935

- Términos conocidos (ficha en oeis/oeisdata, comprobada el 2026-10-20 y por WebFetch cuando fue posible): n = 0..13.
- Términos nuevos: n = 14..60 (47 términos).
- impl1 e impl2 se escribieron por separado (impl2 por un subagente sin ver impl1); ambas reproducen todos los términos conocidos y coinciden en todos los nuevos.

## Notas del cálculo


- Fórmula: tipos pares, con peso 2 si la clase se parte en A_n.
- Clases de subgrupos cíclicos de S_n ↔ tipos de ciclos (todos los generadores de <g> tienen el mismo tipo). <g> ⊊ <h> (salvo conjugación) sii tipo(g) = tipo(h)^p con p primo que divide ord(h); la potencia parte un L-ciclo en mcd(L,p) ciclos de longitud L/mcd. En A_n, la clase de <g> se parte en dos sii N_{S_n}(<g>) ≤ A_n (n ≥ 2): el centralizador exige partes impares distintas, y un elemento del normalizador actúa en cada L-ciclo como x → kx en Z/L, de signo (k|L) (Zolotarev); así se parte sii el producto de las partes es un cuadrado perfecto (la primera vez en n=9, tipo (9)).
- impl1 (`../A218935/impl1/cyclic_sn.py`, sesión principal: las cuatro A2189xx a la vez) e impl2 (`../A218932/impl2/cyc.py`, subagente Sonnet sin ver impl1; además `brute.py` construye los subgrupos cíclicos de S_n y A_n como conjuntos y sus clases por conjugación para n ≤ 8, `bruteforce.txt`). Coinciden en n=0..60 y reproducen n=0..13 (Naughton 2012, tablas de marcas de GAP).
- Ficha comprobada por WebFetch el 2026-10-20 (A218932, A218935, A218949; A218975 solo en oeisdata): n=0..13, `more`, sin extensiones desde 2012.
