#!/usr/bin/env python3
"""Checks the OEIS submission packages in envios/ against the OEIS style sheet and the current entries.

Usage: python3 herramientas/comprobar_oeis.py --oeisdata <clone of oeis/oeisdata with the seq/*.seq files>

For every envios/Axxxxxx/ it checks:
  - files: COMO-ENVIAR.md, terminos.txt, datos-propuestos.txt, verificacion.md, programas/ (and the b-file);
  - term format: plain integers, no leading zeros, no spaces in DATA;
  - DATA: about three lines (<= 260 characters), starts at the offset (%O), matches the b-file;
  - b-file: named bNNNNNN.txt, lines "n a(n)" with consecutive n from the offset, no blank or
    trailing-space lines, ASCII only, "# " comments only at the top, final LF, lines of at most
    1000 characters, at most 10000 terms (https://oeis.org/wiki/B-files, https://oeis.org/wiki/Style_Sheet);
  - current entry: every published term equals the package's, except a(n) declared as corrected in
    the EXTENSIONS line; nobody has extended the entry past the package's first new term;
  - fields: an EXTENSIONS line `a(X)-a(Y) from _Tu Nombre_, <fecha>` whose range is exactly the
    new terms, and, with a b-file, a LINKS line `Table of n, a(n) for n = off..last` matching it;
  - without a b-file, all new terms must fit in DATA.
Prints one line per package (OK/MAL) and exits 1 if any fails.
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INT = re.compile(r"-?(0|[1-9][0-9]*)$")
DATA_MAX = 260
DIGITS_MAX = 1000  # DATA terms
LINE_MAX = 1000    # b-file lines (https://oeis.org/wiki/B-files)
BFILE_MAX = 10000


def read_entry(oeisdata, a):
    f = Path(oeisdata) / "seq" / a[:4] / f"{a}.seq"
    if not f.exists():
        return None
    data, off = "", None
    lines = f.read_text().splitlines()
    for l in lines:
        tag, _, rest = l.partition(" ")
        body = rest.partition(" ")[2]
        if tag in ("%S", "%T", "%U"):
            data += body.strip()
        elif tag == "%O":
            off = int(body.split(",")[0])
    terms = [int(t) for t in data.split(",") if t]
    return {"off": off, "terms": {off + i: v for i, v in enumerate(terms)}, "lines": lines}


def read_pairs(path, errors, what, bfile=False):
    """Lines 'n a(n)'; '#' comments allowed only before the first term."""
    pairs, started = [], False
    raw = path.read_text()
    if raw and not raw.endswith("\n"):
        errors.append(f"{what}: falta el salto de línea final")
    for i, l in enumerate(raw.splitlines(), 1):
        if bfile and not l.isascii():
            errors.append(f"{what}:{i}: caracteres no ASCII")
        if l.startswith("#"):
            if bfile and not (l == "#" or l.startswith("# ")):
                errors.append(f"{what}:{i}: los comentarios empiezan por «# »")
            if started:
                errors.append(f"{what}:{i}: comentario después de los términos")
            continue
        if l != l.strip() or not l:
            errors.append(f"{what}:{i}: línea vacía o con espacios sobrantes")
            continue
        parts = l.split(" ")
        if len(parts) != 2 or not INT.match(parts[0]) or not INT.match(parts[1]):
            errors.append(f"{what}:{i}: no es «n a(n)» con enteros separados por un espacio: {l[:40]}")
            continue
        started = True
        if len(l) > LINE_MAX:
            errors.append(f"{what}: la línea de a({parts[0]}) tiene {len(l)} caracteres (máximo {LINE_MAX})")
        pairs.append((int(parts[0]), int(parts[1])))
    return pairs


def check(pkg, oeisdata):
    a = pkg.name
    e = []
    for f in ["COMO-ENVIAR.md", "terminos.txt", "datos-propuestos.txt", "verificacion.md"]:
        if not (pkg / f).exists():
            e.append(f"falta {f}")
    progs = list((pkg / "programas").glob("*")) if (pkg / "programas").is_dir() else []
    if not progs:
        e.append("programas/ vacío")
    if e:
        return e
    entry = read_entry(oeisdata, a)
    if entry is None:
        return [f"no encuentro la ficha {a} en {oeisdata}"]
    off, pub = entry["off"], entry["terms"]
    how = (pkg / "COMO-ENVIAR.md").read_text()

    new = dict(read_pairs(pkg / "terminos.txt", e, "terminos.txt"))
    bpath = pkg / f"b{a[1:]}.txt"
    others = [p.name for p in pkg.glob("b*.txt") if p != bpath]
    if others:
        e.append(f"b-file con nombre incorrecto: {others[0]} (debe ser {bpath.name})")
    full = {}
    if bpath.exists():
        b = read_pairs(bpath, e, bpath.name, bfile=True)
        idx = [n for n, _ in b]
        if idx and idx != list(range(off, off + len(idx))):
            e.append(f"{bpath.name}: los índices no son consecutivos desde el offset {off}")
        if len(b) > BFILE_MAX:
            e.append(f"{bpath.name}: {len(b)} términos (máximo {BFILE_MAX})")
        full = dict(b)

    # DATA
    dl = [l for l in (pkg / "datos-propuestos.txt").read_text().splitlines() if l and not l.startswith("#")]
    if len(dl) != 1:
        e.append("datos-propuestos.txt: debe tener una sola línea de términos")
    else:
        d = dl[0]
        if " " in d:
            e.append("DATA con espacios")
        if len(d) > DATA_MAX:
            e.append(f"DATA de {len(d)} caracteres (máximo ~{DATA_MAX})")
        toks = d.split(",")
        if not all(INT.match(t) for t in toks):
            e.append("DATA con algo que no es un entero")
        else:
            for i, t in enumerate(toks):
                if len(t.lstrip("-")) > DIGITS_MAX:
                    e.append(f"DATA: a({off + i}) con más de {DIGITS_MAX} cifras")
            data = {off + i: int(t) for i, t in enumerate(toks)}
            for n, v in data.items():
                if n in full and full[n] != v:
                    e.append(f"DATA y b-file no coinciden en a({n})")
                    break
            if not full:
                full = data

    # New terms must be in the package, after the published ones.
    for n, v in new.items():
        if n in full and full[n] != v:
            e.append(f"terminos.txt y el paquete no coinciden en a({n})")
            break
    ext = re.search(r"EXTENSIONS: `([^`]+)`", how)
    ext_text = ext.group(1) if ext else ""
    corrected = {int(x) for x in re.findall(r"a\((\d+)\) corrected", ext_text)}
    ext_only = [n for n in new if n not in corrected]
    first_new = min(ext_only) if ext_only else None
    last_pub = max(pub)
    if first_new is not None and last_pub >= first_new:
        e.append(f"la ficha ya llega a a({last_pub}) y el primer término nuevo es a({first_new}): alguien la amplió")
    if first_new is not None and first_new != last_pub + 1:
        e.append(f"el primer término nuevo es a({first_new}) y la ficha llega a a({last_pub})")

    # Published terms: equal, unless declared as corrected.
    for n, v in pub.items():
        if n in full and full[n] != v and n not in corrected:
            e.append(f"a({n}) = {v} en la ficha y {full[n]} en el paquete, sin declararlo como corrección")
            break
    for n in corrected:
        if n not in pub or full.get(n) == pub[n]:
            e.append(f"EXTENSIONS declara a({n}) corregido pero no difiere de la ficha")

    # Fields.
    in_pkg = sorted(n for n in full if n > last_pub)
    if not ext:
        e.append("COMO-ENVIAR.md sin línea EXTENSIONS: `...`")
    elif in_pkg:
        m = re.search(r"a\((\d+)\)-a\((\d+)\) from _Tu Nombre_, <fecha>$", ext_text)
        if not m:
            e.append(f"EXTENSIONS sin el formato «a(X)-a(Y) from _Tu Nombre_, <fecha>»: {ext_text}")
        elif (int(m.group(1)), int(m.group(2))) != (in_pkg[0], in_pkg[-1]):
            e.append(f"EXTENSIONS dice a({m.group(1)})-a({m.group(2)}) y los términos nuevos son a({in_pkg[0]})-a({in_pkg[-1]})")
    if new and in_pkg and max(new) > in_pkg[-1]:
        e.append(f"terminos.txt llega a a({max(new)}) pero el envío solo a a({in_pkg[-1]})")
    if bpath.exists() and full:
        m = re.search(r"Table of n, a\(n\) for n = (\d+)\.\.(\d+)", how)
        if not m:
            e.append("COMO-ENVIAR.md sin la línea LINKS «Table of n, a(n) for n = a..b»")
        elif (int(m.group(1)), int(m.group(2))) != (min(full), max(full)):
            e.append(f"LINKS dice {m.group(1)}..{m.group(2)} y el b-file va de {min(full)} a {max(full)}")
    if not bpath.exists() and new and max(new) not in full:
        e.append("sin b-file, pero los términos nuevos no caben en DATA")
    if "NORMAS-OEIS.md" not in how:
        e.append("COMO-ENVIAR.md no remite a NORMAS-OEIS.md (política de IA)")
    return e


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--oeisdata", required=True)
    ap.add_argument("--envios", default=str(ROOT / "envios"))
    args = ap.parse_args()
    pkgs = sorted(p for p in Path(args.envios).glob("A[0-9]*") if p.is_dir())
    bad = 0
    for p in pkgs:
        errs = check(p, args.oeisdata)
        if errs:
            bad += 1
            print(f"MAL {p.name}: " + "; ".join(errs))
        else:
            print(f"OK  {p.name}")
    print(f"{'OK' if not bad else 'MAL'}: {len(pkgs) - bad}/{len(pkgs)} paquetes cumplen la hoja de estilo")
    sys.exit(1 if bad or not pkgs else 0)


if __name__ == "__main__":
    main()
