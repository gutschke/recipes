import markdown
from weasyprint import HTML

def generate_recipe_pdf(md_file_path, pdf_file_path):
    # Read the Markdown file
    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(md_text, extensions=['tables'])

    # Inject a page break right before the instructions start.
    # This searches for the Phase 1 heading and prepends a CSS break directive.
    html_content = html_content.replace(
        '<h2>Phase 1', 
        '<div style="break-before: page;"></div><h2>Phase 1'
    )

    # High-density, two-column CSS layout 
    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            @page {{
                size: Letter;
                margin: 0.4in;
            }}
            body {{
                font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
                font-size: 9pt;
                line-height: 1.2;
                color: #111;
                column-count: 2;
                column-gap: 0.4in;
            }}
            h1 {{
                font-size: 16pt;
                text-align: center;
                border-bottom: 2px solid #000;
                padding-bottom: 5px;
                margin-top: 0;
                margin-bottom: 15px;
                column-span: all; /* Centers title across both columns */
            }}
            h2 {{
                font-size: 12pt;
                color: #222;
                margin-top: 12px;
                margin-bottom: 6px;
                border-bottom: 1px solid #ccc;
                page-break-after: avoid;
            }}
            h3 {{
                font-size: 10pt;
                margin-top: 10px;
                margin-bottom: 4px;
                color: #333;
                page-break-after: avoid;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 10px;
                font-size: 8.5pt;
                page-break-inside: avoid;
            }}
            th, td {{
                border-bottom: 1px solid #ddd;
                padding: 3px 4px;
                text-align: left;
                vertical-align: top;
            }}
            th {{
                background-color: #f8f9fa;
                font-weight: bold;
                border-bottom: 1px solid #999;
            }}
            ul {{
                margin-top: 0;
                margin-bottom: 10px;
                padding-left: 18px;
            }}
            li {{
                margin-bottom: 4px;
            }}
            p {{
                margin-top: 0;
                margin-bottom: 8px;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # Render and save the PDF
    print("Generating split-page, two-column PDF...")
    HTML(string=styled_html).write_pdf(pdf_file_path)
    print(f"Success! Front-and-back recipe saved to {pdf_file_path}")

if __name__ == "__main__":
    # Hardcoded single-use filenames
    input_markdown = "irishstew.md"
    output_pdf = "irishstew.pdf"
    
    generate_recipe_pdf(input_markdown, output_pdf)
