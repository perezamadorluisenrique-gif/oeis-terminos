# A267132 (impl2) sq.py, bf.cpp
Unipotente u=I+N, N nilpotente. En car. 2, (I+M)^2 = I+M^2, asi que u es cuadrado de unipotente sii N = M^2 con M nilpotente.
Bloque de Jordan de tamaño m en M da en M^2 bloques (ceil(m/2), floor(m/2)) (el 0 se omite). Conjunto S_n de tipos alcanzables por DP sobre bloques.
Conteo = sum_{lambda in S_n} |GL_n(2)| / |C(lambda)|, con |C| = q^{sum lambda'_i^2} prod_i prod_{j=1}^{m_i}(1-q^-j), q=2 (comprobado: suma sobre todas las particiones = q^{n(n-1)}).
No se uso la formula de OEIS. Fuerza bruta (bf.cpp): todas las matrices n<=5 sobre GF(2), unipotentes (N^n=0), cuadrados distintos: 1,1,22,316,85096 = impl2.
