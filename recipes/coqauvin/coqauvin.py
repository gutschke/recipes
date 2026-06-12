import sys
import markdown
from weasyprint import HTML

RECIPE_MD = """
## 1. The Farce & Assembly
* **400g Pork Tenderloin** & **200g Boneless Skinless Chicken Thighs** (finely hand-chopped)
* **60ml Heavy Cream** | **50g Panko Breadcrumbs** | **5g Fresh Thyme** (chopped) | **10g Salt** | **Black Pepper**
* **2 Whole Chickens** (deboned; in marinade of dry red wine, e.g., Burgundy, with onions, carrots, garlic, and peppercorns)

Remove chickens from marinade. Strain the marinade, discarding the spent solid aromatics; reserve the liquid. Tare a mixing bowl on a scale. Add the hand-chopped pork, chicken, cream, panko, thyme, exactly 10g salt, and pepper. Mix vigorously by hand until cohesive. Pan-fry a thumbnail-sized patty to verify seasoning. Pack the farce into the cavities, shaping them to replicate whole birds. Secure the openings tightly using poultry pins.

## 2. Blanch & Stock
* **Reserved Chicken Bones** | **1 Medium Onion** (quartered) | **6 Cloves Garlic** | **Thyme sprigs** | **2 Fresh Bay Leaves**
* **Beef Gelatin** & **Fish Sauce**
* **30g Ghee** (melted) | **Kosher Salt**

Bring water to a rolling boil in your uncovered pressure cooker pot. Plunge the pinned birds into the water for 30 seconds. Remove, air dry briefly, insert a thermometer into the exact center, brush with melted ghee, and generously salt the exterior skin. Pour the scalding water into a heat-proof container and reserve.

Wipe the pressure cooker pot, place back on the stove over medium-high heat, and roast the bones, onion, garlic, thyme, and bay leaves until deeply browned. Deglaze with some of the reserved scalding water. Add a splash of fish sauce, a dash of gelatin, and water to barely cover. Cook at high pressure for 45 mins; natural release.

## 3. Roast the Ballotines
* **1 Fresh Onion** & **1 Fresh Carrot** (thickly sliced)

Preheat oven to 190°C (375°F). Scatter the sliced onion and carrot on a rimmed baking sheet, tossed with a drop of neutral oil. Set a wire rack directly over the vegetables and place the birds on top. Roast for 30 mins, then increase heat to 220°C (430°F). Cook until the thermometer reads exactly 63°C (145°F). Rest uncovered on a board for 15 mins.

## 4. Reduce Marinade & Garnishes
* **Reserved Red Wine Marinade** (~750ml)
* **200g Thick-cut Bacon or Pancetta** (lardons)
* **250g Cremini Mushrooms** (quartered) | **200g Pearl Onions** (peeled)

Bring the strained marinade to a rolling boil, skim foam, and reduce by two-thirds to a syrup. In a Dutch oven, render bacon lardons until crisp; remove. Sauté mushrooms in bacon fat until deeply browned; remove. Sauté pearl onions in the fat for about 20 minutes until blistered, translucent, and tender. Return bacon and mushrooms to the pot.

## 5. Deglaze, Temper & Finish
* **60g Unsalted Butter** (cold, cubed)
* **Cornstarch** (as needed, mixed with cold water)
* **Rice** & **Fresh Vegetables** (for serving)

Strain finished bone broth. Place the baking sheet (with browned veg and drippings) over medium-high heat. Pour in ~250ml hot bone broth, scraping to dissolve the fond. Strain this liquid into the Dutch oven, pressing the vegetables. Discard veg. Add reduced wine syrup to the Dutch oven. Simmer for 5–10 mins. If the combined liquids yield a thin sauce, whisk in a small amount of cornstarch slurry to reach a nappe consistency. 

Off heat, temper cold cubed butter in a small bowl with a ladle of the hot sauce to equalize the temperature, then whisk the stabilized emulsion back into the Dutch oven. Do not boil. Torch rested chickens to blister pale skin. Remove pins, slice, and serve alongside rice and fresh vegetables with the sauce spooned over the top.
"""

def generate_recipe_docs():
    html_content = markdown.markdown(RECIPE_MD)
    
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Coq au Vin Ballotines</title>
        <style>
            @page {{
                size: letter;
                margin: 0.5in;
            }}
            body {{
                font-family: 'Georgia', serif;
                color: #2b2b2b;
                line-height: 1.4;
                margin: 0;
                padding: 0;
                background-color: #ffffff;
            }}
            * {{
                box-sizing: border-box;
            }}
            .header-banner {{
                background-color: #fdfafb;
                border-top: 4px solid #6a1b2a;
                border-bottom: 1px solid #e2d1d5;
                padding: 10px;
                margin-bottom: 15px;
                text-align: center;
            }}
            h1 {{
                font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
                font-size: {title_size}pt;
                color: #6a1b2a;
                margin: 0 0 8px 0;
                text-transform: uppercase;
                letter-spacing: 1px;
            }}
            .meta-box {{
                display: inline-block;
                background: #ffffff;
                border: 1px solid #e2d1d5;
                border-radius: 15px;
                padding: 3px 12px;
                font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
                font-size: {meta_size}pt;
                color: #6a1b2a;
                text-transform: uppercase;
                letter-spacing: 0.5px;
                font-weight: bold;
            }}
            .content-wrapper {{
                column-count: 2;
                column-gap: 0.35in;
                font-size: {base_font_size}pt;
            }}
            h2 {{
                font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
                font-size: {h2_size}pt;
                color: #6a1b2a;
                margin-top: 0;
                margin-bottom: 0.08in;
                border-left: 4px solid #6a1b2a;
                padding-left: 6px;
                page-break-after: avoid;
            }}
            ul {{
                margin-top: 0.04in;
                margin-bottom: 0.08in;
                padding-left: 0.18in;
                list-style-type: square;
            }}
            li {{
                margin-bottom: 0.02in;
            }}
            li strong {{
                color: #4a131d;
            }}
            p {{
                margin-top: 0.04in;
                margin-bottom: 0.1in;
                text-align: justify;
            }}
            .ingredient-highlight {{
                background-color: #fdfafb;
                padding: 6px;
                border-radius: 4px;
                margin-bottom: 8px;
                border: 1px solid #f0e6e8;
            }}
        </style>
    </head>
    <body>
        <div class="header-banner">
            <h1>Deconstructed Coq au Vin Ballotines</h1>
            <div class="meta-box">
                Yield: 4-6 servings &nbsp;&nbsp;|&nbsp;&nbsp; Prep: 60 mins &nbsp;&nbsp;|&nbsp;&nbsp; Cook: 1 hr 45 mins
            </div>
        </div>
        <div class="content-wrapper">
            {recipe_body}
        </div>
    </body>
    </html>
    """

    base_font = 10.5
    title_font = 22.0
    h2_font = 12.0
    meta_font = 9.0
    
    styled_content = html_content.replace('<ul>', '<div class="ingredient-highlight"><ul>').replace('</ul>', '</ul></div>')

    for attempt in range(1, 8):
        css_populated = html_template.format(
            base_font_size=base_font, 
            title_size=title_font, 
            h2_size=h2_font,
            meta_size=meta_font,
            recipe_body=styled_content
        )
        
        doc = HTML(string=css_populated)
        pdf = doc.render()
        num_pages = len(pdf.pages)
        
        if num_pages == 1:
            pdf.write_pdf('coqauvin.pdf')
            with open('coqauvin.html', 'w', encoding='utf-8') as f:
                f.write(css_populated)
            break
        else:
            base_font -= 0.3
            title_font -= 0.5
            h2_font -= 0.3
            meta_font -= 0.2
    else:
        pdf.write_pdf('coqauvin.pdf')
        with open('coqauvin.html', 'w', encoding='utf-8') as f:
            f.write(css_populated)

if __name__ == "__main__":
    generate_recipe_docs()
