# NOURBIA FOODS™ — End-to-End Custom E-Commerce & Platform Architecture
**Advancing Culturally Relevant Nutrition • Meeting People Where They Are**
*Food products • Food processing • Food solutions*

---

## 1. Executive Overview & System Architecture

### 1.1 Brand & Product Vision
**Nourbia Foods™** is a modern, for-profit food processing and distribution company with a strong social purpose: **advancing culturally relevant nutrition and food sovereignty** by meeting people where they are.

Nourbia bridges the gap across the complete food lifecycle:
$$\text{Food Sourcing} \longrightarrow \text{Food Processing} \longrightarrow \text{Freeze-Drying} \longrightarrow \text{Product Development} \longrightarrow \text{Packaging} \longrightarrow \text{Distribution}$$

```
┌───────────────────────────────────────────────────────────────────────────────────────────┐
│                                 NOURBIA CORE SERVICES ENGINE                              │
│  Source ──► Process ──► Preserve (Freeze-Dry) ──► Product Dev ──► Package ──► Distribute   │
└─────────────────────────────────────────────┬─────────────────────────────────────────────┘
                                              │
        ┌──────────────────────────────┬──────┴──────────────────────┬──────────────────────┐
        ▼                              ▼                             ▼                      ▼
┌───────────────┐              ┌───────────────┐             ┌───────────────┐      ┌───────────────┐
│  Custom D2C   │              │ Nourbia Boxes │             │   Community   │      │  B2B/Services │
│ (Catalog/Shop)│              │ (Box Builder) │             │  (Taste Lab)  │      │ (Wholesale)   │
└───────┬───────┘              └───────┬───────┘             └───────┬───────┘      └───────┬───────┘
        │                              │                             │                      │
        └──────────────────────────────┴──────────────┬──────────────┴──────────────────────┘
                                                      ▼
┌───────────────────────────────────────────────────────────────────────────────────────────┐
│              CUSTOM FULL-STACK ENGINE & SECURE INFRASTRUCTURE (NO SHOPIFY)                │
│   Next.js 14+ Frontend • Python FastAPI Async Backend • PostgreSQL (SQLAlchemy) • Redis   │
│   Stripe Elements (Cards/Apple Pay/Google Pay) • Stripe Billing Subscriptions             │
│   SendGrid / Resend Transactional Emails • EasyPost / Carrier Shipping Calculation       │
└───────────────────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Core Strategic Principles (Prove • Build • Scale)
1. **Prove**: Initial launch with 20–40 high-priority SKUs focused on the Haitian food foundation as proof-of-concept, establishing demand validation, food-safety review, and community testing.
2. **Build**: Expand processing and freeze-drying infrastructure, B2B wholesale distribution, surplus food recovery, and custom co-packing / private-label services.
3. **Scale**: Expand into African, Latin American, Caribbean, and global diaspora markets across all 50 US states, Canada, and international territories.
4. **Cultural Food Sovereignty**: Don't dictate what people need; provide the platform for communities to express food desires, test samples, share authentic feedback, and shape future SKUs.

---

## 2. User Personas & System Roles

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                               USER ACTOR MATRIX                                  │
├──────────────────────┬────────────────────────────────────┬──────────────────────┤
│ Actor                │ Core Motivations                   │ Primary Touchpoints  │
├──────────────────────┼────────────────────────────────────┼──────────────────────┤
│ 1. Diaspora Consumer │ Access authentic cultural foods,   │ Custom D2C Catalog,  │
│    (e.g., Marie)     │ long shelf life, convenient prep   │ Food Box Builder     │
├──────────────────────┼────────────────────────────────────┼──────────────────────┤
│ 2. Community Co-     │ Taste-test samples, shape new SKUs,│ Community Taste Lab, │
│    Creator / Tester  │ vote on regional foods, earn perks │ QR Feedback Portal   │
├──────────────────────┼────────────────────────────────────┼──────────────────────┤
│ 3. B2B / Wholesale   │ Sourcing shelf-stable ingredients, │ B2B Wholesale Hub,   │
│    Buyer (Retail/FS) │ private label, retail packaging    │ Sample RFQ Generator │
├──────────────────────┼────────────────────────────────────┼──────────────────────┤
│ 4. Food Service &    │ Commercial kitchen ingredients,    │ Food Service Portal, │
│    Institution Buyer │ pre-portioned prepared meals       │ Bulk Ordering Desk   │
├──────────────────────┼────────────────────────────────────┼──────────────────────┤
│ 5. Food Recovery &   │ Monetize surplus produce, partner  │ Partner Ingestion    │
│    Farm Partner      │ on freeze-drying / processing      │ Portal               │
├──────────────────────┼────────────────────────────────────┼──────────────────────┤
│ 6. Food Brand / Co-  │ Private label, custom product dev, │ Services Hub,        │
│    Pack Client       │ contract freeze-drying & packaging │ Custom RFQ Builder   │
├──────────────────────┼────────────────────────────────────┼──────────────────────┤
│ 7. Store Operations  │ SKU catalog, box assembly rules,   │ Custom Admin Console │
│    & Fulfillment     │ B2B leads, batch traceability      │ & Order Pipeline     │
└──────────────────────┴────────────────────────────────────┴──────────────────────┘
```

---

## 3. Global Information Architecture & Sitemap

```mermaid
graph TD
    Home[Homepage /] --> Shop[Shop Products /shop]
    Home --> Services[Our Services /services]
    Home --> Boxes[Nourbia Food Boxes /boxes]
    Home --> FreezeDry[Freeze-Drying Tech /freeze-drying]
    Home --> Community[Taste Lab & Community /community]
    Home --> B2B[For Business / B2B /b2b]
    Home --> Partners[Partner With Us /partners]
    Home --> Recovery[Food Recovery /food-recovery]
    Home --> About[About Nourbia /about]
    Home --> Contact[Contact Us /contact]

    Shop --> Haitian[Haitian Heritage Line]
    Shop --> African[African Heritage Line]
    Shop --> Latin[Latin American Line]
    Shop --> Caribbean[Caribbean Heritage Line]
    Shop --> CatFruits[Fruits]
    Shop --> CatVeg[Vegetables & Herbs]
    Shop --> CatProt[Proteins]
    Shop --> CatStaples[Staples - Rice/Beans/Grains]
    Shop --> CatSpices[Seasonings & Flavors]
    Shop --> CatPrepared[Prepared Foods & Sauces]
    Shop --> CatSnacks[Snacks]
    Shop --> PDP[Product Detail Page /products/:slug]

    Services --> ServSourcing[Food Sourcing]
    Services --> ServProcessing[Food Processing]
    Services --> ServFreezeDry[Freeze-Drying Preservation]
    Services --> ServProdDev[Product Development]
    Services --> ServPackaging[Packaging & Private Label]
    Services --> ServDist[Distribution & Logistics]

    Boxes --> BoxConfig[Interactive Box Builder /boxes/build]
    Boxes --> BoxTiers[Individual / Family / Multi-Family / Custom]

    Community --> TasteTest[Dynamic QR Feedback /taste-lab?batch=...]
    Community --> RequestFood[Request a Cultural Food /request-food]
    Community --> ReferShare[Share & Earn Rewards /share]

    B2B --> B2BRetail[Retail Ready Products]
    B2B --> B2BWholesale[Wholesale Distribution & Net-30]
    B2B --> B2BFoodService[Food Service & Bulk]
    B2B --> B2BPrivateLabel[Private Label & Custom]

    Partners --> PartFarmers[Farmers & Producers]
    Partners --> PartRetailers[Retailers & Grocers]
    Partners --> PartDistributors[Distributors & Institutions]

    PDP --> Cart[Slide-Out Cart Drawer /cart]
    BoxConfig --> Cart
    Cart --> Checkout[Custom Stripe Embedded Checkout /checkout]
    Checkout --> OrderSuccess[Order Confirmation & Tracking /orders/:id]
    
    Account[Customer Portal /account] --> AccOrders[Order History & PDF Invoices]
    Account --> AccSubs[Stripe Box Subscriptions Management]
    Account --> AccTaste[Taste Lab Badges & Wishlist Votes]
    
    Admin[Admin Console /admin] --> AdmCatalog[Catalog & Inventory Manager]
    Admin --> AdmOrders[Orders & Carrier Label Dispatch]
    Admin --> AdmBoxes[Box Allocation Rules]
    Admin --> AdmTaste[Taste Lab & Demand Analytics]
    Admin --> AdmB2B[B2B & Surplus Partner Pipelines]
```

---

## 4. End-to-End Application Flows with Step-by-Step Logic

### 4.1 Flow 1: Custom D2C E-Commerce Product Discovery & Stripe Checkout Flow

```mermaid
sequenceDiagram
    autonumber
    actor Customer as Diaspora Shopper (Marie)
    participant Web as Custom Next.js Storefront
    participant API as Custom Backend API
    participant DB as PostgreSQL Database
    participant Stripe as Stripe Payment Engine
    participant Notify as SendGrid Email / SMS Service

    Customer->>Web: Visits Shop / Collections (Filter: Haitian / Freeze-Dried)
    Web->>API: GET /api/products?heritage=haitian&processing=freeze-dried
    API->>DB: Queries active SKUs with real-time stock
    DB-->>API: Returns SKUs (Haitian Epis, Freeze-Dried Lalo, Suya)
    API-->>Web: Renders Product Grid with Quick-View
    Customer->>Web: Clicks "Freeze-Dried Lalo (Jute Leaves)"
    Web-->>Customer: Renders PDP with Shelf-Life, Rehydration Guide, Cultural Provenance
    Customer->>Web: Selects 2x Quantity & clicks "Add to Cart"
    Web->>API: POST /api/cart/items (Sync session / reserve stock)
    API-->>Web: Returns updated subtotal + Free Shipping progress ($42.00 / $50.00)
    Customer->>Web: Clicks "Checkout"
    Web->>API: POST /api/checkout/create-intent (Calculates tax & shipping)
    API->>Stripe: stripe.paymentIntents.create({ amount: 4850, currency: 'usd' })
    Stripe-->>API: Returns client_secret
    API-->>Web: Mounts Custom Stripe Elements (Card, Apple Pay, Google Pay, Link)
    Customer->>Web: Authorizes payment via Apple Pay / Credit Card
    Web->>Stripe: stripe.confirmPayment()
    Stripe-->>Web: Payment Succeeded
    Stripe->>API: Webhook (payment_intent.succeeded)
    API->>DB: Creates Order record, deducts inventory, generates invoice
    API->>Notify: Dispatches Branded Order Confirmation + QR Taste Lab invite
    Web-->>Customer: Displays Order Confirmation (/orders/ORD-8821) with Live Tracking
```

---

### 4.2 Flow 2: Nourbia Food Boxes (Interactive Customizer & Stripe Subscription Flow)

```mermaid
sequenceDiagram
    autonumber
    actor User as Family Shopper
    participant BoxUI as /boxes/build Configurator
    participant SlotEngine as Slot Validation Engine
    participant API as Custom Subscription API
    participant Stripe as Stripe Billing Subscriptions
    participant DB as PostgreSQL Database

    User->>BoxUI: Selects Tier (Family Box - 12 Curated Items)
    User->>BoxUI: Selects Frequency (Monthly Subscription - Save 15%)
    User->>BoxUI: Chooses Heritage Preset ("Haitian Heritage")
    BoxUI->>SlotEngine: Initializes Slots: 4 Proteins, 4 Vegetables, 3 Seasonings, 1 Snack
    loop Dynamic Customization
        User->>BoxUI: Swaps Default Okra for Freeze-Dried Shrimp
        BoxUI->>SlotEngine: Validates category slot constraints (Proteins <= 4)
        SlotEngine-->>BoxUI: Updates completeness meter (12/12 Slots Filled)
    end
    User->>BoxUI: Clicks "Subscribe to Custom Box ($76.49/mo)"
    BoxUI->>API: POST /api/subscriptions/create-box-session
    API->>Stripe: stripe.subscriptions.create() with recurring schedule metadata
    Stripe-->>API: Returns customer subscription profile
    API->>DB: Stores Box Manifest & customer recurring profile
    API-->>User: Navigates to Subscription Confirmation with Self-Service Portal link
```

#### Box Tier Matrix:
| Box Tier | Target Household | Standard Contents | Customization Options | Delivery Options |
| :--- | :--- | :--- | :--- | :--- |
| **Individual Box** | 1 Person (Everyday needs) | 6 Items (2 Proteins, 2 Veg/Fruits, 2 Seasonings) | 100% custom swap or Chef Curated | One-Time / Bi-Weekly / Monthly (15% Off) |
| **Family Box** | 3–5 Persons | 12 Items (4 Proteins, 4 Veg, 3 Seasonings, 1 Snack) | Cultural Theme presets + item swaps | Monthly / Bi-Monthly (15% Off) |
| **Multi-Family Box** | Extended families / Shared | 24 Items (Bulk Staples, Proteins, Large Seasonings) | Bulk allocation per culture | Monthly / Custom Schedule (15% Off) |
| **Custom / Organization** | Community Hubs / Relief / Special | Fully dynamic line items | Tailored dietary & cultural specs | On-demand / Invoice Net terms |

---

### 4.3 Flow 3: Community Voice & Cultural Food Sovereignty Flow
*(Taste → Test → Share → Recommend → Shape the Next Product)*

```mermaid
sequenceDiagram
    autonumber
    actor CommunityMember as Community Member (Jean)
    participant QR as Mobile QR Scanner
    participant Portal as /taste-lab?batch=...
    participant API as Feedback Ingestion Engine
    participant DB as PostgreSQL Database
    participant Loyalty as Coupon & Referral Engine

    Note over CommunityMember,QR: Customer receives physical sample pouch with printed QR
    CommunityMember->>QR: Scans QR code on sample pouch
    QR->>Portal: Resolves to /taste-lab?batch=HA-EPI-2026-01
    Portal-->>CommunityMember: Displays 4-Step Interactive Sensory Review
    CommunityMember->>Portal: Submits Flavor Rating, Authenticity Score (9/10), Texture, Notes
    CommunityMember->>Portal: Submits Cultural Wishlist: "Please freeze-dry Haitian Djon Djon mushrooms!"
    Portal->>API: POST /api/taste-lab/submit
    API->>DB: Stores sensory data & increments Wishlist votes for Djon Djon
    API->>Loyalty: Generates single-use 10% coupon + personal referral link
    Loyalty-->>CommunityMember: Instant display & email copy: "Use code JEAN10 on your next box!"
    CommunityMember->>Portal: Shares link with family WhatsApp group
```

---

### 4.4 Flow 4: Core Services & Custom Processing Inquiry Flow (`/services`)

```mermaid
sequenceDiagram
    autonumber
    actor BrandClient as Food Brand / Co-Pack Client
    participant ServPage as /services Portal
    participant Calculator as Interactive Scope Builder
    participant API as RFQ Ingestion API
    participant CRM as Admin B2B CRM Pipeline
    participant OpsTeam as Nourbia Technical Ops

    BrandClient->>ServPage: Explores 6 Core Services (Sourcing, Processing, Freeze-Drying, R&D, Packaging, Distribution)
    BrandClient->>ServPage: Clicks "Explore Product Development & Freeze-Drying"
    BrandClient->>Calculator: Selects Service Modules: [Freeze-Drying + Custom Packaging + Recipe Scaling]
    BrandClient->>Calculator: Enters Target Input (e.g. 5,000 lbs Fresh Mango / Month)
    BrandClient->>Calculator: Uploads spec sheet & submits RFQ form
    Calculator->>API: POST /api/rfq/services
    API->>CRM: Creates qualified enterprise lead record with attachments
    API->>OpsTeam: Dispatches instant alert to Food Science & Production team
    OpsTeam-->>BrandClient: Sends Feasibility Estimate & Lab Trial Proposal within 24h
```

---

### 4.5 Flow 5: B2B Wholesale, Retailer & Food Service Acquisition Flow (`/b2b`)

```mermaid
sequenceDiagram
    autonumber
    actor Buyer as Supermarket / Food Service Buyer (Marcus)
    participant B2BHub as /b2b Portal
    participant API as Custom B2B Engine
    participant DB as PostgreSQL Database
    participant SalesTeam as Nourbia B2B Accounts Team

    Buyer->>B2BHub: Explores B2B Offerings (Retail Ready, Food Service, Private Label, Bulk)
    Buyer->>B2BHub: Clicks "Download Digital Line Sheet (PDF)" -> Instant PDF generated
    Buyer->>B2BHub: Clicks "Request B2B Sample Kit & Net-30 Account"
    Buyer->>B2BHub: Fills out Buyer Profile (Store name, 6 locations, Tax ID, SKU interest)
    B2BHub->>API: POST /api/b2b/apply
    API->>DB: Creates B2B Account record in "Pending Verification"
    API->>SalesTeam: Dispatches High-Priority Lead Alert
    SalesTeam->>API: Approves B2B Account & triggers Wholesale Sample Kit dispatch
    API-->>Buyer: Sends Approval Email with Temporary Password
    Buyer->>B2BHub: Logs into Wholesale Portal with Tiered Volume Pricing (Case discounts)
    Buyer->>B2BHub: Places First Wholesale Order (120 Cases Haitian Epis & Freeze-Dried Okra)
```

---

### 4.6 Flow 6: Food Surplus Recovery & Partner Sourcing Flow (`/partners` & `/food-recovery`)

```mermaid
graph TD
    A[Partner: Farmer / Food Producer / Retailer Surplus] -->|Visits /partners or /food-recovery| B[Partner Ingestion & Surplus Form]
    B -->|Submits Crop Type, Volume in lbs/tons, Location, Harvest Date, Photos| C[Custom Sourcing Ingestion API]
    C -->|Quality & Food Safety Protocol Audit| D{Approved for Processing?}
    D -->|Yes| E[Logistics Dispatch & Cold-Chain Intake Protocol]
    D -->|No| F[Feedback & Alternative Sourcing Guidance]
    E --> G[Nourbia Processing & Freeze-Drying Facility]
    G --> H[Transformation into Market-Ready SKUs & Ingredients]
    H --> I[Inventory Distributed to D2C / B2B Products & Food Boxes]
    I --> J[Partner Impact Report: Pounds Saved & Revenue Generated]
```

---

## 5. Complete Product Architecture & 7 Product Categories

The platform supports the complete range of product categories defined in the website project documentation:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                           7 CORE PRODUCT CATEGORIES                              │
├──────────────────────┬───────────────────────────────────────────────────────────┤
│ Category             │ Products / SKUs Included                                  │
├──────────────────────┼───────────────────────────────────────────────────────────┤
│ 1. Fruits            │ Freeze-dried Mango, Strawberry, Banana, Pineapple,        │
│                      │ Passionfruit, Soursop, and culturally relevant fruits     │
├──────────────────────┼───────────────────────────────────────────────────────────┤
│ 2. Vegetables & Herbs│ Okra / Kalalou, Lalo (Jute Leaves), Epis herbs, Spinach,   │
│                      │ Bitter Leaf, Callaloo, and regional cooking greens        │
├──────────────────────┼───────────────────────────────────────────────────────────┤
│ 3. Proteins          │ Freeze-dried Fish (Snapper/Cod), Shrimp, Beef, Pork,      │
│                      │ Goat, and shelf-stable prepared protein cuts              │
├──────────────────────┼───────────────────────────────────────────────────────────┤
│ 4. Staples           │ Rice varieties, Dried & Pre-cooked Beans, Grains, Corn,    │
│                      │ Flours, Cassava, and Plantain meal                        │
├──────────────────────┼───────────────────────────────────────────────────────────┤
│ 5. Seasonings &      │ Haitian Epis, Pikliz blend, Suya spice, Jollof seasoning, │
│    Flavors           │ Shito, Berbere, Latin American Sazón, Épice blends        │
├──────────────────────┼───────────────────────────────────────────────────────────┤
│ 6. Prepared Foods    │ Shelf-stable meals, traditional sauces, soups, and ready- │
│                      │ to-use cooking bases & simmer pastes                      │
├──────────────────────┼───────────────────────────────────────────────────────────┤
│ 7. Snacks            │ Freeze-dried fruit crisps, seasoned crunchy vegetables,   │
│                      │ spiced seeds, plantain chips, and savory bites            │
└──────────────────────┴───────────────────────────────────────────────────────────┘
```

---

## 6. Complete Data Models & Schemas

### 6.1 Product Schema (`product.json`)
```json
{
  "id": "prod_haitian_epis_01",
  "sku": "NB-HT-EPI-01",
  "title": "Haitian Epis Traditional Seasoning",
  "brand": "Nourbia Foods",
  "category": "Seasonings & Flavors",
  "cultural_heritage": "Haitian",
  "processing_type": "Freeze-Dried Formulation",
  "pricing": {
    "retail_price_usd": 9.99,
    "subscription_price_usd": 8.49,
    "wholesale_case_price_usd": 72.00,
    "case_pack_qty": 12
  },
  "specifications": {
    "net_weight_oz": 3.2,
    "reconstituted_yield_oz": 16.0,
    "shelf_life_months": 300,
    "ingredients": ["Scallions", "Garlic", "Scotch Bonnet Peppers", "Thyme", "Bell Peppers", "Parsley", "Cloves", "Sea Salt"],
    "preservatives_added": false,
    "allergens": []
  },
  "culinary_notes": {
    "flavor_profile": "Herbaceous, aromatic, medium-hot citrus finish",
    "traditional_uses": ["Marinade for Griot (pork)", "Base for Rice and Beans (Diri ak Pwa)", "Fish & Poultry rubs"],
    "preparation_instructions": "Mix 1 tbsp Epis powder with 2 tbsp warm water and 1 tsp olive oil to rehydrate into fresh paste."
  },
  "inventory": {
    "warehouse_stock": 2400,
    "in_production_pipeline": 5000,
    "is_available_d2c": true,
    "is_available_b2b": true
  }
}
```

### 6.2 Custom Food Box Manifest (`food_box_order.json`)
```json
{
  "box_order_id": "BOX-99201",
  "box_type": "Family Box",
  "customer_id": "cust_440192",
  "stripe_subscription_id": "sub_1N8xQ2LkdIwHu7ix9",
  "cadence": "monthly_subscription",
  "allocated_items_count": 12,
  "manifest": [
    { "sku": "NB-HT-EPI-01", "name": "Haitian Epis", "qty": 2, "slot": "Seasoning" },
    { "sku": "NB-AF-SUY-01", "name": "Suya Seasoning Blend", "qty": 1, "slot": "Seasoning" },
    { "sku": "NB-FD-LAL-01", "name": "Freeze-Dried Lalo Leaves", "qty": 2, "slot": "Vegetable" },
    { "sku": "NB-FD-OKR-01", "name": "Freeze-Dried Okra (Kalalou)", "qty": 2, "slot": "Vegetable" },
    { "sku": "NB-FD-SHR-01", "name": "Freeze-Dried Wild Shrimp", "qty": 2, "slot": "Protein" },
    { "sku": "NB-FD-FIS-01", "name": "Freeze-Dried Snapper Fillets", "qty": 2, "slot": "Protein" },
    { "sku": "NB-FD-MNG-01", "name": "Freeze-Dried Mango Slices", "qty": 1, "slot": "Snack" }
  ],
  "pricing_summary": {
    "base_box_price": 89.99,
    "subscription_discount_15pct": -13.50,
    "shipping_fee": 0.00,
    "tax_amount": 0.00,
    "total_billed": 76.49
  }
}
```

---

## 7. Launch Roadmap (Prove • Build • Scale)

```mermaid
gantt
    title Nourbia Foods™ — Launch Roadmap (Prove • Build • Scale)
    dateFormat  YYYY-MM-DD
    section Phase 1: Prove (Launch)
    Architecture, DB Schema & Stripe Setup :done, 2026-09-01, 20d
    Custom D2C Catalog & PDP (20-40 SKUs)  :done, 2026-09-15, 25d
    Food Box Builder & Stripe Billing MVP  :active, 2026-10-01, 30d
    Taste Lab QR Feedback & Wishlist       :active, 2026-10-15, 25d
    section Phase 2: Build
    Services & Co-Packing Hub (/services)  :2026-11-01, 25d
    B2B Wholesale Portal & Net-30 Engine   :2026-11-15, 35d
    African & Caribbean Food Lines         :2026-12-01, 45d
    Surplus Farm Recovery Portal           :2027-01-15, 35d
    section Phase 3: Scale
    Latin American Food Line Expansion     :2027-03-01, 45d
    Local Delivery / Pickup Logistics      :2027-04-01, 35d
    Nourbia Code Ecosystem                 :2027-04-15, 45d
    International Shipping (Canada/CA)     :2027-06-01, 60d
```

---

**NOURBIA FOODS™**  
*Advancing Culturally Relevant Nutrition • Meeting People Where They Are*  
© Nourbia Foods. All Rights Reserved.
