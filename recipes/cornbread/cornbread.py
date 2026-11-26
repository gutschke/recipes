import os
from weasyprint import HTML

basename = "cornbread"
html_file = f"{basename}.html"
pdf_file = f"{basename}.pdf"

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Brown Butter Cast-Iron Cornbread</title>
<style>
    @page {
        size: letter;
        margin: 15mm;
    }
    *, *::before, *::after { box-sizing: border-box; }
    body {
        font-family: 'Georgia', serif;
        font-size: 10.5pt;
        line-height: 1.4;
        color: #222;
        margin: 0;
        padding: 0;
    }
    h1 {
        font-size: 22pt;
        text-align: center;
        border-bottom: 2px solid #444;
        padding-bottom: 8px;
        margin-top: 0;
        margin-bottom: 20px;
    }
    h2 {
        font-size: 13pt;
        color: #333;
        border-bottom: 1px solid #bbb;
        padding-bottom: 2px;
        margin-top: 0;
        margin-bottom: 10px;
        break-after: avoid;
    }
    .container {
        column-count: 2;
        column-gap: 12mm;
    }
    .ingredients-box {
        background-color: #f7f5f2;
        border: 1px solid #e5e0d8;
        padding: 12px;
        margin-bottom: 20px;
        break-inside: avoid;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        font-size: 10pt;
        margin-bottom: 10px;
    }
    th, td {
        padding: 5px 2px;
        text-align: left;
        border-bottom: 1px solid #e5e0d8;
        vertical-align: bottom;
    }
    th {
        font-weight: bold;
        color: #333;
    }
    .instructions-list {
        padding-left: 18px;
        margin: 0;
    }
    .instructions-list li {
        margin-bottom: 12px;
        text-align: justify;
    }
    .ahead-of-time {
        font-weight: bold;
        margin-bottom: 15px;
        padding: 10px;
        border: 1px dashed #bbb;
        background-color: #fafafa;
    }
</style>
</head>
<body>
    <h1>Brown Butter Cast-Iron Cornbread</h1>
    
    <div class="ahead-of-time">
        Ahead-of-Time: Place a cast-iron skillet (10-inch or 12-inch) on the middle rack of the oven. Preheat the oven to 425°F / 220°C. Allow the skillet to heat up along with the oven for at least 30 minutes.
    </div>

    <div class="container">
        <div class="ingredients-box">
            <h2>Ingredients</h2>
            <table>
                <thead>
                    <tr>
                        <th>Ingredient</th>
                        <th>10-inch</th>
                        <th>12-inch</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td colspan="3" style="padding-top: 10px;"><strong>Skillet Preparation</strong></td></tr>
                    <tr><td>Unsalted Butter</td><td>15g</td><td>20g</td></tr>
                    
                    <tr><td colspan="3" style="padding-top: 10px;"><strong>Batter Base (Wet)</strong></td></tr>
                    <tr><td>Unsalted Butter</td><td>120g</td><td>175g</td></tr>
                    <tr><td>Full-fat Buttermilk</td><td>350g</td><td>500g</td></tr>
                    <tr><td>Eggs (cold)</td><td>100g</td><td>150g</td></tr>
                    <tr><td>Honey</td><td>40g</td><td>60g</td></tr>

                    <tr><td colspan="3" style="padding-top: 10px;"><strong>Dry Ingredients</strong></td></tr>
                    <tr><td>Medium-grind Cornmeal</td><td>150g</td><td>215g</td></tr>
                    <tr><td>All-purpose Flour</td><td>140g</td><td>200g</td></tr>
                    <tr><td>Kosher Salt</td><td>5g</td><td>7g</td></tr>
                    <tr><td>Baking Powder</td><td>5g</td><td>7g</td></tr>
                    <tr><td>Baking Soda</td><td>3g</td><td>4g</td></tr>
                </tbody>
            </table>
        </div>

        <div class="instructions">
            <h2>Instructions</h2>
            <ol class="instructions-list">
                <li><strong>Brown the Butter:</strong> In a small saucepan over medium heat, melt the batter base butter. Cook, swirling occasionally, until the bubbling subsides, milk solids toast to dark golden brown, and it smells nutty (5-7 minutes). Remove from heat.</li>
                <li><strong>Scale the Wet Base:</strong> Place the primary mixing bowl on a scale and tare it to zero. Measure in the cold buttermilk, eggs, and honey. Whisk thoroughly until smooth.</li>
                <li><strong>Temper the Butter:</strong> To prevent seizing, begin whisking the buttermilk mixture vigorously. While whisking constantly, slowly stream the hot brown butter into the bowl to equalize the temperatures and create a stable emulsion.</li>
                <li><strong>Incorporate Dry Ingredients:</strong> Place the bowl back onto the scale and tare. Measure the cornmeal, flour, salt, baking powder, and baking soda directly onto the surface of the wet ingredients.</li>
                <li><strong>Fold and Rest:</strong> Using a spatula, gently fold the dry ingredients down into the wet mixture just until no dry streaks remain (lumps are fine). Let the batter rest at room temperature for 10 to 15 minutes to hydrate the cornmeal.</li>
                <li><strong>Sizzle and Initial Bake:</strong> Carefully remove the smoking-hot skillet from the oven. Drop in the reserved skillet butter and swirl to coat. Immediately pour the rested batter into the skillet. Return to the oven and bake at 425°F / 220°C for 7 minutes to set the crust.</li>
                <li><strong>Reduce Heat and Finish:</strong> Without opening the oven door, lower the temperature to 375°F / 190°C. Bake for an additional 13-18 minutes (10-inch) or 18-23 minutes (12-inch), until the top is deeply golden brown and a tester comes out clean. Let cool in the skillet for 10 minutes before slicing.</li>
            </ol>
        </div>
    </div>
</body>
</html>
"""

with open(html_file, "w", encoding="utf-8") as f:
    f.write(html_content)

HTML(filename=html_file).write_pdf(pdf_file)

print(f"Generated {html_file} and {pdf_file}")
