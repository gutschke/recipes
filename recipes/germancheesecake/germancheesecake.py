import markdown
from weasyprint import HTML

ingredients_md = """
### Crust
* 255g All-purpose flour
* 85g Sugar
* 2g Salt
* 170g Unsalted butter (cold, cubed)
* 8g Vanilla extract

### Filling
* 240g Heavy whipping cream (chilled)
* 170g Unsalted butter (softened)
* 260g Sugar
* 225g Eggs (approx. 4 to 5 large)
* 450g Cream cheese (softened)
* 600g Fage Greek yogurt
* 15g Pure vanilla extract
* 65g Lemon juice (plus zest of 2 lemons)
* 45g Cornstarch
* 2g Salt
"""

instructions_md = """
### Instructions

**1. Ahead of Time**
Preheat the steam oven to 160°C (320°F) with low steam (25-30% humidity). Whip the 240g heavy cream to stiff peaks and chill. 

**2. Crust**
Combine the 255g flour, 85g sugar, and 2g salt. Cut in the 170g cold butter and 8g vanilla until a crumbly dough forms. Press into the bottom and 1 inch up the sides of an 11-inch springform pan. Chill the pan.

**3. Cream the Base**
In your main mixing bowl, cream the 170g softened butter and 260g sugar until pale and fluffy. Add the 225g eggs one at a time, mixing fully after each.

**4. Incorporate the Tang**
Add the 450g cream cheese, 600g yogurt, 15g vanilla, and 65g lemon juice/zest to the butter mixture. Mix until completely smooth.

**5. Dry Ingredients & Fold**
Sift the 45g cornstarch and 2g salt directly over the wet mixture. Whisk gently until no dry spots remain. Temper the textures by thoroughly mixing a scoop of the heavy cream cheese batter into the chilled whipped cream. Gently fold this lightened mixture back into the bulk of the cream cheese batter by hand using a spatula.

**6. Step-Down Bake**
Pour the batter into the chilled crust. Bake at 160°C (320°F) with 25-30% humidity for 40 minutes. Drop the oven temperature to 110°C (230°F), maintaining 25-30% humidity, and bake for an additional 25 to 35 minutes until the center reaches 70°C to 73°C (158°F to 163°F).

**7. Cool and Release**
Turn the oven off, prop the door open, and let cool inside for 60 minutes. Remove and rest for exactly 10 minutes. Run a thin, hot paring knife around the edge to release lateral tension. Cool completely on a wire rack, then refrigerate.
"""

ingredients_html = markdown.markdown(ingredients_md)
instructions_html = markdown.markdown(instructions_md)

full_html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>German-Style Cheesecake (Käsekuchen) - 11 Inch</title>
<style>
    @page {{
        size: letter;
        margin: 0.5in;
    }}
    body {{
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #333;
        line-height: 1.35;
        font-size: 11pt;
    }}
    h1 {{
        text-align: center;
        border-bottom: 2px solid #333;
        padding-bottom: 8px;
        margin-bottom: 15px;
    }}
    h3 {{
        margin-top: 0;
        color: #444;
        border-bottom: 1px solid #ccc;
        padding-bottom: 4px;
        margin-bottom: 8px;
    }}
    .container {{
        display: flex;
        flex-direction: row;
        width: 100%;
    }}
    .ingredients {{
        width: 32%;
        padding-right: 25px;
    }}
    .instructions {{
        width: 68%;
    }}
    ul {{
        padding-left: 20px;
        margin-bottom: 15px;
    }}
    li {{
        margin-bottom: 4px;
    }}
    p {{
        margin-bottom: 10px;
        text-align: justify;
    }}
</style>
</head>
<body>
    <h1>German-Style Cheesecake (Käsekuchen)</h1>
    <div class="container">
        <div class="ingredients">
            {ingredients_html}
        </div>
        <div class="instructions">
            {instructions_html}
        </div>
    </div>
</body>
</html>
"""

with open("germancheesecake.html", "w", encoding="utf-8") as f:
    f.write(full_html)

HTML(string=full_html).write_pdf("germancheesecake.pdf")
