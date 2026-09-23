"""
ITPrior Solutions — Nourbia Foods Comprehensive Functional Requirements,
Technical Architecture & Acceptance Criteria Document Generator.
Compiles Markdown, HTML, and high-resolution PDF for Ernso Pierre (CEO, Nourbia Foods).
"""

import os
import sys
import base64
import subprocess

# Ensure UTF-8 console output
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = r"c:\Siddhu\Works\Nourbia"
LOGO_PATH = os.path.join(BASE_DIR, "ITPrior_full_logo_master.png")
OUTPUT_MD = os.path.join(BASE_DIR, "Nourbia_Foods_ITPrior_Functional_Requirements_and_Acceptance.md")
OUTPUT_HTML = os.path.join(BASE_DIR, "Nourbia_Foods_ITPrior_Functional_Requirements_and_Acceptance.html")
OUTPUT_PDF = os.path.join(BASE_DIR, "Nourbia_Foods_ITPrior_Functional_Requirements_and_Acceptance.pdf")

# Also sync to itprior-quotes/Nourbia if available
QUOTES_NOURBIA_DIR = r"c:\Siddhu\Works\itprior-quotes\Nourbia"


def find_chrome_executable() -> str:
    paths = [
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Users\%USERNAME%\AppData\Local\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "/usr/bin/google-chrome",
        "/usr/bin/chromium-browser"
    ]
    for p in paths:
        expanded = os.path.expandvars(p)
        if os.path.exists(expanded):
            return expanded
    return "chrome"


def get_base64_logo() -> str:
    if os.path.exists(LOGO_PATH):
        with open(LOGO_PATH, "rb") as f:
            return base64.b64encode(f.read()).decode('utf-8')
    return ""


def build_html_content(logo_b64: str) -> str:
    logo_tag = f'<img src="data:image/png;base64,{logo_b64}" alt="ITPrior Solutions Logo" class="brand-logo" />' if logo_b64 else '<div class="brand-fallback">ITPrior Solutions</div>'

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>NOURBIA FOODS™ — Functional Requirements & Acceptance Criteria Specification | ITPrior Solutions</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    @page {{
      size: A4 portrait;
      margin: 12mm 14mm 14mm 14mm;
      @bottom-right {{
        content: "Page " counter(page) " of " counter(pages);
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 9px;
        color: #94a3b8;
      }}
    }}

    * {{
      box-sizing: border-box;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }}

    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      color: #1e293b;
      background: #ffffff;
      margin: 0;
      padding: 0;
      font-size: 11.5px;
      line-height: 1.55;
    }}

    .doc-container {{
      max-width: 860px;
      margin: 0 auto;
      padding: 0;
    }}

    /* Header & Cover Banner */
    .header-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 2px solid #0284c7;
      padding-bottom: 12px;
      margin-bottom: 20px;
    }}

    .brand-logo {{
      max-height: 46px;
      width: auto;
      object-fit: contain;
    }}

    .brand-fallback {{
      font-size: 22px;
      font-weight: 800;
      color: #0284c7;
    }}

    .doc-badge {{
      background: #f0f9ff;
      border: 1px solid #bae6fd;
      color: #0369a1;
      font-size: 10px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      display: inline-block;
      margin-bottom: 4px;
    }}

    .doc-meta {{
      text-align: right;
      font-size: 11px;
      color: #64748b;
    }}

    .doc-title-block {{
      background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
      color: #ffffff;
      border-radius: 10px;
      padding: 22px 26px;
      margin-bottom: 22px;
      position: relative;
      overflow: hidden;
    }}

    .doc-title-block::after {{
      content: "";
      position: absolute;
      right: -20px;
      top: -20px;
      width: 140px;
      height: 140px;
      background: radial-gradient(circle, rgba(56, 189, 248, 0.2) 0%, rgba(2, 132, 199, 0) 70%);
      border-radius: 50%;
    }}

    .doc-title-block h1 {{
      margin: 0 0 6px 0;
      font-size: 20px;
      font-weight: 800;
      letter-spacing: -0.3px;
      color: #ffffff;
    }}

    .doc-title-block .subtitle {{
      color: #38bdf8;
      font-size: 13px;
      font-weight: 600;
      margin-bottom: 12px;
    }}

    .meta-grid-header {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 6px;
      padding: 10px 14px;
      font-size: 10.5px;
    }}

    .meta-grid-header div span {{
      display: block;
      color: #94a3b8;
      font-size: 9.5px;
      text-transform: uppercase;
      font-weight: 700;
      letter-spacing: 0.5px;
    }}

    .meta-grid-header div strong {{
      color: #f8fafc;
      font-size: 11.5px;
    }}

    /* Executive Callout */
    .executive-card {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-left: 4px solid #0284c7;
      border-radius: 8px;
      padding: 14px 18px;
      margin-bottom: 22px;
    }}

    .executive-card h3 {{
      margin: 0 0 8px 0;
      font-size: 13px;
      font-weight: 800;
      color: #0f172a;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .executive-card p {{
      margin: 0 0 8px 0;
      font-size: 11.5px;
      color: #334155;
      line-height: 1.6;
    }}

    .executive-card p:last-child {{
      margin-bottom: 0;
    }}

    /* Section Headings */
    h2.section-header {{
      font-size: 14px;
      font-weight: 800;
      color: #0f172a;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      border-bottom: 2px solid #0f172a;
      padding-bottom: 5px;
      margin: 26px 0 14px 0;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      page-break-after: avoid;
    }}

    h2.section-header .sub {{
      font-size: 10px;
      color: #64748b;
      font-weight: 600;
      text-transform: none;
    }}

    h3.sub-header {{
      font-size: 12.5px;
      font-weight: 700;
      color: #0284c7;
      margin: 18px 0 8px 0;
      border-bottom: 1px solid #e2e8f0;
      padding-bottom: 4px;
      page-break-after: avoid;
    }}

    /* Module Box */
    .module-card {{
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      margin-bottom: 18px;
      overflow: hidden;
      page-break-inside: avoid;
      box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    }}

    .module-card-header {{
      background: #f1f5f9;
      border-bottom: 1px solid #cbd5e1;
      padding: 9px 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .mod-title {{
      font-size: 12.5px;
      font-weight: 800;
      color: #0f172a;
    }}

    .mod-hours-badge {{
      background: #0284c7;
      color: #ffffff;
      font-size: 10px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 12px;
    }}

    .mod-body {{
      padding: 12px 14px;
    }}

    .mod-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 10px 14px;
      margin-bottom: 10px;
    }}

    .mod-grid-item {{
      font-size: 11px;
    }}

    .mod-grid-item .label {{
      font-weight: 700;
      color: #475569;
      text-transform: uppercase;
      font-size: 9.5px;
      letter-spacing: 0.4px;
      margin-bottom: 2px;
      display: block;
    }}

    .mod-grid-item .val {{
      color: #1e293b;
      line-height: 1.45;
    }}

    .mod-acceptance {{
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      border-radius: 6px;
      padding: 8px 12px;
      margin-top: 8px;
    }}

    .mod-acceptance .title {{
      font-size: 10px;
      font-weight: 800;
      color: #166534;
      text-transform: uppercase;
      letter-spacing: 0.4px;
      margin-bottom: 3px;
    }}

    .mod-acceptance ul {{
      margin: 0;
      padding-left: 16px;
      font-size: 10.5px;
      color: #14532d;
    }}

    /* Tables */
    table.data-table {{
      width: 100%;
      border-collapse: collapse;
      margin: 10px 0 16px 0;
      font-size: 11px;
      page-break-inside: avoid;
    }}

    table.data-table th {{
      background: #0f172a;
      color: #ffffff;
      font-weight: 700;
      text-transform: uppercase;
      font-size: 10px;
      letter-spacing: 0.4px;
      padding: 7px 10px;
      text-align: left;
      border: 1px solid #0f172a;
    }}

    table.data-table td {{
      padding: 7px 10px;
      border: 1px solid #e2e8f0;
      vertical-align: top;
      color: #334155;
    }}

    table.data-table tr:nth-child(even) td {{
      background: #f8fafc;
    }}

    table.data-table tr:hover td {{
      background: #f1f5f9;
    }}

    /* Diagrams & Code Boxes */
    .flow-diagram {{
      background: #0f172a;
      color: #38bdf8;
      font-family: 'JetBrains Mono', monospace;
      font-size: 10.5px;
      line-height: 1.45;
      padding: 12px 14px;
      border-radius: 6px;
      overflow-x: auto;
      margin: 10px 0 14px 0;
      border: 1px solid #1e293b;
      page-break-inside: avoid;
    }}

    /* Callout Alert */
    .alert-box {{
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      border-left: 4px solid #2563eb;
      border-radius: 6px;
      padding: 10px 14px;
      margin: 12px 0;
      font-size: 11px;
      color: #1e40af;
      page-break-inside: avoid;
    }}

    .alert-box strong {{
      color: #1e3a8a;
    }}

    /* Signoff block */
    .signoff-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      border: 1.5px dashed #cbd5e1;
      border-radius: 8px;
      padding: 16px;
      margin-top: 24px;
      page-break-inside: avoid;
    }}

    .sign-box h6 {{
      margin: 0 0 6px 0;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      color: #475569;
    }}

    .sign-line {{
      height: 36px;
      border-bottom: 1px solid #94a3b8;
      margin-bottom: 6px;
    }}

    .sign-sub {{
      font-size: 10px;
      color: #64748b;
    }}

    .footer-note {{
      margin-top: 20px;
      border-top: 1px solid #e2e8f0;
      padding-top: 10px;
      display: flex;
      justify-content: space-between;
      font-size: 10px;
      color: #94a3b8;
    }}

    /* Print Break Utilities */
    .page-break {{
      page-break-before: always;
    }}
  </style>
</head>
<body>
<div class="doc-container">

  <!-- Header -->
  <div class="header-bar">
    <div>
      {logo_tag}
      <div style="font-size: 10.5px; color: #64748b; font-weight: 500; margin-top: 2px;">
        ITPrior Solutions • Enterprise Digital Engineering & Commercial Architecture
      </div>
    </div>
    <div class="doc-meta">
      <div class="doc-badge">Technical & Functional Specification</div>
      <div style="font-weight: 700; color: #0f172a; font-size: 12px;">DOC REF: ITP-NOURBIA-FRS-2026-FINAL</div>
      <div>Date: <strong>March 24, 2026</strong> • Version: <strong>2.0 (Executive Edition)</strong></div>
    </div>
  </div>

  <!-- Title Block -->
  <div class="doc-title-block">
    <h1>NOURBIA FOODS™ — FUNCTIONAL REQUIREMENTS & ACCEPTANCE CRITERIA SPECIFICATION</h1>
    <div class="subtitle">Complete Technical Definition, Architecture Guide & Operational Framework for All 14 Platform Modules</div>
    
    <div class="meta-grid-header">
      <div>
        <span>Client Organization</span>
        <strong>Nourbia Foods Inc.</strong>
      </div>
      <div>
        <span>Attention / Stakeholder</span>
        <strong>Ernso Pierre (Founder & CEO)</strong>
      </div>
      <div>
        <span>Engineering Agency</span>
        <strong>ITPrior Solutions</strong>
      </div>
      <div>
        <span>Core Tech Stack</span>
        <strong>Next.js 15 • FastAPI • PostgreSQL</strong>
      </div>
    </div>
  </div>

  <!-- Executive Response -->
  <div class="executive-card">
    <h3>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#0284c7" stroke-width="2.5"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
      Executive Commitment & Engineering Alignment
    </h3>
    <p>
      Dear Ernso Pierre & The Nourbia Foods Leadership Team,<br>
      Thank you for your structured, comprehensive feedback. We fully share your vision: <strong>Nourbia Foods is not merely building a static web store, but establishing an enterprise-grade digital commerce ecosystem</strong> capable of scaling seamlessly across DTC e-commerce, cultural food boxes, wholesale B2B lead generation, bulk ingredient distribution, 5-language multilingual localization, and community-driven R&D.
    </p>
    <p>
      This document serves as our binding <strong>Functional Requirements Specification (FRS), Technical Architecture Blueprint, and Acceptance Criteria Charter</strong>. It covers each of the <strong>14 Proposal Modules</strong> with granular workflows, data entities, admin capabilities, and objective completion criteria, followed by in-depth operational blueprints for the <strong>Food Box Engine, B2B Hub, 50-State Fulfillment, "Taste • Test • Shape" Platform, Multilingual Engine, Admin Wireframes, Testing Protocols, and Itemized Third-Party Operating Costs</strong>.
    </p>
    <p>
      <strong>Agile Milestone Validation Protocol:</strong> We formalize the exact review sequence you requested: 
      <code>Sprint Build ➔ Staging Deployment ➔ Live Demonstration ➔ Nourbia Team Testing & Verification ➔ Defect Corrections ➔ Formal Written Acceptance ➔ Milestone Release</code>.
    </p>
  </div>

  <!-- SECTION 1: 14 MODULES DETAILED SPECIFICATION -->
  <h2 class="section-header">
    <span>Section 1: 14 Functional Modules — Detailed Specification & Acceptance</span>
    <span class="sub">Comprehensive Functional, Administrative & Technical Definition</span>
  </h2>

  <!-- MODULE 1 -->
  <div class="module-card">
    <div class="module-card-header">
      <span class="mod-title">Module 1: Custom Full-Stack Architecture, Cloud Infrastructure & DevOps Pipeline</span>
      <span class="mod-hours-badge">30 Development Hours</span>
    </div>
    <div class="mod-body">
      <div class="mod-grid">
        <div class="mod-grid-item">
          <span class="label">Exact Functionality Included</span>
          <div class="val">Next.js 15 App Router frontend architecture, Python FastAPI REST backend, PostgreSQL relational database, Redis cache/state engine, Docker containerization, automated GitHub Actions CI/CD staging/production pipelines, SSL/TLS, and domain configuration.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">User Experience & Workflow</span>
          <div class="val">Sub-second page loads (&lt;0.8s LCP), zero layout shifts, continuous uptime, secure HTTPS encryption across all routes, automated error recovery pages (404/500).</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">Administrative Functionality</span>
          <div class="val">Health-check monitoring endpoints (<code>/api/health</code>), automated daily PostgreSQL backups, environment variable secret management via cloud console.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">Data Stored & Managed</span>
          <div class="val">System logs, API audit trails, session stores in Redis, connection pool metrics, database migration history (Alembic).</div>
        </div>
      </div>
      <div class="mod-acceptance">
        <div class="title">Objective Acceptance Criteria</div>
        <ul>
          <li>Next.js 15 and FastAPI services deployed inside Docker containers on staging server.</li>
          <li>Automated SSL certificates active with A+ security rating; PostgreSQL migrations execute cleanly with zero errors.</li>
          <li>Automated GitHub Actions pipeline triggers build and deploy on staging within &lt;3 minutes of push.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- MODULE 2 -->
  <div class="module-card">
    <div class="module-card-header">
      <span class="mod-title">Module 2: UI/UX Design System, Clean Harvest Right Aesthetic & Global Navigation</span>
      <span class="mod-hours-badge">28 Development Hours</span>
    </div>
    <div class="mod-body">
      <div class="mod-grid">
        <div class="mod-grid-item">
          <span class="label">Exact Functionality Included</span>
          <div class="val">Modern, product-first UI component library inspired by Harvest Right commercial aesthetic: high-contrast typography (Inter/Jakarta), brand color tokens (#0284c7, #0f172a, #10b981), sticky header, mega-navigation for Heritage Lines & Categories, and mobile drawer.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">User Experience & Workflow</span>
          <div class="val">Clean, intuitive browsing without clutter. Mega-menu displays visual category pills, cultural flags, food box links, B2B portal link, and community hub with 1-click access.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">Administrative Functionality</span>
          <div class="val">Admin can toggle navigation items, update announcement bar text (e.g., "Free Shipping over $75"), and configure promo banners.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">Data Stored & Managed</span>
          <div class="val">Navigation hierarchy, announcement banner states, promo banners, theme token definitions.</div>
        </div>
      </div>
      <div class="mod-acceptance">
        <div class="title">Objective Acceptance Criteria</div>
        <ul>
          <li>Mobile drawer and desktop mega-menu navigate smoothly without lag across all modern browsers (Chrome, Safari, iOS Safari, Android Chrome).</li>
          <li>Design matches Harvest Right-grade commercial clarity, visual hierarchy, and accessibility contrast standards (WCAG AA).</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- MODULE 3 -->
  <div class="module-card">
    <div class="module-card-header">
      <span class="mod-title">Module 3: Homepage, Interactive Mission & Brand Storytelling Engine</span>
      <span class="mod-hours-badge">26 Development Hours</span>
    </div>
    <div class="mod-body">
      <div class="mod-grid">
        <div class="mod-grid-item">
          <span class="label">Exact Functionality Included</span>
          <div class="val">Dynamic Hero section with dual CTAs ("Explore Products" / "Partner With Us"), Interactive 6-step service module ("Source ➔ Process ➔ Preserve ➔ Develop ➔ Package ➔ Distribute"), Freeze-drying science showcase (25-year shelf-life, 97% nutrient retention), and Cultural Provenance story ("Prove • Build • Scale").</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">User Experience & Workflow</span>
          <div class="val">Engaging scroll-driven storytelling. Interactive modules expand on hover/click to explain Nourbia's preservation standards and cultural mission.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">Administrative Functionality</span>
          <div class="val">Admin can edit hero headlines, replace hero photography, update mission bullet points, and select which featured products/boxes appear on the homepage.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">Data Stored & Managed</span>
          <div class="val">Homepage content blocks, featured product IDs, customer testimonial quotes, preservation stat counters.</div>
        </div>
      </div>
      <div class="mod-acceptance">
        <div class="title">Objective Acceptance Criteria</div>
        <ul>
          <li>All 6 interactive service modules expand and animate cleanly on both mobile touch and desktop cursor hover.</li>
          <li>Admin changes to hero copy and featured products reflect on homepage in real time without code deployment.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- MODULE 4 -->
  <div class="module-card">
    <div class="module-card-header">
      <span class="mod-title">Module 4: Cultural Product Catalog & Faceted Search Engine</span>
      <span class="mod-hours-badge">32 Development Hours</span>
    </div>
    <div class="mod-body">
      <div class="mod-grid">
        <div class="mod-grid-item">
          <span class="label">Exact Functionality Included</span>
          <div class="val">Multi-dimensional catalog supporting 20–40 launch SKUs. Faceted filtering by Cultural Heritage (Haitian, African, Latin American, Caribbean), Category (Fruits, Vegetables, Fish/Proteins, Seasonings, Staples, Prepared, Snacks), Dietary attributes (Gluten-Free, Halal, Vegan, Non-GMO), and Price Range with dynamic sorting.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">User Experience & Workflow</span>
          <div class="val">Instant filter responses (&lt;100ms) with clean URL query parameters for SEO; quick-view product modal, badge indicators (e.g., "Authentic Haitian", "25-Yr Shelf Life").</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">Administrative Functionality</span>
          <div class="val">Admin creates categories, assigns heritage tags, sets SKU availability, manages product pricing, uploads high-res photography, and toggles active/inactive display states.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">Data Stored & Managed</span>
          <div class="val">Products, SKUs, category hierarchies, heritage tags, dietary flags, price history, stock status.</div>
        </div>
      </div>
      <div class="mod-acceptance">
        <div class="title">Objective Acceptance Criteria</div>
        <ul>
          <li>Filtering simultaneously by Cultural Heritage + Category + Dietary tags accurately narrows down products with zero page reloads.</li>
          <li>Products marked "Out of Stock" display clear waitlist/inquiry badges and disable direct add-to-cart.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- MODULE 5 -->
  <div class="module-card">
    <div class="module-card-header">
      <span class="mod-title">Module 5: Product Detail Pages (PDP), Nutrition Facts & Rehydration Guides</span>
      <span class="mod-hours-badge">28 Development Hours</span>
    </div>
    <div class="mod-body">
      <div class="mod-grid">
        <div class="mod-grid-item">
          <span class="label">Exact Functionality Included</span>
          <div class="val">Harvest Right-inspired PDP layout: multi-angle zoomable gallery, interactive Nutrition Facts Panel (FDA compliant format), allergen declarations, 25-Year shelf life badge, Preparation & Rehydration Water-Ratio Guide (e.g., "Add 1 Cup boiling water, wait 8 mins"), and related cultural pairings.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">User Experience & Workflow</span>
          <div class="val">Customer reads exact culinary provenance, reviews rehydration instructions, selects quantity, views bulk-savings badges, and clicks "Add to Cart".</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">Administrative Functionality</span>
          <div class="val">Admin inputs calories, macros, serving size, net weight, water-to-product ratio, rehydration time, ingredients list, and allergen checkboxes via Admin Panel.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">Data Stored & Managed</span>
          <div class="val">Product specifications, nutrition facts data table, rehydration formulas, gallery image URLs, cross-sell product relations.</div>
        </div>
      </div>
      <div class="mod-acceptance">
        <div class="title">Objective Acceptance Criteria</div>
        <ul>
          <li>Nutrition facts panel renders cleanly formatted according to FDA structure across mobile and desktop.</li>
          <li>Rehydration instructions and allergen badges display accurately for every SKU.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- MODULE 6 -->
  <div class="module-card">
    <div class="module-card-header">
      <span class="mod-title">Module 6: Curated & Cultural Nourbia Food Box Engine</span>
      <span class="mod-hours-badge">30 Development Hours</span>
    </div>
    <div class="mod-body">
      <div class="mod-grid">
        <div class="mod-grid-item">
          <span class="label">Exact Functionality Included</span>
          <div class="val">Comprehensive Food Box Configurator supporting 3 Box Tiers (Individual/Personal, Family, Multi-Family) across 4 Cultural Heritage Profiles (Haitian, Caribbean, Latin American, West African). Transparent Itemized Manifest showing exact included SKUs, net weight, servings, and price.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">User Experience & Workflow</span>
          <div class="val">Customer selects Heritage Profile ➔ chooses Box Tier ➔ views transparent itemized breakdown (e.g., "12 Meals • 3.2 lbs • $89.00") ➔ optional slot-swap within designated category constraints ➔ adds to cart with 1 click.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">Administrative Functionality</span>
          <div class="val">Admin creates new box profiles, edits SKU allocations per box tier, sets custom box bundle pricing, defines slot replacement rules, and manages out-of-stock substitutions.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">Data Stored & Managed</span>
          <div class="val">Box templates, tier configurations, SKU slot allocation rules, net weight calculations, serving counts, bundle discounts.</div>
        </div>
      </div>
      <div class="mod-acceptance">
        <div class="title">Objective Acceptance Criteria</div>
        <ul>
          <li>All 12 combinations (3 Tiers x 4 Cultural Profiles) generate accurate itemized manifests, servings, and prices.</li>
          <li>Adding a Food Box to cart properly stores all bundled items and passes accurate total weight to shipping rate engine.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- MODULE 7 -->
  <div class="module-card">
    <div class="module-card-header">
      <span class="mod-title">Module 7: Slide-Out Cart Drawer, Multi-Step Checkout & Customer Accounts</span>
      <span class="mod-hours-badge">36 Development Hours</span>
    </div>
    <div class="mod-body">
      <div class="mod-grid">
        <div class="mod-grid-item">
          <span class="label">Exact Functionality Included</span>
          <div class="val">Persistent slide-out cart drawer supporting single SKUs and food boxes; real-time line-item quantity edits, coupon code validation engine, shipping threshold progress bar ("Add $15 for Free Shipping"), mobile-optimized multi-step checkout (Guest & Account), Google Places address autocomplete, and customer portal.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">User Experience & Workflow</span>
          <div class="val">Frictionless drawer opens without navigating away; 1-thumb checkout on mobile; customer account shows real-time order history, tracking links, and saved addresses.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">Administrative Functionality</span>
          <div class="val">Admin views customer account profiles, order histories, active cart abandonment stats, and manages promotional coupon rules.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">Data Stored & Managed</span>
          <div class="val">User profiles, encrypted passwords (bcrypt), saved delivery addresses, active carts, coupon redemption records.</div>
        </div>
      </div>
      <div class="mod-acceptance">
        <div class="title">Objective Acceptance Criteria</div>
        <ul>
          <li>Cart drawer persists across page reloads without losing items; coupon discounts apply correctly to eligible SKUs.</li>
          <li>Guest checkout seamlessly completes order; customer can opt to create account with 1 click on confirmation page.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- MODULE 8 -->
  <div class="module-card">
    <div class="module-card-header">
      <span class="mod-title">Module 8: Secure Payment Gateway Integration (Stripe Elements & Digital Invoices)</span>
      <span class="mod-hours-badge">26 Development Hours</span>
    </div>
    <div class="mod-body">
      <div class="mod-grid">
        <div class="mod-grid-item">
          <span class="label">Exact Functionality Included</span>
          <div class="val">Stripe Elements integration supporting Credit/Debit Cards, Apple Pay, Google Pay; server-side PaymentIntent orchestration, webhook state machine, duplicate-charge idempotency keys, payment failure inline error recovery, and automated PDF invoice generator.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">User Experience & Workflow</span>
          <div class="val">Instant 1-click payment with Apple Pay / Google Pay; inline card validation with zero redirects; instant order success screen with printable digital receipt.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">Administrative Functionality</span>
          <div class="val">Admin views payment status (Paid, Failed, Refunded), transaction IDs, initiates partial/full refunds directly from Admin Dashboard.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">Data Stored & Managed</span>
          <div class="val">Stripe PaymentIntent IDs, transaction status, payment method type (Card/ApplePay), payment webhook event logs (Zero raw card numbers stored).</div>
        </div>
      </div>
      <div class="mod-acceptance">
        <div class="title">Objective Acceptance Criteria</div>
        <ul>
          <li>Successful test payments in Stripe Test Mode trigger instant order creation and transition status to <code>Paid</code>.</li>
          <li>Duplicate network submissions do not cause double billing (validated via idempotency keys).</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- MODULE 9 -->
  <div class="module-card">
    <div class="module-card-header">
      <span class="mod-title">Module 9: Shipping Matrix, 50-State Fulfillment & Order Lifecycle</span>
      <span class="mod-hours-badge">28 Development Hours</span>
    </div>
    <div class="mod-body">
      <div class="mod-grid">
        <div class="mod-grid-item">
          <span class="label">Exact Functionality Included</span>
          <div class="val">50-State US shipping rate calculation matrix, ShipStation API integration, multi-carrier support (USPS Priority, UPS Ground, FedEx), Alaska/Hawaii/APO surcharge rules, automated thermal 4x6 label generation, tracking number injection, and return/replacement tracking.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">User Experience & Workflow</span>
          <div class="val">Customer selects shipping speed during checkout; receives automated dispatch email with live clickable carrier tracking URL.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">Administrative Functionality</span>
          <div class="val">Admin clicks "Create Label" in order view to generate PDF thermal shipping label and packing slip; orders automatically transition from <code>Processing</code> to <code>Shipped</code>.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">Data Stored & Managed</span>
          <div class="val">Shipping rates, weight calculation rules, tracking numbers, carrier labels (PDF), carrier shipment status logs.</div>
        </div>
      </div>
      <div class="mod-acceptance">
        <div class="title">Objective Acceptance Criteria</div>
        <ul>
          <li>Live rate calculation or configured tiered matrix accurately returns rates for continental US and Alaska/Hawaii addresses.</li>
          <li>Generating label successfully stores tracking code and triggers dispatch notification email with valid carrier link.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- MODULE 10 -->
  <div class="module-card">
    <div class="module-card-header">
      <span class="mod-title">Module 10: For Business / B2B Partner Inquiries & Lead Routing Engine</span>
      <span class="mod-hours-badge">20 Development Hours</span>
    </div>
    <div class="mod-body">
      <div class="mod-grid">
        <div class="mod-grid-item">
          <span class="label">Exact Functionality Included</span>
          <div class="val">Dedicated "For Business" Hub supporting 5 commercial channels: Retail, Wholesale, Food Service, Private Label, Bulk Ingredients. Comprehensive RFQ submission form with file/spec upload, instant digital Line Sheet PDF download engine, and automated sales lead notification routing.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">User Experience & Workflow</span>
          <div class="val">B2B buyers review commercial capabilities, download digital product catalog PDF instantly upon entering business email, or submit RFQ with volume specs.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">Administrative Functionality</span>
          <div class="val">Admin reviews incoming B2B leads, filters by business type (Wholesale, Private Label, Food Service), tracks lead status (New ➔ Contacted ➔ Qualified ➔ Closed), and exports lead CSVs.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">Data Stored & Managed</span>
          <div class="val">Company name, contact person, business email, phone, annual volume estimates, channel type, uploaded spec documents, lead status notes.</div>
        </div>
      </div>
      <div class="mod-acceptance">
        <div class="title">Objective Acceptance Criteria</div>
        <ul>
          <li>Submitting RFQ form triggers immediate email notification to Nourbia sales inbox and securely logs lead in Admin CRM.</li>
          <li>Digital Line Sheet PDF downloads instantly upon verified business form submission.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- MODULE 11 -->
  <div class="module-card">
    <div class="module-card-header">
      <span class="mod-title">Module 11: Customer & Community "Taste • Test • Shape" Operational Platform</span>
      <span class="mod-hours-badge">18 Development Hours</span>
    </div>
    <div class="mod-body">
      <div class="mod-grid">
        <div class="mod-grid-item">
          <span class="label">Exact Functionality Included</span>
          <div class="val">Interactive Community Co-Creation Hub: Cultural Food Request form ("Tell us the cultural dishes you miss"), Structured Flavor & Authenticity Feedback ratings (1–5 stars on Authenticity, Rehydration Texture, Taste), SKU Wishlist suggestion engine, and admin demand aggregation reports.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">User Experience & Workflow</span>
          <div class="val">Customers actively participate in food innovation, vote on proposed cultural recipes, submit product ideas, and provide verified review feedback.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">Administrative Functionality</span>
          <div class="val">Admin reviews feedback submissions, aggregates cultural demand rankings (e.g., "#1 Requested: Haitian Diri ak Djon Djon"), and exports R&D demand reports.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">Data Stored & Managed</span>
          <div class="val">Community suggestions, cultural origin tags, authenticity ratings, feedback comments, customer votes, R&D demand tallies.</div>
        </div>
      </div>
      <div class="mod-acceptance">
        <div class="title">Objective Acceptance Criteria</div>
        <ul>
          <li>Customer can submit cultural food requests with dish name, cultural origin, and key ingredients.</li>
          <li>Admin dashboard aggregates feedback and ranks requested dishes by community interest and frequency.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- MODULE 12 -->
  <div class="module-card">
    <div class="module-card-header">
      <span class="mod-title">Module 12: Comprehensive Administration Dashboard & Operations Console</span>
      <span class="mod-hours-badge">38 Development Hours</span>
    </div>
    <div class="mod-body">
      <div class="mod-grid">
        <div class="mod-grid-item">
          <span class="label">Exact Functionality Included</span>
          <div class="val">Complete self-service Admin Web Portal: Product & SKU management, Inventory stock controls, Nutrition facts manager, Food Box bundle editor, Live Order processing console, 1-Click packing slips, Tracking assignment, Customer accounts manager, Coupon creator, and Sales reports with CSV/PDF exports.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">User Experience & Workflow</span>
          <div class="val">Nourbia staff manage 100% of day-to-day operations with zero developer dependence; fast search, bulk product status toggles, and visual sales graphs.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">Administrative Functionality</span>
          <div class="val">Role-based access (Admin, Fulfillment Manager), comprehensive CRUD across all catalog, orders, customers, coupons, and content entities.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">Data Stored & Managed</span>
          <div class="val">Staff user credentials, access permissions, audit logs, catalog datasets, order transaction records, export job histories.</div>
        </div>
      </div>
      <div class="mod-acceptance">
        <div class="title">Objective Acceptance Criteria</div>
        <ul>
          <li>Admin can create a new SKU, upload photos, set nutrition specs, and publish it live without developer assistance.</li>
          <li>Orders can be filtered by status (Pending, Paid, Shipped), printed as packing slips, and exported to CSV.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- MODULE 13 -->
  <div class="module-card">
    <div class="module-card-header">
      <span class="mod-title">Module 13: Multilingual Framework (5 Languages) & Internationalized SEO Engine</span>
      <span class="mod-hours-badge">28 Development Hours</span>
    </div>
    <div class="mod-body">
      <div class="mod-grid">
        <div class="mod-grid-item">
          <span class="label">Exact Functionality Included</span>
          <div class="val">Full 5-language localization: English (EN), Haitian Creole (HT), French (FR), Spanish (ES), Portuguese (PT). Language switcher in header/footer, localized routing (<code>/ht/...</code>, <code>/fr/...</code>), admin database translation fields for products and food boxes, multilingual transactional emails, and hreflang SEO meta tags.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">User Experience & Workflow</span>
          <div class="val">Instant language toggle preserves current page context; customers browse products, rehydration instructions, and checkout in their native cultural language.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">Administrative Functionality</span>
          <div class="val">Admin inputs localized titles, descriptions, and preparation guides per language directly in the product/box editor; static UI labels managed via central dictionary.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">Data Stored & Managed</span>
          <div class="val">Localized product copy tables, language preference cookies, i18n translation dictionary files, multilingual sitemaps.</div>
        </div>
      </div>
      <div class="mod-acceptance">
        <div class="title">Objective Acceptance Criteria</div>
        <ul>
          <li>Switching between English, Haitian Creole, French, Spanish, and Portuguese correctly updates all UI text, product descriptions, and navigation.</li>
          <li>Search engine bots receive valid <code>hreflang</code> alternate tags and localized XML sitemaps for all 5 languages.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- MODULE 14 -->
  <div class="module-card">
    <div class="module-card-header">
      <span class="mod-title">Module 14: Quality Assurance, Security Hardening & Cloud Production Launch</span>
      <span class="mod-hours-badge">60 Hours Total (20 Base + 40 Complimentary QA)</span>
    </div>
    <div class="mod-body">
      <div class="mod-grid">
        <div class="mod-grid-item">
          <span class="label">Exact Functionality Included</span>
          <div class="val">End-to-end regression testing, cross-device mobile/tablet/desktop verification, payment webhook load testing, OWASP Top 10 security audit (SQL injection, XSS, CSRF, rate-limiting), production cloud provisioning in Nourbia's accounts, DNS/SSL handover, and staff operational training.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">User Experience & Workflow</span>
          <div class="val">Flawless, bug-free launch with zero transaction drop-offs and rock-solid mobile responsiveness.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">Administrative Functionality</span>
          <div class="val">Nourbia team receives complete administrative training session (recorded video) and operational handbook.</div>
        </div>
        <div class="mod-grid-item">
          <span class="label">Data Stored & Managed</span>
          <div class="val">Automated test suites (PyTest, Playwright/Cypress), security scan reports, deployment checklists.</div>
        </div>
      </div>
      <div class="mod-acceptance">
        <div class="title">Objective Acceptance Criteria</div>
        <ul>
          <li>All automated test suites pass with 100% success; zero critical or high-severity vulnerabilities in security scan.</li>
          <li>Staging UAT sign-off completed by Ernso Pierre prior to official DNS cutover to live production domain.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="page-break"></div>

  <!-- SECTION 2: SPECIAL DEEP-DIVE BLUEPRINTS -->
  <h2 class="section-header">
    <span>Section 2: Deep-Dive Technical Blueprints & Operational Architecture</span>
    <span class="sub">Detailed Resolution of Key Stakeholder Queries</span>
  </h2>

  <!-- 2.1 FOOD BOX ENGINE -->
  <h3 class="sub-header">2.1 Nourbia Food Box Engine Architecture & Allocation Rules</h3>
  <p>
    The Food Box Engine is designed as a core revenue driver, allowing Nourbia to bundle culturally resonant, high-margin freeze-dried SKUs into convenient multi-meal boxes:
  </p>

  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 18%;">Box Tier</th>
        <th style="width: 20%;">Target Audience & Servings</th>
        <th style="width: 32%;">SKU Allocation & Category Composition</th>
        <th style="width: 30%;">Configurability & Manifest</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Individual / Personal Box</strong></td>
        <td>1 Person • 6–8 Prepared Meals / Servings (~1.5–2.0 lbs)</td>
        <td>2x Main Cultural Dishes, 2x Vegetables/Sides, 1x Fruit Pack, 1x Seasoning/Sauce Pack</td>
        <td>Pre-curated with 1 optional side item swap; transparent itemized manifest on PDP & invoice.</td>
      </tr>
      <tr>
        <td><strong>Family Box</strong></td>
        <td>2–4 People • 18–24 Prepared Meals / Servings (~4.5–6.0 lbs)</td>
        <td>6x Main Cultural Dishes, 4x Vegetables/Sides, 3x Fruit Packs, 2x Seasonings/Staples</td>
        <td>Pre-curated with up to 2 item swaps within category rules; automated weight calculation.</td>
      </tr>
      <tr>
        <td><strong>Multi-Family / Emergency Box</strong></td>
        <td>4–8 People • 45–60 Prepared Meals / Servings (~12–15 lbs)</td>
        <td>15x Main Dishes, 10x Vegetables, 8x Fruits, 5x Staples (Rice/Beans), 4x Cultural Seasonings</td>
        <td>Heavy-duty bundle packing; custom shipping rules with flat-rate heavy freight option.</td>
      </tr>
    </tbody>
  </table>

  <div class="flow-diagram">
FOOD BOX ORDER & INVENTORY ALLOCATION WORKFLOW:
Customer selects: [Haitian Heritage Box - Family Tier] ($119.00 • 20 Servings)
       │
       ▼
System Validates Real-Time Inventory for Bundled SKUs:
├─ SKU-HT-01 (Diri ak Djon Djon): [IN STOCK - 42 units available] ──► Allocated
├─ SKU-HT-04 (Griot Pork Cubes):  [IN STOCK - 18 units available] ──► Allocated
└─ SKU-HT-08 (Pikliz Seasoning):  [OUT OF STOCK] ────────────────► Automated Substitution Engine:
                                                                  ├─ Option A: Auto-swap with pre-defined equal substitute (SKU-HT-09)
                                                                  └─ Option B: Customer prompted with 1-click alternative selection
       │
       ▼
Dynamic Box Manifest Generated ──► Added to Cart Drawer as Single Bundle Entity with Child SKU Pick-List
  </div>

  <p><strong>Out-of-Stock Handling:</strong> In the admin panel, Nourbia staff can set a "Fallback Replacement SKU" for every slot in a food box. If an item runs out of stock, the system automatically uses the fallback or displays an intuitive "Choose your replacement" selector on the PDP, preventing abandoned purchases.</p>

  <!-- 2.2 B2B / BUSINESS PLATFORM -->
  <h3 class="sub-header">2.2 B2B & Wholesale Partner Hub Architecture</h3>
  <p>
    The "For Business" Hub is engineered to capture high-value commercial sales leads across 5 commercial verticals, with an architecture designed to easily upgrade into a full self-service wholesale ordering portal in future phases:
  </p>

  <div class="mod-grid" style="margin-top: 10px;">
    <div class="executive-card" style="margin-bottom: 0;">
      <h4 style="margin: 0 0 6px 0; color: #0284c7; font-size: 12px;">B2B Commercial Channels Covered</h4>
      <ul style="margin: 0; padding-left: 16px; font-size: 11px; color: #334155;">
        <li><strong>Retail & Supermarkets:</strong> Branded cultural retail pouch distribution.</li>
        <li><strong>Wholesale Distributors:</strong> Case-pack purchasing and pallet pricing.</li>
        <li><strong>Food Service & Restaurants:</strong> Commercial kitchen freeze-dried bulk ingredients.</li>
        <li><strong>Private Label & Co-Packing:</strong> Custom recipe freeze-drying and white-labeling.</li>
        <li><strong>Bulk Ingredients & NGOs:</strong> Disaster relief, institutional cultural food boxes.</li>
      </ul>
    </div>
    <div class="executive-card" style="margin-bottom: 0;">
      <h4 style="margin: 0 0 6px 0; color: #0284c7; font-size: 12px;">Operational Lead-to-Sale Workflow</h4>
      <ul style="margin: 0; padding-left: 16px; font-size: 11px; color: #334155;">
        <li><strong>Instant Line Sheet PDF Download:</strong> Buyer inputs email/company ➔ Instant spec sheet download ➔ Lead logged in Admin CRM.</li>
        <li><strong>Custom RFQ Submission:</strong> Upload custom specs, target volume, and delivery timeline requirements.</li>
        <li><strong>Automated Lead Routing:</strong> Real-time alert dispatched to <code>epierre@nourbiafoods.com</code> and sales team.</li>
        <li><strong>Future Ready:</strong> Database schema includes <code>is_b2b_approved</code> and <code>wholesale_tier</code> flags ready for future password-protected B2B wholesale checkout.</li>
      </ul>
    </div>
  </div>

  <!-- 2.3 50-STATE SHIPPING WORKFLOW -->
  <h3 class="sub-header">2.3 End-to-End Shipping & 50-State Fulfillment Lifecycle</h3>
  <div class="flow-diagram">
COMPLETE ORDER FULFILLMENT & LIFECYCLE STATE MACHINE:
[Customer Places Order] ──► [Stripe Authorizes & Captures Payment]
                                         │
                                         ▼ Webhook Updates Status to 'Paid'
                            [Order Appears in Admin Dispatch Console]
                                         │
                                         ▼ Staff clicks 'Print Packing Slip' & 'Create Shipping Label'
                            [ShipStation API Generates 4x6 Thermal Label & Tracking Code]
                                         │
                                         ▼ Status transitions to 'Shipped'
                            [Automated Customer Email Dispatched with Carrier Tracking URL]
                                         │
                                         ▼ Webhook receives Carrier Delivery Event
                            [Order Status Marked 'Delivered' • Review Request Sent]
  </div>

  <p><strong>Shipping Rate Calculation Engine:</strong> Supports both <strong>Live Carrier Rates</strong> (via ShipStation / EasyPost lookup for USPS Priority, UPS Ground, FedEx) and <strong>Configurable Rule Matrix</strong> (e.g., Free Shipping on orders &gt;$75 in continental US; $14.99 flat surcharge for Alaska, Hawaii, and military APO/FPO addresses).</p>

  <!-- 2.4 TASTE TEST SHAPE -->
  <h3 class="sub-header">2.4 "Taste • Test • Shape" Operational Co-Creation Hub</h3>
  <p>
    Rather than a passive feedback form, this module functions as an active R&D demand aggregation engine:
  </p>
  <ul>
    <li><strong>Cultural Flavor & Dish Submissions:</strong> Diaspora community members submit missing cultural dishes, specifying cultural provenance, traditional spices, and dietary preferences.</li>
    <li><strong>Structured 3-Point Sample Evaluation:</strong> Verified customers review sample batches across 3 structured dimensions: <em>Authenticity Score (1–5)</em>, <em>Rehydration Texture & Ease (1–5)</em>, and <em>Overall Flavor (1–5)</em>.</li>
    <li><strong>Admin R&D Prioritization Matrix:</strong> Admin dashboard aggregates submissions into a prioritized demand leaderboard (e.g., "Top 5 Caribbean Requests this Month"), providing empirical market data before Nourbia commits to commercial production runs.</li>
  </ul>

  <!-- 2.5 ADMIN DASHBOARD WIREFRAME & INDEPENDENCE -->
  <h3 class="sub-header">2.5 Administration Dashboard Layout & Operational Independence</h3>
  <p>
    The Admin Dashboard is engineered for complete operational autonomy. Nourbia staff will manage all aspects of products, prices, food boxes, inventory, orders, coupons, and content without requiring technical support:
  </p>

  <div class="flow-diagram">
ADMINISTRATION DASHBOARD CONCEPTUAL WIREFRAME:
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│ NOURBIA FOODS™ Operations Console                 [Search SKU / Order...]   👤 Ernso (Admin)    │
├─────────────────┬───────────────────────────────────────────────────────────────────────────────┤
│ 📊 Dashboard    │ TODAY'S OVERVIEW                                                              │
│ 📦 Products     │ Sales: $4,280.00 | Orders: 34 | Pending Shipments: 8 | B2B RFQs: 3            │
│ 🍱 Food Boxes   ├───────────────────────────────────────────────────────────────────────────────┤
│ 🛒 Live Orders  │ RECENT ORDERS (DISPATCH CONSOLE)                                              │
│ 👥 Customers    │ Order #1042 • Pierre E. • 1x Haitian Family Box • $119.00 • [Create Label]    │
│ 🏢 B2B Leads    │ Order #1041 • Marie K.  • 2x Griot Pork SKUs   • $38.00  • [Print Slip]       │
│ 💬 Community R&D├───────────────────────────────────────────────────────────────────────────────┤
│ 🏷️ Coupons     │ QUICK CATALOG & INVENTORY CONTROLS                                            │
│ 🌐 Languages    │ [ + Add New Product ] [ + Configure Food Box ] [ Export Sales CSV ]           │
│ ⚙️ Settings     │ Active SKUs: 32 | Out of Stock: 2 | Total Registered Customers: 418           │
└─────────────────┴───────────────────────────────────────────────────────────────────────────────┘
  </div>

  <div class="page-break"></div>

  <!-- 2.6 MULTILINGUAL ARCHITECTURE -->
  <h3 class="sub-header">2.6 Multilingual Architecture & Internationalized SEO</h3>
  <p>
    To honor Nourbia's mission of serving diverse cultural diaspora communities, the platform provides comprehensive native localization across 5 target languages:
  </p>

  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 20%;">Language</th>
        <th style="width: 15%;">Locale Code</th>
        <th style="width: 35%;">URL Routing Structure</th>
        <th style="width: 30%;">Translation Management</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>English (Primary)</strong></td>
        <td><code>en-US</code></td>
        <td><code>nourbiafoods.com/products/...</code></td>
        <td>Default database fields & UI dictionary.</td>
      </tr>
      <tr>
        <td><strong>Haitian Creole (Kreyòl)</strong></td>
        <td><code>ht-HT</code></td>
        <td><code>nourbiafoods.com/ht/products/...</code></td>
        <td>Dedicated localized DB columns in Admin Console.</td>
      </tr>
      <tr>
        <td><strong>French</strong></td>
        <td><code>fr-FR</code></td>
        <td><code>nourbiafoods.com/fr/products/...</code></td>
        <td>Dedicated localized DB columns in Admin Console.</td>
      </tr>
      <tr>
        <td><strong>Spanish</strong></td>
        <td><code>es-US</code></td>
        <td><code>nourbiafoods.com/es/products/...</code></td>
        <td>Dedicated localized DB columns in Admin Console.</td>
      </tr>
      <tr>
        <td><strong>Portuguese</strong></td>
        <td><code>pt-BR</code></td>
        <td><code>nourbiafoods.com/pt/products/...</code></td>
        <td>Dedicated localized DB columns in Admin Console.</td>
      </tr>
    </tbody>
  </table>

  <p><strong>Multilingual SEO Implementation:</strong> Every product and food box page automatically renders canonical <code>&lt;link rel="alternate" hreflang="ht" href="..."&gt;</code> tags and submits localized multi-language XML sitemaps to Google Search Console to rank natively in Creole, French, Spanish, Portuguese, and English.</p>

  <!-- 2.7 QUALITY ASSURANCE & UAT MATRIX -->
  <h3 class="sub-header">2.7 Comprehensive Quality Assurance & Acceptance Testing Charter</h3>
  <p>
    Our quality assurance program guarantees enterprise stability prior to public launch, leveraging the <strong>40 Complimentary QA Hours</strong> included in the engagement:
  </p>

  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 22%;">Testing Domain</th>
        <th style="width: 48%;">Verification Scope & Methodologies</th>
        <th style="width: 30%;">Pass / Acceptance Criteria</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>1. Payment & Checkout</strong></td>
        <td>Stripe 3D-Secure cards, Apple Pay, Google Pay, failed card error handling, duplicate click prevention, webhook event verification.</td>
        <td>100% accurate charge authorization, zero duplicate charges, instant PDF invoice generation.</td>
      </tr>
      <tr>
        <td><strong>2. Shipping & Labels</strong></td>
        <td>Live ShipStation carrier rate lookup, weight aggregation of single SKUs + multi-item food boxes, APO/FPO and AK/HI address rules.</td>
        <td>Thermal 4x6 label generated with valid tracking code and dispatched via automated email.</td>
      </tr>
      <tr>
        <td><strong>3. Cross-Device Responsive</strong></td>
        <td>Testing across real physical devices: iPhone (Safari), Android (Chrome), iPad/Tablet, Mac/Windows Desktops (Chrome, Edge, Safari, Firefox).</td>
        <td>Fluid touch targets (&gt;48px), zero horizontal scrolling, fast &lt;1.0s page renders.</td>
      </tr>
      <tr>
        <td><strong>4. Multilingual Integrity</strong></td>
        <td>Verifying full translation continuity across all 5 languages during PDP browsing, Cart, Checkout, and Order confirmation emails.</td>
        <td>Zero missing translation keys (no fallback error strings visible to customer).</td>
      </tr>
      <tr>
        <td><strong>5. Security & Penetration</strong></td>
        <td>OWASP Top 10 automated vulnerability scanning, SQL injection protection, XSS sanitation, rate limiting on auth and RFQ forms.</td>
        <td>Zero Critical or High severity security vulnerabilities identified.</td>
      </tr>
    </tbody>
  </table>

  <!-- 2.8 THIRD PARTY OPERATING COSTS -->
  <h3 class="sub-header">2.8 Itemized Third-Party Operating Costs & Environment Infrastructure</h3>
  <p>
    Below is the complete, transparent breakdown of external operating costs outside the $6,000 ITPrior development investment. As recommended, we configure a <strong>Cost-Optimized Cloud Architecture</strong> to minimize monthly overhead while maintaining enterprise performance:
  </p>

  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 25%;">Service & Provider</th>
        <th style="width: 35%;">Purpose & Scope</th>
        <th style="width: 20%;">Estimated Monthly Cost</th>
        <th style="width: 20%;">Billing Relationship</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Cloud VPS Hosting</strong><br><small>DigitalOcean / Hetzner</small></td>
        <td>Docker containers, Next.js 15 SSR, FastAPI Backend, Redis Cache & PostgreSQL DB</td>
        <td><strong>$12.00 – $24.00 / mo</strong></td>
        <td>Billed directly to Nourbia's cloud card</td>
      </tr>
      <tr>
        <td><strong>ShipStation Integration</strong><br><small>ShipStation API</small></td>
        <td>Multi-carrier shipping rates, USPS/UPS/FedEx label printing & tracking sync</td>
        <td><strong>$9.99 / mo</strong><br><small>(Starter Tier: up to 50 shipments)</small></td>
        <td>Billed directly to Nourbia</td>
      </tr>
      <tr>
        <td><strong>Transactional Email</strong><br><small>SendGrid / Postmark</small></td>
        <td>Order confirmation emails, tracking notifications, B2B lead alerts</td>
        <td><strong>$0.00 – $15.00 / mo</strong><br><small>(Free tier covers first 3,000 emails)</small></td>
        <td>Billed directly to Nourbia</td>
      </tr>
      <tr>
        <td><strong>Stripe Payment Gateway</strong><br><small>Stripe Inc.</small></td>
        <td>Credit/Debit cards, Apple Pay, Google Pay merchant processing</td>
        <td><strong>2.9% + $0.30</strong><br><small>per successful transaction (No monthly fee)</small></td>
        <td>Deducted automatically per sale</td>
      </tr>
      <tr>
        <td><strong>SSL & Global CDN</strong><br><small>Cloudflare</small></td>
        <td>DDoS protection, Edge CDN caching, SSL encryption certificate</td>
        <td><strong>$0.00 / mo (FREE)</strong><br><small>(Standard Cloudflare Tier)</small></td>
        <td>Free tier included</td>
      </tr>
      <tr>
        <td><strong>Address Autocomplete</strong><br><small>Google Maps API</small></td>
        <td>Checkout address autocomplete & validation</td>
        <td><strong>$0.00 / mo</strong><br><small>(Covered under Google's $200 free monthly credit)</small></td>
        <td>Direct Google account</td>
      </tr>
      <tr>
        <td><strong>Domain Registration</strong><br><small>GoDaddy / Namecheap</small></td>
        <td>Domain registration for <code>nourbiafoods.com</code></td>
        <td><strong>~$15.00 / year</strong></td>
        <td>Nourbia existing asset</td>
      </tr>
      <tr style="background: #f1f5f9; font-weight: 700;">
        <td colspan="2"><strong>ESTIMATED TOTAL MONTHLY OPERATING EXPENSE</strong></td>
        <td colspan="2" style="color: #0284c7; font-size: 12.5px;"><strong>~$35.00 – $55.00 / month</strong></td>
      </tr>
    </tbody>
  </table>

  <!-- 2.9 SOURCE CODE OWNERSHIP -->
  <h3 class="sub-header">2.9 100% Intellectual Property & Source Code Ownership Charter</h3>
  <div class="alert-box">
    <strong>Binding Ownership Guarantee:</strong> Upon final milestone settlement, <strong>100% of the entire platform intellectual property transfers unconditionally to Nourbia Foods Inc.</strong> This includes all Git source code repositories (Next.js frontend, FastAPI backend), PostgreSQL schema scripts, Docker configuration files, CI/CD deployment pipelines, and OpenAPI documentation. All production servers, Stripe accounts, ShipStation accounts, and DNS domains remain strictly in Nourbia's name with zero vendor lock-in. Nourbia retains the full legal and technical freedom to maintain, modify, or transfer development to any internal or external engineering team in the future.
  </div>

  <!-- SIGN-OFF & ACCEPTANCE -->
  <div class="signoff-grid">
    <div class="sign-box">
      <h6>Prepared & Submitted On Behalf Of ITPrior Solutions</h6>
      <div class="sign-line"></div>
      <div class="sign-sub">
        <strong>Siddhartha E.</strong> • Lead Technical Architect<br>
        ITPrior Solutions • {BASE_DIR} • March 24, 2026
      </div>
    </div>
    <div class="sign-box">
      <h6>Accepted & Confirmed On Behalf Of Nourbia Foods Inc.</h6>
      <div class="sign-line"></div>
      <div class="sign-sub">
        <strong>Ernso Pierre</strong> • Founder & Chief Executive Officer<br>
        Nourbia Foods Inc. • epierre@nourbiafoods.com
      </div>
    </div>
  </div>

  <div class="footer-note">
    <div><strong>ITPrior Solutions</strong> — Premier Enterprise Engineering Agency • www.itprior.com</div>
    <div>CONFIDENTIAL & PROPRIETARY — PREPARED EXCLUSIVELY FOR NOURBIA FOODS INC.</div>
  </div>

</div>
</body>
</html>
"""
    return html


def generate_markdown_specification() -> str:
    """Generates comprehensive markdown mirror of the specification."""
    md = """# NOURBIA FOODS™ — FUNCTIONAL REQUIREMENTS & ACCEPTANCE CRITERIA SPECIFICATION
**Complete Technical Architecture, Module Definitions & Operational Blueprint**
*Prepared by ITPrior Solutions for Ernso Pierre (Founder & CEO, Nourbia Foods Inc.)*
*Reference Standard: Harvest Right (`harvestright.com`) Commercial & Product Presentation*

---

## Executive Response & Alignment
Nourbia Foods is building a long-term, enterprise-grade digital commerce ecosystem. This document formally defines the **Functional Requirements, Technical Architecture, and Acceptance Criteria** for all 14 proposal modules and key operational workflows:

- **Agile Milestone Verification Protocol**: `Build ➔ Staging ➔ Live Demo ➔ Nourbia Team UAT ➔ Corrections ➔ Formal Written Acceptance ➔ Milestone Release`.
- **100% Source Code & Infrastructure Ownership**: Delivered in Nourbia's own cloud accounts with zero vendor lock-in.
- **Cost-Optimized Operating Stack**: ~$35–$55/month total recurring operating expenses.

---

## Section 1: 14 Functional Modules Detailed Breakdown

### Module 1: Custom Full-Stack Architecture, Cloud Infrastructure & DevOps Pipeline (30 Hours)
- **Included**: Next.js 15 App Router frontend, Python FastAPI backend, PostgreSQL relational database, Redis cache/telemetry, Docker containerization, GitHub Actions CI/CD staging/production pipelines, SSL/TLS, and automated daily database backups.
- **UX**: Sub-second page loads (<0.8s LCP), zero layout shifts, continuous uptime, secure HTTPS encryption across all routes.
- **Admin**: Health check monitoring (`/api/health`), database connection pooling metrics, automated backup status.
- **Acceptance Criteria**: Docker containers deployed on staging; automated SSL active with A+ rating; GitHub Actions CI/CD pipeline deploys automatically upon code commit.

### Module 2: UI/UX Design System, Clean Harvest Right Aesthetic & Global Navigation (28 Hours)
- **Included**: Product-centric UI design tokens (#0284c7 brand blue, #0f172a slate, #10b981 emerald), sticky navigation header, mega-menu showcasing Heritage Collections & Categories, mobile drawer navigation, announcement bar.
- **Acceptance Criteria**: Smooth mobile drawer navigation; WCAG AA accessibility contrast compliance; Harvest Right-grade commercial clarity.

### Module 3: Homepage, Interactive Mission & Brand Storytelling Engine (26 Hours)
- **Included**: Dynamic hero banner with dual CTAs, interactive 6-step service module (*Source ➔ Process ➔ Preserve ➔ Develop ➔ Package ➔ Distribute*), freeze-drying preservation science showcase (25-year shelf life, 97% nutrient retention), provenance storytelling (*Prove • Build • Scale*).
- **Acceptance Criteria**: All 6 service modules animate cleanly on mobile and desktop; admin can update hero headlines and featured products without code changes.

### Module 4: Cultural Product Catalog & Faceted Search Engine (32 Hours)
- **Included**: Catalog supporting 20–40 launch SKUs; faceted filtering by Cultural Heritage (Haitian, African, Latin American, Caribbean), Category (Fruits, Veg, Fish/Proteins, Seasonings, Staples, Prepared, Snacks), Dietary tags, and Price Range with instant client-side updates and SEO-friendly query parameters.
- **Acceptance Criteria**: Multi-facet filtering responds in <100ms; out-of-stock items display clear badges and disable checkout.

### Module 5: Product Detail Pages (PDP), Nutrition Facts & Rehydration Guides (28 Hours)
- **Included**: Multi-angle zoomable photo gallery, FDA-structured Nutrition Facts Panel, allergen declarations, 25-Year shelf-life badge, interactive Rehydration & Culinary Preparation instructions (water ratios, boiling time), related cultural food pairings.
- **Acceptance Criteria**: FDA-style nutrition table renders cleanly across devices; preparation instructions accurately reflect SKU formulas.

### Module 6: Curated & Cultural Nourbia Food Box Engine (30 Hours)
- **Included**: Configurator supporting 3 Box Tiers (Individual/Personal, Family, Multi-Family) across 4 Cultural Heritage Profiles (Haitian, Caribbean, Latin American, West African); transparent itemized manifests showing exact SKUs, net weight, servings, and price; out-of-stock substitution engine.
- **Acceptance Criteria**: All 12 tier/cultural combinations generate accurate manifests, servings, and prices; bundle adds to cart with accurate aggregate weight for shipping.

### Module 7: Slide-Out Cart Drawer, Multi-Step Checkout & Customer Accounts (36 Hours)
- **Included**: Persistent slide-out cart drawer supporting single SKUs and food boxes; real-time line-item quantity edits, coupon validation engine, free-shipping progress indicator, mobile-optimized checkout (Guest & Account), Google Places address autocomplete, customer account portal.
- **Acceptance Criteria**: Cart drawer persists across browser reloads; guest checkout operates seamlessly; customer can view live order tracking in account portal.

### Module 8: Secure Payment Gateway Integration (Stripe Elements & Digital Invoices) (26 Hours)
- **Included**: Stripe Elements (Credit/Debit Cards, Apple Pay, Google Pay), server-side PaymentIntent orchestration, webhook order state machine, duplicate-charge idempotency keys, payment failure inline error recovery, automated PDF invoice generation.
- **Acceptance Criteria**: Stripe test payments transition orders to `Paid`; duplicate network clicks do not cause double billing.

### Module 9: Shipping Matrix, 50-State Fulfillment & Order Lifecycle (28 Hours)
- **Included**: 50-State US shipping rate calculation matrix, ShipStation API integration, multi-carrier support (USPS Priority, UPS Ground, FedEx), Alaska/Hawaii/APO surcharge rules, automated 4x6 thermal label generation, tracking number injection, return/replacement handling.
- **Acceptance Criteria**: Live rate lookup or configured tiered matrix accurately returns rates; generating label updates status to `Shipped` and sends customer tracking email.

### Module 10: For Business / B2B Partner Inquiries & Lead Routing Engine (20 Hours)
- **Included**: Dedicated B2B Hub supporting 5 commercial channels (Retail, Wholesale, Food Service, Private Label, Bulk Ingredients); RFQ form with spec uploads, instant digital Line Sheet PDF download engine, automated sales lead email routing.
- **Acceptance Criteria**: Submitting RFQ sends instant email alert to `epierre@nourbiafoods.com` and logs lead in Admin CRM; Line Sheet PDF downloads immediately.

### Module 11: Customer & Community "Taste • Test • Shape" Operational Platform (18 Hours)
- **Included**: Community cultural food request form, structured 3-point sample evaluation ratings (Authenticity, Rehydration Texture, Flavor), SKU wishlist suggestions, admin demand aggregation leaderboard for R&D prioritization.
- **Acceptance Criteria**: Submissions successfully log in database and aggregate into a demand leaderboard in the admin panel.

### Module 12: Comprehensive Administration Dashboard & Operations Console (38 Hours)
- **Included**: 100% self-service Admin Web Portal: Product & SKU management, inventory stock controls, nutrition facts manager, food box bundle editor, live order dispatch console, 1-click packing slips, customer manager, coupon creator, and sales reports with CSV exports.
- **Acceptance Criteria**: Admin can create new SKUs, modify food boxes, and manage orders with zero developer assistance.

### Module 13: Multilingual Framework (5 Languages) & Internationalized SEO Engine (28 Hours)
- **Included**: Complete native localization across English, Haitian Creole (Kreyòl), French, Spanish, and Portuguese. Localized URL routing (`/ht/...`, `/fr/...`), admin database translation fields for products and food boxes, multilingual transactional emails, hreflang SEO meta tags.
- **Acceptance Criteria**: Language switcher updates all UI and catalog content; search engines receive valid `hreflang` tags and localized XML sitemaps.

### Module 14: Quality Assurance, Security Hardening & Cloud Production Launch (60 Hours Total: 20 Base + 40 Complimentary QA)
- **Included**: End-to-end regression testing, cross-device physical testing (iPhone, Android, iPad, Mac, Windows), payment webhook load testing, OWASP Top 10 security audit, production cloud provisioning in Nourbia's accounts, DNS/SSL handover, staff training.
- **Acceptance Criteria**: 100% automated test suite pass rate; zero critical/high security vulnerabilities; formal UAT sign-off completed.

---

## Section 2: Deep-Dive Operational Blueprints

### 2.1 Nourbia Food Box Engine Matrix
| Box Tier | Servings & Weight | Composition | Customization & Manifest |
| :--- | :--- | :--- | :--- |
| **Individual Box** | 1 Person • 6–8 Meals (~1.5–2 lbs) | 2 Mains, 2 Veg/Sides, 1 Fruit, 1 Seasoning | Pre-curated, 1 item swap allowed |
| **Family Box** | 2–4 People • 18–24 Meals (~4.5–6 lbs) | 6 Mains, 4 Veg/Sides, 3 Fruits, 2 Seasonings | Up to 2 item swaps within category |
| **Multi-Family Box** | 4–8 People • 45–60 Meals (~12–15 lbs) | 15 Mains, 10 Veg, 8 Fruits, 5 Staples, 4 Seasonings | Heavy-duty bundle packing rules |

### 2.2 Third-Party Operating Costs Breakdown
- **Cloud VPS Hosting (DigitalOcean/Hetzner)**: $12.00 – $24.00 / month
- **ShipStation API Integration**: $9.99 / month
- **Transactional Email (SendGrid/Postmark)**: $0.00 – $15.00 / month (Free tier covers 3,000 emails)
- **Stripe Gateway**: 2.9% + $0.30 per transaction (No monthly fee)
- **Cloudflare CDN & SSL**: $0.00 / month (Free tier)
- **Google Maps API**: $0.00 / month (Covered by $200 free credit)
- **Total Estimated Operating Cost**: **~$35.00 – $55.00 / month**

### 2.3 Source Code & Data Ownership Charter
Upon final milestone completion, **100% full intellectual property and source code ownership** transfers to Nourbia Foods Inc. with zero vendor lock-in.
"""
    return md


def main():
    print("=================================================================")
    print("Generating NOURBIA FOODS™ Comprehensive FRS & Acceptance Document")
    print("=================================================================")

    # 1. Write Markdown
    print(f"Writing Markdown specification: {OUTPUT_MD}")
    md_content = generate_markdown_specification()
    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write(md_content)
    print("✓ Markdown written successfully.")

    # 2. Write HTML
    print(f"Writing HTML document: {OUTPUT_HTML}")
    logo_b64 = get_base64_logo()
    html_content = build_html_content(logo_b64)
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html_content)
    print("✓ HTML written successfully.")

    # 3. Compile PDF via Headless Chrome
    chrome_exe = find_chrome_executable()
    print(f"Compiling PDF via Headless Chrome: {chrome_exe}")
    cmd = [
        chrome_exe,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={OUTPUT_PDF}",
        OUTPUT_HTML
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"✓ PDF successfully compiled: {OUTPUT_PDF}")
    else:
        print(f"✗ PDF generation error: {res.stderr}")

    # 4. Sync files to itprior-quotes/Nourbia if directory exists
    if os.path.exists(QUOTES_NOURBIA_DIR):
        print(f"Syncing documents to {QUOTES_NOURBIA_DIR} ...")
        quotes_pdf = os.path.join(QUOTES_NOURBIA_DIR, "Nourbia_Foods_ITPrior_Functional_Requirements_and_Acceptance.pdf")
        quotes_html = os.path.join(QUOTES_NOURBIA_DIR, "Nourbia_Foods_ITPrior_Functional_Requirements_and_Acceptance.html")
        quotes_md = os.path.join(QUOTES_NOURBIA_DIR, "Nourbia_Foods_ITPrior_Functional_Requirements_and_Acceptance.md")
        with open(quotes_html, "w", encoding="utf-8") as f:
            f.write(html_content)
        with open(quotes_md, "w", encoding="utf-8") as f:
            f.write(md_content)
        if os.path.exists(OUTPUT_PDF):
            import shutil
            shutil.copyfile(OUTPUT_PDF, quotes_pdf)
        print("✓ Synced to itprior-quotes repository.")


if __name__ == "__main__":
    main()
