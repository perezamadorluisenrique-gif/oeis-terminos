# A267132 — matrices unipotentes n×n sobre GF(2) que son cuadrados de unipotentes

- Ficha (oeisdata y WebFetch, 2026-10-20): n=1..7 (Victor S. Miller, 2016), `more`, b-file n=1..7.
- impl1 (`impl1/squares.py`, sesión principal): la caracterización de Miller (%F, demostrada en arXiv:1606.09299): suma sobre particiones λ cuya conjugada tiene las partes impares con multiplicidad ≤ 1 de |GL_n(2)|/|C(λ)|, con |C(λ)| = 2^{Σ λ'_i²} ∏_i ∏_{k=1}^{m_i} (1 − 2^{−k}) el centralizador de un nilpotente de tipo λ.
- **Errata en %F:** tal como está escrita, C(λ,2) = ∏_i ∏_{k=0}^{m_i}(1 − 2^{−k}) incluye el factor k=0, que vale 0, y omite la potencia 2^{Σ λ'_i²}; leída al pie de la letra no reproduce los datos (impl1 lo comprobó: sale 2,16,1184,…). Con el centralizador estándar sí.
- impl2 (`impl2/sq.py`, subagente sin ver impl1 ni usar %F): (I+M)² = I+M² en característica 2, así que se buscan los nilpotentes que son cuadrados de nilpotentes; un bloque de Jordan de tamaño m da en M² los bloques ⌈m/2⌉, ⌊m/2⌋; programación dinámica de tipos alcanzables y suma de |GL_n(2)|/|C(λ)|. `impl2/bf.cpp` cuenta por fuerza bruta las 2^{n²} matrices para n ≤ 5 (1, 1, 22, 316, 85096).
- Coinciden en n=1..60 y reproducen n=1..7. impl1: 162 s.
