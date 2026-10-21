# A053773 — soluciones de X^8 = I en GL(n,2)

- En característica 2, X^8 − I = (X − I)^8: X = I + N con N nilpotente y N^8 = 0 (y todo X así es invertible). Para n ≤ 8 sale 2^(n(n−1)) (todas las nilpotentes, Fine–Herstein); a partir de n = 9 la restricción importa.
- impl1 (`impl1/impl1.py`): suma sobre tipos de Jordan (particiones de n con partes ≤ 8) de |GL_n(2)| / |C(λ)|, con |C(λ)| = 2^(Σ λ'_i²) ∏_i ∏_{k≤m_i} (1 − 2^−k).
- impl2 (`impl2/impl2.py`, subagente sin ver impl1): recursión distinta sobre la dimensión del núcleo y la restricción a la imagen (N^k = 0 ⇔ N|_{Im N} cumple M^(k−1) = 0), sin tipos de Jordan; además fuerza bruta de las 2^(n²) matrices para n ≤ 4.
- Coinciden en n = 0..40 (salida idéntica) y reproducen n = 0..11.
