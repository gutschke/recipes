import markdown
from weasyprint import HTML, CSS
import re

def convert_recipe_to_pdf(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as file:
        md_content = file.read()

    # Remove horizontal rules (---) so they don't interfere with our CSS pagination
    md_content = re.sub(r'^---$', '', md_content, flags=re.MULTILINE)

    html_content = markdown.markdown(md_content)

    # CSS configured to fit page 1, and bundle page 2 and 3 together
    css = CSS(string='''
        @page {
            size: letter;
            margin: 0.4in; /* Margins tightened slightly to fit the chicken instructions */
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            font-size: 9.5pt; /* Slightly smaller font to guarantee page 1 fits */
            line-height: 1.3;
        }
        h1 {
            text-align: center;
            font-size: 14pt;
            border-bottom: 2px solid #000;
            padding-bottom: 6px;
            margin-bottom: 12px;
            margin-top: 0;
        }
        /* Force a page break ONLY before the second h1 (Arroz Verde) */
        h1:nth-of-type(2) {
            page-break-before: always;
        }
        /* Ensure the third h1 (Salad) stays on the same page, but give it breathing room */
        h1:nth-of-type(3) {
            margin-top: 40px;
        }
        h2 {
            font-size: 11pt;
            margin-top: 12px;
            margin-bottom: 6px;
            color: #333;
        }
        /* Two-column layout for lists */
        ul, ol {
            column-count: 2;
            column-gap: 30px;
            margin-top: 0;
            padding-left: 20px;
        }
        li {
            break-inside: avoid-column;
            margin-bottom: 5px;
        }
    ''')

    HTML(string=html_content).write_pdf(output_path, stylesheets=[css])
    print(f"PDF successfully generated at: {output_path}")

if __name__ == "__main__":
    input_file = 'mole.md'
    output_file = 'mole.pdf'
    convert_recipe_to_pdf(input_file, output_file)
