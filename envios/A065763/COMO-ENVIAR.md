# Cómo enviar A065763 (matrices de Steinhaus invertibles)

Lee antes `../NORMAS-OEIS.md`.

## Qué aportas

La ficha llega a a(24) (Sean A. Irvine, 2023). Aquí van los términos de `terminos.txt`. Caben en DATA (ver `datos-propuestos.txt`), así que no hace falta b-file.

## El método

Una matriz de Steinhaus de orden n es simétrica, con ceros en la diagonal, y queda fijada por su primera fila: hay 2^(n−1) primeras filas posibles, y cada entrada es el XOR de las dos de encima, a[i][j] = a[i−1][j−1] XOR a[i−1][j]. Se recorren todas y se mira si el determinante (entero) es distinto de cero. Se calcula módulo tres primos de 31 bits: si es no nulo módulo alguno, es no nulo. Si se anula módulo los tres, es cero, porque el producto de los primos (~2^93) supera la cota de Hadamard del determinante. Son dos programas en C escritos por separado. Ambos reproducen a(2)..a(24) y coinciden en los nuevos.

Ojo a la definición: «invertible» es sobre los enteros/reales. Sobre GF(2) no sale a(5) = 3.

## Pasos

1. Abre A065763 y pulsa «edit». Añade los términos nuevos al final de DATA (`datos-propuestos.txt`).
2. EXTENSIONS: `a(25)-a(28) from _Tu Nombre_, <fecha>`.
3. Pulsa «ready for review». El programa en C es largo para PROG: si un editor lo pide, súbelo como fichero enlazado.
