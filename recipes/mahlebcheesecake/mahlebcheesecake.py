#!/usr/bin/env python3
import sys
import os
import markdown
from weasyprint import HTML

def generate_recipe():
    basename = os.path.splitext(os.path.basename(sys.argv[0]))[0]
    if not basename or basename == '<stdin>' or basename == '-':
        basename = 'mahleb_kasekuchen'
        
    html_file = f"{basename}.html"
    pdf_file = f"{basename}.pdf"

    md_content = """
# Mahleb & Cherry Käsekuchen

**Preparation**
* **Oven:** Preheat the steam oven to 160°C (320°F) with low steam (25-30% humidity)[cite: 1].
* **Pan:** 11-inch springform pan[cite: 1].
* **Ahead of Time:** Whip the 240g heavy cream to stiff peaks and chill[cite: 1].

## 1. Crust
| Ingredient | Weight | Baker's % (relative to flour) |
| :--- | :--- | :--- |
| All-purpose flour | 255g | 100.0% |
| Unsalted butter (cold, cubed) | 170g | 66.7% |
| Sugar | 85g | 33.3% |
| Vanilla extract | 8g | 3.1% |
| Salt | 2g | 0.8% |

1. Combine the 255g flour, 85g sugar, and 2g salt[cite: 1]. 
2. Cut in the 170g cold butter and 8g vanilla until a crumbly dough forms[cite: 1]. 
3. Press into the bottom and 1 inch up the sides of an 11-inch springform pan[cite: 1]. 
4. Chill the pan[cite: 1].

## 2. Mahleb Käsekuchen Filling
| Ingredient | Weight | Baker's % (relative to total cheese/yogurt) |
| :--- | :--- | :--- |
| Fage Greek yogurt | 600g | 57.1% |
| Cream cheese (softened) | 450g | 42.9% |
| Sugar | 260g | 24.8% |
| Heavy whipping cream (chilled) | 240g | 22.9% |
| Eggs (approx. 4 to 5 large) | 225g | 21.4% |
| Unsalted butter (softened) | 170g | 16.2% |
| Lemon juice (plus zest of 2 lemons) | 65g | 6.2% |
| Cornstarch | 45g | 4.3% |
| Pure vanilla extract | 15g | 1.4% |
| Ground mahleb | 3g | 0.3% |
| Salt | 2g | 0.2% |

1. **Cream the Base:** In your main mixing bowl, cream the 170g softened butter and 260g sugar until pale and fluffy[cite: 1]. Add the 225g eggs one at a time, mixing fully after each[cite: 1].
2. **Incorporate the Tang & Spice:** Add the 450g cream cheese, 600g yogurt, 15g vanilla, 3g ground mahleb, and 65g lemon juice/zest to the butter mixture. Mix until completely smooth.
3. **Dry Ingredients & Fold:** Sift the 45g cornstarch and 2g salt directly over the wet mixture[cite: 1]. Whisk gently until no dry spots remain[cite: 1]. Temper the textures by thoroughly mixing a scoop of the heavy cream cheese batter into the chilled whipped cream[cite: 1]. Gently fold this lightened mixture back into the bulk of the cream cheese batter by hand using a spatula[cite: 1].
4. **Step-Down Bake:** Pour the batter into the chilled crust[cite: 1]. Bake at 160°C (320°F) with 25-30% humidity for 40 minutes[cite: 1]. Drop the oven temperature to 110°C (230°F) maintaining 25-30% humidity, and bake for an additional 25 to 35 minutes until the center reaches 70°C to 73°C (158°F to 163°F)[cite: 1].
5. **Cool and Release:** Turn the oven off, prop the door open, and let cool inside for 60 minutes[cite: 1]. Remove and rest for exactly 10 minutes[cite: 1]. Run a thin, hot paring knife around the edge to release lateral tension[cite: 1]. Cool completely on a wire rack, then refrigerate[cite: 1].

## 3. Cherry Compote Topping (Choose One)

### Option A: Traditional Sour Cherry
| Ingredient | Weight | Baker's % (relative to cherries) |
| :--- | :--- | :--- |
| Jarred pitted sour cherries (e.g., Marco Polo) | 680g | 100.0% |
| Granulated sugar | 20g | 2.9% |
| Cornstarch | 15g | 2.2% |

1. Drain the sour cherries through a sieve, reserving all the juice. Set the cherries aside.
2. Measure 30g of the cold cherry juice into a small bowl. Add the cornstarch and whisk to create a smooth slurry.
3. Pour the remaining cherry juice and the sugar into a small saucepan. Heat over medium-high until it comes to a simmer.
4. Whisk a few tablespoons of the simmering cherry juice into the cold cornstarch slurry to temper it and equalize the temperatures.
5. Pour the stabilized slurry mixture back into the simmering juice, whisking constantly. Let boil for 1 to 2 minutes until translucent and noticeably thickened.
6. Remove from the heat and fold in the reserved sour cherries. Allow to cool completely before topping the chilled cheesecake.

### Option B: Sweet Cherry & Red Wine
| Ingredient | Weight | Baker's % (relative to cherries) |
| :--- | :--- | :--- |
| Jarred pitted sweet cherries in syrup (e.g., Bada Bing) | 680g | 100.0% |
| Fresh lemon juice | 20g | 2.9% |
| Dry red wine | 15g | 2.2% |
| Cornstarch | 15g | 2.2% |

1. Drain the sweet cherries through a sieve, reserving the heavy syrup. Set the cherries aside.
2. Whisk the 20g lemon juice and 15g red wine into the cold reserved syrup to introduce acidity. 
3. Measure 30g of this soured syrup into a small bowl. Add the cornstarch and whisk to create a smooth slurry.
4. Pour the remaining soured syrup into a small saucepan. Heat over medium-high until it comes to a simmer.
5. Whisk a few tablespoons of the simmering syrup into the cold cornstarch slurry to temper it and equalize the temperatures.
6. Pour the stabilized slurry mixture back into the simmering syrup, whisking constantly. Let boil for 1 to 2 minutes until translucent and noticeably thickened.
7. Remove from the heat and fold in the reserved sweet cherries. Allow to cool completely before topping the chilled cheesecake.
"""

    html_body = markdown.markdown(md_content, extensions=['tables'])

    if "</h1>" in html_body:
        html_body = html_body.replace("</h1>", "</h1>\n<div class='twocol'>", 1) + "\n</div>"
    else:
        html_body = f"<div class='twocol'>\n{html_body}\n</div>"

    # Expanded font sizes down to 7.0pt to accommodate the extra compote text on a single page
    font_sizes = [10.5, 10.0, 9.5, 9.0, 8.5, 8.0, 7.5, 7.0]
    
    for size in font_sizes:
        css_content = f"""
        @page {{
            size: letter;
            margin: 0.5in;
        }}
        body {{
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            font-size: {size}pt;
            line-height: 1.3;
            color: #111;
        }}
        .twocol {{
            column-count: 2;
            column-gap: 0.3in;
        }}
        h1 {{
            font-size: 1.6em;
            text-align: center;
            margin-top: 0;
            border-bottom: 2px solid #111;
            padding-bottom: 0.2em;
            margin-bottom: 0.8em;
        }}
        h2 {{
            font-size: 1.1em;
            margin-top: 1.0em;
            margin-bottom: 0.4em;
            border-bottom: 1px solid #aaa;
            break-after: avoid;
        }}
        h3 {{
            font-size: 1.0em;
            margin-top: 0.8em;
            margin-bottom: 0.3em;
            break-after: avoid;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 0.6em;
        }}
        th, td {{
            text-align: left;
            padding: 0.15em 0;
            border-bottom: 1px solid #eee;
        }}
        p, ul, ol {{
            margin-top: 0;
            margin-bottom: 0.6em;
        }}
        li {{
            margin-bottom: 0.2em;
            break-inside: avoid; 
        }}
        ul, ol {{
            padding-left: 1.2em;
        }}
        strong {{
            color: #000;
        }}
        """
        
        full_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Mahleb & Cherry Käsekuchen</title>
    <style>{css_content}</style>
</head>
<body>
    {html_body}
</body>
</html>
"""
        
        doc = HTML(string=full_html).render()
        
        print(f"Testing font size {size}pt... Layout yielded {len(doc.pages)} page(s).", file=sys.stderr)

        if len(doc.pages) == 1 or size == font_sizes[-1]:
            if len(doc.pages) > 1:
                print(f"Warning: Document spans {len(doc.pages)} pages even at minimum font size ({size}pt).", file=sys.stderr)
            else:
                print(f"Layout optimization successful: Content fits perfectly on 1 page using {size}pt font size.", file=sys.stderr)
            
            doc.write_pdf(pdf_file)
            
            with open(html_file, "w", encoding="utf-8") as f:
                f.write(full_html)
                
            print(f"Artifacts successfully written to {pdf_file} and {html_file}", file=sys.stderr)
            break

if __name__ == "__main__":
    generate_recipe()