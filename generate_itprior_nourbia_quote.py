import csv
import os
import sys
import base64
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

def encode_img(path):
    if os.path.exists(path):
        with open(path, 'rb') as f:
            ext = os.path.splitext(path)[1].replace('.', '')
            if ext == 'jpg': ext = 'jpeg'
            return f"data:image/{ext};base64,{base64.b64encode(f.read()).decode('utf-8')}"
    return ""

def generate_itprior_quote():
    csv_path = r'c:\Siddhu\Works\Nourbia\Nourbia-Quote.csv'
    output_html = r'c:\Siddhu\Works\Nourbia\Nourbia_Foods_ITPrior_Quote.html'
    output_pdf = r'c:\Siddhu\Works\Nourbia\Nourbia_Foods_ITPrior_Quote.pdf'
    logo_path = r'c:\Siddhu\Works\Nourbia\ITPrior_full_logo_master.png'
    chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    if not os.path.exists(chrome_path):
        chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

    logo_b64 = encode_img(logo_path)

    modules = []
    current_module = None

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if not row or not any(x.strip() for x in row):
                continue
            
            mod_raw = row[0].strip() if len(row) > 0 else ''
            hrs_raw = row[-1].strip() if len(row) > 2 else ''
            task_raw = ', '.join([c.strip() for c in row[1:-1] if c.strip()]) if len(row) > 2 else (row[1].strip() if len(row) > 1 else '')
            
            if mod_raw:
                mod_title = mod_raw
                if mod_title and mod_title[0].isdigit() and '.' in mod_title[:4]:
                    mod_title = mod_title.split('.', 1)[1].strip()
                current_module = {'name': mod_title, 'tasks': [], 'subtotal': 0}
                modules.append(current_module)
            
            if task_raw and hrs_raw and hrs_raw.isdigit():
                if current_module is not None:
                    hrs_val = int(hrs_raw)
                    current_module['tasks'].append((task_raw, hrs_val))
                    current_module['subtotal'] += hrs_val

    total_hours = sum(m['subtotal'] for m in modules)
    hourly_rate = 900
    grand_total_inr = total_hours * hourly_rate
    formatted_total_inr = f"₹{grand_total_inr:,.0f}"

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>ITPrior Quote — Nourbia Foods Custom E-Commerce Platform</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&family=Open+Sans:wght@400;500;600;700&display=swap');

  @page {{
    size: A4;
    margin: 12mm 14mm 12mm 14mm;
  }}

  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }}

  body {{
    font-family: 'Open Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    color: #212529;
    background-color: #ffffff;
    font-size: 8.2pt;
    line-height: 1.35;
  }}

  /* Header */
  .header-wrap {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    padding-top: 2px;
    margin-bottom: 14px;
  }}

  .logo-box img {{
    height: 72px;
    width: auto;
    display: block;
  }}

  /* Title Block */
  .title-block {{
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 14px;
  }}

  .title-accent-bar {{
    width: 50px;
    height: 16px;
    background-color: #6ba5e7;
    border-radius: 1px;
  }}

  .title-text {{
    font-family: 'Montserrat', sans-serif;
    font-size: 15pt;
    font-weight: 800;
    letter-spacing: 0.5px;
    color: #111827;
  }}

  /* Meta Info Grid */
  .meta-grid {{
    display: grid;
    grid-template-columns: 1.3fr 1fr;
    gap: 16px;
    margin-bottom: 14px;
  }}

  .to-block .to-label {{
    font-weight: 700;
    font-size: 9.5pt;
    color: #111827;
    margin-bottom: 2px;
  }}

  .to-block .client-name {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 10pt;
    color: #111827;
    letter-spacing: 0.2px;
  }}

  .to-block .client-sub {{
    font-size: 7.8pt;
    color: #4b5563;
    margin-top: 1px;
  }}

  .invoice-meta {{
    text-align: right;
  }}

  .meta-row {{
    display: flex;
    justify-content: flex-end;
    gap: 14px;
    font-size: 8.5pt;
    margin-bottom: 2px;
  }}

  .meta-row .label {{
    color: #374151;
    font-weight: 600;
  }}

  .meta-row .value {{
    color: #111827;
    font-weight: 700;
    font-family: 'Montserrat', sans-serif;
    min-width: 80px;
    text-align: right;
  }}

  /* Table Style */
  table.quote-table {{
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 12px;
  }}

  table.quote-table thead th {{
    font-family: 'Montserrat', sans-serif;
    font-size: 8pt;
    font-weight: 800;
    color: #111827;
    padding: 6px 5px;
    text-align: left;
    border-top: 2px solid #5b9de6;
    border-bottom: 2px solid #5b9de6;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}

  table.quote-table thead th.th-no {{
    width: 30px;
    text-align: center;
  }}

  table.quote-table thead th.th-hrs {{
    width: 48px;
    text-align: center;
  }}

  table.quote-table thead th.th-price {{
    width: 70px;
    text-align: right;
  }}

  table.quote-table thead th.th-total {{
    width: 85px;
    text-align: right;
  }}

  /* Module Row */
  .mod-row td {{
    padding: 5px 5px 2px 5px;
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    font-size: 8pt;
    color: #111827;
    background-color: #f8fafc;
    border-top: 1px solid #e2e8f0;
    page-break-after: avoid;
  }}

  .mod-row td.mod-no {{
    text-align: center;
    color: #2563eb;
    font-weight: 800;
  }}

  .mod-row td.mod-hrs {{
    text-align: center;
    color: #1e293b;
  }}

  .mod-row td.mod-price {{
    text-align: right;
    color: #4b5563;
    font-weight: 600;
  }}

  .mod-row td.mod-total {{
    text-align: right;
    color: #111827;
    font-weight: 800;
  }}

  /* Task Rows */
  .task-subrow td {{
    padding: 2.2px 5px 2.2px 5px;
    font-size: 7.6pt;
    color: #4b5563;
    border-bottom: 1px solid #f1f5f9;
  }}

  .task-subrow td.task-desc {{
    padding-left: 12px;
  }}

  .task-bullet {{
    color: #6ba5e7;
    font-weight: bold;
    margin-right: 3px;
  }}

  .task-subrow td.task-hrs {{
    text-align: center;
    color: #6b7280;
    font-size: 7.2pt;
  }}

  /* Summary Section */
  .summary-wrap {{
    page-break-inside: avoid;
    margin-top: 10px;
    margin-bottom: 14px;
    display: flex;
    justify-content: flex-end;
  }}

  .summary-box {{
    width: 280px;
  }}

  .summary-line {{
    display: flex;
    justify-content: space-between;
    padding: 3px 0;
    font-size: 8.5pt;
  }}

  .summary-line .sum-label {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    color: #111827;
  }}

  .summary-line .sum-val {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    color: #111827;
  }}

  /* Grand Total Banner */
  .grand-total-banner {{
    background-color: #6ba5e7;
    color: #ffffff;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 7px 10px;
    border-radius: 2px;
    margin-top: 5px;
  }}

  .grand-total-banner .gt-label {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 9.5pt;
    letter-spacing: 0.5px;
    text-transform: uppercase;
  }}

  .grand-total-banner .gt-val {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 10.5pt;
    letter-spacing: 0.2px;
  }}

  /* Payment & Terms Box */
  .details-section {{
    page-break-inside: avoid;
    margin-bottom: 16px;
  }}

  .block-title {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 800;
    font-size: 9pt;
    color: #111827;
    margin-bottom: 3px;
  }}

  .payment-details {{
    font-size: 7.8pt;
    color: #374151;
    line-height: 1.45;
    margin-bottom: 10px;
  }}

  .payment-details strong {{
    color: #111827;
    font-weight: 700;
  }}

  .terms-text {{
    font-size: 7.2pt;
    color: #4b5563;
    line-height: 1.4;
  }}

  /* Footer */
  .footer-container {{
    page-break-inside: avoid;
    margin-top: 12px;
  }}

  .footer-divider {{
    height: 1.5px;
    background-color: #6ba5e7;
    margin-bottom: 8px;
  }}

  .footer-wrap {{
    display: grid;
    grid-template-columns: 1fr 1.2fr 2fr;
    gap: 14px;
    font-size: 7.2pt;
    color: #4b5563;
  }}

  .footer-item {{
    display: flex;
    align-items: flex-start;
    gap: 6px;
  }}

  .footer-icon-svg {{
    width: 15px;
    height: 15px;
    flex-shrink: 0;
    color: #5b9de6;
    margin-top: 1px;
  }}

  .footer-content strong {{
    display: block;
    color: #5b9de6;
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    font-size: 7.8pt;
    margin-bottom: 1px;
  }}
</style>
</head>
<body>

  <!-- Header with Master Logo -->
  <div class="header-wrap">
    <div class="logo-box">
      <img src="{logo_b64}" alt="ITPrior Logo" />
    </div>
  </div>

  <!-- Title Block -->
  <div class="title-block">
    <div class="title-accent-bar"></div>
    <div class="title-text">PROJECT QUOTATION</div>
  </div>

  <!-- Meta Grid -->
  <div class="meta-grid">
    <div class="to-block">
      <div class="to-label">To</div>
      <div class="client-name">NOURBIA FOODS — Custom E-Commerce Project</div>
      <div class="client-sub">Advancing Culturally Relevant Nutrition • Meeting People Where They Are</div>
    </div>
    <div class="invoice-meta">
      <div class="meta-row">
        <span class="label">Quote no :</span>
        <span class="value">00007</span>
      </div>
      <div class="meta-row">
        <span class="label">Date :</span>
        <span class="value">15 Sep 2026</span>
      </div>
    </div>
  </div>

  <!-- Table -->
  <table class="quote-table">
    <thead>
      <tr>
        <th class="th-no">NO</th>
        <th>DESCRIPTION & DELIVERABLES</th>
        <th class="th-hrs">HRS</th>
        <th class="th-price">PRICE</th>
        <th class="th-total">TOTAL</th>
      </tr>
    </thead>
    <tbody>
"""

    for idx, mod in enumerate(modules, start=1):
        mod_cost = mod['subtotal'] * hourly_rate
        html_content += f"""
      <tr class="mod-row">
        <td class="mod-no">{idx}</td>
        <td>{mod['name']}</td>
        <td class="mod-hrs">{mod['subtotal']}</td>
        <td class="mod-price">₹{hourly_rate}</td>
        <td class="mod-total">₹{mod_cost:,.0f}</td>
      </tr>
"""
        for task_name, hrs in mod['tasks']:
            html_content += f"""
      <tr class="task-subrow">
        <td></td>
        <td class="task-desc"><span class="task-bullet">▸</span>{task_name}</td>
        <td class="task-hrs">{hrs} hrs</td>
        <td></td>
        <td></td>
      </tr>
"""

    html_content += f"""
    </tbody>
  </table>

  <!-- Summary Section -->
  <div class="summary-wrap">
    <div class="summary-box">
      <div class="summary-line">
        <span class="sum-label">Total Hours</span>
        <span class="sum-val">{total_hours} HRS</span>
      </div>
      <div class="summary-line">
        <span class="sum-label">Hourly Rate</span>
        <span class="sum-val">₹{hourly_rate} / hr</span>
      </div>
      <div class="summary-line">
        <span class="sum-label">Sub Total</span>
        <span class="sum-val">{formatted_total_inr}</span>
      </div>
      <div class="summary-line">
        <span class="sum-label">Tax 0%</span>
        <span class="sum-val">₹0</span>
      </div>
      <div class="grand-total-banner">
        <span class="gt-label">GRAND TOTAL</span>
        <span class="gt-val">{formatted_total_inr}</span>
      </div>
    </div>
  </div>

  <!-- Details / Payment & Terms -->
  <div class="details-section">
    <div class="block-title">Payment Method</div>
    <div class="payment-details">
      Bank Name : <strong>Axis Bank</strong><br>
      Account Number : <strong>921020028481906</strong><br>
      Account Name: <strong>ITPRIOR INNOVATIONS PRIVATE LIMITED</strong><br>
      Branch: <strong>MVP COLONY, VISAKHAPATNAM [AP]</strong>
    </div>

    <div class="block-title">Term and Conditions :</div>
    <div class="terms-text">
      • Scope includes full-stack custom engineering (Next.js, Python FastAPI, PostgreSQL, Redis), Stripe payments & billing, dynamic box configurator, community taste lab, B2B wholesale portal, surplus farm recovery, and custom admin/customer dashboards.<br>
      • Payments released in milestone tranches upon verified phase deliverables.<br>
      • Full intellectual property, code repository ownership, and documentation handed over upon completion.
    </div>
  </div>

  <!-- Footer Container -->
  <div class="footer-container">
    <div class="footer-divider"></div>
    <div class="footer-wrap">
      <div class="footer-item">
        <svg class="footer-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <rect width="14" height="20" x="5" y="2" rx="2" ry="2"/>
          <path d="M12 18h.01"/>
        </svg>
        <div class="footer-content">
          <strong>Phone</strong>
          9912238386
        </div>
      </div>

      <div class="footer-item">
        <svg class="footer-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <rect width="20" height="16" x="2" y="4" rx="2"/>
          <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>
        </svg>
        <div class="footer-content">
          <strong>Mail</strong>
          info@itprior.com
        </div>
      </div>

      <div class="footer-item">
        <svg class="footer-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/>
          <circle cx="12" cy="10" r="3"/>
        </svg>
        <div class="footer-content">
          <strong>Address</strong>
          H No.50-53- 14, 1st Floor, Harish Roy Nilayam, near NRI Hospital Road, Seethammadara, Visakhapatnam, Andhra Pradesh 530016
        </div>
      </div>
    </div>
  </div>

</body>
</html>
"""

    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"HTML saved to {output_html}")

    cmd = [
        chrome_path,
        '--headless',
        '--disable-gpu',
        '--no-pdf-header-footer',
        f'--print-to-pdf={output_pdf}',
        output_html
    ]
    
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0 and os.path.exists(output_pdf):
        print(f"SUCCESS: Generated PDF at {output_pdf} (Size: {os.path.getsize(output_pdf)} bytes)")
    else:
        print("ERROR rendering PDF:", res.stderr)

if __name__ == '__main__':
    generate_itprior_quote()
