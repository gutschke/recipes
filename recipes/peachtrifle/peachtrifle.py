import sys
from weasyprint import HTML

font_sizes = ["11pt", "10.5pt", "10pt", "9.5pt", "9pt"]
line_heights = ["1.4", "1.35", "1.3", "1.25", "1.2"]

success = False
for fs, lh in zip(font_sizes, line_heights):
    css = f"""
    *, *::before, *::after {{ box-sizing: border-box; }}
    @page {{
        size: letter;
        margin: 12mm 12mm;
        background-color: #faf8f5;
    }}
    body {{
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: {fs};
        line-height: {lh};
        background-color: #faf8f5;
        margin: 0; padding: 0;
        color: #333;
    }}
    .container {{
        display: table;
        width: 100%;
    }}
    .col {{
        display: table-cell;
        width: 50%;
        vertical-align: top;
        padding: 0 15px;
    }}
    h1 {{
        font-size: 1.8em;
        margin-top: 10px;
        margin-bottom: 5px;
        text-align: center;
        color: #2c3e50;
    }}
    h2 {{
        font-size: 1.3em;
        margin-top: 15px;
        margin-bottom: 5px;
        border-bottom: 1px solid #ccc;
        color: #2980b9;
        page-break-after: avoid;
    }}
    h3 {{
        font-size: 1.1em;
        margin-top: 12px;
        margin-bottom: 3px;
        color: #34495e;
        page-break-after: avoid;
    }}
    p, ul, ol {{
        margin-top: 5px;
        margin-bottom: 8px;
    }}
    ul, ol {{
        padding-left: 20px;
    }}
    li {{
        margin-bottom: 4px;
    }}
    .meta {{
        text-align: center;
        font-style: italic;
        color: #7f8c8d;
        margin-bottom: 15px;
    }}
    .step-title {{
        font-weight: bold;
    }}
    .ingredient-group {{
        margin-bottom: 10px;
        page-break-inside: avoid;
    }}
    .instruction-step {{
        margin-bottom: 8px;
        page-break-inside: avoid;
    }}
    """
    
    html_content = f"""<!DOCTYPE html>
    <html>
    <head><style>{css}</style></head>
    <body>
    <h1>Broiled Peach & Mascarpone Diplomat Trifle</h1>
    <div class="meta">Yield: 6-8 portions (in Martini glasses) | Active Time: 45 minutes | Chill Time: 3 hours</div>
    
    <div class="container">
        <div class="col">
            <h2>Ingredients</h2>
            
            <div class="ingredient-group">
                <h3>Pastry Cream Base (Make First)</h3>
                <ul>
                    <li>250g whole milk</li>
                    <li>5g vanilla extract</li>
                    <li>3 large egg yolks (~55g)</li>
                    <li>50g granulated sugar</li>
                    <li>20g cornstarch</li>
                    <li>Pinch of kosher salt</li>
                </ul>
            </div>

            <div class="ingredient-group">
                <h3>Broiled Peaches & Soak</h3>
                <ul>
                    <li>600g fresh peaches (about 4-5), pitted and sliced into thick wedges</li>
                    <li>30g honey (for broiling)</li>
                    <li>10g water</li>
                    <li>1 dash Cointreau</li>
                    <li>3 dashes cardamom bitters</li>
                    <li>1.6g crystallized orange (e.g., True Orange, ~2 packets)</li>
                </ul>
            </div>

            <div class="ingredient-group">
                <h3>Mascarpone Whip</h3>
                <ul>
                    <li>250g mascarpone, cold</li>
                    <li>150g heavy cream, cold</li>
                    <li>50g greek yogurt</li>
                </ul>
            </div>

            <div class="ingredient-group">
                <h3>Assembly</h3>
                <ul>
                    <li>200g commercial ladyfingers (savoiardi)</li>
                    <li>60g raspberry or mango puree</li>
                    <li>2 pinches fennel pollen</li>
                    <li>Honey for garnish</li>
                </ul>
            </div>
        </div>
        
        <div class="col">
            <h2>Instructions</h2>
            <ol>
                <li class="instruction-step"><span class="step-title">Prep:</span> Preheat the broiler. Prepare an ice bath in a large bowl.</li>
                
                <li class="instruction-step"><span class="step-title">Cook the Pastry Cream Base:</span> In a medium saucepan, bring the 250g milk and 5g vanilla to a bare simmer. Meanwhile, place a bowl on your scale, tare it, and measure in the 3 egg yolks, 50g sugar, 20g cornstarch, and salt. Whisk until pale. Temper the egg mixture by slowly streaming in half of the hot milk while whisking vigorously. Pour the stabilized mixture back into the saucepan and cook over medium heat, whisking constantly, until it bubbles and thickens significantly (about 2 minutes).</li>
                
                <li class="instruction-step"><span class="step-title">Cool the Base:</span> Immediately transfer the hot pastry cream to a bowl and set it inside the prepared ice bath. Press plastic wrap or parchment paper directly against the surface of the cream. Transfer the bowl to the refrigerator for 20&ndash;30 minutes until completely cold.</li>
                
                <li class="instruction-step"><span class="step-title">Broil the Peaches:</span> Toss the 600g peach wedges with the 30g honey. Spread in a single layer on a parchment-lined baking sheet. Place under the broiler until softened and slightly charred at the edges (watch closely to prevent burning). Transfer the peaches to a cutting board and cut into bite-size pieces. Scrape all the exuded juices and caramelized honey from the pan into a small bowl for the soaking liquid.</li>
                
                <li class="instruction-step"><span class="step-title">Build the Soaking Liquid:</span> To the bowl of warm peach juices, whisk in the 10g water, Cointreau, cardamom bitters, and 1.6g orange crystals until dissolved.</li>
                
                <li class="instruction-step"><span class="step-title">Prep the Ladyfingers:</span> Working quickly, give each ladyfinger a rapid 1-second dip in the soaking liquid. Arrange the dipped ladyfingers at the bottom of 6-8 Martini glasses. <strong>Reserve any remaining soaking liquid.</strong></li>

                <li class="instruction-step"><span class="step-title">Whip the Mascarpone:</span> Place your final mixing bowl on the scale and tare. Add the 250g mascarpone, 150g heavy cream, and 50g greek yogurt directly into the bowl. Whip until medium-stiff peaks form. Do not over-whip.</li>
                
                <li class="instruction-step"><span class="step-title">Form the Diplomat Cream:</span> Once the pastry cream is entirely cold and firm, whisk it vigorously to loosen it up. Whisk in the reserved soaking liquid. First, temper the dense pastry cream by folding in one-third of the lighter mascarpone whip until homogenous. Then, gently fold this stabilized blend back into the remaining mascarpone mixture until just combined.</li>
                
                <li class="instruction-step"><span class="step-title">Assemble and Chill:</span> Drizzle the raspberry puree over the ladyfingers in the glasses. Layer the diplomat cream and the bite-size broiled peaches. Warm the garnishing honey briefly in the microwave to thin it, then finish each glass with a delicate honey drizzle and a dusting of fennel pollen. Chill for at least 2 hours.</li>
            </ol>
        </div>
    </div>
    </body>
    </html>
    """
    
    doc = HTML(string=html_content).render()
    pages = len(doc.pages)
    
    if pages == 1:
        print(f"Layout successful: Fit on 1 page with font size {fs} and line height {lh}.", file=sys.stderr)
        doc.write_pdf('peachtrifle.pdf')
        with open('peachtrifle.html', 'w') as f:
            f.write(html_content)
        success = True
        break
    else:
        print(f"Layout iteration: Rendered {pages} pages with font size {fs}. Shrinking...", file=sys.stderr)

if not success:
    print("Warning: Exhausted adjustment options. Falling back to smallest font settings.", file=sys.stderr)
    doc.write_pdf('peachtrifle.pdf')
    with open('peachtrifle.html', 'w') as f:
         f.write(html_content)
