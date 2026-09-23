# NOURBIA FOODS™ — Technical & Commercial Q&A Document
**Custom E-Commerce Platform Architecture & Operations Guide**
*Prepared by ITPrior Solutions for Nourbia Foods Team*
*Reference Model: Harvest Right (`harvestright.com`) Commercial & Product Presentation*

---

## Table of Contents
1. [E-Commerce End-to-End Scope & Customer Experience](#1-e-commerce-end-to-end-scope--customer-experience)
2. [Shipping & 50-State Fulfillment Integration](#2-shipping--50-state-fulfillment-integration)
3. [Payment Processing & Security (Stripe Engine)](#3-payment-processing--security-stripe-engine)
4. [Multilingual Strategy & Translation Framework](#4-multilingual-strategy--translation-framework)
5. [Product Catalog (20–40 SKUs) & PDP Architecture](#5-product-catalog-2040-skus--pdp-architecture)
6. [Food Box Configurator & Admin Independence](#6-food-box-configurator--admin-independence)
7. [Administration Dashboard Capabilities](#7-administration-dashboard-capabilities)
8. [For Business / B2B Wholesale Section Scope](#8-for-business--b2b-wholesale-section-scope)
9. [Customer & Community "Taste • Test • Shape" Concept](#9-customer--community-taste--test--shape-concept)
10. [Cloud Hosting, Database & Infrastructure Ownership](#10-cloud-hosting-database--infrastructure-ownership)
11. [Source Code & Intellectual Property Ownership](#11-source-code--intellectual-property-ownership)
12. [Third-Party Services & Recurring Operating Costs](#12-third-party-services--recurring-operating-costs)
13. [Quality Assurance & 40 Complimentary QA Hours](#13-quality-assurance--40-complimentary-qa-hours)
14. [Project Timeline, Milestones & Sprint Management](#14-project-timeline-milestones--sprint-management)
15. [30-Day Post-Launch Warranty & Maintenance](#15-30-day-post-launch-warranty--maintenance)
16. [Change Requests & Out-of-Scope Management](#16-change-requests--out-of-scope-management)
17. [Analytics, SEO & Conversion Tracking](#17-analytics-seo--conversion-tracking)
18. [Security Hardening, Backups & Disaster Recovery](#18-security-hardening-backups--disaster-recovery)
19. [Final Handover, Training & Operations](#19-final-handover-training--operations)
20. [Final Scope Matrix: Included vs. Excluded](#20-final-scope-matrix-included-vs-excluded)

---

## 1. E-Commerce End-to-End Scope & Customer Experience

### Question:
> *Please clearly define everything included in the e-commerce platform from product browsing through checkout, payment, fulfillment, tracking, and customer account management.*

### Answer:
The custom platform (built on **Next.js 15 App Router** and **Python FastAPI**) delivers a clean, focused, product-centric commercial shopping experience designed with the clarity of **Harvest Right**:

```
[Homepage / Heritage Collections] ──► [Faceted Filter & Search] ──► [PDP / Rehydration Guide / Box Builder]
                                                                                      │
                                                                                      ▼
[Automated Notifications & Tracking] ◄─── [Stripe Payment Engine] ◄─── [Cart Drawer & 1-Page Checkout]
```

#### Included Customer Journey Steps:
1. **Homepage & Brand Storytelling**: Clean hero section showcasing the core mission (*"Advancing Culturally Relevant Nutrition" • "Meeting People Where They Are"*), interactive **What We Do** section (Source $\rightarrow$ Process $\rightarrow$ Freeze-Dry $\rightarrow$ Develop $\rightarrow$ Package $\rightarrow$ Distribute), featured freeze-dried foods, and food box showcases.
2. **Product Discovery & Catalog**: Filter products by Cultural Heritage (Haitian, African, Latin American, Caribbean), Category (Fruits, Vegetables, Proteins, Seasonings, Staples, Prepared Foods, Snacks), Dietary attributes, and Price.
3. **Product Detail Page (PDP)**: Multi-angle photo gallery (client-supplied images), nutritional facts panel, allergen declarations, 25-year shelf-life badge, preparation/rehydration water-ratio guide, and related product recommendations.
4. **Food Box Configurator**: Select from pre-curated cultural bundles (Single/Personal Box, Family Box, Multi-Family Box) with clear itemized manifests.
5. **Slide-Out Cart Drawer**: Persistent cart drawer supporting single items + boxes, real-time subtotal/weight aggregation, promo codes, and shipping threshold indicators.
6. **Mobile-Optimized Checkout**: One-step/multi-step checkout supporting Guest Checkout or Account Login, address validation, shipping method selection, and tax calculation.
7. **Secure Payment**: Integrated Stripe Elements (Credit/Debit, Apple Pay, Google Pay) with instant order confirmation.
8. **Automated Order Processing**: Real-time webhook order state machine (`Paid` $\rightarrow$ `Processing` $\rightarrow$ `Shipped` $\rightarrow$ `Delivered`), generating downloadable PDF invoices and packing slips.
9. **Customer Self-Service Account**: Secure account login, order history with live carrier tracking links, saved shipping addresses, and profile settings.

---

## 2. Shipping & 50-State Fulfillment Integration

### Question:
> *Please clarify exactly how the 50-state shipping functionality will work, including whether USPS, UPS, FedEx, or ShipStation integrations are included and whether live carrier rates can be calculated.*

### Answer:
The platform includes multi-carrier shipping functionality integrated with **ShipStation API** (and direct carrier fallback via **EasyPost / USPS / UPS / FedEx** APIs):

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                       50-STATE SHIPPING ARCHITECTURE                                        │
├────────────────────────────────┬────────────────────────────────────────────────────────────────────────────┤
│ Capability                     │ Technical Implementation & Possibilities                                   │
├────────────────────────────────┼────────────────────────────────────────────────────────────────────────────┤
│ 1. Real-Time Live Carrier Rates│ Live API lookup returning standard commercial rates from USPS, UPS, FedEx  │
│ 2. Flexible Rate Matrix (Rules)│ Admin-configured flat rates, tiered weight tables, or free-shipping over $X│
│ 3. Automated Label Creation    │ 1-click shipping label generation directly from Nourbia's Admin Console     │
│ 4. Tracking Webhook Sync       │ Automatic tracking number injection sending live carrier tracking links     │
│ 5. Alaska / Hawaii / APO Rules │ Configurable surcharge rules for non-contiguous US states & military bases │
│ 6. Future Expansion Ready      │ Architecture ready for future international shipping expansion             │
└────────────────────────────────┴────────────────────────────────────────────────────────────────────────────┘
```

#### Recommended Workflow:
- **Rate Display**: Connect Nourbia’s carrier accounts via **ShipStation API** to display live commercial rates (e.g., *USPS Priority Mail: 2–3 Days*, *UPS Ground*) or straightforward flat-rate/promotional shipping (e.g., *$7.99 Flat Rate or Free Shipping on orders over $75.00*).
- **Fulfillment**: In the admin panel, clicking *"Create Label"* generates the 4x6 thermal shipping label, updates the order status to `Shipped`, and sends the customer an automated email with their tracking link.

---

## 3. Payment Processing & Security (Stripe Engine)

### Question:
> *Please confirm that payment processing (Stripe, Apple Pay, Google Pay) is included, including refunds, failed payments, duplicate-payment protection, webhooks, and order-status updates.*

### Answer:
Yes, confirmed. The payment engine uses **Stripe Elements & Payment Intents API** as the single, robust, reliable payment gateway:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                      PAYMENT PROCESSING SPECIFICATIONS                                      │
├────────────────────────────────┬────────────────────────────────────────────────────────────────────────────┤
│ Payment Methods                │ • Credit/Debit Cards (Visa, Mastercard, American Express, Discover)        │
│                                │ • Apple Pay (1-touch mobile biometric checkout)                            │
│                                │ • Google Pay (1-touch Android/Chrome checkout)                             │
├────────────────────────────────┼────────────────────────────────────────────────────────────────────────────┤
│ Duplicate-Payment Protection   │ Cryptographic Idempotency Keys generated per checkout session to eliminate │
│                                │ accidental double-charging from repeated button clicks or network drops.   │
├────────────────────────────────┼────────────────────────────────────────────────────────────────────────────┤
│ Automated Webhook Pipeline     │ Secure Stripe webhooks verify transaction state asynchronously,            │
│                                │ updating inventory and setting order status to `Paid`.                     │
├────────────────────────────────┼────────────────────────────────────────────────────────────────────────────┤
│ Failed Payments & Retries      │ Clear inline error messages (e.g., Card Declined, 3D Secure verification)  │
│                                │ with automatic cart preservation.                                          │
├────────────────────────────────┼────────────────────────────────────────────────────────────────────────────┤
│ Admin Refunds & Adjustments    │ Full and partial refunds executable directly inside Nourbia’s Admin        │
│                                │ Dashboard without needing to navigate outside the platform.                │
├────────────────────────────────┼────────────────────────────────────────────────────────────────────────────┤
│ PCI Compliance & Security      │ PCI-DSS SAQ-A compliant (zero raw credit card numbers touch Nourbia's      │
│                                │ servers; tokenization handled directly in Stripe’s secure vault).          │
└────────────────────────────────┴────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Multilingual Strategy & Translation Framework

### Question:
> *Please confirm whether the five-language functionality is included only as the technical multilingual framework or whether actual translation is included. Nourbia can provide the translations if necessary.*

### Answer:
- **What is Included by ITPrior**: Complete technical multilingual framework (**i18n architecture**, locale routing `/en/`, `/ht/`, `/fr/`, `/es/`, `/pt/`, language-preference persistence, hreflang SEO tags, and UI translation dictionaries).
- **Translation Content Provision**: **Nourbia Foods supplies the translated copy and product descriptions**.
- **How It Works Practically**:
  - UI labels (e.g., *"Add to Cart"*, *"Checkout"*, *"Nutrition Facts"*, *"Rehydration Guide"*) are stored in organized JSON translation files (`en.json`, `ht.json`, `fr.json`, `es.json`, `pt.json`).
  - Database schema includes multilingual fields for Product Titles, Descriptions, Ingredients, and Preparation Steps.
  - ITPrior configures the English master templates and assists with the initial translation file structure so your team can easily review and supply the translated text.

---

## 5. Product Catalog (20–40 SKUs) & PDP Architecture

### Question:
> *Please confirm what is included for approximately 20–40 initial SKUs, including product pages, nutrition information, allergens, preparation/rehydration instructions, inventory, pricing, and product images supplied by Nourbia.*

### Answer:
The product catalog engine is purpose-built for the initial launch (20–40 SKUs) and easily expandable to support future product lines without structural redesign:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                       PRODUCT DATA SCHEMA ARCHITECTURE                                      │
├────────────────────────────────┬────────────────────────────────────────────────────────────────────────────┤
│ Visual Presentation            │ Multi-angle image gallery with high-res zoom (Client-supplied photography) │
│ Pricing & Inventory            │ Regular price, sale price, SKU code, stock quantity & low-stock alerts     │
│ Nutrition Facts Panel          │ Standard digital Nutrition Facts label layout with serving information     │
│ Ingredients & Allergens        │ Ingredient list + clear allergen warning badges (e.g., Gluten-Free)        │
│ Shelf-Life Specifications      │ 25-Year shelf-life durability specs and storage recommendations            │
│ Preparation / Rehydration Guide│ Clear water-ratio and preparation instructions                             │
│ Cultural Heritage Metadata     │ Country of origin, cultural culinary pairings, and traditional recipes    │
│ Search & Tagging Taxonomy      │ Category, regional collection, dietary flags (Halal, Vegan, Non-GMO)       │
└────────────────────────────────┴────────────────────────────────────────────────────────────────────────────┘
```

---

## 6. Food Box Configurator & Admin Independence

### Question:
> *Please clarify exactly what functionality is included in the food-box configurator and whether Nourbia will be able to create, modify, price, and manage different boxes through the admin panel without developer assistance.*

### Answer:
Yes, Nourbia administrators will have **full autonomy** to create, price, edit, and manage food boxes through the admin panel without requiring developer assistance:

```
[Admin Creates Box: "Haitian Family Box"] ──► [Sets Price: $89.00] ──► [Assigns Included Items & Quantities]
                                                                                       │
                                                                                       ▼
[Customers Purchase 1-Click Box OR Customize] ◄── [Publishes to Live Storefront with Itemized Manifest]
```

#### Included Food Box Capabilities:
1. **Curated Preset Boxes**: Create standard pre-packaged bundles (e.g., *Haitian Single Box*, *Medium Family Box*, *Multi-Family Box*).
2. **Transparent Manifest Viewer**: Customers see the exact contents, net weights, item counts, and servings included before purchasing.
3. **Admin Box Manager Console**:
   - Add new food box bundles with custom titles, descriptions, and photography.
   - Set bundle pricing and promotional discounts.
   - Add, remove, or update component SKUs inside any box.
   - Activate/Deactivate boxes seasonally with a simple toggle.

---

## 7. Administration Dashboard Capabilities

### Question:
> *Please specify exactly what Nourbia will be able to manage ourselves, including products, inventory, pricing, orders, customers, coupons, food boxes, and reports.*

### Answer:
The platform includes a clean, practical **Custom Administration Dashboard** giving your team day-to-day operational control:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                     ADMIN DASHBOARD FUNCTIONAL MATRIX                                       │
├────────────────────┬────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. Product Manager │ Add/edit/delete SKUs, upload photos, update prices, sale pricing, nutrition & specs    │
│ 2. Inventory Engine│ Real-time stock counts, out-of-stock badges, low-stock threshold email warnings        │
│ 3. Order Management│ View orders, filter by status, process fulfillments, print packing slips & PDF invoices│
│ 4. Food Box Manager│ Create/edit food box bundles, customize SKU compositions, set box prices & availability│
│ 5. Customer Center │ View customer profiles, order history, shipping addresses, and customer notes          │
│ 6. Promotions & Vouchers│ Create percentage or fixed-dollar coupon codes, set expiration dates & minimums   │
│ 7. Sales Reports   │ Total revenue, sales by category/box, average order value, exportable CSV/PDF reports  │
│ 8. Content Manager │ Update homepage banners, FAQs, policy pages (shipping/returns), and contact details    │
└────────────────────┴────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 8. For Business / B2B Wholesale Section Scope

### Question:
> *Please clarify what is included in the B2B/wholesale section and whether this is simply an inquiry/application system or a complete wholesale ordering platform.*

### Answer:
- **Phase 1 Scope (Included in Core $6,000 Quote)**: **Streamlined B2B Inquiry & Partner Lead Ingestion System**.
  - Dedicated `/business` landing page highlighting capabilities: *Retail Distribution, Food Service, Private Label, Bulk Freeze-Dried Ingredients, and Custom Product Processing*.
  - Comprehensive Business Application & RFQ Form (capturing Company Name, EIN/Tax ID, Order Volume, Product Interest, Delivery Schedule, and Spec Uploads).
  - Instant Digital Line Sheet / Product Spec Overview PDF download.
  - Automatic lead routing sending instant email alerts to Nourbia’s sales team.
- **Phase 2 Expansion (Optional Future Add-On)**:
  - Password-protected wholesale customer login, tiered custom wholesale case pricing (e.g., 20% off for Tier 1, 35% off for Tier 2), Net-30 purchase order workflows, and bulk invoice checkout.

---

## 9. Customer & Community "Taste • Test • Shape" Concept

### Question:
> *Please identify what is included in the “Taste • Test • Shape” functionality and whether this can be moved to a later phase if necessary.*

### Answer:
- **Phase 1 Scope (Included in Core $6,000 Quote)**: **Streamlined Community Voice & Flavor Request Hub**.
  - A clean, simple page where customers can submit:
    1. *Foods & flavors they miss from home* (e.g., specific regional fruits, peppers, or spices).
    2. *Product suggestions and feedback on samples they received*.
    3. *Reviews on existing SKUs*.
  - Admin view aggregating customer requests to guide R&D product development.
  - **Kept simple and practical** — strictly focused on capturing customer demand without unnecessary social network overhead.
- **Can it be moved to Phase 2?**: Yes. If you prefer to launch without this page initially, we can reallocate its 18 hours toward additional checkout tuning or testing.

---

## 10. Cloud Hosting, Database & Infrastructure Ownership

### Question:
> *Please clarify who will own and control the AWS/cloud account, database, domain, DNS, SSL, repository, and deployment environment. I would like Nourbia to own the primary accounts and infrastructure.*

### Answer:
**Nourbia Foods will own 100% of all accounts, infrastructure, databases, domains, and credentials from Day 1.**

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                     INFRASTRUCTURE OWNERSHIP TOPOLOGY                                       │
├────────────────────────┬──────────────────────────────────────────┬─────────────────────────────────────────┤
│ Component              │ Recommended Cloud Provider               │ Account Ownership                       │
├────────────────────────┼──────────────────────────────────────────┼─────────────────────────────────────────┤
│ Frontend (Next.js)     │ Vercel Pro or AWS CloudFront/Amplify     │ Nourbia's Dedicated Account             │
│ Backend API (FastAPI)  │ Render, Railway, or AWS ECS/Fargate      │ Nourbia's Dedicated Account             │
│ Database (PostgreSQL)  │ Supabase, Neon, or AWS RDS PostgreSQL    │ Nourbia's Dedicated Account             │
│ Caching (Redis)        │ Upstash Redis or AWS ElastiCache         │ Nourbia's Dedicated Account             │
│ Domain & DNS           │ Cloudflare, GoDaddy, or AWS Route53      │ Nourbia's Direct Registrar              │
│ Code Repository        │ GitHub (Private Repository)              │ Nourbia's GitHub Organization           │
└────────────────────────┴──────────────────────────────────────────┴─────────────────────────────────────────┘
```
ITPrior sets up the automated deployment pipelines directly inside Nourbia’s accounts, ensuring zero agency lock-in.

---

## 11. Source Code & Intellectual Property Ownership

### Question:
> *Please confirm that Nourbia will receive 100% ownership of the source code, database structure, website-related design files, deployment scripts, and documentation upon payment and completion.*

### Answer:
**Yes, 100% confirmed.**
Upon milestone completion and payment:
- All source code (Next.js frontend, FastAPI backend, custom modules) is transferred to Nourbia’s private GitHub repository.
- All PostgreSQL database schemas, migration scripts, and seed files are transferred.
- All website-related digital design assets and documentation become the sole intellectual property of Nourbia Foods Inc.
- No proprietary licenses, royalty fees, or recurring agency software lock-ins.

---

## 12. Third-Party Services & Recurring Operating Costs

### Question:
> *Please identify any recurring costs that Nourbia will have beyond the development fee, such as hosting, databases, Redis, email services, payment processing, ShipStation, APIs, monitoring, or other subscriptions.*

### Answer:
Because we are building a custom, high-performance architecture rather than a bloated app ecosystem, your recurring operating costs are practical, transparent, and scalable:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   ESTIMATED MONTHLY OPERATING COSTS                                         │
├────────────────────────┬──────────────────────────────────────────┬─────────────────────────────────────────┤
│ Service Category       │ Recommended Provider                     │ Estimated Monthly Cost                  │
├────────────────────────┼──────────────────────────────────────────┼─────────────────────────────────────────┤
│ Frontend Hosting       │ Vercel Pro                               │ $20.00 / month                          │
│ Backend API & DB       │ Render / Supabase Managed PostgreSQL     │ $15.00 – $25.00 / month                 │
│ Cloud Cache (Redis)    │ Upstash (Serverless Redis)               │ $0.00 – $5.00 / month (Free Tier)       │
│ Transactional Email    │ Resend / SendGrid (3,000 emails/mo)      │ $0.00 – $15.00 / month (Free Tier)      │
│ Shipping Software      │ ShipStation Starter                      │ $9.99 / month                           │
│ Domain & SSL           │ Cloudflare                               │ Free SSL ($12/yr domain)                │
│ Error Monitoring       │ Sentry (Developer Tier)                  │ $0.00 (Free Tier)                       │
├────────────────────────┼──────────────────────────────────────────┼─────────────────────────────────────────┤
│ TOTAL FIXED HOSTING    │                                          │ ~$45.00 – $70.00 / month                │
├────────────────────────┼──────────────────────────────────────────┼─────────────────────────────────────────┤
│ Payment Gateway (Card) │ Stripe Standard                          │ Standard 2.9% + 30¢ per transaction     │
└────────────────────────┴──────────────────────────────────────────┴─────────────────────────────────────────┘
```
*(Compare this to Shopify Plus which starts at $2,000/month + app subscription fees).*

---

## 13. Quality Assurance & 40 Complimentary QA Hours

### Question:
> *Please clarify what is included in the 40 complimentary QA hours and what testing will be completed before launch.*

### Answer:
The **+40 Complimentary QA Hours** ($0.00 billing) are dedicated to thorough pre-launch verification:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                       QA & TESTING EXECUTION MATRIX                                         │
├────────────────────────┬────────────────────────────────────────────────────────────────────────────────────┤
│ 1. E2E User Journeys   │ Automated Playwright test suites testing complete purchase paths:                  │
│                        │ Browse ──► Filter ──► PDP ──► Add Box ──► Cart ──► Stripe Checkout ──► Invoice    │
├────────────────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ 2. Multi-Device QA     │ Real-device testing on iPhones (iOS Safari), Android (Chrome), Tablets & Desktops  │
├────────────────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ 3. Cross-Browser QA    │ Verified across Apple Safari, Google Chrome, Mozilla Firefox, and Microsoft Edge   │
├────────────────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ 4. Payment Sandbox QA  │ Thorough Stripe sandbox testing: Success, 3DS, Declines, and Refunds               │
├────────────────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ 5. Security Scanning   │ Automated vulnerability scanning, SQL injection checks, CSRF, and input validation │
├────────────────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ 6. UAT & Pilot Staging │ Staging environment walkthrough with Nourbia team for final pre-launch sign-off    │
└────────────────────────┴────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 14. Project Timeline, Milestones & Sprint Management

### Question:
> *Please provide the expected timeline for each milestone and clarify what happens if a milestone takes longer than the estimated timeframe.*

### Answer:
The project is delivered across an **8–10 Weeks** timeline divided into **4 structured 25% milestones**:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                     4-STAGE MILESTONE DELIVERY SCHEDULE                                     │
├─────────────┬─────────────┬───────────┬─────────────────────────────────────────────────────────────────────┤
│ Milestone   │ Split (%)   │ Timeline  │ Deliverables & Verification Sign-Off                                │
├─────────────┼─────────────┼───────────┼─────────────────────────────────────────────────────────────────────┤
│ Milestone 1 │ 25% ($1,500)│ Weeks 1–2 │ Architecture Setup, DB Modeling, Auth, API Framework & CI/CD Pipeline│
│ Milestone 2 │ 25% ($1,500)│ Weeks 3–5 │ Harvest Right UI/UX Layout, Homepage, Catalog, PDP & Food Boxes     │
│ Milestone 3 │ 25% ($1,500)│ Weeks 6–8 │ Cart, Checkout, Stripe Payments, 50-State Shipping & B2B/Taste Hub  │
│ Milestone 4 │ 25% ($1,500)│ Weeks 9–10│ Admin Panel, Multilingual SEO, QA Testing, Cloud Deployment & Launch│
└─────────────┴─────────────┴───────────┴─────────────────────────────────────────────────────────────────────┘
```

#### What happens if a milestone takes longer?
- **Fixed-Price Milestone Commitment**: The project fee remains fixed at **$6,000.00 USD**. You are never billed for additional hours resulting from our internal development adjustments.
- **Weekly Progress Demonstrations**: Every sprint includes staging demonstrations, keeping both teams aligned on progress.

---

## 15. 30-Day Post-Launch Warranty & Maintenance

### Question:
> *Please clarify what is covered by the 30-day warranty/hypercare period and what hourly rate or maintenance cost would apply after that period.*

### Answer:
- **30-Day Hypercare Warranty (Included at $0.00)**:
  - Covers all bug fixes, glitch remediation, performance tuning, and technical adjustments related to the approved scope.
  - Prompt investigation and resolution of any operational bugs or glitches during standard business support.
- **After the 30-Day Warranty (Ongoing Maintenance & Support Options)**:
  - **Dedicated Monthly Maintenance Package**: **$600.00 USD / month** (equivalent to **₹50,000 INR / month**). This comprehensive retainer package includes up to 40 dedicated hours per month covering continuous server health monitoring, proactive security updates, database optimization, bug fixes, routine content adjustments, small feature enhancements, and priority technical support.
  - **On-Demand Hourly Maintenance**: Alternatively available on an ad-hoc basis at the discounted partner rate of **$15.00 USD / hour** (billed strictly for actual hours requested, with zero monthly commitment or retainers required).

---

## 16. Change Requests & Out-of-Scope Management

### Question:
> *Please explain how changes outside the agreed scope will be handled and what rate would apply.*

### Answer:
1. If Nourbia identifies a new feature or scope addition during development, we provide a quick **Scope Addendum Estimate** (Deliverable Description + Estimated Hours $\times$ **$15.00/hr**).
2. Work on the addition only proceeds upon your explicit written approval.
3. Core milestone timelines remain protected.

---

## 17. Analytics, SEO & Conversion Tracking

### Question:
> *Please confirm whether Google Analytics, Google Search Console, sitemap, metadata, structured data, and basic e-commerce conversion tracking are included.*

### Answer:
**Yes, 100% included.**
- **Google Analytics 4 (GA4)**: Configured with standard e-commerce event tracking (`view_item`, `add_to_cart`, `begin_checkout`, `purchase`).
- **Google Search Console**: Verified domain ownership and sitemap submission.
- **Automated Sitemaps & Robots.txt**: Dynamic XML sitemap generator indexing all products, food boxes, and categories.
- **Schema.org JSON-LD**: Structured rich snippet data for Product pricing, availability, and brand organization.
- **Performance Optimization**: Built with modern web performance best practices, optimized assets, and efficient caching for fast mobile and desktop loading.

---

## 18. Security Hardening, Backups & Disaster Recovery

### Question:
> *Please clarify what security monitoring, database backups, recovery procedures, and ongoing maintenance are included.*

### Answer:
- **Automated Daily Database Backups**: Automated snapshots with 7-day rolling retention and 1-click point-in-time recovery.
- **Security Hardening**: OWASP Top 10 defenses, rate limiting against brute-force attacks, CSRF token validation, and secure password hashing with bcrypt.
- **Error Tracking**: Integration with **Sentry** for real-time error alerts and uptime monitoring.

---

## 19. Final Handover, Training & Operations

### Question:
> *At completion, please confirm that Nourbia will receive all credentials, documentation, source code, repositories, deployment information, and administrator access necessary to operate the platform independently.*

### Answer:
**Yes, 100% confirmed.**
Upon final milestone sign-off, ITPrior delivers:
1. **Master Credentials Document**: Master access to Vercel, Render, Supabase, Stripe, ShipStation, and GitHub.
2. **Operations Documentation Wiki**: Step-by-step guides on adding products, editing food boxes, fulfilling orders, and creating coupons.
3. **Recorded Video Walkthrough**: A clear video walkthrough demonstrating daily administrator workflows.
4. **Full Git Repository Transfer**: Ownership transfer of the private GitHub repository to Nourbia's organization.

---

## 20. Final Scope Matrix: Included vs. Excluded

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                       FINAL PROJECT SCOPE MATRIX                                            │
├─────────────────────────────────────────────────────────────┬───────────────────────────────────────────────┤
│ INCLUDED IN CUSTOM E-COMMERCE PLATFORM ($6,000 USD)         │ EXCLUDED / TO BE HANDLED SEPARATELY           │
├─────────────────────────────────────────────────────────────┼───────────────────────────────────────────────┤
│ • Full Custom Next.js 15 & FastAPI Stack (No Shopify)       │ • Brand Strategy & Logo Design (By Nourbia)   │
│ • Harvest Right Commercial Reference Architecture           │ • Packaging & Product Label System (By Nourbia)│
│ • Custom Product Catalog (20–40 Initial Launch SKUs)        │ • Photography Services (Photos By Nourbia)    │
│ • Nutrition Facts Panels, Allergens & Shelf-Life Specs      │ • Full B2B Password-Gated Portal (Phase 2)    │
│ • Preparation & Rehydration Guides                          │ • Recurring Automated Subscriptions (Phase 2) │
│ • Curated & Custom Food Box Configurator                    │ • Advanced QR Community Voting Lab (Phase 2)  │
│ • Shopping Cart Drawer & Mobile Checkout                    │ • Native Mobile iOS/Android App (Future Phase)│
│ • Stripe (Cards, Apple Pay, Google Pay)                     │ • Content Translation Writing (By Nourbia)    │
│ • 50-State ShipStation & Multi-Carrier Shipping Engine      │                                               │
│ • Streamlined B2B Partner Inquiries & Line Sheet Download   │                                               │
│ • Streamlined "Taste • Test • Shape" Feedback Hub           │                                               │
│ • Full Administration Dashboard (Products, Orders, Reports) │                                               │
│ • 5-Language i18n Technical Framework                       │                                               │
│ • GA4 Analytics & Schema.org JSON-LD SEO Structure          │                                               │
│ • +40 Hours Complimentary QA & Cross-Browser Testing Buffer │                                               │
│ • Production Cloud Deployment on Nourbia's Accounts         │                                               │
│ • 100% Source Code & IP Ownership Transfer                  │                                               │
│ • 30-Day Post-Launch Warranty & Hypercare Support           │                                               │
└─────────────────────────────────────────────────────────────┴───────────────────────────────────────────────┘
```
