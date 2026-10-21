# Términos nuevos para la OEIS

Trece secuencias de la [OEIS](https://oeis.org) ampliadas (y dos corregidas) con cálculos propios:
20 000 términos nuevos, cada uno confirmado por **dos programas independientes** que reproducen todo
lo ya publicado. Casi todas cuentan cosas de grupos de matrices sobre cuerpos finitos (GL(n,q), AGL(n,2))
y de subgrupos cíclicos de los grupos simétrico y alternado.

| Secuencia | Qué cuenta | Aporte |
|---|---|---|
| A086087 | mínimo m con un elemento de orden n en GL(m,3) | a(25)..a(10000) |
| A085430 | ídem en GL(m,2) | **a(49) corregido (12 → 21)** y a(58)..a(10000) |
| A267132 | unipotentes de GF(2) que son cuadrados | a(8)..a(58) y **errata en la fórmula** |
| A053651, A053658, A053660, A062766 | órdenes distintos de elementos de GL(n,2), GL(n,3), GL(n,4), AGL(n,2) | decenas de términos cada una |
| A053773 | soluciones de X^8 = I en GL(n,2) | a(12)..a(40) |
| A065763 | matrices de Steinhaus invertibles | a(25)..a(28) |
| A218932, A218935, A218949, A218975 | clases de subgrupos cíclicos de S_n y A_n | a(14)..a(60) |

## Qué hay

- `envios/Axxxxxx/`: el paquete de cada envío: b-file (`bNNNNNN.txt`), `datos-propuestos.txt` (DATA),
  `terminos.txt`, `programas/`, `verificacion.md` y `COMO-ENVIAR.md`. `envios/NORMAS-OEIS.md` resume la
  hoja de estilo y la política de la OEIS sobre herramientas de IA.
- `trabajo/Axxxxxx/`: las dos implementaciones (`impl1/`, `impl2/`), sus salidas y `NOTAS.md` con el método.
- `herramientas/comprobar_oeis.py`: valida los 13 paquetes contra la hoja de estilo y contra la ficha
  actual (formato de términos, DATA, b-files, EXTENSIONS, LINKS, que nadie la haya ampliado entretanto).

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/oeis/oeisdata ../oeisdata
git -C ../oeisdata sparse-checkout set --no-cone $(ls envios | grep ^A | sed -E 's#(A...)(.*)#/seq/\1/\1\2.seq#')
python3 herramientas/comprobar_oeis.py --oeisdata ../oeisdata
pip install sympy && python3 trabajo/A053658/impl1/glq_orders.py 3 55 salida.txt   # recalcular, por ejemplo
```

La web (https://perezamadorluisenrique-gif.github.io/oeis-terminos/, con versión en inglés en `/en/`) es una
tabla de las trece secuencias con sus b-files; la construye `python3 herramientas/construir.py` en `_site/` y la
publica `.github/workflows/pages.yml`.

Los envíos los hace el autor a mano, uno cada vez, desde su cuenta en oeis.org.

## Licencias

Programas: MIT. Textos: CC BY 4.0. Datos tomados de la OEIS: CC BY-SA 4.0. Ver [LICENSE.md](LICENSE.md) y [CREDITOS.md](CREDITOS.md).

## In English

New terms for thirteen OEIS sequences (about 20,000 terms in all, plus a corrected term in A085430
and a formula erratum in A267132), mostly counting orders and elements of matrix groups over finite
fields and cyclic subgroups of symmetric and alternating groups. Every new term was computed by two
independent programs that reproduce all previously published terms. `envios/` holds one submission
package per sequence (b-file, proposed DATA, programs, verification notes), `trabajo/` the two
implementations, and `herramientas/comprobar_oeis.py` validates the packages against the OEIS style
sheet and the current entries. Submissions are made by hand, one at a time, by the author. The web page (`herramientas/construir.py`, published by
the Pages workflow) lists the thirteen sequences with their b-files, in Spanish and English.
