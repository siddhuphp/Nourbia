"""
ITPrior Solutions — High-Quality Q&A Document PDF Generator
Converts QandA.md into a beautifully styled HTML & compiles to PDF using headless Chrome.
"""

import os
import sys
import base64
import subprocess
import re
import markdown

sys.stdout.reconfigure(encoding='utf-8')

QANDA_MD_PATH = r"c:\Siddhu\Works\Nourbia\QandA.md"
LOGO_PATH = r"c:\Siddhu\Works\Nourbia\ITPrior_full_logo_master.png"
OUTPUT_HTML_PATH = r"c:\Siddhu\Works\Nourbia\Nourbia_Foods_ITPrior_QandA.html"
OUTPUT_PDF_PATH = r"c:\Siddhu\Works\Nourbia\Nourbia_Foods_ITPrior_QandA.pdf"


def encode_image_base64(image_path: str) -> str:
    if os.path.exists(image_path):
        with open(image_path, 'rb') as f:
            ext = os.path.splitext(image_path)[1].replace('.', '').lower()
            if ext == 'jpg':
                ext = 'jpeg'
            return f"data:image/{ext};base64,{base64.b64encode(f.read()).decode('utf-8')}"
    return ""


def find_chrome_executable() -> str:
    standard_paths = [
        r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
        os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe'),
        os.path.expandvars(r'%PROGRAMFILES%\Google\Chrome\Application\chrome.exe'),
    ]
    for p in standard_paths:
        if os.path.exists(p):
            return p
    return 'chrome'


def build_styled_html(md_text: str, logo_base64: str) -> str:
    # Convert markdown to html using extensions
    html_body = markdown.markdown(
        md_text,
        extensions=[
            'tables',
            'fenced_code',
            'sane_lists',
            'toc'
        ]
    )

    # Wrap h2 sections into article cards for page break control and clean visual boxing
    # Replace <h2> with closing div if not first, and opening div
    sections = re.split(r'(<h2>.*?</h2>)', html_body)
    processed_body = ""
    
    in_section = False
    for part in sections:
        if part.startswith('<h2>'):
            if in_section:
                processed_body += "</div>\n"  # close previous section card
            processed_body += "<div class='qa-section-card'>\n" + part
            in_section = True
        else:
            processed_body += part
            
    if in_section:
        processed_body += "</div>\n"

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>NOURBIA FOODS™ — Technical & Commercial Q&A Document</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
    @page {{
        size: A4 portrait;
        margin: 16mm 14mm 16mm 14mm;
    }}

    *, *::before, *::after {{
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }}

    body {{
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        color: #1e293b;
        background-color: #ffffff;
        font-size: 13px;
        line-height: 1.6;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
    }}

    .container {{
        max-width: 100%;
        margin: 0 auto;
    }}

    /* Header Banner */
    .header-banner {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 2px solid #0284c7;
        padding-bottom: 12px;
        margin-bottom: 20px;
    }}

    .header-left {{
        display: flex;
        align-items: center;
        gap: 14px;
    }}

    .header-logo {{
        height: 44px;
        width: auto;
        object-fit: contain;
    }}

    .header-right {{
        text-align: right;
        font-size: 11px;
        color: #64748b;
        line-height: 1.4;
    }}

    .header-right strong {{
        color: #0f172a;
        font-size: 12px;
    }}

    /* Document Title Cover Area */
    .doc-hero {{
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #ffffff;
        padding: 22px 24px;
        border-radius: 8px;
        margin-bottom: 22px;
        border-left: 6px solid #0284c7;
    }}

    .doc-hero h1 {{
        font-size: 22px;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 6px;
        letter-spacing: -0.3px;
    }}

    .doc-hero .subtitle {{
        font-size: 14px;
        font-weight: 600;
        color: #38bdf8;
        margin-bottom: 8px;
    }}

    .doc-hero .meta-info {{
        font-size: 11.5px;
        color: #94a3b8;
        display: flex;
        flex-wrap: wrap;
        gap: 16px;
        margin-top: 10px;
        padding-top: 10px;
        border-top: 1px solid rgba(255, 255, 255, 0.12);
    }}

    .doc-hero .meta-badge {{
        background: rgba(2, 132, 199, 0.25);
        color: #7dd3fc;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 11px;
        font-weight: 500;
        border: 1px solid rgba(56, 189, 248, 0.3);
    }}

    /* TOC Section */
    .toc-card {{
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 6px;
        padding: 16px 20px;
        margin-bottom: 24px;
        page-break-after: always;
    }}

    .toc-card h2 {{
        font-size: 15px;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 12px;
        border-bottom: 1px solid #cbd5e1;
        padding-bottom: 6px;
    }}

    .toc-card ol, .toc-card ul {{
        columns: 2;
        column-gap: 24px;
        padding-left: 20px;
        font-size: 12px;
    }}

    .toc-card li {{
        margin-bottom: 6px;
        color: #334155;
    }}

    .toc-card a {{
        color: #0284c7;
        text-decoration: none;
        font-weight: 500;
    }}

    /* Q&A Section Cards */
    .qa-section-card {{
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 6px;
        padding: 18px 20px;
        margin-bottom: 20px;
        page-break-inside: avoid;
        box-shadow: 0 1px 3px rgba(0,0,0,0.03);
    }}

    h2 {{
        font-size: 15px;
        font-weight: 700;
        color: #0f172a;
        margin-top: 0;
        margin-bottom: 12px;
        padding-bottom: 6px;
        border-bottom: 2px solid #e2e8f0;
        display: flex;
        align-items: center;
        gap: 8px;
    }}

    h3 {{
        font-size: 13px;
        font-weight: 700;
        color: #0369a1;
        margin-top: 14px;
        margin-bottom: 6px;
        text-transform: uppercase;
        letter-spacing: 0.4px;
    }}

    h4 {{
        font-size: 12.5px;
        font-weight: 600;
        color: #1e293b;
        margin-top: 12px;
        margin-bottom: 6px;
    }}

    p {{
        margin-bottom: 10px;
        color: #334155;
    }}

    /* Question Callouts */
    blockquote {{
        background: #f0f9ff;
        border-left: 4px solid #0284c7;
        padding: 10px 14px;
        margin: 8px 0 14px 0;
        border-radius: 0 6px 6px 0;
        font-size: 12.5px;
        font-weight: 500;
        color: #0c4a6e;
    }}

    blockquote p {{
        margin-bottom: 0;
        color: #0369a1;
        font-style: italic;
    }}

    /* Lists */
    ul, ol {{
        margin-bottom: 12px;
        padding-left: 20px;
    }}

    li {{
        margin-bottom: 4px;
        color: #334155;
    }}

    li strong {{
        color: #0f172a;
    }}

    /* Tables & ASCII diagrams */
    pre {{
        background: #0f172a;
        color: #e2e8f0;
        font-family: 'JetBrains Mono', Consolas, monospace;
        font-size: 10.5px;
        line-height: 1.45;
        padding: 12px 14px;
        border-radius: 6px;
        overflow-x: auto;
        margin: 12px 0;
        border: 1px solid #1e293b;
        page-break-inside: avoid;
    }}

    code {{
        font-family: 'JetBrains Mono', Consolas, monospace;
        font-size: 11px;
        background: #f1f5f9;
        color: #0369a1;
        padding: 1px 4px;
        border-radius: 3px;
        border: 1px solid #e2e8f0;
    }}

    pre code {{
        background: transparent;
        color: inherit;
        padding: 0;
        border: none;
    }}

    table {{
        width: 100%;
        border-collapse: collapse;
        margin: 12px 0;
        font-size: 11.5px;
        page-break-inside: avoid;
    }}

    th, td {{
        border: 1px solid #cbd5e1;
        padding: 6px 10px;
        text-align: left;
    }}

    th {{
        background-color: #f1f5f9;
        font-weight: 700;
        color: #0f172a;
    }}

    tr:nth-child(even) td {{
        background-color: #f8fafc;
    }}

    hr {{
        border: none;
        border-top: 1px solid #e2e8f0;
        margin: 16px 0;
    }}

    /* Footer */
    .doc-footer {{
        border-top: 1px solid #cbd5e1;
        padding-top: 12px;
        margin-top: 24px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 10.5px;
        color: #64748b;
        page-break-inside: avoid;
    }}

    .doc-footer strong {{
        color: #0f172a;
    }}
</style>
</head>
<body>

<div class="container">
    <!-- Header Banner -->
    <div class="header-banner">
        <div class="header-left">
            {'<img src="' + logo_base64 + '" class="header-logo" alt="ITPrior Solutions" />' if logo_base64 else '<strong style="font-size: 16px; color: #0284c7;">ITPrior Solutions</strong>'}
        </div>
        <div class="header-right">
            <strong>ITPrior Solutions</strong> • Engineering Agency<br>
            Email: <a href="mailto:info@itprior.com" style="color:#0284c7; text-decoration:none;">info@itprior.com</a> | Web: <a href="https://www.itprior.com" style="color:#0284c7; text-decoration:none;">www.itprior.com</a>
        </div>
    </div>

    <!-- Document Hero / Header -->
    <div class="doc-hero">
        <h1>NOURBIA FOODS™ — Technical & Commercial Q&A Document</h1>
        <div class="subtitle">Custom E-Commerce Platform Architecture & Operations Guide</div>
        <div class="meta-info">
            <span><strong>Client:</strong> Nourbia Foods Team</span>
            <span><strong>Prepared By:</strong> ITPrior Solutions</span>
            <span><strong>Architecture:</strong> Next.js 15 • FastAPI • PostgreSQL (100% Custom)</span>
            <span class="meta-badge">Reference Model: Harvest Right (harvestright.com)</span>
        </div>
    </div>

    <!-- Body Content -->
    <div class="content-wrapper">
        {processed_body}
    </div>

    <!-- Footer -->
    <div class="doc-footer">
        <div>
            <strong>ITPrior Solutions</strong> — Proprietary & Confidential Technical Proposal Document
        </div>
        <div>
            Client: <strong>Nourbia Foods Inc.</strong> | Scope: <strong>14 Modules ($6,000 USD)</strong>
        </div>
    </div>
</div>

</body>
</html>
"""
    return full_html


def main():
    print(f"Reading markdown from: {QANDA_MD_PATH}")
    if not os.path.exists(QANDA_MD_PATH):
        print(f"Error: {QANDA_MD_PATH} not found!")
        sys.exit(1)

    with open(QANDA_MD_PATH, 'r', encoding='utf-8') as f:
        md_text = f.read()

    logo_b64 = encode_image_base64(LOGO_PATH)
    html_content = build_styled_html(md_text, logo_b64)

    print(f"Writing HTML to: {OUTPUT_HTML_PATH}")
    with open(OUTPUT_HTML_PATH, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("✓ HTML generated successfully.")

    chrome_exe = find_chrome_executable()
    print(f"Compiling PDF using Chrome executable: {chrome_exe}")

    cmd = [
        chrome_exe,
        '--headless',
        '--disable-gpu',
        '--no-sandbox',
        '--run-all-compositor-stages-before-draw',
        f'--print-to-pdf={OUTPUT_PDF_PATH}',
        '--no-pdf-header-footer',
        OUTPUT_HTML_PATH
    ]

    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0 and os.path.exists(OUTPUT_PDF_PATH):
        print(f"✓ PDF generated successfully at: {OUTPUT_PDF_PATH} ({os.path.getsize(OUTPUT_PDF_PATH):,} bytes)")
    else:
        print(f"Error compiling PDF: {res.stderr}")
        sys.exit(1)


if __name__ == '__main__':
    main()
