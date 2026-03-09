import markdown
from weasyprint import HTML, CSS

def generate_recipe_pdf(md_filepath, pdf_filepath):
    """
    Reads a Markdown recipe file and converts it to a single-page, 
    two-column PDF using WeasyPrint.
    """
    # Read the markdown source
    with open(md_filepath, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Convert Markdown to HTML with table extension
    html_body = markdown.markdown(md_text, extensions=['tables'])

    # Wrap in basic HTML structure
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head><title>Recipe</title></head>
    <body>
        {html_body}
    </body>
    </html>
    """

    # Define CSS for a two-column US Letter layout
    css = CSS(string='''
        @page { 
            size: letter; 
            margin: 0.5in; 
        }
        body { 
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; 
            font-size: 10pt; 
            color: #333;
            line-height: 1.3;
            column-count: 2;
            column-gap: 0.4in;
        }
        h1 { 
            font-size: 18pt; 
            text-align: center; 
            margin-bottom: 15px;
            color: #000;
            column-span: all;
        }
        h2 { 
            font-size: 13pt; 
            border-bottom: 1px solid #ccc; 
            padding-bottom: 2px; 
            margin-top: 10px;
            margin-bottom: 5px;
            break-after: avoid;
        }
        p { margin: 5px 0; }
        table { 
            width: 100%; 
            border-collapse: collapse; 
            margin-bottom: 15px; 
            font-size: 9pt;
        }
        th, td { 
            border-bottom: 1px solid #ddd; 
            padding: 4px; 
            text-align: left; 
        }
        th { background-color: #f9f9f9; }
        ul, ol { 
            margin-top: 5px; 
            padding-left: 18px; 
        }
        li { margin-bottom: 4px; }
    ''')

    # Render the PDF
    HTML(string=html_content).write_pdf(pdf_filepath, stylesheets=[css])
    print(f"Successfully generated two-column {pdf_filepath}")

if __name__ == "__main__":
    generate_recipe_pdf('chocolateflan.md', 'chocolateflan.pdf')
