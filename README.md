# J.R. Gutierrez - Resume

Professional resume for Product Security Engineer positions.

## Files

- `RESUME.md` - Markdown source file
- `resume.css` - Styling for professional two-page layout
- `RESUME.html` - HTML version with embedded CSS
- `JR_Gutierrez_Resume.pdf` - Auto-generated PDF (via GitHub Actions)
- `convert_to_html.py` - Python script to convert Markdown to HTML

## Automatic PDF Generation

This repository uses GitHub Actions to automatically generate a PDF whenever you push changes to:
- `RESUME.md`
- `resume.css`
- `.github/workflows/build-resume.yml`

The workflow:
1. Converts Markdown to HTML with embedded CSS
2. Generates PDF using wkhtmltopdf
3. Commits the PDF back to the repository
4. Makes the PDF available as a downloadable artifact

## Manual PDF Generation

### Option 1: Browser (Recommended)
1. Open `RESUME.html` in Chrome, Firefox, or Edge
2. Press `Ctrl+P` (or `Cmd+P` on Mac)
3. Select "Save as PDF"
4. Ensure margins are set to "Default"
5. Save

### Option 2: Command Line
```bash
# Regenerate HTML from Markdown
python3 convert_to_html.py

# Convert HTML to PDF using wkhtmltopdf
wkhtmltopdf \
  --page-size Letter \
  --margin-top 0.6in \
  --margin-right 0.75in \
  --margin-bottom 0.6in \
  --margin-left 0.75in \
  --enable-local-file-access \
  RESUME.html \
  JR_Gutierrez_Resume.pdf
```

## Editing

1. Edit `RESUME.md` to update content
2. Edit `resume.css` to adjust styling
3. Commit and push - PDF will be auto-generated
4. Or run `python3 convert_to_html.py` locally to preview

## Layout

The resume is designed as a professional two-page layout with:
- Clean typography (Segoe UI font family)
- Professional color scheme (blue accents: #2c5282)
- Comfortable spacing and readability
- Print-optimized margins and page breaks
