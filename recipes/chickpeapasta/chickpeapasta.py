import os
import sys

try:
    import markdown
    from weasyprint import HTML, CSS
    from PyPDF2 import PdfReader
except ImportError as e:
    print(f"Required libraries not available: {e}", file=sys.stderr)
    markdown = None

if markdown:
    md_text = """
# Turmeric & Chickpea Fresh Pasta with Caramelized Turnip and Paneer

**Yield:** 5 portions

## Turmeric-Chickpea Pasta Dough
* **20g** olive oil or ghee
* **5g** ground turmeric
* **300g** '00' or all-purpose flour
* **75g** chickpea flour (besan)
* **4g** fine sea salt
* **205g** whole eggs (approx. 4 large eggs)

## Paneer & Tomato Sugo
* **20g** ghee or olive oil
* **250g** paneer, cut into 1cm cubes
* **185g** purple top turnip, peeled and finely diced
* **3g** whole cumin seeds
* **13g** fresh garlic, minced
* **375g** fresh tomatoes, roughly chopped
* **20g** fresh basil leaves, gently torn
* **6g** fresh cilantro, roughly chopped (optional)
* **75g** starchy pasta water
* Sea salt and black pepper

## Procedure

1. **Bloom the Turmeric:** Place a small butter warmer on your scale and tare. Weigh 20g oil/ghee and 5g turmeric directly into it. Warm gently over low heat just until fragrant and bubbling slightly (about 30 seconds). Remove from heat and let cool. 
2. **Mix Dough:** Place your primary mixing bowl on the scale and tare. Weigh in 300g '00' flour, 75g chickpea flour, and 4g salt. Whisk briefly to distribute.
3. Tare again and add 205g eggs into the center, followed by the cooled turmeric oil. Mix into a shaggy dough.
4. **Knead & Rest:** Knead vigorously on the counter for 8–10 minutes until smooth and elastic. Wrap tightly in plastic and rest at room temperature for at least 30 minutes.
5. **Prep Boiling Water:** Bring a large pot of heavily salted water to a boil.
6. **Sear Paneer & Turnip:** Heat a large, wide skillet over medium-high heat. Add 20g ghee. Fry paneer cubes until golden brown on all sides, then remove and set aside. Add diced turnips to the residual fat and sauté until deeply caramelized (6–8 minutes).
7. **Build Sugo:** Push turnips to the edges. Add 3g cumin seeds to the center for 15 seconds, then 13g minced garlic until fragrant.
8. Add 375g chopped tomatoes, scraping up any fond. Let break down gently over medium-low heat. 
9. **Extrude Pasta:** Sheet the rested dough to a medium-thin setting (e.g., setting 6) and cut into tagliatelle.
10. **Cook Pasta:** Drop pasta into boiling water. Cook for 90 to 120 seconds.
11. **Temper & Combine:** To prevent the starches from clumping, temper the sauce by first ladling 75g (1/3 cup) of hot pasta water into the tomato base and stirring to incorporate. Transfer the cooked pasta directly into the skillet and toss vigorously to emulsify.
12. **Finish:** Fold in the reserved paneer and torn basil. Season to taste with salt and pepper. Garnish with cilantro and serve immediately.
"""

    html_body = markdown.markdown(md_text)
    
    css_template = """
    @page {
        size: Letter;
        margin: 0.5in;
    }
    body {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 11pt;
        line-height: 1.4;
        color: #333;
    }
    h1 {
        font-size: 18pt;
        text-align: center;
        margin-bottom: 0.2in;
        column-span: all;
    }
    h2 {
        font-size: 13pt;
        border-bottom: 1px solid #ccc;
        margin-top: 0.2in;
        padding-bottom: 2px;
        break-after: avoid;
    }
    .content {
        column-count: 2;
        column-gap: 0.4in;
    }
    ul, ol {
        margin-left: 0;
        padding-left: 1.2em;
    }
    li {
        margin-bottom: 0.5em;
    }
    p {
        margin-top: 0.5em;
        margin-bottom: 0.5em;
    }
    """

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>{css_template}</style>
    </head>
    <body>
    <div class="content">
    {html_body}
    </div>
    </body>
    </html>
    """
    
    with open("chickpeapasta.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    html_obj = HTML(string=html_content)
    
    pdf_path = "chickpeapasta.pdf"
    
    for font_size in [12, 11.5, 11, 10.5, 10]:
        current_css = css_template.replace("font-size: 11pt;", f"font-size: {font_size}pt;")
        html_obj.write_pdf(pdf_path, stylesheets=[CSS(string=current_css)])
        
        try:
            reader = PdfReader(pdf_path)
            num_pages = len(reader.pages)
            if num_pages == 1:
                print(f"Success: Fit on 1 page with font size {font_size}pt", file=sys.stderr)
                break
            else:
                print(f"Warning: Document is {num_pages} pages at {font_size}pt. Trying smaller...", file=sys.stderr)
        except Exception as e:
            print(f"Could not verify page count: {e}", file=sys.stderr)
            break
