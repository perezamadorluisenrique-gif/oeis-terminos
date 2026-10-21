# Verificación de A053651

- Términos conocidos (ficha en oeis/oeisdata, comprobada el 2026-10-20 y por WebFetch cuando fue posible): n = 1..22.
- Términos nuevos: n = 23..72 (50 términos).
- impl1 e impl2 se escribieron por separado (impl2 por un subagente sin ver impl1); ambas reproducen todos los términos conocidos y coinciden en todos los nuevos.

## Notas del cálculo


- Ficha (oeisdata, clon del 2026-10-20): n=1..22, Jovovic 2000, término 22 vía programa Java de Sean A. Irvine; `more`, sin b-file.
- Método: los órdenes de elementos de GL(n,2) son exactamente {2^a·o : c(o) + u(a) ≤ n} con o impar, u(0)=0, u(a)=2^(a−1)+1 y c(o) el coste mínimo de A085430 (justificación en `impl1/gl2orders.py` y `impl2/METODO.md`). Basta enumerar el conjunto C_k de impares con c(o) ≤ k: mochila 0/1 sobre los grados d con los divisores e de 2^d−1 de orden exacto d (un e por grado basta, porque dos del mismo grado se funden en su mcm). Nada de recorrer el grupo: n=72 en ~1 min frente a |GL(72,2)| ≈ 2^5184.
- impl1 (`impl1/gl2orders.py`, Python con enteros grandes) e impl2 (`impl2/prim.py` + `impl2/cnt.cpp` por capas c(o)=k con u128, subagente sin ver impl1). Coinciden en n=1..72 y reproducen n=1..22; impl2 tiene además fuerza bruta de GL(n,2), n ≤ 5.
- Incidente útil: la primera versión de impl2 leía los órdenes con `%llu` y truncaba e > 2^64 (d ≥ 65); la discrepancia entre implementaciones lo detectó y se corrigió. Compilar impl2: `g++ -O2 -o cnt cnt.cpp`.
ALGORITMO NUEVO: lo publicado (índices de ciclos de Jovovic; programa Java de Irvine, que no se ha leído) se queda en n=22, coherente con métodos que recorren clases de conjugación de GL(n,2) (su número crece exponencialmente); aquí el conjunto de órdenes se caracteriza por una fórmula de coste (bloque unipotente mínimo + mochila sobre grados con órdenes de polinomios irreducibles) y se cuenta sin tocar el grupo, lo que lleva la secuencia de 22 a 72 términos en un minuto.
