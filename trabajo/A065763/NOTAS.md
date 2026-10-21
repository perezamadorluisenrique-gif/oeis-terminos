# A065763 — matrices de Steinhaus invertibles

- Definición usada: matriz simétrica 0/1 de diagonal nula; la primera fila es libre y a[i][j] = a[i-1][j-1] XOR a[i-1][j]. "Invertible" = determinante real no nulo (comprobado: sobre GF(2) no reproduce a(5)=3).
- impl1 (`impl1/stein2.c`, sesión principal): eliminación sin divisiones módulo tres primos de 31 bits; det≠0 si es no singular módulo alguno; det=0 solo si es singular módulo los tres, cuyo producto (≈2^93) supera 2·(n-1)^(n/2) (cota de Hadamard, < 2^80 para n ≤ 32). Exacto.
- impl2 (`impl2/impl2.c`, subagente sin acceso a impl1): escrita aparte; usa el mismo argumento (aritmética modular + Hadamard), con su propio código.
- Ambas reproducen n=2..24 y coinciden en n=25..28. Tiempos (2 procesos): n=25 ≈ 2 min, n=26 ≈ 4 min, n=27 ≈ 9 min, n=28 ≈ 13 min (impl1 796 s, impl2 809 s; sesión 866f6ffd).
