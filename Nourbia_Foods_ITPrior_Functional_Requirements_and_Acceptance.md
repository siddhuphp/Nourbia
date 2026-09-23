# NOURBIA FOODS™ — FUNCTIONAL REQUIREMENTS & ACCEPTANCE CRITERIA SPECIFICATION
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
