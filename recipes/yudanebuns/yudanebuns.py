#!/usr/bin/env python3
"""Soft burger buns (yudane formula, microwave scald) -> HTML + one-page PDF.

Output names derive from this script's name (yudanebuns.py -> yudanebuns.html,
yudanebuns.pdf). A photo next to the script with the same stem (.jpg, .jpeg,
.png, .webp), or PHOTO set below, is added as a thumbnail; the auto-fit then
accounts for it.

PDF: WeasyPrint if importable, else headless Chrome/Chromium. The base font is
lowered in 0.25pt steps from 11pt until the PDF is a single page.
"""

import html
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT = Path(__file__).resolve()
STEM = SCRIPT.stem
OUT_HTML = SCRIPT.with_name(f"{STEM}.html")
OUT_PDF = SCRIPT.with_name(f"{STEM}.pdf")
PHOTO = None  # optional explicit file name, e.g. "buns.jpg"

THEME = "#8a5418"   # baked-crust brown
TINT = "#fbf3e6"
RULE = "#e6d2b0"

TITLE = "Super-Soft Burger Buns"
SUBTITLE = "Soft enriched buns with a microwave scald"
META = ["Makes 4 large buns", "About 5½ h, 40 min of it active"]
SOURCE = 'Adapted from ChainBaker’s yudane buns (chainbaker.com/yudane-buns).'

# (name, grams-or-text, baker's % of total flour or None, note)
FLOUR_TOTAL = 300
INGREDIENTS = [
    ("Scald", [
        ("Bread flour", 50, "", ""),
        ("Water", 50, "", ""),
        ("Milk", 150, "", ""),
    ]),
    ("Dough", [
        ("Water", 10, "", "to dissolve the yeast"),
        ("Instant yeast", 4, "", "or 4.8 g active dry / 12 g fresh"),
        ("Egg yolk", 20, "", "1 large egg (20–25 g)"),
        ("Sugar", 20, "", ""),
        ("Salt", 6, "", ""),
        ("Bread flour", 250, "", ""),
        ("Butter, cold", 20, "", "small cubes"),
    ]),
    ("Finish", [
        ("Egg white", "1", None, ""),
        ("Sesame seeds", "", None, "to sprinkle"),
    ]),
]
TOTALS = [
    ("Total flour", 300),
    ("Total liquid", 210),
    ("Dough weight", 580),
]

STEPS = [
    ("Scald",
     "Whisk flour, water and milk in a microwave-safe mixing bowl. Heat in "
     "20 s bursts, whisking in between, until it thickens at 65 °C (150 °F). "
     "This takes about 90 s, or a little over 3 min for a double batch."),
    ("Cool",
     "Let cool to about 27 °C (80 °F), roughly 45 min. An ice-water bath "
     "speeds this up. The scald can be made a day ahead and refrigerated; warm "
     "it back up to 27 °C before using."),
    ("Mix",
     "Dissolve the yeast in the water. Add yolk, sugar and salt to the scald "
     "and stir until dissolved. Add the flour, the yeast and the cold butter "
     "cut into small cubes, and mix until no dry flour remains. Cover and rest "
     "for 15 min."),
    ("Knead",
     "Tip onto the counter and knead for about 9 min using stretch-and-folds. "
     "The dough is sticky at first, and the butter works itself in. Desired "
     "dough temperature is 25–26 °C (77–79 °F)."),
    ("Bulk ferment",
     "Return to the bowl, cover and ferment for 2 to 2½ h."),
    ("Shape",
     "Divide into 4 pieces of about 145 g, pre-shape and rest for 20 min. "
     "Shape into tight rounds and place on a parchment-lined baking sheet."),
    ("Proof",
     "Proof covered for about 2 h. Preheat the oven to 160 °C (320 °F) fan "
     "during the last hour."),
    ("Bake",
     "Brush with egg white, sprinkle with sesame seeds and press them on "
     "lightly. Bake for about 25 min until golden brown, rotating halfway "
     "through. Start checking at 18 min; the inside should reach "
     "90 °C (195 °F)."),
]

NOTES = [
    ("Dough temperature",
     "The scald temperature sets the dough temperature. As a rule of thumb, "
     "scald temperature = (3 × 25.5 °C − flour temperature) ÷&nbsp;2."),
    ("Variations",
     "In Europe, use Type 550 (DE), T65 (FR) or strong (UK) bread flour. For "
     "active dry yeast, give it 5–10 min to bloom. The dough also makes a "
     "soft sandwich loaf in a 1 lb (8½ × 4½ in) pan; bake until it reaches "
     "93 °C inside."),
]


def find_photo():
    if PHOTO:
        p = SCRIPT.with_name(PHOTO)
        return p if p.exists() else None
    for ext in (".jpg", ".jpeg", ".png", ".webp"):
        p = SCRIPT.with_name(STEM + ext)
        if p.exists():
            return p
    return None


def fmt_qty(q):
    return f"{q} g" if isinstance(q, (int, float)) else html.escape(q)


def fmt_pct(q, pct):
    if pct is None or not isinstance(q, (int, float)):
        return ""
    return f"{100 * q / FLOUR_TOTAL:.1f}%".replace(".0%", "%")


CSS = """
@page {{ size: letter; margin: 0.5in; }}
* {{ box-sizing: border-box; }}
body {{ font-family: -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
       font-size: {fs}pt; line-height: 1.36; color: #222; margin: 0; }}
header {{ text-align: center; border-bottom: 2px solid {theme}; padding-bottom: 0.45em;
          margin-bottom: 0.9em; }}
h1 {{ color: {theme}; font-size: 1.75em; margin: 0 0 0.1em; letter-spacing: -0.01em; }}
.subtitle {{ color: #555; font-size: 1em; margin: 0 0 0.2em; font-style: italic; }}
.meta {{ color: #444; font-size: 0.86em; margin: 0; }}
.meta span + span::before {{ content: " • "; color: {theme}; }}
.cols {{ }}
.left {{ float: left; width: 36%; background: {tint}; border: 1px solid {rule}; border-radius: 8px;
         padding: 0.8em 0.9em; }}
.right {{ margin-left: 39%; }}
h2 {{ color: {theme}; font-size: 1.12em; margin: 0 0 0.45em; border-bottom: 1px solid {rule};
      padding-bottom: 0.2em; }}
h3 {{ color: {theme}; font-size: 0.82em; text-transform: uppercase; letter-spacing: 0.05em;
      margin: 0.8em 0 0.25em; }}
h3.first {{ margin-top: 0.2em; }}
table.ing {{ width: 100%; border-collapse: collapse; font-size: 0.9em; }}
table.ing td {{ padding: 0.14em 0; vertical-align: top; border-bottom: 1px dotted {rule}; }}
td.q {{ font-weight: 700; white-space: nowrap; text-align: right; padding-right: 0.5em !important;
        width: 4.6em; }}
td.p {{ color: #8a7a66; text-align: right; white-space: nowrap; width: 3.6em; font-size: 0.9em; }}
.inote {{ display: block; color: #6b6b6b; font-size: 0.86em; }}
table.tot td {{ border-bottom: none; color: #555; }}
table.tot td.q {{ font-weight: 600; }}
.photo {{ width: 100%; max-width: 1.9in; display: block; margin: 0 auto 0.7em;
          border-radius: 8px; }}
ol.steps {{ list-style: none; counter-reset: s; margin: 0; padding: 0; }}
ol.steps li {{ counter-increment: s; position: relative; padding-left: 1.9em; margin-bottom: 0.55em;
              font-size: 0.95em; }}
ol.steps li::before {{ content: counter(s); position: absolute; left: 0; top: 0.05em;
    width: 1.35em; height: 1.35em; line-height: 1.35em; border-radius: 50%; background: {theme};
    color: #fff; text-align: center; font-size: 0.85em; font-weight: 700; }}
ol.steps strong.t {{ color: {theme}; }}
.note {{ background: #f8f6f2; border-left: 3px solid {theme}; border-radius: 0 6px 6px 0;
         padding: 0.45em 0.7em; margin: 0.55em 0 0; font-size: 0.86em; }}
.note strong {{ color: {theme}; }}
.source {{ margin-top: 0.9em; font-size: 0.75em; color: #777; text-align: center; }}
"""


def render_html(fs, photo):
    out = ['<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">',
           f"<title>{html.escape(TITLE)}</title><style>",
           CSS.format(fs=fs, theme=THEME, tint=TINT, rule=RULE),
           "</style></head><body>",
           f"<header><h1>{html.escape(TITLE)}</h1>",
           f'<p class="subtitle">{html.escape(SUBTITLE)}</p>',
           '<p class="meta">' + "".join(f"<span>{html.escape(m)}</span>" for m in META)
           + "</p></header>",
           '<div class="cols"><div class="left">']
    if photo:
        out.append(f'<img class="photo" src="{html.escape(photo.name)}" alt="">')
    out.append("<h2>Ingredients</h2>")
    for i, (group, items) in enumerate(INGREDIENTS):
        out.append(f'<h3{" class=first" if i == 0 else ""}>{html.escape(group)}</h3>')
        out.append('<table class="ing">')
        for name, q, pct, note in items:
            n = html.escape(name)
            if note:
                n += f'<span class="inote">{html.escape(note)}</span>'
            out.append(f'<tr><td class="q">{fmt_qty(q)}</td><td>{n}</td>'
                       f'<td class="p">{fmt_pct(q, pct)}</td></tr>')
        out.append("</table>")
    out.append('<h3>Totals</h3><table class="ing tot">')
    for name, q in TOTALS:
        pct = fmt_pct(q, "") if name != "Dough weight" else ""
        out.append(f'<tr><td class="q">{fmt_qty(q)}</td><td>{html.escape(name)}</td>'
                   f'<td class="p">{pct}</td></tr>')
    out.append("</table></div>")
    out.append('<div class="right"><h2>Method</h2><ol class="steps">')
    for title, body in STEPS:
        out.append(f'<li><strong class="t">{title}.</strong> {body}</li>')
    out.append("</ol>")
    for title, body in NOTES:
        out.append(f'<div class="note"><strong>{title}:</strong> {body}</div>')
    out.append(f'<p class="source">{html.escape(SOURCE)}</p>')
    out.append("</div></div></body></html>")
    doc = "\n".join(out)
    head, body = doc.split("</head>", 1)
    body = re.sub(r"(\d) (?=°|g\b|min\b|s\b|h\b|lb\b|in\b|×|÷)", "\\1&nbsp;", body)
    return head + "</head>" + body


def pdf_weasyprint(doc_html):
    import weasyprint
    doc = weasyprint.HTML(string=doc_html, base_url=str(SCRIPT.parent)).render()
    return len(doc.pages), doc.write_pdf()


def find_chrome():
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser"):
        if shutil.which(name):
            return shutil.which(name)
    return None


def pdf_chrome(doc_html, chrome):
    with tempfile.TemporaryDirectory() as tmp:
        src = SCRIPT.parent / f".{STEM}.tmp.html"  # same dir so the photo resolves
        dst = Path(tmp) / "out.pdf"
        src.write_text(doc_html, encoding="utf-8")
        try:
            subprocess.run([chrome, "--headless", "--no-sandbox", "--disable-gpu",
                            "--no-pdf-header-footer", f"--print-to-pdf={dst}",
                            src.as_uri()], check=True, capture_output=True)
        finally:
            src.unlink(missing_ok=True)
        data = dst.read_bytes()
    pages = len(re.findall(rb"/Type\s*/Page(?!s)", data))
    return pages, data


def main():
    photo = find_photo()
    try:
        import weasyprint  # noqa: F401
        backend = pdf_weasyprint
    except ImportError:
        chrome = find_chrome()
        if not chrome:
            sys.exit("Neither WeasyPrint nor Chrome/Chromium is available.")
        backend = lambda h: pdf_chrome(h, chrome)  # noqa: E731

    fs = 11.0
    while True:
        doc_html = render_html(fs, photo)
        pages, pdf = backend(doc_html)
        print(f"  {fs:.2f}pt -> {pages} page(s)", file=sys.stderr)
        if pages == 1 or fs <= 7.5:
            break
        fs -= 0.25
    OUT_HTML.write_text(doc_html, encoding="utf-8")
    OUT_PDF.write_bytes(pdf)
    print(f"{OUT_PDF.name}: {pages} page(s) at {fs:.2f}pt"
          + (f", photo {photo.name}" if photo else ""))
    if pages != 1:
        print("WARNING: did not fit on one page", file=sys.stderr)


if __name__ == "__main__":
    main()
