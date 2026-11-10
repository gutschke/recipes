import sys
import os
from weasyprint import HTML

# Dynamically adopt the executed Python script's name as the base filename
try:
    script_name = os.path.basename(sys.argv[0])
    if not script_name or script_name == "-c":
        script_name = "creamy_tomato_soup_recipe.py"
except IndexError:
    script_name = "creamy_tomato_soup_recipe.py"

base_name = os.path.splitext(script_name)[0]
html_file = f"{base_name}.html"
pdf_file = f"{base_name}.pdf"

def get_html_content(base_font_size):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Creamy Tomato, Carrot, and Ginger Soup</title>
<style>
    @page {{
        size: letter;
        margin: 20mm;
        background-color: #fff9f2;
    }}
    body {{
        margin: 0;
        padding: 0;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #2c2c2c;
        background-color: #fff9f2;
        box-sizing: border-box;
        font-size: {base_font_size}pt;
    }}
    *, *::before, *::after {{
        box-sizing: border-box;
    }}
    .header {{
        margin-bottom: 25px;
    }}
    h1 {{
        color: #8b2500;
        border-bottom: 3px solid #e67300;
        padding-bottom: 8px;
        font-size: 2.4em;
        margin-top: 0;
        margin-bottom: 10px;
    }}
    .intro {{
        font-style: italic;
        font-size: 1em;
        line-height: 1.4;
        color: #555;
    }}
    .recipe-body {{
        display: table;
        width: 100%;
        margin-top: 15px;
    }}
    .col {{
        display: table-cell;
        vertical-align: top;
    }}
    .ingredients-col {{
        width: 35%;
        padding-right: 25px;
        border-right: 1px solid #d4c5b4;
    }}
    .instructions-col {{
        width: 65%;
        padding-left: 25px;
    }}
    h2 {{
        color: #8b2500;
        font-size: 1.5em;
        margin-top: 0;
        margin-bottom: 12px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}
    h3 {{
        color: #e67300;
        font-size: 1.1em;
        margin-top: 15px;
        margin-bottom: 5px;
    }}
    ul {{
        list-style-type: none;
        padding-left: 0;
        margin-top: 0;
        line-height: 1.4;
    }}
    ul li {{
        margin-bottom: 6px;
        position: relative;
        padding-left: 14px;
    }}
    ul li::before {{
        content: "•";
        color: #e67300;
        position: absolute;
        left: 0;
        font-weight: bold;
    }}
    ol {{
        padding-left: 20px;
        margin-top: 0;
        line-height: 1.5;
    }}
    ol li {{
        margin-bottom: 12px;
        padding-left: 5px;
    }}
    ol li::marker {{
        color: #8b2500;
        font-weight: bold;
    }}
    .step-title {{
        font-weight: bold;
        color: #333;
    }}
</style>
</head>
<body>

<div class="header">
    <h1>Creamy Tomato, Carrot, and Ginger Soup</h1>
    <div class="intro">
        This recipe has been developed to deliver a velvety texture with a carefully balanced flavor profile. The natural acidity of the tomatoes is strictly countered by a precise measure of sugar and the inherent sweetness of the carrots, ensuring a rounded, savory finish without sharp or sour notes. Fresh ginger provides a warm, aromatic backbone, while the coconut milk adds a rich, creamy mouthfeel.
    </div>
</div>

<div class="recipe-body">
    <div class="col ingredients-col">
        <h2>Ingredients</h2>
        
        <h3>Soup Base</h3>
        <ul>
            <li>15g Coconut oil (or neutral cooking oil)</li>
            <li>150g Yellow onion, roughly chopped</li>
            <li>200g Carrots, peeled and sliced into thin rounds</li>
            <li>30g Fresh ginger, peeled and minced</li>
            <li>800g Canned whole peeled tomatoes (with juices)</li>
            <li>250ml Vegetable broth or water</li>
            <li>15g Granulated sugar</li>
            <li>10g Kosher salt (adjust to taste)</li>
        </ul>

        <h3>Finishing</h3>
        <ul>
            <li>400ml Full-fat coconut milk, unsweetened</li>
        </ul>
    </div>

    <div class="col instructions-col">
        <h2>Instructions</h2>
        <ol>
            <li><span class="step-title">Prep and Sauté:</span> Place a large, heavy-bottomed pot on a kitchen scale and tare to zero. Weigh the coconut oil directly into the pot. Tare again, and weigh in the onion, carrots, and ginger sequentially. Transfer the pot to the stove and cook over medium heat for 8 to 10 minutes, stirring occasionally, until the onions are completely translucent and the carrots have begun to soften.</li>
            <li><span class="step-title">Simmer:</span> Remove the pot from the heat and place it back on the scale (using a heat-proof trivet). Tare to zero. Weigh in the whole peeled tomatoes, vegetable broth, sugar, and salt. Return the pot to the stove and bring the mixture to a gentle simmer (approximately 90°C / 195°F). Reduce the heat to low, cover, and let simmer for 35 to 40 minutes to fully develop the flavors, break down the acidity of the tomatoes, and ensure the carrots are completely tender.</li>
            <li><span class="step-title">Blend:</span> Remove the pot from the heat. Using an immersion blender directly in the pot, process the soup until it is completely smooth and uniform.</li>
            <li><span class="step-title">Temper and Finish:</span> Before incorporating the coconut milk, it is crucial to temper the mixture to perfectly equalize the differing temperatures and densities. Pour the coconut milk into a separate pouring jug or large measuring cup. Ladle a small amount (approximately 100ml) of the hot, blended soup base into the coconut milk and whisk thoroughly to stabilize it. Pour this stabilized blend back into the main pot of soup.</li>
            <li><span class="step-title">Serve:</span> Stir the soup gently over low heat until just warmed through. Do not allow the soup to boil once the coconut milk has been added. Taste and adjust the salt if necessary before serving.</li>
        </ol>
    </div>
</div>

</body>
</html>"""

best_font_size = 11.0

# Try different base font sizes sequentially to find the optimal 1-page fit
for font_size in [12.0, 11.5, 11.0, 10.8, 10.5, 10.2, 10.0, 9.5]:
    html_str = get_html_content(font_size)
    doc = HTML(string=html_str).render()
    if len(doc.pages) == 1:
        best_font_size = font_size
        print(f"Diagnostics: Successfully fit to 1 page using base font size {font_size}pt.", file=sys.stderr)
        break
else:
    print("Diagnostics: Warning - Could not fit onto 1 page even at minimum readable font size.", file=sys.stderr)
    best_font_size = 9.5

final_html = get_html_content(best_font_size)
with open(html_file, "w", encoding="utf-8") as f:
    f.write(final_html)

HTML(string=final_html).write_pdf(pdf_file)
print(f"Generation complete: {html_file} and {pdf_file} have been saved.")
