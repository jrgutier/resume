#!/usr/bin/env python3
"""Convert markdown resume to HTML with embedded CSS for PDF printing."""

import re
import sys

def parse_markdown(md_content):
    """Simple markdown to HTML converter."""
    lines = md_content.split('\n')
    html = []
    in_list = False

    for line in lines:
        # Skip frontmatter
        if line.strip() == '---':
            continue
        if line.startswith('css:'):
            continue

        # Headers
        if line.startswith('# '):
            html.append(f'<h1>{line[2:]}</h1>')
        elif line.startswith('## '):
            html.append(f'<h2>{line[3:]}</h2>')
        # Bold text with pipes (job titles)
        elif '**' in line and '|' in line:
            # Convert **text** | **text** | **text** format
            line = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', line)
            html.append(f'<p>{line}</p>')
        # List items
        elif line.startswith('- '):
            if not in_list:
                html.append('<ul>')
                in_list = True
            html.append(f'<li>{line[2:]}</li>')
        else:
            if in_list and line.strip():
                html.append('</ul>')
                in_list = False
            if line.strip():
                # Convert **text** to <strong>
                line = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', line)
                # Convert links [text](url)
                line = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', line)
                # Convert iconify spans
                line = re.sub(r'<span class="iconify"[^>]*></span>', '', line)
                html.append(f'<p>{line}</p>')

    if in_list:
        html.append('</ul>')

    return '\n'.join(html)

def main():
    # Read markdown file
    with open('RESUME.md', 'r') as f:
        md_content = f.read()

    # Read CSS file
    with open('resume.css', 'r') as f:
        css_content = f.read()

    # Convert markdown to HTML
    html_body = parse_markdown(md_content)

    # Create full HTML document
    html_doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>J.R. Gutierrez - Resume</title>
    <style>
{css_content}
    </style>
</head>
<body>
{html_body}
</body>
</html>'''

    # Write HTML file
    with open('RESUME.html', 'w') as f:
        f.write(html_doc)

    print("✅ Created RESUME.html")
    print("\nTo generate PDF:")
    print("1. Open RESUME.html in your browser")
    print("2. Press Ctrl+P (or Cmd+P on Mac)")
    print("3. Select 'Save as PDF' as the destination")
    print("4. Ensure margins are set to 'Default' or 'Minimum'")
    print("5. Save the PDF")

if __name__ == '__main__':
    main()
