# Verificación de A062766

- Términos conocidos (ficha en oeis/oeisdata, comprobada el 2026-10-20 y por WebFetch cuando fue posible): n = 1..22.
- Términos nuevos: n = 23..71 (49 términos).
- impl1 e impl2 se escribieron por separado (impl2 por un subagente sin ver impl1); ambas reproducen todos los términos conocidos y coinciden en todos los nuevos.

## Notas del cálculo


- Ficha (oeisdata, clon del 2026-10-20, %I #20): n=1..22, Jovovic 2001 (índices de ciclos), `more`, sin b-file.
- Método: AGL(n,2) es el estabilizador en GL(n+1,2) de un hiperplano con acción trivial en el cociente; sus órdenes son {o : c(o) ≤ n} ∪ {2^a·o : a ≥ 1, c(o) + 2^(a−1) ≤ n}, con c(o) de A085430/A053651. impl1 lo deduce como "elementos de GL(n+1,2) con autovalor 1" (`../A053651/impl1/gl2orders.py`); impl2 (subagente) lo deduce directamente de M=[[A,b],[0,1]] (el orden se duplica sii la parte de autovalor 1 tiene un bloque de tamaño exactamente 2^T), `../A053651/impl2/METODO.md`, y lo comprueba por fuerza bruta en AGL(n,2), n ≤ 4 (`impl2/bf.cpp`).
- Coinciden en n=1..71 y reproducen n=1..22.
