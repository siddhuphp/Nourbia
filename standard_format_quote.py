"""
ITPrior Solutions — Enterprise Quotation Generator & PDF Publishing Engine
Standardized Reusable Template for Commercial Proposals & Technical Estimates.
"""

import csv
import os
import sys
import base64
import subprocess
from dataclasses import dataclass, field
from typing import List, Tuple, Dict, Any, Optional

sys.stdout.reconfigure(encoding='utf-8')


# ==============================================================================
# 1. CONFIGURATION DATA STRUCTURES (Reusable for any client & project)
# ==============================================================================

@dataclass
class AgencyConfig:
    name: str = "ITPrior Solutions"
    subtitle: str = "Custom Web Applications • Brand Identity • E-Commerce Platforms"
    tagline: str = "Premier Enterprise Engineering Agency"
    website: str = "www.itprior.com"
    inquiries_email: str = "info@itprior.com"
    logo_path: str = r"c:\Siddhu\Works\Nourbia\ITPrior_full_logo_master.png"
    primary_color: str = "#0284c7"  # Brand Blue
    dark_color: str = "#0f172a"     # Slate 900
    accent_color: str = "#38bdf8"   # Sky Blue
    success_color: str = "#10b981"  # Emerald Green


@dataclass
class ClientConfig:
    company_name: str = "Nourbia Foods Inc."
    attn_name: str = "Pierre Ernso"
    attn_email: str = "pierre.ernso@gmail.com"
    cc_contacts: List[Tuple[str, str]] = field(default_factory=lambda: [
        ("Mickelsen", "mickelsen@newheightsconsulting.biz"),
        ("LBTZ Group", "lbtzea@gmail.com")
    ])
    project_title: str = "Custom E-Commerce Website, Brand Identity, Packaging & Digital Platform"
    tech_stack: str = "Next.js 15 • FastAPI • PostgreSQL • Redis (Custom / No Shopify)"


@dataclass
class MilestoneItem:
    title: str
    percentage: float  # e.g., 0.25 for 25%
    deliverables_summary: str


@dataclass
class CommercialConfig:
    bid_reference: str = "BID REF: ITP-NOURBIA-2026-FINAL"
    quote_date: str = "March 17, 2026"
    validity_period: str = "45 Days"
    currency_symbol: str = "$"
    currency_code: str = "USD"
    hourly_rate: float = 15.00
    estimated_timeline: str = "10 – 12 Weeks"
    complimentary_qa_hours: int = 40
    milestones: List[MilestoneItem] = field(default_factory=lambda: [
        MilestoneItem(
            title="Milestone 1",
            percentage=0.25,
            deliverables_summary="Brand Strategy, Visual Guidelines, Packaging Design System, DB Modeling & Tech Setup"
        ),
        MilestoneItem(
            title="Milestone 2",
            percentage=0.25,
            deliverables_summary="UI/UX Design System, Homepage, Cultural Product Catalog, PDPs & Food Box Configurator"
        ),
        MilestoneItem(
            title="Milestone 3",
            percentage=0.25,
            deliverables_summary="Shopping Cart, Checkout, Stripe & PayPal Payments, 50-State Shipping & B2B/Community Hub"
        ),
        MilestoneItem(
            title="Milestone 4",
            percentage=0.25,
            deliverables_summary="Administration Dashboard, Multilingual SEO, QA Testing, Production Deployment & Handover"
        )
    ])


@dataclass
class QuoteScopeConfig:
    executive_summary: str = (
        "This quotation strictly covers the 20 exact project requirements for <strong>Nourbia Foods Inc.</strong>: "
        "<strong>(1)</strong> Brand Strategy & Brand Guidelines, <strong>(2)</strong> Packaging Design & Label System, "
        "<strong>(3)</strong> Custom E-Commerce Web Platform (Next.js + FastAPI + Postgres + Redis — Fully Custom / No Shopify), "
        "<strong>(4)</strong> Cultural Catalog (20–40 SKUs) & PDPs with Rehydration Specs, <strong>(5)</strong> Curated Cultural Food Boxes, "
        "<strong>(6)</strong> Cart, Checkout & Stripe/Wallets/PayPal, <strong>(7)</strong> 50-State Shipping & Fulfillment, "
        "<strong>(8)</strong> For Business (B2B Hub), <strong>(9)</strong> Community 'Taste • Test • Shape' Concept, "
        "<strong>(10)</strong> Comprehensive Admin Panel, <strong>(11)</strong> Multilingual i18n (5 Languages: English, Haitian Creole, French, Spanish, Portuguese), "
        "and <strong>(12)</strong> +40 Hours Complimentary QA & Testing."
    )
    asset_supply_note: str = (
        "All product and lifestyle photographs will be provided directly by Nourbia Foods. Photography services and costs are excluded from this quotation."
    )
    technical_governance_terms: List[str] = field(default_factory=lambda: [
        "<strong>Full Source Code Ownership:</strong> 100% intellectual property, packaging vector artwork, brand guide PDF, repository transfer, and deployment scripts provided to client upon final sign-off.",
        "<strong>Custom Architecture Guarantee:</strong> 100% custom-built Next.js 15 & FastAPI infrastructure (No Shopify dependencies or recurring app license fees).",
        "<strong>Complimentary QA & Warranty:</strong> +40 hours complimentary testing buffer plus 30 days post-launch hypercare and bug-fix warranty."
    ])
    commercial_payment_terms: List[str] = field(default_factory=lambda: [
        "<strong>Milestone Sign-Off:</strong> Invoices issued upon staging demonstration and test sign-off of each milestone stage.",
        "<strong>International Remittance:</strong> Wire Transfer / ACH / Corporate Card via Stripe Invoicing (USD Currency).",
        "<strong>Photography Supply:</strong> High-res packaging & lifestyle photos supplied by client; integration into PDPs and UI included."
    ])


# ==============================================================================
# 2. UTILITY & DATA PARSING FUNCTIONS
# ==============================================================================

def encode_image_base64(image_path: str) -> str:
    """Encodes an image file to Base64 data URI for self-contained PDF/HTML rendering."""
    if os.path.exists(image_path):
        with open(image_path, 'rb') as f:
            ext = os.path.splitext(image_path)[1].replace('.', '').lower()
            if ext == 'jpg':
                ext = 'jpeg'
            return f"data:image/{ext};base64,{base64.b64encode(f.read()).decode('utf-8')}"
    return ""


def find_chrome_executable() -> str:
    """Finds Google Chrome executable across standard Windows installation paths."""
    standard_paths = [
        r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
        os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe'),
        os.path.expandvars(r'%PROGRAMFILES%\Google\Chrome\Application\chrome.exe'),
    ]
    for p in standard_paths:
        if os.path.exists(p):
            return p
    return 'chrome'  # fallback to PATH


def parse_quote_csv(csv_path: str) -> List[Dict[str, Any]]:
    """
    Parses standard quotation CSV format:
    Row format: [Module Name, Task Description, Hours]
    """
    modules = []
    current_module = None

    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Quotation CSV not found at: {csv_path}")

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader, None)
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

    return modules


# ==============================================================================
# 3. HTML & CSS GENERATION ENGINE (Standard UI Template)
# ==============================================================================

def generate_standard_quote_html(
    agency: AgencyConfig,
    client: ClientConfig,
    commercial: CommercialConfig,
    scope: QuoteScopeConfig,
    modules: List[Dict[str, Any]]
) -> str:
    """Builds a standardized, high-density, print-optimized HTML quotation."""
    logo_b64 = encode_image_base64(agency.logo_path)

    total_billed_hours = sum(m['subtotal'] for m in modules)
    complimentary_qa_hours = commercial.complimentary_qa_hours
    total_effort_hours = total_billed_hours + complimentary_qa_hours
    grand_total_amount = total_billed_hours * commercial.hourly_rate

    # Generate Module Rows
    module_rows_html = ""
    for idx, m in enumerate(modules, start=1):
        subtotal_amount = m['subtotal'] * commercial.hourly_rate
        module_rows_html += f"""
      <tr class="mod-row">
        <td class="mod-num">{idx}</td>
        <td>{m['name']}</td>
        <td class="mod-hrs">{m['subtotal']}</td>
        <td class="mod-rate">${commercial.hourly_rate:.2f}</td>
        <td class="mod-total">${subtotal_amount:,.2f}</td>
      </tr>
"""
        for task, hrs in m['tasks']:
            if 'Complimentary' in task or hrs == 0:
                module_rows_html += f"""
      <tr class="task-row" style="background-color: #f0fdf4;">
        <td></td>
        <td class="task-name"><span class="task-bullet" style="color: {agency.success_color};">›</span>{task} <span class="complimentary-badge">+{complimentary_qa_hours} Hrs Included</span></td>
        <td class="task-hrs" style="color: #059669; font-weight: bold;">+{complimentary_qa_hours}</td>
        <td class="mod-rate" style="color: #059669; font-weight: bold;">FREE</td>
        <td class="mod-total" style="color: #059669; font-weight: bold;">$0.00</td>
      </tr>
"""
            else:
                module_rows_html += f"""
      <tr class="task-row">
        <td></td>
        <td class="task-name"><span class="task-bullet">›</span>{task}</td>
        <td class="task-hrs">{hrs}</td>
        <td></td>
        <td></td>
      </tr>
"""

    # Generate Milestones Rows
    milestones_rows_html = ""
    for ms in commercial.milestones:
        ms_amount = grand_total_amount * ms.percentage
        milestones_rows_html += f"""
      <div class="ms-row">
        <span class="ms-name"><strong>{ms.title}:</strong> {ms.deliverables_summary}</span>
        <span class="ms-split">{int(ms.percentage * 100)}%</span>
        <span class="ms-val">${ms_amount:,.2f}</span>
      </div>
"""

    # Generate CC Contacts List
    cc_html = "".join([f"<p>Cc: <strong>{name}</strong> ({email})</p>" for name, email in client.cc_contacts])

    # Generate Governance Terms List
    gov_terms_html = "".join([f"<li>{term}</li>" for term in scope.technical_governance_terms])
    comm_terms_html = "".join([f"<li>{term}</li>" for term in scope.commercial_payment_terms])

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{agency.name} Quotation — {client.company_name}</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&family=Open+Sans:wght@400;500;600;700&display=swap');

  @page {{
    size: A4;
    margin: 8mm 10mm 8mm 10mm;
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
    color: #1e293b;
    background-color: #ffffff;
    font-size: 7.2pt;
    line-height: 1.25;
  }}

  /* Header */
  .header-wrap {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    padding-top: 0;
    margin-bottom: 7px;
    border-bottom: 2px solid {agency.primary_color};
    padding-bottom: 5px;
  }}

  .logo-box img {{
    height: 48px;
    width: auto;
    display: block;
  }}

  .company-sub {{
    font-size: 6.8pt;
    color: #64748b;
    margin-top: 2px;
    font-family: 'Montserrat', sans-serif;
    letter-spacing: 0.5px;
    text-transform: uppercase;
  }}

  .quote-badge-box {{
    text-align: right;
  }}

  .quote-title {{
    font-family: 'Montserrat', sans-serif;
    font-size: 13.5pt;
    font-weight: 900;
    color: {agency.dark_color};
    letter-spacing: 0.5px;
  }}

  .quote-number {{
    font-family: 'Montserrat', sans-serif;
    font-size: 8.5pt;
    font-weight: 700;
    color: {agency.primary_color};
    margin-top: 1px;
  }}

  .quote-date {{
    font-size: 7.2pt;
    color: #64748b;
    margin-top: 1px;
  }}

  /* Meta Details Grid */
  .meta-grid {{
    display: grid;
    grid-template-columns: 1.25fr 1fr 1.05fr;
    gap: 8px;
    background-color: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 6px 8px;
    margin-bottom: 7px;
  }}

  .meta-col h4 {{
    font-family: 'Montserrat', sans-serif;
    font-size: 7.2pt;
    font-weight: 800;
    text-transform: uppercase;
    color: {agency.primary_color};
    margin-bottom: 2px;
    letter-spacing: 0.3px;
  }}

  .meta-col p {{
    font-size: 7.1pt;
    color: #334155;
    line-height: 1.3;
  }}

  .meta-col strong {{
    color: {agency.dark_color};
    font-weight: 700;
  }}

  /* Executive Highlight Box */
  .exec-box {{
    background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
    border-left: 3px solid {agency.primary_color};
    border-radius: 3px;
    padding: 5px 8px;
    margin-bottom: 7px;
    font-size: 7pt;
    color: #0369a1;
    line-height: 1.32;
  }}

  .exec-box strong {{
    color: #0c4a6e;
    font-family: 'Montserrat', sans-serif;
  }}

  /* Section Title */
  .section-heading {{
    font-family: 'Montserrat', sans-serif;
    font-size: 8.2pt;
    font-weight: 800;
    color: {agency.dark_color};
    text-transform: uppercase;
    letter-spacing: 0.3px;
    margin-top: 6px;
    margin-bottom: 3px;
    display: flex;
    align-items: center;
    gap: 5px;
  }}

  .section-heading .bar {{
    width: 3.5px;
    height: 11px;
    background-color: {agency.primary_color};
    border-radius: 1px;
  }}

  .section-tag {{
    font-size: 6.8pt;
    font-weight: 700;
    background-color: {agency.primary_color};
    color: #ffffff;
    padding: 1px 5px;
    border-radius: 2px;
    margin-left: auto;
    text-transform: none;
  }}

  /* Tables */
  .quote-table {{
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 6px;
    page-break-inside: auto;
  }}

  .quote-table thead tr {{
    background-color: {agency.dark_color};
    color: #ffffff;
  }}

  .quote-table th {{
    font-family: 'Montserrat', sans-serif;
    font-size: 6.9pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.2px;
    padding: 3px 5px;
    text-align: left;
    border-top: 1px solid {agency.dark_color};
    border-bottom: 1px solid {agency.dark_color};
  }}

  .quote-table th.col-center {{
    text-align: center;
  }}

  .quote-table th.col-right {{
    text-align: right;
  }}

  /* Module Parent Row */
  .mod-row {{
    background-color: #f1f5f9;
    border-top: 1px solid #cbd5e1;
    border-bottom: 1px solid #e2e8f0;
    page-break-inside: avoid;
    page-break-after: avoid;
  }}

  .mod-row td {{
    padding: 2.3px 5px;
    font-family: 'Montserrat', sans-serif;
    font-size: 7.2pt;
    font-weight: 800;
    color: {agency.dark_color};
  }}

  .mod-row td.mod-num {{
    color: {agency.primary_color};
    text-align: center;
    width: 26px;
  }}

  .mod-row td.mod-hrs {{
    text-align: center;
    color: {agency.dark_color};
    width: 45px;
  }}

  .mod-row td.mod-rate {{
    text-align: right;
    color: #475569;
    font-weight: 600;
    width: 60px;
  }}

  .mod-row td.mod-total {{
    text-align: right;
    color: {agency.dark_color};
    font-weight: 900;
    width: 75px;
  }}

  /* Task Subrows */
  .task-row td {{
    padding: 1.3px 5px 1.3px 5px;
    font-size: 6.8pt;
    color: #334155;
    border-bottom: 1px solid #f1f5f9;
  }}

  .task-row td.task-name {{
    padding-left: 12px;
  }}

  .task-bullet {{
    color: {agency.primary_color};
    font-weight: 900;
    margin-right: 3px;
  }}

  .task-row td.task-hrs {{
    text-align: center;
    color: #64748b;
    font-size: 6.7pt;
  }}

  /* Complimentary Badge */
  .complimentary-badge {{
    background-color: {agency.success_color};
    color: #ffffff;
    font-weight: 700;
    font-size: 6pt;
    padding: 1px 4px;
    border-radius: 2px;
    margin-left: 5px;
    text-transform: uppercase;
  }}

  /* Totals & Summary Block */
  .totals-container {{
    display: grid;
    grid-template-columns: 1.25fr 1fr;
    gap: 10px;
    margin-top: 6px;
    margin-bottom: 8px;
    page-break-inside: avoid;
  }}

  .milestones-box {{
    background-color: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 7px 9px;
  }}

  .milestones-box h4 {{
    font-family: 'Montserrat', sans-serif;
    font-size: 7.6pt;
    font-weight: 800;
    color: {agency.dark_color};
    text-transform: uppercase;
    margin-bottom: 4px;
    display: flex;
    justify-content: space-between;
  }}

  .ms-row {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 2.2px 0;
    border-bottom: 1px dashed #e2e8f0;
    font-size: 7pt;
  }}

  .ms-row:last-child {{
    border-bottom: none;
  }}

  .ms-name {{
    color: #334155;
  }}

  .ms-split {{
    color: {agency.primary_color};
    font-weight: 700;
  }}

  .ms-val {{
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    color: {agency.dark_color};
  }}

  .summary-box {{
    background-color: {agency.dark_color};
    color: #ffffff;
    border-radius: 4px;
    padding: 7px 10px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}

  .sum-line {{
    display: flex;
    justify-content: space-between;
    font-size: 7.3pt;
    padding: 1.5px 0;
    color: #cbd5e1;
  }}

  .sum-line.highlight {{
    border-top: 1px solid #334155;
    padding-top: 3px;
    margin-top: 2px;
    font-weight: 700;
    color: #ffffff;
  }}

  .sum-line.grand {{
    border-top: 1.5px solid {agency.primary_color};
    padding-top: 4px;
    margin-top: 3px;
  }}

  .sum-line.grand .label {{
    font-family: 'Montserrat', sans-serif;
    font-size: 8.8pt;
    font-weight: 900;
    color: {agency.accent_color};
    text-transform: uppercase;
  }}

  .sum-line.grand .val {{
    font-family: 'Montserrat', sans-serif;
    font-size: 10.5pt;
    font-weight: 900;
    color: {agency.accent_color};
  }}

  /* Terms & Notes */
  .terms-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    margin-bottom: 6px;
    font-size: 6.8pt;
    color: #475569;
    line-height: 1.32;
    page-break-inside: avoid;
  }}

  .terms-card {{
    background-color: #fafafa;
    border: 1px solid #f1f5f9;
    border-radius: 3px;
    padding: 5px 7px;
  }}

  .terms-card h5 {{
    font-family: 'Montserrat', sans-serif;
    font-size: 7.2pt;
    font-weight: 800;
    color: {agency.dark_color};
    margin-bottom: 2px;
    text-transform: uppercase;
  }}

  .terms-card ul {{
    list-style: none;
    padding-left: 0;
  }}

  .terms-card li {{
    margin-bottom: 1.5px;
  }}

  .terms-card li::before {{
    content: "•";
    color: {agency.primary_color};
    font-weight: bold;
    display: inline-block;
    width: 7px;
  }}

  /* Footer */
  .footer-container {{
    border-top: 1.5px solid {agency.primary_color};
    padding-top: 5px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 6.6pt;
    color: #64748b;
    page-break-inside: avoid;
  }}

  .footer-contacts {{
    display: flex;
    gap: 10px;
  }}

  .footer-contacts strong {{
    color: {agency.dark_color};
  }}
</style>
</head>
<body>

  <!-- Header -->
  <div class="header-wrap">
    <div>
      <div class="logo-box">
        <img src="{logo_b64}" alt="{agency.name} Logo">
      </div>
      <div class="company-sub">{agency.subtitle}</div>
    </div>
    <div class="quote-badge-box">
      <div class="quote-title">PROJECT QUOTATION</div>
      <div class="quote-number">{commercial.bid_reference}</div>
      <div class="quote-date">Date: {commercial.quote_date} &nbsp;|&nbsp; Validity: {commercial.validity_period}</div>
    </div>
  </div>

  <!-- Meta Information -->
  <div class="meta-grid">
    <div class="meta-col">
      <h4>CLIENT / PROJECT STAKEHOLDERS</h4>
      <p><strong>{client.company_name}</strong></p>
      <p>Attn: <strong>{client.attn_name}</strong> ({client.attn_email})</p>
      {cc_html}
    </div>
    <div class="meta-col">
      <h4>DELIVERY AGENCY</h4>
      <p><strong>{agency.name}</strong></p>
      <p>Web: <strong>{agency.website}</strong></p>
      <p>Inquiries: <strong>{agency.inquiries_email}</strong></p>
      <p>Tech Stack: <strong>{client.tech_stack}</strong></p>
    </div>
    <div class="meta-col">
      <h4>COMMERCIAL SUMMARY</h4>
      <p>Billed Development: <strong>{len(modules)} Modules ({total_billed_hours} Hrs)</strong></p>
      <p>Complimentary QA: <strong>+{complimentary_qa_hours} Hrs ($0.00 Included)</strong></p>
      <p>Hourly Billing Rate: <strong>${commercial.hourly_rate:.2f} {commercial.currency_code} / Hour</strong></p>
      <p>Project Investment: <strong>${grand_total_amount:,.2f} {commercial.currency_code}</strong> ({commercial.estimated_timeline})</p>
    </div>
  </div>

  <!-- Executive Summary Box -->
  <div class="exec-box">
    <strong>Project Scope & Technical Alignment:</strong> {scope.executive_summary}<br>
    <em><strong>Asset Note:</strong> {scope.asset_supply_note}</em>
  </div>

  <!-- Module Table -->
  <div class="section-heading">
    <div class="bar"></div>
    <span>Core Functional Scope & Technical Deliverables</span>
    <span class="section-tag">{len(modules)} Deliverable Modules</span>
  </div>

  <table class="quote-table">
    <thead>
      <tr>
        <th class="col-center" style="width: 26px;">#</th>
        <th>Module & Technical Scope Deliverables</th>
        <th class="col-center" style="width: 45px;">Hours</th>
        <th class="col-right" style="width: 60px;">Rate</th>
        <th class="col-right" style="width: 75px;">Total ({commercial.currency_code})</th>
      </tr>
    </thead>
    <tbody>
      {module_rows_html}
    </tbody>
  </table>

  <!-- Commercial Summary & Milestones Block -->
  <div class="totals-container">
    <div class="milestones-box">
      <h4>
        <span>Milestone Payment Schedule</span>
        <span style="color: {agency.primary_color};">{commercial.estimated_timeline}</span>
      </h4>
      {milestones_rows_html}
    </div>

    <div class="summary-box">
      <div>
        <div class="sum-line">
          <span>Total Billed Engineering:</span>
          <span>{total_billed_hours} Hours</span>
        </div>
        <div class="sum-line" style="color: #34d399; font-weight: 600;">
          <span>Complimentary QA & Testing:</span>
          <span>+{complimentary_qa_hours} Hrs (FREE)</span>
        </div>
        <div class="sum-line">
          <span>Total Project Effort:</span>
          <span>{total_effort_hours} Hours</span>
        </div>
        <div class="sum-line">
          <span>Standard Hourly Rate:</span>
          <span>${commercial.hourly_rate:.2f} {commercial.currency_code} / Hr</span>
        </div>
      </div>
      <div class="sum-line grand">
        <span class="label">Total Project Investment:</span>
        <span class="val">${grand_total_amount:,.2f}</span>
      </div>
    </div>
  </div>

  <!-- Terms & Project Governance -->
  <div class="terms-grid">
    <div class="terms-card">
      <h5>Technical Governance & Deliverables</h5>
      <ul>
        {gov_terms_html}
      </ul>
    </div>
    <div class="terms-card">
      <h5>Commercial & Payment Terms</h5>
      <ul>
        {comm_terms_html}
      </ul>
    </div>
  </div>

  <!-- Footer -->
  <div class="footer-container">
    <div class="footer-contacts">
      <div><strong>{agency.name}</strong> — {agency.tagline}</div>
      <div>Inquiries: <strong>{agency.inquiries_email}</strong></div>
      <div>Web: <strong>{agency.website}</strong></div>
    </div>
    <div>Official Quotation Proposal • {agency.name}</div>
  </div>

</body>
</html>
"""
    return html_content


def compile_pdf_from_html(html_path: str, pdf_path: str) -> bool:
    """Compiles HTML to PDF via Chrome Headless CLI."""
    chrome_exe = find_chrome_executable()
    chrome_cmd = [
        chrome_exe,
        '--headless=new',
        '--disable-gpu',
        '--no-pdf-header-footer',
        '--run-all-compositor-stages-before-draw',
        f'--print-to-pdf={pdf_path}',
        html_path
    ]
    print(f"Compiling PDF using: {chrome_exe} ...")
    res = subprocess.run(chrome_cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"✓ PDF generated successfully at: {pdf_path}")
        return True
    else:
        print(f"✗ PDF generation error: {res.stderr}")
        return False


# ==============================================================================
# 4. PRIMARY GENERATOR ORCHESTRATOR
# ==============================================================================

def generate_quote(
    csv_path: str = r'c:\Siddhu\Works\Nourbia\Nourbia-Quote.csv',
    output_html: str = r'c:\Siddhu\Works\Nourbia\Nourbia_Foods_ITPrior_Quote.html',
    output_pdf: str = r'c:\Siddhu\Works\Nourbia\Nourbia_Foods_ITPrior_Quote.pdf',
    agency: Optional[AgencyConfig] = None,
    client: Optional[ClientConfig] = None,
    commercial: Optional[CommercialConfig] = None,
    scope: Optional[QuoteScopeConfig] = None
):
    """Orchestrates complete quote parsing, HTML rendering, and PDF generation."""
    agency = agency or AgencyConfig()
    client = client or ClientConfig()
    commercial = commercial or CommercialConfig()
    scope = scope or QuoteScopeConfig()

    print(f"Loading tasks from: {csv_path}")
    modules = parse_quote_csv(csv_path)

    print("Generating HTML template...")
    html_content = generate_standard_quote_html(agency, client, commercial, scope, modules)

    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"✓ HTML generated at: {output_html}")

    compile_pdf_from_html(output_html, output_pdf)


if __name__ == '__main__':
    generate_quote()
