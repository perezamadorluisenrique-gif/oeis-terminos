#!/usr/bin/env python3
"""Builds envios/Axxxxxx/ packages from trabajo/Axxxxxx/ (run from repo root)."""
import os, shutil, sys, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def terms(p):
    d = {}
    for l in open(p):
        l = l.split('#')[0].split()
        if len(l) >= 2: d[int(l[0])] = int(l[1])
    return d

SEQ = {
 'A086087': dict(nombre='a(n) is the minimal m such that the group GL(m,3) has an element of order n.',
     bfile=True, progs=['impl1/impl1.py', 'impl2/a086087.py', 'impl2/brute.c', 'impl2/README.txt']),
 'A053773': dict(nombre='Number of n X n binary matrices of order dividing 8 (i.e., number of solutions of X^8=I in GL(n,2)).',
     bfile=True, progs=['impl1/impl1.py', 'impl2/impl2.py', 'impl2/README.txt']),
 'A065763': dict(nombre='Number of invertible Steinhaus matrices of order n.',
     bfile=False, progs=['impl1/stein2.c', 'impl2/impl2.c', 'impl2/run.sh', 'impl2/README.txt']),
 # Phase 2 (2026-10-20). A085430: n=49 is a correction (excluded from conocidos.txt),
 # so the contiguity check below covers it through impl1/impl2.
 'A085430': dict(nombre='a(n) is the minimal m such that the group GL(m,2) has an element of order n.',
     bfile=True, progs=['impl1/mindeg.py', 'impl2/a085430.py']),
 'A053651': dict(nombre='Number of nonisomorphic cyclic subgroups of general linear group GL(n,2).',
     bfile=True, progs=['impl1/gl2orders.py', 'impl2/prim.py', 'impl2/cnt.cpp', 'impl2/comb.py', 'impl2/METODO.md']),
 'A062766': dict(nombre='Number of nonisomorphic cyclic subgroups of general affine group AGL(n,2).',
     bfile=True, progs=['impl1/gl2orders.py', 'impl2/bf.cpp']),
 'A053658': dict(nombre='Number of nonisomorphic cyclic subgroups of general linear group GL(n,3).',
     bfile=True, progs=['impl1/glq_orders.py', 'impl2/prim.py', 'impl2/cnt.cpp', 'impl2/final.py', 'impl2/bf.cpp', 'impl2/METODO.md']),
 'A053660': dict(nombre='Number of nonisomorphic cyclic subgroups of general linear group GL(n,4).',
     bfile=True, progs=['impl1/glq_orders.py', '../A053658/impl2/prim.py', 'impl2/cnt.cpp', 'impl2/final.py', 'impl2/METODO.md']),
 **{a: dict(nombre=n, bfile=True, progs=['../A218935/impl1/cyclic_sn.py', '../A218932/impl2/cyc.py',
                                         '../A218932/impl2/brute.py', '../A218932/impl2/METODO.md'])
    for a, n in [('A218932', 'Number of maximal cyclic conjugacy classes of subgroups of the symmetric group.'),
                 ('A218935', 'Number of cyclic conjugacy classes of subgroups of the alternating group.'),
                 ('A218949', 'Number of maximal cyclic conjugacy classes of subgroups of the alternating group.'),
                 ('A218975', 'Number of connected cyclic conjugacy classes of subgroups of the alternating group.')]},
 'A267132': dict(nombre='Unipotent n X n matrices over GF(2) that are squares of other such matrices.',
     bfile=True, progs=['impl1/squares.py', 'impl2/sq.py', 'impl2/bf.cpp', 'impl2/METODO.md']),
}

def data_lines(vals, limit=260):
    """Comma-separated terms that fit in ~limit characters (OEIS DATA field)."""
    out, s = [], ''
    for v in vals:
        t = (',' if s else '') + str(v)
        if len(s) + len(t) > limit: break
        s += t; out.append(v)
    return s, len(out)

for a, cfg in SEQ.items():
    w = os.path.join(ROOT, 'trabajo', a); e = os.path.join(ROOT, 'envios', a)
    os.makedirs(os.path.join(e, 'programas'), exist_ok=True)
    k, i1, i2 = terms(f'{w}/conocidos.txt'), terms(f'{w}/impl1.txt'), terms(f'{w}/impl2.txt')
    assert all(i1[n] == v and i2[n] == v for n, v in k.items()), a
    new = sorted(n for n in i1 if n not in k and i2.get(n) == i1[n])
    full = sorted(set(k) | set(new))
    assert full == list(range(full[0], full[-1] + 1)), a
    with open(f'{e}/terminos.txt', 'w') as f:
        f.write(f'# {a}: términos nuevos (n a(n)), confirmados por dos implementaciones independientes\n')
        for n in new: f.write(f'{n} {i1[n]}\n')
    if cfg['bfile']:
        with open(f'{e}/b{a[1:]}.txt', 'w') as f:
            for n in full: f.write(f'{n} {k.get(n, i1.get(n))}\n')
    s, cnt = data_lines([k.get(n, i1.get(n)) for n in full])
    with open(f'{e}/datos-propuestos.txt', 'w') as f:
        f.write(f'# DATA propuesto (≈260 caracteres): a({full[0]})..a({full[0]+cnt-1})\n{s}\n')
    for p in cfg['progs']:
        shutil.copy(f"{w}/{p}", f"{e}/programas/{p.replace('../', '').replace('/', '-')}")
    with open(f'{e}/verificacion.md', 'w') as f:
        f.write(f'# Verificación de {a}\n\n')
        f.write(f'- Términos conocidos (ficha en oeis/oeisdata, comprobada el 2026-10-20): n = {min(k)}..{max(k)}.\n')
        f.write(f'- Términos nuevos: n = {new[0]}..{new[-1]} ({len(new)} términos).\n')
        f.write(f'- impl1 e impl2 se escribieron por separado (impl2 por un subagente sin ver impl1) y ambas reproducen todos los términos conocidos; coinciden en todos los nuevos (comprobado por `generar.py` y por `score`).\n\n')
        f.write('## Notas del cálculo\n\n' + open(f'{w}/NOTAS.md').read().split('\n', 1)[1])
    print(a, 'nuevos', len(new), 'data hasta', full[0] + cnt - 1, 'bfile' if cfg['bfile'] else '')
