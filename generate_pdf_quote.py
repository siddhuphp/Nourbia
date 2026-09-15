import csv
import os
import subprocess

def generate_pdf():
    csv_path = r'c:\Siddhu\Works\Nourbia\Nourbia-Quote.csv'
    output_html = r'c:\Siddhu\Works\Nourbia\Nourbia_Foods_Project_Quote.html'
    output_pdf = r'c:\Siddhu\Works\Nourbia\Nourbia_Foods_Project_Quote.pdf'
    chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    if not os.path.exists(chrome_path):
        chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

    modules = []
    current_module = None

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if not row or not any(x.strip() for x in row):
                continue
            mod = row[0].strip() if len(row) > 0 else ''
            task = row[1].strip() if len(row) > 1 else ''
            hrs = row[2].strip() if len(row) > 2 else ''
            
            if mod:
                current_module = {'name': mod, 'tasks': [], 'subtotal': 0}
                modules.append(current_module)
            if task and hrs and hrs.isdigit():
                if current_module:
                    current_module['tasks'].append((task, int(hrs)))
                    current_module['subtotal'] += int(hrs)

    total_hours = sum(m['subtotal'] for m in modules)

    # Build sleek HTML with modern typography & print CSS
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Nourbia Foods — Project Scope & Quotation</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap');

  @page {{
    size: letter;
    margin: 14mm 14mm 16mm 14mm;
    @bottom-right {{
      content: "Page " counter(page) " of " counter(pages);
      font-size: 8pt;
      color: #718096;
      font-family: 'Plus Jakarta Sans', sans-serif;
    }}
  }}

  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }}

  body {{
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    color: #1a202c;
    background-color: #ffffff;
    font-size: 9.5pt;
    line-height: 1.45;
  }}

  /* Header Section */
  .header-card {{
    background: linear-gradient(135deg, #18382b 0%, #0d231a 100%);
    color: #ffffff;
    padding: 24px 28px;
    border-radius: 12px;
    margin-bottom: 20px;
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    box-shadow: 0 4px 20px rgba(13, 35, 26, 0.15);
  }}

  .brand-title {{
    font-family: 'Space+Grotesk', sans-serif;
    font-size: 22pt;
    font-weight: 700;
    letter-spacing: -0.5px;
    color: #f7fafc;
    display: flex;
    align-items: center;
    gap: 8px;
  }}

  .brand-title span {{
    color: #e2a84b;
    font-size: 14pt;
    font-weight: 600;
  }}

  .tagline {{
    font-size: 9.5pt;
    color: #cbd5e0;
    margin-top: 4px;
    font-weight: 400;
    letter-spacing: 0.2px;
  }}

  .doc-meta {{
    text-align: right;
    font-size: 8.5pt;
    color: #e2e8f0;
  }}

  .doc-badge {{
    display: inline-block;
    background: rgba(226, 168, 75, 0.2);
    border: 1px solid #e2a84b;
    color: #f6ad55;
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 20px;
    font-size: 8pt;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    margin-bottom: 8px;
  }}

  /* Executive Summary Box */
  .exec-summary {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-left: 4px solid #18382b;
    border-radius: 8px;
    padding: 14px 18px;
    margin-bottom: 20px;
  }}

  .exec-summary h3 {{
    font-size: 10.5pt;
    font-weight: 700;
    color: #0f291e;
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    gap: 6px;
  }}

  .exec-summary p {{
    font-size: 9pt;
    color: #4a5568;
    line-height: 1.5;
  }}

  /* Quick Stats Grid */
  .stats-grid {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin-bottom: 22px;
  }}

  .stat-card {{
    background: #ffffff;
    border: 1px solid #edf2f7;
    border-radius: 8px;
    padding: 10px 14px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
  }}

  .stat-label {{
    font-size: 7.5pt;
    text-transform: uppercase;
    color: #718096;
    font-weight: 600;
    letter-spacing: 0.5px;
  }}

  .stat-value {{
    font-family: 'Space+Grotesk', sans-serif;
    font-size: 13pt;
    font-weight: 700;
    color: #18382b;
    margin-top: 2px;
  }}

  /* Section Headings */
  .section-title {{
    font-family: 'Space+Grotesk', sans-serif;
    font-size: 12pt;
    font-weight: 700;
    color: #1a202c;
    border-bottom: 2px solid #edf2f7;
    padding-bottom: 6px;
    margin-top: 18px;
    margin-bottom: 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}

  .section-title span {{
    font-size: 9pt;
    color: #718096;
    font-weight: 500;
  }}

  /* Modules Table */
  table.quote-table {{
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
    font-size: 8.5pt;
  }}

  table.quote-table th {{
    background: #f1f5f9;
    color: #334155;
    text-align: left;
    padding: 8px 10px;
    font-weight: 600;
    border-top: 1px solid #e2e8f0;
    border-bottom: 1px solid #cbd5e1;
    text-transform: uppercase;
    font-size: 7.5pt;
    letter-spacing: 0.4px;
  }}

  table.quote-table th.hrs-col {{
    text-align: right;
    width: 65px;
  }}

  .module-header-row td {{
    background: #f8fafc;
    color: #0f291e;
    font-weight: 700;
    padding: 9px 10px 6px 10px;
    border-top: 1px solid #e2e8f0;
    font-size: 9pt;
  }}

  .module-header-row td.subtotal-cell {{
    text-align: right;
    color: #18382b;
    font-family: 'Space+Grotesk', sans-serif;
  }}

  .task-row td {{
    padding: 5px 10px 5px 22px;
    color: #475569;
    border-bottom: 1px solid #f1f5f9;
  }}

  .task-row td.hrs-val {{
    text-align: right;
    font-weight: 500;
    color: #334155;
  }}

  .task-bullet {{
    color: #e2a84b;
    margin-right: 6px;
    font-weight: bold;
  }}

  /* Total Summary Bar */
  .grand-total-card {{
    background: linear-gradient(135deg, #18382b 0%, #0f291e 100%);
    color: #ffffff;
    border-radius: 8px;
    padding: 16px 20px;
    margin-top: 18px;
    margin-bottom: 22px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    page-break-inside: avoid;
  }}

  .grand-total-label {{
    font-size: 11pt;
    font-weight: 600;
    letter-spacing: 0.3px;
  }}

  .grand-total-sub {{
    font-size: 8pt;
    color: #cbd5e0;
    margin-top: 2px;
  }}

  .grand-total-value {{
    font-family: 'Space+Grotesk', sans-serif;
    font-size: 20pt;
    font-weight: 700;
    color: #e2a84b;
    text-align: right;
  }}

  /* Tech Stack & Architecture Highlights */
  .tech-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    margin-bottom: 20px;
    page-break-inside: avoid;
  }}

  .tech-card {{
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 10px 12px;
    background: #ffffff;
  }}

  .tech-card h4 {{
    font-size: 8.5pt;
    font-weight: 700;
    color: #18382b;
    margin-bottom: 4px;
    text-transform: uppercase;
    letter-spacing: 0.3px;
  }}

  .tech-card p {{
    font-size: 8pt;
    color: #64748b;
    line-height: 1.35;
  }}

  /* Terms and Sign-off */
  .terms-box {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 12px 16px;
    font-size: 8pt;
    color: #64748b;
    line-height: 1.45;
    margin-bottom: 24px;
    page-break-inside: avoid;
  }}

  .terms-box h4 {{
    font-size: 8.5pt;
    font-weight: 700;
    color: #334155;
    margin-bottom: 6px;
    text-transform: uppercase;
  }}

  .sign-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
    margin-top: 20px;
    page-break-inside: avoid;
  }}

  .sign-col {{
    border-top: 1px solid #cbd5e1;
    padding-top: 8px;
    font-size: 8.5pt;
    color: #475569;
  }}

  .sign-title {{
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 2px;
  }}

  .page-break {{
    page-break-after: always;
    break-after: page;
  }}
</style>
</head>
<body>

  <!-- Header Card -->
  <div class="header-card">
    <div>
      <div class="brand-title">NOURBIA FOODS™ <span>CUSTOM PLATFORM</span></div>
      <div class="tagline">Advancing Culturally Relevant Nutrition • Meeting People Where They Are</div>
    </div>
    <div class="doc-meta">
      <div class="doc-badge">Official Scope & Quotation</div>
      <div><strong>Doc Ref:</strong> NB-PROP-2026-V2</div>
      <div><strong>Date:</strong> September 15, 2026</div>
      <div><strong>Scope:</strong> Custom E-Commerce & Platform</div>
    </div>
  </div>

  <!-- Executive Summary -->
  <div class="exec-summary">
    <h3>Executive Architecture & Scope Overview</h3>
    <p>
      This proposal outlines the end-to-end technical scope, modular architecture, and effort estimation for building the <strong>Bespoke Nourbia Foods Custom E-Commerce & Digital Platform</strong> (No Shopify). The solution is engineered as a modern, high-performance web platform featuring a dedicated D2C Storefront (7 Categories & 4 Heritage Lines), Interactive Nourbia Food Box Builder & Subscriptions, Community Taste Lab & Food Sovereignty Feedback Loop, B2B Wholesale & RFQ Engine, Surplus Food Recovery Intake, and a Comprehensive Multi-Role Operations Admin Dashboard powered by <strong>Stripe Payments & Stripe Billing</strong>.
    </p>
  </div>

  <!-- Quick Stats -->
  <div class="stats-grid">
    <div class="stat-card">
      <div class="stat-label">Total Modules</div>
      <div class="stat-value">{len(modules)} Core Modules</div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Payment Engine</div>
      <div class="stat-value">Stripe Fullstack</div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Architecture</div>
      <div class="stat-value">Custom Next / Node</div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Total Effort</div>
      <div class="stat-value" style="color: #c05621;">{total_hours} Hours</div>
    </div>
  </div>

  <!-- Architecture Highlights -->
  <div class="tech-grid">
    <div class="tech-card">
      <h4>⚡ Custom Full-Stack Core</h4>
      <p>Next.js App Router, TypeScript, PostgreSQL (Prisma), Redis cache, and AWS S3 cloud asset pipeline.</p>
    </div>
    <div class="tech-card">
      <h4>💳 Stripe Payment & Billing</h4>
      <p>Stripe Elements (Cards/Apple Pay/Google Pay/Link), Recurring Subscriptions, and Idempotent Webhooks.</p>
    </div>
    <div class="tech-card">
      <h4>📦 Dynamic Box Builder</h4>
      <p>Interactive slot-swapping (Individual, Family, Multi-Family, Custom), constraint engine & auto-manifest.</p>
    </div>
    <div class="tech-card">
      <h4>🧪 Community Taste Lab</h4>
      <p>Dynamic QR batch scanner, 4-step sensory evaluation, Cultural Wishlist voting, and referral perk wallet.</p>
    </div>
    <div class="tech-card">
      <h4>🏢 B2B Wholesale & RFQs</h4>
      <p>Automated PDF line sheet downloads, sample kit ordering, tiered case calculator, and Net-30 onboarding.</p>
    </div>
    <div class="tech-card">
      <h4>🛡️ Admin Operations Console</h4>
      <p>Multi-role RBAC, SKU & stock manager, live order fulfillment, carrier label integration, and demand heatmaps.</p>
    </div>
  </div>

  <!-- Detailed Scope Table -->
  <div class="section-title">
    <span>Module Breakdown & Detailed Engineering Deliverables</span>
    <span>{total_hours} Total Hours</span>
  </div>

  <table class="quote-table">
    <thead>
      <tr>
        <th style="width: 85%;">Module & Detailed Deliverable Tasks</th>
        <th class="hrs-col">Hours</th>
      </tr>
    </thead>
    <tbody>
"""

    for idx, mod in enumerate(modules):
        html_content += f"""
      <tr class="module-header-row">
        <td>{mod['name']}</td>
        <td class="subtotal-cell">{mod['subtotal']} hrs</td>
      </tr>
"""
        for task_name, hrs in mod['tasks']:
            html_content += f"""
      <tr class="task-row">
        <td><span class="task-bullet">▸</span>{task_name}</td>
        <td class="hrs-val">{hrs}</td>
      </tr>
"""

    html_content += f"""
    </tbody>
  </table>

  <!-- Grand Total Card -->
  <div class="grand-total-card">
    <div>
      <div class="grand-total-label">TOTAL ESTIMATED DEVELOPMENT EFFORT</div>
      <div class="grand-total-sub">Includes Custom UI/UX, Full-Stack Development, Stripe Integration, QA & Production Cloud Launch</div>
    </div>
    <div class="grand-total-value">{total_hours} HOURS</div>
  </div>

  <!-- Phased Rollout Roadmap -->
  <div class="section-title">
    <span>Project Phasing & Strategic Roadmap (Prove • Build • Scale)</span>
    <span>16 Weeks</span>
  </div>

  <div class="tech-grid">
    <div class="tech-card" style="border-left: 3px solid #18382b;">
      <h4>Phase 1: Prove (Weeks 1–6)</h4>
      <p>Architecture, Database Schema, Custom D2C Storefront (Haitian line proof-of-concept), Stripe Elements & Checkout, Food Box Builder MVP, and Community Taste Lab QR resolver.</p>
    </div>
    <div class="tech-card" style="border-left: 3px solid #2b6cb0;">
      <h4>Phase 2: Build (Weeks 7–11)</h4>
      <p>Recurring Stripe Subscriptions, B2B Wholesale Portal & Line Sheets, Core Services RFQ Hub, Surplus Farm Recovery Intake, Customer Account Dashboard, and SendGrid transactional emails.</p>
    </div>
    <div class="tech-card" style="border-left: 3px solid #c05621;">
      <h4>Phase 3: Scale & Launch (Weeks 12–16)</h4>
      <p>Multi-Role Admin Console, Carrier Shipping Labels (EasyPost), Multi-language i18n (EN/HT/FR/ES), Security Audits, Automated Playwright E2E Testing, and Production Cloud Launch.</p>
    </div>
  </div>

  <!-- Terms & Acceptance -->
  <div class="terms-box">
    <h4>Project Terms & Engagement Guidelines</h4>
    <p>
      1. <strong>Scope Baseline</strong>: All deliverables encompass custom software development, custom database modeling, Stripe API integration, and cloud deployment as defined in this specification.<br>
      2. <strong>Testing & QA</strong>: Includes automated unit testing, end-to-end user journey tests (Playwright), and Stripe sandbox-to-live transactional verification.<br>
      3. <strong>Client Assets</strong>: High-resolution brand assets, product imagery, and copy will be integrated as provided based on Nourbia brand standards.<br>
      4. <strong>Warranty & Handover</strong>: 30 days of post-launch hypercare, bug fixes, operational handover documentation, and staff training are included.
    </p>
  </div>

  <div class="sign-grid">
    <div class="sign-col">
      <div class="sign-title">Prepared By: Lead Software Architect & Engineering</div>
      <div>Signature: ____________________________________</div>
      <div>Date: September 15, 2026</div>
    </div>
    <div class="sign-col">
      <div class="sign-title">Accepted By: Nourbia Foods Executive Management</div>
      <div>Signature: ____________________________________</div>
      <div>Date: ________________________</div>
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
    generate_pdf()
