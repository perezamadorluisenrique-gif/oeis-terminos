# A085430 — mínimo m con un elemento de orden n en GL(m,2)

- Ficha (oeisdata, clon del 2026-10-20, %I #15 del 15-10-2025): n=2..57, `more`, sin b-file. a(27)-a(57) de Bill McEachen (oct. 2025).
- Método (el mismo esquema que A086087 con q=2): n = 2^a·o, o impar; m(n) = u(a) + c(o), u(0)=0, u(a)=2^(a−1)+1 (bloque de Jordan unipotente sobre x+1), c(o) = mínimo, sobre particiones de las potencias de primo de o, de Σ ord_{∏B}(2).
- impl1 (`impl1/mindeg.py`, sesión principal) e impl2 (`impl2/a085430.py`, subagente Sonnet sin ver impl1): ficheros idénticos para n = 2..10000. impl2 además enumera GL(n,2) completo para n ≤ 5 (`../A053651/impl2/bruteforce.txt`).
- **Corrección:** la ficha publica a(49) = 12; el valor correcto es **21**. Prueba: 49 es impar, así que un elemento g de orden 49 es semisimple y tiene un autovalor λ de orden multiplicativo 49 en alguna extensión GF(2^k); como 49 | 2^k − 1 exige k ≥ ord_49(2) = 21, el polinomio mínimo de λ tiene grado 21 y m ≥ 21; la matriz compañera de ese polinomio da m = 21. (Además 7^2 no divide ∏_{i≤12}(2^i − 1) salvo por factores 7 sueltos: el 7-Sylow de GL(12,2) es elemental abeliano.) Probablemente una errata 21→12. Por eso `conocidos.txt` deja n=49 comentado y `score` lo cuenta como término "nuevo" (en realidad, corregido).
- Se propone a(2..~90) en los datos y el resto en un b-file n ≤ 10000.
