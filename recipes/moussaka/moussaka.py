import sys
import pypdf
import weasyprint
import markdown

recipe_md = """
## Ingredients

<div class="ingredients-wrapper">
<div class="ingredients">
<div class="group-title">Vegetable Layers</div>
<ul>
<li>500g Asian eggplants</li>
<li>300g zucchini</li>
<li>600g waxy potatoes (e.g., Yukon Gold)</li>
<li>Extra virgin olive oil (for brushing)</li>
<li>5g salt</li>
</ul>
</div>

<div class="ingredients">
<div class="group-title">Meat Sauce</div>
<ul>
<li>Extra virgin olive oil</li>
<li>150g yellow onion, finely diced</li>
<li>35g tomato paste</li>
<li>2g whole cinnamon (broken pieces)</li>
<li>1g whole cloves</li>
<li>Whole black peppercorns (to taste)</li>
<li>5g sugar</li>
<li>Salt (to taste)</li>
<li>900g ground meat (50% lamb mix)</li>
<li>15g roasted beef base (e.g., Better Than Bouillon)</li>
<li>15g garlic, minced</li>
<li>120ml dry red or white wine</li>
<li>300g fresh tomatoes, grated (discard skins)</li>
<li>3g dried oregano</li>
<li>2g dried spearmint</li>
</ul>
</div>

<div class="ingredients">
<div class="group-title">Béchamel Sauce & Topping</div>
<ul>
<li>100g unsalted butter</li>
<li>100g all-purpose flour</li>
<li>1000ml whole milk, warmed</li>
<li>2 whole eggs</li>
<li>130g Gruyère cheese, grated (divided)</li>
<li>5g roasted garlic base (e.g., Better Than Bouillon)</li>
<li>1g ground nutmeg (a pinch)</li>
<li>Salt (to taste)</li>
<li>200g firm Roma tomatoes, very thinly sliced</li>
<li>30g dry breadcrumbs (or crushed Cretan barley rusks)</li>
</ul>
</div>
</div>

## Instructions

<div class="instructions-wrapper">
<ol class="steps">
<li>Preheat oven to 200°C (390°F) and position two racks in the middle. Line two baking sheets with parchment paper.</li>
<li>Peel the whole potatoes, then steam them for about 20 minutes until just knife-tender. Allow to cool slightly, then slice into 5mm rounds. Trim and slice the Asian eggplants and zucchini lengthwise into 5mm thick slabs.</li>
<li>Place sliced potatoes on one baking sheet and sliced vegetables on the other. Lightly brush both sides of all slices with olive oil and season with the 5g salt. Roast for 25-30 minutes until tender and slightly golden. Remove from oven and reduce temperature to 180°C (355°F).</li>
<li>In a spice grinder, combine the 2g whole cinnamon, 1g whole cloves, black peppercorns, 5g sugar, and a generous pinch of salt. Grind into a fine powder.</li>
<li>Heat a splash of olive oil in a large sauté pan over medium-high heat. Add the diced onion and sauté for 5 minutes until translucent. Stir in the 35g tomato paste and the ground spice mixture. Cook for 1 minute to toast the paste and bloom the spices. Remove this onion mixture from the pan and set aside.</li>
<li>In the same pan, add the 900g ground meat mix and the 15g roasted beef base. Cook, breaking the meat apart, until completely browned. Transfer the meat to a small colander to drain the excess fat, then set aside with the onions.</li>
<li>Leaving just a thin film of fat in the pan, add the minced garlic and roast briefly (about 30 seconds) until fragrant. Deglaze the pan with the 120ml dry wine, scraping up any browned bits. Simmer until the wine has almost entirely evaporated.</li>
<li>Stir in the grated tomatoes. Return the drained meat and onion mixture to the pan. Add the oregano and spearmint. Adjust salt to taste. Simmer uncovered for 10-15 minutes until the sauce is quite thick and almost dry. Remove from heat.</li>
<li>For the béchamel, melt the 100g butter in a medium saucepan over medium heat. Whisk in the 100g flour and cook for 1-2 minutes until lightly toasted.</li>
<li>Gradually whisk the 1000ml warm milk into the roux, stirring continuously until the sauce thickens and gently bubbles (about 5-7 minutes). Remove from heat.</li>
<li>Crack the 2 eggs into a small mixing bowl and whisk well. Temper the eggs by slowly whisking in a ladleful of the hot béchamel mixture to equalize the temperature. Once stabilized, pour the egg mixture back into the main saucepan while whisking vigorously to incorporate.</li>
<li>Stir 100g of the grated Gruyère, the 5g roasted garlic base, the nutmeg, and a pinch of salt into the béchamel until smooth. Set the remaining 30g of cheese aside for the topping.</li>
<li>To assemble, lightly oil a 9x13-inch (23x33cm) baking dish. Arrange the roasted potato slices in an even, overlapping layer on the bottom. Top with an even layer of the roasted eggplant and zucchini slices.</li>
<li>Spread the thick meat sauce evenly over the vegetables.</li>
<li>Pour the béchamel sauce over the top, smoothing it into an even layer.</li>
<li>Arrange the thinly sliced Roma tomatoes across the surface of the béchamel. Sprinkle the 30g breadcrumbs and the reserved 30g grated cheese evenly over the top.</li>
<li>Bake at 180°C (355°F) for 40-45 minutes. The oven heat will roast the tomatoes and toast the breadcrumbs into a crisp, golden crust.</li>
<li>Remove from the oven and let the moussaka rest for at least 45 minutes before slicing to allow the structure to set completely.</li>
</ol>
</div>
"""

def generate_html(font_size, line_height, column_gap):
    css = f'''
    @page {{ size: letter; margin: 0.6in; }}
    body {{ 
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; 
        font-size: {font_size}pt; 
        line-height: {line_height}; 
        color: #2c3327; 
    }}
    h1 {{ text-align: center; font-size: 1.8em; margin-top: 0; margin-bottom: 0.5em; color: #3a4f29; }}
    
    h2 {{ font-size: 1.3em; margin-top: 0; border-bottom: 1.5px solid #a3b19b; padding-bottom: 0.2em; color: #3a4f29; }}
    
    .ingredients-wrapper {{ column-count: 2; column-gap: {column_gap}em; margin-bottom: 1em; }}
    .instructions-wrapper {{ column-count: 2; column-gap: {column_gap}em; }}
    
    .ingredients {{ 
        break-inside: avoid; 
        margin-bottom: 0.8em; 
        background-color: #f6f8f5; 
        border-left: 3px solid #738a58; 
        padding: 0.6em 0.8em; 
        border-radius: 2px;
    }}
    .ingredients ul {{ margin-top: 0.3em; margin-bottom: 0; padding-left: 1.2em; }}
    .steps {{ counter-reset: step; list-style-type: none; padding-left: 0; margin-top: 0.5em; }}
    .steps li {{ counter-increment: step; position: relative; padding-left: 1.6em; margin-bottom: 0.4em; }}
    .steps li::before {{ 
        content: counter(step) "."; 
        position: absolute; 
        left: 0; 
        color: #5d7048; 
        font-weight: 600; 
    }}
    .group-title {{ font-weight: bold; margin-bottom: 0.2em; color: #435a31; }}
    '''
    html_content = f'''<!DOCTYPE html>
    <html>
    <head><meta charset="utf-8"><style>{css}</style></head>
    <body>
        <h1>Cretan-Style Moussaka</h1>
        {markdown.markdown(recipe_md)}
    </body>
    </html>
    '''
    return html_content

font_size = 11.0
line_height = 1.3
column_gap = 2.0

for attempt in range(8):
    html = generate_html(font_size, line_height, column_gap)
    with open("moussaka.html", "w") as f: 
        f.write(html)
    weasyprint.HTML("moussaka.html").write_pdf("moussaka.pdf")
    
    pdf = pypdf.PdfReader("moussaka.pdf")
    num_pages = len(pdf.pages)
    
    text = pdf.pages[0].extract_text()
    is_intact = "Remove from the oven" in text
    
    if num_pages == 1 and is_intact:
        print(f"Success on attempt {attempt+1}: Fits on 1 page (intact) at {font_size}pt.", file=sys.stderr)
        break
    else:
        reason = "spilled to multiple pages" if num_pages > 1 else "Weasyprint silently truncated content"
        print(f"Attempt {attempt+1} failed: {reason} at {font_size}pt. Adjusting layout.", file=sys.stderr)
        font_size -= 0.5
        if attempt > 2:
            line_height -= 0.05
