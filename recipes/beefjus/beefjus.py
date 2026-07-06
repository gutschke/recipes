#!/usr/bin/env python3
import sys
import markdown
from weasyprint import HTML, CSS

# 1. Define the Refined Markdown Recipe
recipe_md = """
# Faux Bone-Reduction Beef Jus
**Yield:** ~375g | **Prep time:** 5 mins | **Cook time:** 20-25 mins

A rich, glossy pan sauce utilizing gelatin and cornstarch for superior hot stability. Designed with a make-ahead workflow in mind.

## Ingredients

**Prep & Bloom**

* 30g Water, cold
* 7g Unflavored gelatin powder

**Aromatics & Reduction**

* 15g Unsalted butter
* 40g Shallot, finely minced
* 10g Garlic, crushed (about 2 cloves)
* 10g Tomato paste
* 120g Dry red wine

**Broth Build**

* 350g Water
* 15g Better Than Bouillon Roasted Beef Base
* 5g Sugar
* 2 sprigs Fresh thyme
* 2g Black peppercorns, whole

**Thickening**

* 5g Water, cold
* 3g Cornstarch

**Finishing (Just Before Serving)**

* 15g Dry red wine, fresh
* 15g Unsalted butter, cold
* 2g Worcestershire sauce (optional)

## Instructions

1. **Ahead of time (Bloom):** In a small ramekin, sprinkle the gelatin over the 30g of cold water. Stir briefly and set aside to bloom into a solid puck.
2. **Sauté Aromatics:** Place a saucepan directly on the scale, tare, and add the first 15g of butter. Move to the stove over medium heat. Once foaming, add the minced shallots and garlic. Sauté until translucent (about 3 minutes). Add the tomato paste and cook for 1 minute longer to toast it, stirring frequently.
3. **Deglaze & Flambé:** Pour in the 120g of red wine. If comfortable, carefully ignite the wine to flambé, which quickly burns off the alcohol and adds depth. Simmer aggressively until the flames subside and the wine is reduced by at least half, taking on a thick, syrupy consistency.
4. **Infuse the Broth:** Add the 350g of water, beef bouillon, sugar, thyme, and whole peppercorns. Bring to a gentle simmer and let it cook for about 10 minutes to extract the flavors and dissolve the sugar. 
5. **Strain:** Pour the contents of the saucepan through a fine-mesh sieve into a heat-proof jug. Press on the solids to extract all liquid, then discard the solids. Return the strained liquid to the saucepan over medium-low heat.
6. **Incorporate Gelatin:** Add the bloomed gelatin puck directly into the hot, strained jus. Whisk gently until completely dissolved.
7. **Thicken:** In a small bowl, whisk the 3g of cornstarch and 5g of cold water into a smooth slurry. Whisk the slurry directly into the simmering jus. Cook for 1 to 2 minutes until the sauce slightly thickens and any raw starch flavor cooks out.
8. **Make-Ahead Storage:** *If making ahead, remove from heat, let cool completely, and store in an airtight container in the refrigerator.*
9. **Finish:** When ready to serve, gently reheat the jus to a simmer on the stove. Off the heat, whisk in the fresh 15g of red wine, the Worcestershire sauce, and the remaining 15g of cold butter until completely emulsified and glossy. Serve immediately.
"""

# 2. Convert Markdown to HTML
html_body = markdown.markdown(recipe_md)

html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Faux Bone-Reduction Beef Jus</title>
</head>
<body>
    {html_body}
</body>
</html>
"""

# 3. Iterative PDF Generation for Optimal Layout
def generate_documents():
    with open("beefjus.html", "w", encoding="utf-8") as f:
        f.write(html_template)
    sys.stderr.write("Wrote HTML output to beefjus.html\n")

    base_css = """
    @page {
        size: letter portrait;
        margin: 0.75in;
    }
    body {
        font-family: system-ui, -apple-system, sans-serif;
        color: #111;
        line-height: 1.4;
        column-count: 2;
        column-gap: 0.4in;
    }
    h1 {
        column-span: all;
        text-align: center;
        margin-top: 0;
        font-size: 2em;
        border-bottom: 2px solid #000;
        padding-bottom: 10px;
    }
    h2 {
        font-size: 1.3em;
        border-bottom: 1px solid #ccc;
        break-after: avoid;
        margin-top: 1em;
    }
    ul, ol {
        padding-left: 1.2em;
        margin-bottom: 1em;
    }
    li {
        margin-bottom: 0.5em;
        break-inside: avoid;
    }
    strong {
        font-weight: 600;
    }
    """

    font_sizes = [12.0, 11.5, 11.0, 10.5, 10.0, 9.5, 9.0]
    
    html_doc = HTML(string=html_template)
    
    for size in font_sizes:
        dynamic_css = CSS(string=base_css + f"body {{ font-size: {size}pt; }}")
        
        sys.stderr.write(f"Attempting layout with font size {size}pt...\n")
        doc = html_doc.render(stylesheets=[dynamic_css])
        
        if len(doc.pages) == 1:
            sys.stderr.write(f"Success! Document fits on {len(doc.pages)} page(s) at {size}pt.\n")
            doc.write_pdf("beefjus.pdf")
            sys.stderr.write("Wrote PDF output to beefjus.pdf\n")
            return
            
        sys.stderr.write(f"Resulted in {len(doc.pages)} pages. Adjusting...\n")
    
    sys.stderr.write("Could not fit on a single page. Using 10pt as fallback.\n")
    fallback_css = CSS(string=base_css + "body { font-size: 10pt; }")
    doc = html_doc.render(stylesheets=[fallback_css])
    doc.write_pdf("beefjus.pdf")
    sys.stderr.write("Wrote PDF output to beefjus.pdf\n")

if __name__ == "__main__":
    generate_documents()
