# Cómo enviar A086087 (mínimo m con un elemento de orden n en GL(m,3))

Lee antes `../NORMAS-OEIS.md`. Es la más sencilla de las tres: buen primer envío.

## Qué aportas

La ficha tiene a(2)..a(24) (Eric M. Schmidt, 2013). Aquí van a(2)..a(10000) en `b086087.txt`.

## El método, para que lo entiendas antes de enviar

Una matriz invertible sobre F_3 se parte en bloques, uno por factor irreducible f de su polinomio característico (con f ≠ x). Si las raíces de f tienen orden d, el grado de f es el orden de 3 módulo d. Un bloque de Jordan de tamaño s sobre f ocupa s·deg f dimensiones y tiene orden d·3^c, donde 3^c es la menor potencia de 3 ≥ s. El orden de la matriz es el mcm de los órdenes de los bloques. Así, para n = 3^e·n', basta elegir divisores de n' con mcm n' (cada uno cuesta su orden de 3) y, si e > 0, uno de esos bloques lleva tamaño 3^(e−1)+1. a(n) es el mínimo coste.

Hay dos programas independientes que coinciden en todo n ≤ 10000. Además, una búsqueda exhaustiva de todas las matrices de GL(m,3) con m ≤ 4 confirma qué órdenes aparecen.

## Pasos

1. En oeis.org, abre A086087 y pulsa «edit».
2. Sube `b086087.txt` y añade en LINKS, la primera: `Table of n, a(n) for n = 2..10000`.
3. DATA: puedes ampliarlo con `datos-propuestos.txt`, que llega a a(104) en unos 260 caracteres. Si prefieres, déjalo como está, porque el b-file basta.
4. EXTENSIONS: `a(25)-a(10000) from _Tu Nombre_, <fecha>`, o solo los términos que pongas en DATA, si así lo indica el editor.
5. PROG (opcional): `programas/impl1-impl1.py` cabe en el campo PROG como `(Python)`, firmado por ti. Solo si entiendes la programación dinámica sobre divisores que hace.
6. Pulsa «ready for review».
