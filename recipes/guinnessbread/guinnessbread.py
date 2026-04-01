import markdown
from weasyprint import HTML

def main():
    with open('guinnessbread.md', 'r', encoding='utf-8') as f:
        md_text = f.read()

    html_body = markdown.markdown(md_text)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Guinness Muesli Bread</title>
    <style>
        @page {{
            size: letter;
            margin: 0.75in;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            font-size: 10.5pt;
            line-height: 1.5;
            color: #111;
        }}
        h1 {{
            font-size: 22pt;
            text-align: center;
            margin: 0 0 0.8rem 0;
            border-bottom: 2px solid #222;
            padding-bottom: 0.3rem;
        }}
        .content-wrapper {{
            column-count: 2;
            column-gap: 2.2rem;
        }}
        p > strong {{
            display: block;
            font-size: 10.5pt;
            margin: 1rem 0 0 0;
            color: #222;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}
        p {{
            margin-top: 0;
            margin-bottom: 0.2rem;
        }}
        h4 {{
            font-size: 12pt;
            margin: 0 0 0.5rem 0;
            border-bottom: 1px solid #ddd;
            padding-bottom: 0.2rem;
            color: #333;
            text-transform: uppercase;
        }}
        ul {{
            list-style-type: none;
            padding-left: 0;
            margin: 0 0 1rem 0;
        }}
        ul li {{
            margin-bottom: 0.15rem;
        }}
        ol {{
            padding-left: 1.4rem;
            margin: 0.3rem 0;
        }}
        ol li {{
            margin-bottom: 0.5rem;
        }}
        hr {{
            border: 0;
            border-top: 1px solid #bbb;
            margin: 0.8rem 0;
        }}
    </style>
</head>
<body>
    <h1>Guinness Muesli Bread</h1>
    <div class="content-wrapper">
        {html_body}
    </div>
</body>
</html>
"""

    with open('guinnessbread.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

    HTML(string=html_content).write_pdf('guinnessbread.pdf')

if __name__ == '__main__':
    main()
