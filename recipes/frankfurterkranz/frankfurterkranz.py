import weasyprint
import markdown
import sys

markdown_content = """# Frankfurter Kranz

## Preparation

* Cook the pudding for the buttercream early to allow it to cool completely to room temperature.
* Take all butter (for both cake and buttercream) out of the fridge early so it matches the pudding's room temperature exactly.
* Preheat oven to 180°C (350°F).
* Grease and flour a 26 cm ring cake pan (Kranzform).

## Ingredients

**Buttercream Pudding Base**

* 450 ml whole milk
* 1 vanilla bean, scraped
* 100 g sugar
* 45 g cornstarch
* 50 ml whole milk
* 2 egg yolks

**Hazelnut Brittle (Krokant)**

* 15 g butter
* 100 g sugar
* 150 g chopped hazelnuts

**Sponge Cake (Sandmasse)**

* 200 g soft butter
* 200 g sugar
* 1 pinch salt
* 4 eggs (approx. 200 g)
* 150 g wheat flour
* 50 g cornstarch
* 8 g baking powder

**Buttercream & Assembly**

* 250 g soft butter
* 200 g red jam (redcurrant or sour cherry)

## Instructions

**Pudding Base & Brittle**

1. Bring 450 ml milk and the scraped vanilla bean to a boil. In a small bowl, whisk 50 ml milk with sugar, cornstarch, and egg yolks until smooth. 
2. Whisk the yolk mixture into the boiling milk, return to a brief boil until the pudding thickens. Transfer to a shallow dish, cover the surface directly with plastic wrap, and let cool completely to room temperature.
3. For the brittle, melt 15 g butter and 100 g sugar in a pan and caramelize to a light brown. Stir in the hazelnuts. Spread the hot mixture onto parchment paper, let cool completely, then crush into small pieces. 

**Sponge Cake**

1. Place a mixing bowl on the scale and tare. Weigh 200 g soft butter, 200 g sugar, and a pinch of salt directly into the bowl. Beat until creamy and pale using a hand mixer.
2. Beat in the eggs, one at a time, until fully incorporated.
3. Tare the scale again. Weigh 150 g flour, 50 g cornstarch, and 8 g baking powder directly onto the wet mixture. Fold in the dry ingredients just until a homogenous batter forms.
4. Pour the batter into the prepared ring pan, smooth the top, and bake for 35–40 minutes. Let rest in the pan for 10 minutes before turning out onto a wire rack to cool completely.

**German Buttercream**

1. Wash the beaters, then whip 250 g soft butter until pale and fluffy. 
2. To prevent the buttercream from breaking, temper the mixture: Add 2–3 tablespoons of the whipped butter to the smoothed room-temperature pudding and whisk vigorously to equalize the temperatures and densities.
3. Whisk this stabilized pudding mixture back into the remaining whipped butter, a spoonful at a time, until a smooth cream forms.

**Assembly**

1. Slice the cooled cake horizontally twice to create three layers. Briefly stir the jam until smooth.
2. Spread the bottom layer with half of the jam and a thin layer of buttercream. 
3. Place the middle layer on top, spread with the remaining jam and another layer of buttercream.
4. Place the top layer on. Frost the entire outside, inside, and top of the cake with the remaining buttercream, reserving a small amount in a piping bag for decoration.
5. Press the crushed hazelnut brittle evenly all over the frosted cake. Finish by piping buttercream rosettes on top.
"""

def generate_recipe_documents():
    html_body = markdown.markdown(markdown_content)
    font_sizes = ["11pt", "10.5pt", "10pt", "9.5pt", "9pt", "8.5pt"]
    
    for size in font_sizes:
        css = f"""
        @page {{
            size: letter;
            margin: 0.75in;
        }}
        body {{
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            font-size: {size};
            line-height: 1.4;
            color: #333;
        }}
        h1 {{
            text-align: center;
            font-size: 1.8em;
            margin-top: 0;
            margin-bottom: 0.5em;
            column-span: all;
        }}
        h2 {{
            font-size: 1.3em;
            border-bottom: 1px solid #ccc;
            padding-bottom: 0.2em;
            margin-top: 1em;
            margin-bottom: 0.5em;
        }}
        h3, p > strong {{
            display: block;
            margin-top: 1em;
            margin-bottom: 0.5em;
        }}
        ul, ol {{
            margin-top: 0;
            padding-left: 1.5em;
        }}
        li {{
            margin-bottom: 0.4em;
        }}
        .content {{
            column-count: 2;
            column-gap: 2em;
        }}
        """
        
        full_html = f"""<!DOCTYPE html>
        <html>
        <head><style>{css}</style></head>
        <body>
            <h1>Frankfurter Kranz</h1>
            <div class="content">{html_body.replace('<h1>Frankfurter Kranz</h1>', '')}</div>
        </body>
        </html>
        """
        
        pdf = weasyprint.HTML(string=full_html).render()
        if len(pdf.pages) == 1:
            sys.stderr.write(f"Success fitting content on 1 page with font size {size}.\n")
            with open("frankfurterkranz.pdf", "wb") as f:
                f.write(pdf.write_pdf())
            with open("frankfurterkranz.html", "w") as f:
                f.write(full_html)
            break
    else:
        sys.stderr.write("Could not fit content on 1 page even with the smallest font size. Saving multi-page PDF.\n")
        with open("frankfurterkranz.pdf", "wb") as f:
            f.write(pdf.write_pdf())
        with open("frankfurterkranz.html", "w") as f:
            f.write(full_html)

if __name__ == "__main__":
    generate_recipe_documents()
