# A218932, A218935, A218949, A218975 (impl2)

Codigo: cyc.py (n=0..60, ~75 s), comparacion: cmp.py, fuerza bruta: brute.py -> bruteforce.txt.

## Teoria
1. Los generadores g^k (gcd(k,ord g)=1) de <g> tienen el mismo tipo ciclico (cada ciclo de longitud m se eleva a k con gcd(k,m)=1).
   Dos subgrupos ciclicos son conjugados en S_n sii sus generadores lo son => clases S_n de subgrupos ciclicos <-> particiones de n.
2. Potencia: g^d con d | ord(g): cada ciclo de longitud m se parte en gcd(m,d) ciclos de longitud m/gcd(m,d).
3. <g> es no maximal (en S_n) sii <g> < <h> estricto; entonces g = h^d con d>1, d | ord h. Basta d primo (si d=p*e, h^p tiene orden ord h/p y e divide a ese orden; induccion).
   Tipo lambda no maximal <=> lambda = power_p(nu) para alguna particion nu de n y primo p | ord(nu). A218932 = # particiones maximales.
   Maximal en A_n (A218949): igual pero nu y lambda pares (potencias de pares son pares; conjugar h dentro de S_n conserva paridad).
4. A_n: subgrupos ciclicos de A_n = <g> con g par (nº de ciclos de longitud par, par). Clase S_n de H se parte en A_n-clases: por orbita-estabilizador,
   en 2 sii N_{S_n}(H) <= A_n (y n>=2, si n<=1 S_n=A_n), si no en 1.
   N(H)/C(g) ~ (Z/ord)^* (todo k unidad se realiza porque g^k tiene el mismo tipo). C(g) <= A_n sii todas las partes son impares y distintas
   (un ciclo par es impar; intercambiar dos ciclos de longitud impar es impar; dos puntos fijos tambien).
   En ese caso, x_k con x g x^-1 = g^k actua en el ciclo de longitud m como i->k i (+traslacion, par por m impar); la paridad total es
   suma de sign(i->k i en Z/m) (calculada contando ciclos). Parte iff para TODA unidad k la suma es par. Es el normalizador, no solo el centralizador:
   p.ej. (3,1) tiene C <= A_4 pero k=2 da una trasposicion => no parte; (9) y (15,5,3) si parten.
5. A218935 = sum sobre tipos pares de (2 si parte, si no 1). A218949 = idem restringido a pares maximales en A_n.
6. A218975: conexo = grafo con un vertice por parte (con repeticion), aristas gcd>1. Un 1 junto a otra parte queda aislado => no conexo;
   una sola parte (incluida (1)) y la particion vacia (n=0, termino conocido 1) son conexas. Se cuentan A_n-clases: tipo par conexo con multiplicidad 2 si parte, 1 si no.
   Justificacion con datos: a(9)=3 = (9) parte en 2 clases + (3,3,3); sin desdoblar daria 2. Conectividad es invariante bajo g->g^k. Los 14 terminos conocidos coinciden.


## Verificacion
bruteforce.txt: n<=8 subgrupos ciclicos como conjuntos, clases por conjugacion BFS con generadores de S_n / A_n, maximalidad por inclusion: coincide con cyc.py.
