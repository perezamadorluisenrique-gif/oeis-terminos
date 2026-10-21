# A086087 — mínimo m con un elemento de orden n en GL(m,3)

- Ficha (oeisdata, commit del 2026-10-20 03:03 −0400): términos n=2..24, última extensión Eric M. Schmidt 2013, `more`, sin b-file.
- Descomposición primaria: un elemento es suma directa de bloques J_s(f), f irreducible ≠ x con raíz de orden d (mcd(d,3)=1), deg f = ord_d(3); el bloque mide s·deg f y tiene orden d·3^c (3^c la menor potencia de 3 ≥ s). Orden total = mcm. Con n = 3^e·n', solo un bloque necesita s = 3^(e−1)+1.
- impl1 (`impl1/impl1.py`, sesión principal): programación dinámica sobre divisores de n' (estado = mcm alcanzado), probando cada divisor d0 como portador del bloque unipotente.
- impl2 (`impl2/a086087.py`, subagente sin ver impl1): mínimo sobre particiones de conjuntos de las potencias de primo de n'; además `impl2/brute.c` enumera todo GL(m,3) para m ≤ 4 y comprueba que los órdenes de elementos son exactamente {n : a(n) ≤ m}.
- Coinciden en n = 2..10000 (ficheros idénticos) y reproducen n = 2..24. Es un b-file natural (n ≤ 10000); en el envío se proponen ~70 términos en %S/%T/%U y el resto en el b-file.
- Ojo al leer `score`: los 9976 términos de esta secuencia inflan el total; lo significativo es 3 secuencias extendidas.
