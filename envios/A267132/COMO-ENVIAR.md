# Cómo enviar A267132 (matrices unipotentes sobre GF(2) que son cuadrados)

Lee antes `../NORMAS-OEIS.md`.

## Qué aportas

1. La ficha tiene a(1)..a(7) (Victor S. Miller, 2016). Aquí van a(1)..a(58) en `b267132.txt`. Los números crecen como 2^(n²−n) y las líneas de un b-file no deben pasar de 1000 caracteres (https://oeis.org/wiki/B-files): a(59) y a(60) (1013 y 1048 cifras) están calculados en `trabajo/A267132/` pero no van en el b-file.
2. **Una errata en FORMULA:** C(lambda,2) está escrita como prod(k=0 to m_i, 1−2^(−k)), que incluye el factor k = 0 (vale 0) y le falta la potencia 2^(Σ λ'_i²) del centralizador. Con |C(λ)| = 2^(Σ λ'_i²)·∏_i ∏_{k=1}^{m_i}(1 − 2^(−k)) la fórmula reproduce los datos. Propónlo solo si lo entiendes; si no, envía solo los términos.

## El método, en cuatro líneas

En característica 2, (I+M)² = I+M², así que se trata de contar nilpotentes que son cuadrados de nilpotentes. Un bloque de Jordan de tamaño m se convierte al elevar al cuadrado en dos bloques ⌈m/2⌉ y ⌊m/2⌋; se recorren los tipos alcanzables y se suma |GL_n(2)|/|C(λ)| (número de nilpotentes de cada tipo). Un segundo programa usa la caracterización de Miller (conjugada con partes impares sin repetir) y coincide en n ≤ 60 (el b-file llega a 58 por el límite de 1000 caracteres por línea); la fuerza bruta sobre todas las matrices 5×5 da 85096, como la ficha.

## Pasos

1. En oeis.org, abre A267132 y pulsa «edit».
2. Sustituye el b-file por `b267132.txt` (LINKS: `Table of n, a(n) for n = 1..58`).
3. DATA: puedes ampliarlo con `datos-propuestos.txt` (hasta a(13)).
4. EXTENSIONS: `a(8)-a(58) from _Tu Nombre_, <fecha>`.
5. FORMULA: corrige C(lambda,2) como arriba, o explícaselo al editor en la caja de comentarios, con tus palabras.
6. «ready for review».
