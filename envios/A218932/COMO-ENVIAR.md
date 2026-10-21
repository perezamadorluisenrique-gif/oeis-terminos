# Cómo enviar A218932 (clases de conjugación de subgrupos cíclicos maximales de S_n)

Lee antes `../NORMAS-OEIS.md`. Familia de cuatro (A218932, A218935, A218949, A218975, de Liam Naughton, 2012): envíalas de una en una; esta va después de el primero de la familia.

## Qué aportas

La ficha tiene a(0)..a(13) (tablas de marcas de GAP). Aquí van a(0)..a(60) en `b218932.txt` (sustituye al b-file automático n=0..13).

## El método, en cuatro líneas

Las clases de subgrupos cíclicos de S_n son los tipos de ciclos; un subgrupo cíclico está dentro de otro mayor sii su tipo es la potencia p-ésima (p primo que divide el orden) de otro tipo. En A_n solo cuentan los tipos pares, y una clase se parte en dos exactamente cuando las longitudes de ciclo son impares, distintas y su producto es un cuadrado perfecto (el signo de x → kx en Z/L es el símbolo de Jacobi (k|L), lema de Zolotarev); la primera vez es n = 9, el 9-ciclo. Dos programas independientes coinciden en n ≤ 60, y una enumeración directa de subgrupos de S_n y A_n para n ≤ 8 confirma la caracterización (`verificacion.md`).

## Pasos

1. En oeis.org, abre A218932 y pulsa «edit».
2. Sustituye el b-file por `b218932.txt` (LINKS: `Table of n, a(n) for n = 0..60`).
3. DATA: puedes ampliarlo con `datos-propuestos.txt`.
4. EXTENSIONS: `a(14)-a(60) from _Tu Nombre_, <fecha>`.
5. COMMENTS (opcional, escrito por ti): el criterio de partición en A_n, si lo entiendes. No pegues este texto.
6. «ready for review».
