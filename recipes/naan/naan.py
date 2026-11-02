from pathlib import Path
from weasyprint import HTML

# Derive filenames dynamically from the script's basename
SCRIPT_PATH = Path(__file__).resolve()
BASE_STEM = SCRIPT_PATH.stem
HTML_PATH = SCRIPT_PATH.with_name(f"{BASE_STEM}.html")
PDF_PATH = SCRIPT_PATH.with_name(f"{BASE_STEM}.pdf")

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Pan-Baked Naan Recipe</title>
<style>
  @page {{
    size: letter portrait;
    margin: 0.45in;
  }}
  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #1a1a1a;
    background: #fff;
    line-height: 1.35;
    /* Base font size modified by scaling loop */
    font-size: {font_size:.2f}pt;
  }}
  
  header {{
    border-bottom: 2px solid #222;
    padding-bottom: 5px;
    margin-bottom: 10px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }}
  h1 {{
    font-size: 1.6em;
    font-weight: 800;
    letter-spacing: -0.5px;
    text-transform: uppercase;
  }}
  .subtitle {{
    font-size: 0.85em;
    color: #555;
    font-weight: 500;
  }}
  
  /* 2-Column Grid */
  .grid {{
    display: flex;
    gap: 16px;
  }}
  .col-left {{
    width: 36%;
  }}
  .col-right {{
    width: 64%;
  }}

  .panel-title {{
    font-size: 0.95em;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    border-bottom: 1.5px solid #444;
    padding-bottom: 3px;
    margin-bottom: 7px;
    color: #111;
  }}

  /* Ingredients */
  .ingredient-group {{
    margin-bottom: 8px;
  }}
  .ingredient-group h4 {{
    font-size: 0.8em;
    text-transform: uppercase;
    color: #666;
    margin-bottom: 3px;
    letter-spacing: 0.5px;
  }}
  ul {{
    list-style: none;
  }}
  li.ing {{
    padding: 2px 0;
    font-size: 0.82em;
    display: flex;
    justify-content: space-between;
    border-bottom: 1px dotted #ccc;
  }}
  li.ing span.item {{
    font-weight: 500;
  }}
  li.ing span.qty {{
    color: #444;
    font-size: 0.95em;
    text-align: right;
    white-space: nowrap;
    padding-left: 6px;
  }}

  /* Steps */
  ol.steps {{
    list-style: none;
    counter-reset: step-counter;
  }}
  ol.steps li {{
    counter-increment: step-counter;
    position: relative;
    padding-left: 22px;
    margin-bottom: 6px;
    font-size: 0.8em;
    text-align: justify;
  }}
  ol.steps li::before {{
    content: counter(step-counter);
    position: absolute;
    left: 0;
    top: 0;
    background: #222;
    color: #fff;
    width: 15px;
    height: 15px;
    border-radius: 50%;
    text-align: center;
    line-height: 15px;
    font-size: 0.75em;
    font-weight: 700;
  }}

  /* Callout Box */
  .tips-box {{
    margin-top: 8px;
    padding: 6px 8px;
    background: #f8f8f8;
    border-left: 3px solid #333;
    font-size: 0.78em;
    line-height: 1.3;
  }}
</style>
</head>
<body>

  <header>
    <div>
      <h1>Cast Iron Pan Naan</h1>
      <div class="subtitle">High-heat stovetop method with yogurt & water steam-anchor</div>
    </div>
    <div class="subtitle" style="text-align: right;">
      <strong>Yield:</strong> 8 Large Naans<br>
      <strong>Prep & Cook:</strong> 2 hrs
    </div>
  </header>

  <div class="grid">
    <!-- Left Column -->
    <div class="col-left">
      <div class="panel-title">Ingredients</div>

      <div class="ingredient-group">
        <h4>Flour & Leaveners</h4>
        <ul>
          <li class="ing"><span class="item">All-Purpose Flour</span><span class="qty">250 g (2 cups)</span></li>
          <li class="ing"><span class="item">Bread Flour</span><span class="qty">250 g (2 cups)</span></li>
          <li class="ing"><span class="item">Instant Dry Yeast</span><span class="qty">7 g (2¼ tsp)</span></li>
          <li class="ing"><span class="item">Baking Powder</span><span class="qty">1 tsp</span></li>
          <li class="ing"><span class="item">Fine Sea Salt</span><span class="qty">1½ tsp</span></li>
          <li class="ing"><span class="item">Granulated Sugar</span><span class="qty">1 tsp</span></li>
        </ul>
      </div>

      <div class="ingredient-group">
        <h4>Wet Ingredients</h4>
        <ul>
          <li class="ing"><span class="item">Plain Greek Yogurt</span><span class="qty">150 g (room temp)</span></li>
          <li class="ing"><span class="item">Warm Water</span><span class="qty">200 ml (105–110°F)</span></li>
          <li class="ing"><span class="item">Warm Whole Milk</span><span class="qty">60 ml (¼ cup)</span></li>
          <li class="ing"><span class="item">Melted Ghee (dough)</span><span class="qty">30 g (2 tbsp)</span></li>
        </ul>
      </div>

      <div class="ingredient-group">
        <h4>Finishing Ghee</h4>
        <ul>
          <li class="ing"><span class="item">Ghee / Butter</span><span class="qty">45 g (3 tbsp)</span></li>
          <li class="ing"><span class="item">Garlic & Cilantro</span><span class="qty">To taste</span></li>
        </ul>
      </div>

      <div class="tips-box">
        <strong>The Water Trick:</strong> Wetting the dough face produces instant under-steam, blasting blister bubbles upward while gripping the hot cast-iron.
      </div>
    </div>

    <!-- Right Column -->
    <div class="col-right">
      <div class="panel-title">Method</div>
      <ol class="steps">
        <li><strong>Hydrate:</strong> Whisk flours, yeast, baking powder, salt, and sugar. In a jug, blend warm water, warm milk, room-temp yogurt, and 2 tbsp ghee. Pour wet into dry and mix into a shaggy mass.</li>
        <li><strong>Knead:</strong> Knead on a lightly floured surface for 8–10 min (or 6 min in a mixer) until smooth, elastic, and slightly tacky. Avoid over-flouring to keep moisture high.</li>
        <li><strong>Proof:</strong> Shape into a ball, place in a greased bowl, cover tightly, and proof in a warm area for 60–90 min until doubled.</li>
        <li><strong>Divide & Relax:</strong> Deflate gently. Divide into 8 equal portions (~90–95 g each) and roll into balls. Cover loosely on a tray for 15–20 min to relax gluten.</li>
        <li><strong>Preheat & Roll:</strong> Heat a dry 10–12" cast iron skillet over medium-high until lightly smoking. Roll one dough ball into an 8–9" round disk (⅛" / 3–4 mm thick).</li>
        <li><strong>Water & Sear:</strong> Brush top surface generously with water. Slap wet-side directly down into the dry, smoking skillet.</li>
        <li><strong>Blister & Flip:</strong> Cook 45–60 sec until huge blisters balloon across the surface. Flip and sear the reverse side for 45–60 sec until charred spots appear.</li>
        <li><strong>Brush & Wrap:</strong> Transfer immediately to a plate, coat with garlic ghee, and stack inside a clean kitchen towel to steam and maintain pliability.</li>
      </ol>
    </div>
  </div>

</body>
</html>
"""

def render_single_page_pdf():
    # Initial font size (pt). All headings and steps scale relatively via em units.
    current_pt = 11.0
    min_pt = 7.0
    step = 0.25

    final_doc = None
    final_html = ""

    # Iterative solver: render in-memory, inspect page count, adjust font if overflow occurs
    while current_pt >= min_pt:
        html_str = HTML_TEMPLATE.format(font_size=current_pt)
        html_obj = HTML(string=html_str, base_url=str(SCRIPT_PATH.parent))
        doc = html_obj.render()

        page_count = len(doc.pages)
        if page_count == 1:
            final_doc = doc
            final_html = html_str
            break

        current_pt -= step

    if not final_doc:
        # Fallback if content was exceptionally long: take the smallest size tested
        final_doc = doc
        final_html = html_str

    # Write HTML output
    HTML_PATH.write_text(final_html, encoding="utf-8")
    print(f"Wrote HTML: {HTML_PATH.name}")

    # Write PDF output
    final_doc.write_pdf(target=str(PDF_PATH))
    print(f"Generated Single-Page PDF: {PDF_PATH.name} (Base font: {current_pt:.2f}pt, Pages: {len(final_doc.pages)})")

if __name__ == "__main__":
    render_single_page_pdf()
