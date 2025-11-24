#!/usr/bin/env python3
"""Test that job title lines will fit on one line in the PDF."""

import re

def calculate_line_width(text, font_size_pt):
    """
    Estimate if text will fit on one line.
    Assumptions:
    - Page width: 8.5 inches
    - Margins: 0.75 inches on each side = 7 inches usable
    - Font: Segoe UI (average char width ~0.5em)
    - 1 point = 1/72 inch
    """
    usable_width_inches = 8.5 - (2 * 0.75)  # 7 inches
    usable_width_points = usable_width_inches * 72  # 504 points

    # Average character width in points (rough estimate for Segoe UI)
    avg_char_width = font_size_pt * 0.5

    # Calculate how many characters fit
    max_chars = int(usable_width_points / avg_char_width)

    # Remove HTML tags for length calculation
    text_no_html = re.sub(r'<[^>]+>', '', text)
    actual_length = len(text_no_html)

    return actual_length, max_chars, actual_length <= max_chars

def extract_job_titles(md_file):
    """Extract all job title lines from markdown."""
    with open(md_file, 'r') as f:
        content = f.read()

    # Find all lines with ** | ** | ** pattern (job titles)
    pattern = r'\*\*([^*]+)\*\* \| \*\*([^*]+)\*\* \| \*\*([^*]+)\*\*'
    matches = re.findall(pattern, content)

    job_titles = []
    for match in matches:
        # Reconstruct the full line
        line = f"{match[0]} | {match[1]} | {match[2]}"
        job_titles.append(line)

    return job_titles

def main():
    print("Testing job title line lengths...\n")

    job_titles = extract_job_titles('RESUME.md')

    # Test with different font sizes
    font_sizes = [10.5, 10, 9.5, 9, 8.5]

    for font_size in font_sizes:
        print(f"\n{'='*70}")
        print(f"Font Size: {font_size}pt")
        print(f"{'='*70}")

        all_fit = True
        for i, title in enumerate(job_titles, 1):
            length, max_chars, fits = calculate_line_width(title, font_size)
            status = "✓" if fits else "✗"

            if not fits:
                all_fit = False
                overflow = length - max_chars
                print(f"{status} Job {i}: {length} chars (exceeds by {overflow})")
                print(f"   {title[:80]}...")
            else:
                print(f"{status} Job {i}: {length} chars (fits)")

        if all_fit:
            print(f"\n✓ ALL JOB TITLES FIT at {font_size}pt!")
            print(f"\nRecommended CSS:")
            print(f"  p > strong {{ font-size: {font_size}pt; }}")
            break
    else:
        print("\n✗ Even at 8.5pt, some job titles don't fit!")
        print("  Consider abbreviating company names in markdown.")

if __name__ == '__main__':
    main()
