#!/usr/bin/env python3
"""Builds the web page of the project into _site/ (index.html + English version + b-files).

Everything is read from envios/: the title of each sequence from the first line of its
COMO-ENVIAR.md, the new terms from terminos.txt and the range from the b-file.
REPO_URL (env) is the public repo, used for links to each package.
"""
import html
import os
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV = ROOT / "envios"
SITE = ROOT / "_site"
REPO = os.environ.get("REPO_URL", "https://github.com/perezamadorluisenrique-gif/oeis-terminos").rstrip("/")

# English titles (the Spanish ones come from COMO-ENVIAR.md)
EN = {
    "A053651": "number of non-isomorphic cyclic subgroups of GL(n,2)",
    "A053658": "number of non-isomorphic cyclic subgroups of GL(n,3)",
    "A053660": "number of non-isomorphic cyclic subgroups of GL(n,4)",
    "A053773": "solutions of X^8 = I in GL(n,2)",
    "A062766": "number of non-isomorphic cyclic subgroups of AGL(n,2)",
    "A065763": "invertible Steinhaus matrices",
    "A085430": "least m with an element of order n in GL(m,2)",
    "A086087": "least m with an element of order n in GL(m,3)",
    "A218932": "conjugacy classes of maximal cyclic subgroups of S_n",
    "A218935": "conjugacy classes of cyclic subgroups of A_n",
    "A218949": "conjugacy classes of maximal cyclic subgroups of A_n",
    "A218975": "conjugacy classes of \"connected\" cyclic subgroups of A_n",
    "A267132": "unipotent matrices over GF(2) that are squares",
}
NOTA = {"A085430": ("corrige a(49): 12 → 21", "corrects a(49): 12 → 21"),
        "A267132": ("corrige una errata de la fórmula", "fixes a formula erratum")}

TXT = {
    "es": dict(lang="es", title="Términos nuevos para la OEIS",
               intro="Trece secuencias de la <a href=\"https://oeis.org\">OEIS</a> ampliadas (y dos corregidas): "
                     "unos 20 000 términos nuevos, cada uno calculado por <strong>dos programas independientes</strong> "
                     "que reproducen todo lo ya publicado. Los envíos a la OEIS se hacen uno a uno y los revisan sus editores: "
                     "hasta que una ficha no esté aprobada, sus términos nuevos son una propuesta.",
               cols=("Secuencia", "Qué cuenta", "Términos nuevos", "Datos"), pkg="paquete", bfile="b-file",
               more="Más", more_body="Cada paquete trae su b-file, los programas, cómo se verificó y cómo enviarlo. "
                     "El código fuente y las dos implementaciones de cada cálculo están en "
                     "<a href=\"{repo}\">el repositorio</a>.",
               lic="Programas: MIT. Textos: CC BY 4.0. Datos tomados de la OEIS: CC BY-SA 4.0. "
                   "Hecho con ayuda de un asistente de IA (Claude); los resultados están comprobados con dos programas.",
               other="English", other_href="en/", skip="Saltar al contenido"),
    "en": dict(lang="en", title="New terms for the OEIS",
               intro="Thirteen <a href=\"https://oeis.org\">OEIS</a> sequences extended (and two corrected): "
                     "about 20,000 new terms, each computed by <strong>two independent programs</strong> that reproduce "
                     "every published term. Submissions to the OEIS are made one at a time and reviewed by its editors: "
                     "until an entry is approved, its new terms are a proposal.",
               cols=("Sequence", "What it counts", "New terms", "Data"), pkg="package", bfile="b-file",
               more="More", more_body="Each package has its b-file, the programs, how it was verified and how to submit it. "
                     "The source code and both implementations of each computation are in "
                     "<a href=\"{repo}\">the repository</a>.",
               lic="Programs: MIT. Texts: CC BY 4.0. Data taken from the OEIS: CC BY-SA 4.0. "
                   "Made with help from an AI assistant (Claude); results are checked by two programs.",
               other="Español", other_href="../", skip="Skip to content"),
}


def nums(path):
    return [int(l.split()[0]) for l in path.read_text().splitlines() if l.strip() and not l.startswith("#")]


def paquetes():
    out = []
    for d in sorted(ENV.glob("A[0-9]*")):
        a = d.name
        m = re.match(r"# .*?\((.*)\)\s*$", (d / "COMO-ENVIAR.md").read_text().splitlines()[0])
        nuevos = nums(d / "terminos.txt")
        bf = next(d.glob("b*.txt"), None)
        out.append(dict(a=a, es=m.group(1) if m else a, en=EN[a], lo=min(nuevos), hi=max(nuevos),
                        bfile=bf.name if bf else None, rango=(nums(bf)[0], nums(bf)[-1]) if bf else None))
    return out


def pagina(t, pk, pref):
    filas = []
    for p in pk:
        nota = NOTA.get(p["a"])
        que = html.escape(p[t["lang"]]) + (f"<br><em>{nota[0 if t['lang'] == 'es' else 1]}</em>" if nota else "")
        datos = [f'<a href="{REPO}/tree/main/envios/{p["a"]}">{t["pkg"]}</a>']
        if p["bfile"]:
            datos.append(f'<a href="{pref}b/{p["bfile"]}">{t["bfile"]} (n = {p["rango"][0]}..{p["rango"][1]})</a>')
        filas.append(f'<tr><th scope="row"><a href="https://oeis.org/{p["a"]}">{p["a"]}</a></th><td>{que}</td>'
                     f'<td>a({p["lo"]})..a({p["hi"]})</td><td>{" · ".join(datos)}</td></tr>')
    c = t["cols"]
    return f"""<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t['title']}</title>
<link rel="stylesheet" href="{pref}estilo.css">
</head>
<body>
<a class="saltar" href="#contenido">{t['skip']}</a>
<main id="contenido">
<header class="portada">
<p class="idioma"><a href="{t['other_href']}" hreflang="{'en' if t['lang'] == 'es' else 'es'}">{t['other']}</a></p>
<h1>{t['title']}</h1>
<p class="entradilla">{t['intro']}</p>
</header>
<div class="tabla" tabindex="0" role="region" aria-label="{t['title']}">
<table>
<thead><tr><th scope="col">{c[0]}</th><th scope="col">{c[1]}</th><th scope="col">{c[2]}</th><th scope="col">{c[3]}</th></tr></thead>
<tbody>
{chr(10).join(filas)}
</tbody>
</table>
</div>
<h2>{t['more']}</h2>
<p>{t['more_body'].format(repo=REPO)}</p>
</main>
<footer><p>{t['lic']}</p></footer>
</body>
</html>
"""


def main():
    if SITE.exists():
        shutil.rmtree(SITE)
    (SITE / "b").mkdir(parents=True)
    (SITE / "en").mkdir()
    pk = paquetes()
    for p in pk:
        if p["bfile"]:
            shutil.copy(ENV / p["a"] / p["bfile"], SITE / "b" / p["bfile"])
    shutil.copy(ROOT / "sitio" / "estilo.css", SITE / "estilo.css")
    (SITE / "index.html").write_text(pagina(TXT["es"], pk, ""))
    (SITE / "en" / "index.html").write_text(pagina(TXT["en"], pk, "../"))
    peso = sum(f.stat().st_size for f in SITE.rglob("*") if f.is_file())
    print(f"_site: {len(pk)} secuencias, {peso / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
