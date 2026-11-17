#!/usr/bin/env python3
"""Generate single-page HTML and PDF versions of the Taiwanese-style quick pickled cabbage recipe."""

import argparse
from pathlib import Path
import sys
from pypdf import PdfReader
import weasyprint


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Taiwanese-Style Quick Pickled Cabbage (Slaw Cut)</title>
<style>
@page {{
    size: letter;
    margin: 0.5in;
}}
* {{
    box-sizing: border-box;
}}
body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: {font_size}pt;
    line-height: {line_height};
    color: #222;
    margin: 0;
    padding: 0;
}}
header {{
    border-bottom: 2px solid #004d40;
    padding-bottom: 10px;
    margin-bottom: 18px;
    text-align: center;
}}
h1 {{
    color: #004d40;
    font-size: 1.55em;
    margin: 0 0 4px 0;
    letter-spacing: -0.01em;
}}
.subtitle {{
    color: #555;
    font-size: 0.92em;
    margin: 0;
}}
.columns {{
    display: table;
    width: 100%;
    table-layout: fixed;
}}
.left-col {{
    display: table-cell;
    width: 36%;
    vertical-align: top;
    background-color: #e0f2f1;
    padding: 16px 18px;
    border-radius: 8px;
    border: 1px solid #b2dfdb;
}}
.gutter {{
    display: table-cell;
    width: 3%;
}}
.right-col {{
    display: table-cell;
    width: 61%;
    vertical-align: top;
    padding: 4px 2px;
}}
h2 {{
    color: #00695c;
    font-size: 1.18em;
    margin: 0 0 10px 0;
    border-bottom: 1px solid #b2dfdb;
    padding-bottom: 4px;
}}
h3 {{
    font-size: 0.96em;
    margin: 14px 0 6px 0;
    color: #004d40;
    text-transform: uppercase;
    letter-spacing: 0.03em;
}}
h3:first-of-type {{
    margin-top: 6px;
}}
ul, ol {{
    margin: 0;
    padding-left: 18px;
}}
ul {{
    list-style-type: disc;
}}
.left-col li {{
    margin-bottom: {ing_margin}px;
}}
.right-col li {{
    margin-bottom: {step_margin}px;
}}
.note-box {{
    margin-top: {note_margin}px;
    padding: 10px 12px;
    background-color: #f4f9f9;
    border-left: 3px solid #00695c;
    border-radius: 0 6px 6px 0;
    font-size: 0.92em;
    color: #333;
}}
</style>
</head>
<body>
    <header>
        <h1>Taiwanese-Style Quick Pickled Cabbage (Slaw Cut)</h1>
        <p class="subtitle">Yield: ~900g drained slaw &bull; Active Prep: 15 min &bull; Cure: 30 min to 24 hr</p>
    </header>

    <div class="columns">
        <div class="left-col">
            <h2>Ingredients</h2>

            <h3>Vegetables &amp; Purging</h3>
            <ul>
                <li><strong>1000g</strong> Taiwanese flat cabbage (or green cabbage), cored &amp; finely shredded</li>
                <li><strong>100g</strong> Carrots, peeled &amp; julienned or grated</li>
                <li><strong>22g</strong> Kosher salt (2% vegetable weight)</li>
            </ul>

            <h3>Pickling Liquid &amp; Aromatics</h3>
            <ul>
                <li><strong>4g</strong> Whole Sichuan peppercorns</li>
                <li><strong>135g</strong> White sugar</li>
                <li><strong>150ml</strong> Rice vinegar (unseasoned)</li>
                <li><strong>12g</strong> Fresh garlic (~4 cloves), finely grated</li>
                <li><strong>15g</strong> Fresh red chilies, thinly sliced</li>
                <li><strong>15ml</strong> Toasted sesame oil</li>
            </ul>
        </div>

        <div class="gutter"></div>

        <div class="right-col">
            <h2>Instructions</h2>
            <ol>
                <li><strong>Toast the Peppercorns:</strong> Place the whole Sichuan peppercorns in a dry skillet over medium heat. Toss constantly for 1&ndash;2 minutes until highly fragrant, then transfer immediately to a small dish so they do not scorch.</li>
                <li><strong>Prep &amp; Purge the Vegetables:</strong> Set a large mixing bowl directly on a scale and tare to zero. Finely shred the cabbage into the bowl to reach 1000g. Tare again and grate or julienne the carrots to reach 100g. Tare once more and add 22g kosher salt. Massage thoroughly until the vegetables feel damp, then let stand at room temperature (68&ndash;72&deg;F / 20&ndash;22&deg;C) for 15&ndash;20 minutes.</li>
                <li><strong>Dissolve &amp; Infuse the Brine:</strong> While the cabbage purges, place a microwave-safe measuring cup on the scale. Weigh out 135g white sugar and 150ml rice vinegar. Microwave on high for ~40 seconds until warm, then stir until the sugar completely dissolves without diluting the brine. Stir in the grated garlic, sliced chilies, toasted sesame oil, and toasted Sichuan peppercorns.</li>
                <li><strong>Extract Moisture:</strong> After 15&ndash;20 minutes, the fine-cut vegetables will have released a pool of liquid. Grab handfuls and squeeze firmly to extract as much liquid as possible, discarding the liquid. Do not rinse.</li>
                <li><strong>Combine &amp; Cure:</strong> Return the squeezed vegetables to the wiped-out mixing bowl or a glass storage container. Pour the warm aromatic vinegar mixture over top and toss thoroughly until evenly coated.</li>
                <li><strong>Chill &amp; Serve:</strong> Cover and refrigerate. The slaw is crisp and ready to eat after 30 minutes, while the Sichuan peppercorn and garlic notes peak between 12 and 24 hours.</li>
            </ol>

            <div class="note-box">
                <strong>Technique Note:</strong> Dissolving the sugar directly in briefly warmed rice vinegar eliminates added water, keeping the fine slaw cut crisp and preventing a diluted, soggy finish.
            </div>
        </div>
    </div>
</body>
</html>
"""

LAYOUT_CANDIDATES = [
    (11.5, 1.42, 10, 12, 16),
    (11.0, 1.38, 8, 10, 14),
    (10.5, 1.35, 7, 9, 12),
    (10.0, 1.32, 6, 8, 10),
]


def render_recipe(html_path: Path, pdf_path: Path) -> None:
    for font_size, line_height, ing_margin, step_margin, note_margin in LAYOUT_CANDIDATES:
        html_content = HTML_TEMPLATE.format(
            font_size=font_size,
            line_height=line_height,
            ing_margin=ing_margin,
            step_margin=step_margin,
            note_margin=note_margin,
        )
        html_path.write_text(html_content, encoding="utf-8")
        weasyprint.HTML(filename=str(html_path)).write_pdf(str(pdf_path))

        reader = PdfReader(str(pdf_path))
        extracted = reader.pages[0].extract_text() or ""
        if len(reader.pages) == 1 and "diluted, soggy finish." in extracted:
            return

    raise RuntimeError("Unable to fit document cleanly onto a single page.")


def main() -> None:
    stem = Path(__file__).stem
    parser = argparse.ArgumentParser(
        description="Generate HTML and PDF recipe files."
    )
    parser.add_argument(
        "--html",
        type=Path,
        default=Path(f"{stem}.html"),
        help=f"Output HTML file path (default: {stem}.html)",
    )
    parser.add_argument(
        "--pdf",
        type=Path,
        default=Path(f"{stem}.pdf"),
        help=f"Output PDF file path (default: {stem}.pdf)",
    )
    args = parser.parse_args()
    render_recipe(args.html, args.pdf)


if __name__ == "__main__":
    main()
