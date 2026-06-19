# Multi-Vendor E-Commerce Platform

A robust, feature-rich Django-based e-commerce platform that enables multiple independent vendors to register, list, manage, and sell their products. Customers can browse products, manage their shopping cart, save items for later, write product reviews, and complete checkout — all within a single unified storefront.

---

## 🚀 Key Features

### 👤 User & Authentication Management (`account` app)
- **Custom User Model**: Utilizes `CustomUser` extending Django's `AbstractUser` with a unique `email` field and an `is_vendor` boolean flag to distinguish vendor accounts from regular customers.
- **Email Authentication**: Custom authentication backend (`EmailBackend`) allowing users to sign in via email address instead of username.
- **Registration & Profile Management**: Custom forms for seamless user onboarding and profile updates.

### 🛍️ Storefront & Discovery (`store` app)
- **Interactive Homepage**: Dynamically displays all products, a random selection of featured categories, and featured vendor profiles.
- **Product Listing & Category Filtering**: Browse all products or filter them by a specific category.
- **Product Search**: Search products by name or description using a case-insensitive query (`Q` objects).
- **Recently Viewed Products**: Session-persistent tracking of the last products a user visited, powered by a custom `RecentlyViewed` session class.
- **Product Reviews & Ratings**: Authenticated customers can submit star ratings and written reviews directly on product detail pages.

### 🛒 Shopping Cart & Checkout (`cart` app)
- **Session-Based Cart**: Add items, adjust quantities, or remove items from the cart without requiring a database write — all powered by Django sessions (`CART_SESSION_ID`). Sessions persist for 24 hours (`SESSION_COOKIE_AGE = 86400`).
- **Checkout Flow**: Customers select a saved delivery address from their account to finalise the order.
- **Order Creation**: Upon successful checkout, an `Order` record and individual `OrderItem` records are automatically created and linked to the customer.

### 🏢 Vendor Ecosystem (`vendor` app)
- **Vendor Registration**: Any authenticated user can apply to become a vendor. On approval, their `is_vendor` flag is set to `True`.
- **Edit Vendor Profile**: Update business name, logo, contact number, and address details.
- **Vendor Dashboard**: Personal command centre showing the vendor's own product listings and a filtered view of orders placed for their products.
- **Product CRUD**:
  - **Add Product**: Create a product with category, name, price, stock quantity (`in_store`), description, and multiple gallery images (`ProductImage`).
  - **Edit Product**: Update product details and selectively delete individual gallery images (files are also removed from `MEDIA_ROOT` to avoid clutter).
  - **Delete Product**: Remove a product and all associated gallery image files from storage.

### 📊 Customer Dashboard (`dashboard` app)
- **Account Hub**: Central landing page for all account-related activities.
- **Profile Center**: View and edit personal information.
- **Saved Products**: Save or remove products for later via a session-based wishlist (`SavedProduct`). Requires login.
- **Address Book**: Add, edit, and delete multiple delivery addresses. Smart redirect back to checkout when address management is triggered from the checkout page.
- **Order History**: Review all past orders and their individual line items.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Framework** | Django 6.0.6 (Python 3.10+) |
| **Database** | SQLite (default; swappable to PostgreSQL or MySQL) |
| **Image Handling** | Pillow 12.2.0 |
| **Forms** | django-crispy-forms 2.6 + crispy-bootstrap4 |
| **Environment Config** | django-environ 0.14.0 (`.env` file support) |
| **Static Files** | whitenoise 6.12.0 (compressed & cached static serving) |
| **Frontend** | Bootstrap 4, HTML5, CSS3, JavaScript |

---

## 📁 Project Structure

```text
multi_vendor_ecommerce/
│
├── account/                    # Custom user model, email auth backend, registration & login
├── cart/                       # Session-based cart, checkout, and order creation logic
├── dashboard/                  # Customer dashboard, profiles, addresses, saved products, orders; also houses all shared models
├── multi_vendor_ecommerce/     # Core project: settings.py, root urls.py, wsgi.py, asgi.py
├── static/                     # Global static assets (CSS, JS, images)
├── store/                      # Storefront views: homepage, product listing, detail, search, reviews
├── templates/                  # Project-level base templates and shared layouts
├── uploads/                    # User-uploaded media files (product gallery images, vendor logos)
├── vendor/                     # Vendor registration, dashboard, and product management views
│
├── db.sqlite3                  # Local SQLite database (auto-created on first migrate)
├── manage.py                   # Django management CLI
└── requirements.txt            # Python package dependencies
```

---

## 🗄️ Database Models Overview

All core business models live in the `dashboard` app.

| Model | App | Key Fields |
|---|---|---|
| `CustomUser` | `account` | `email` (unique), `is_vendor` (bool), inherits all `AbstractUser` fields |
| `Vendor` | `dashboard` | `user` (OneToOne → CustomUser), `vendor_name`, `logo`, `number`, `street`, `city`, `state`, `country` |
| `Category` | `dashboard` | `category` (name string) |
| `Product` | `dashboard` | `user` (FK → CustomUser), `category` (FK → Category), `name`, `slug` (auto-generated, unique), `price`, `in_store` (stock qty), `description`, `date_created`, `last_modified` |
| `ProductImage` | `dashboard` | `product` (FK → Product), `image` (gallery photo) |
| `ProductReview` | `dashboard` | `product` (FK → Product), `username`, `rating`, `review` |
| `Order` | `dashboard` | `first_name`, `last_name`, `city`, `state`, `country`, `phone_number`, `paid_amount`, `is_paid`, `vendor_id`, `created_by` (FK → CustomUser), `time_created` |
| `OrderItem` | `dashboard` | `order` (FK → Order), `product` (FK → Product), `price`, `quantity` |
| `Address` | `dashboard` | `user` (FK → CustomUser), `first_name`, `last_name`, `city`, `state`, `country`, `phone_number` |

> **Note on slugs**: Product slugs are auto-generated using `unique_product_slug()`, which prepends an 8-character random alphanumeric string to the slugified product name to guarantee uniqueness.

---

## 🌐 URL Routes

| URL Prefix | App | Description |
|---|---|---|
| `/` | `store` | Storefront — homepage, product listings, search, detail, reviews |
| `/account/` | `account` | Registration, login, logout |
| `/dashboard/` | `dashboard` | Customer profile, orders, addresses, saved products |
| `/vendor/` | `vendor` | Vendor registration, dashboard, product CRUD |
| `/cart/` | `cart` | Cart view, add/update/remove items, checkout |
| `/admin/` | Django Admin | Built-in admin panel |

---

## 💻 Getting Started & Installation

### 1. Prerequisites
Ensure you have **Python 3.10+** and **pip** installed on your machine.

### 2. Clone the Repository
```bash
git clone <repository-url>
cd multi_vendor_ecommerce
```

### 3. Set Up a Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables
Create a `.env` file in the project root directory. The project uses **django-environ** to load settings from this file:
```env
# .env
SECRET_KEY=your-strong-secret-key-here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

> **Note**: If `.env` is absent or a variable is not set, safe defaults are used (`DEBUG=True`, the bundled insecure key, and `localhost`/`127.0.0.1` for allowed hosts). Always set all three in production.

### 6. Apply Database Migrations
Create the SQLite database and set up all schema tables:
```bash
python manage.py migrate
```

### 7. Create a Superuser
Set up an admin account to access Django's admin panel:
```bash
python manage.py createsuperuser
```

### 8. Run the Development Server
```bash
python manage.py runserver
```

- **Storefront**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin panel**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🔒 Security Recommendations for Production

> These settings are intentionally permissive for local development. Harden them before any public deployment.

- **Secret Key**: Set a strong, randomly generated `SECRET_KEY` in your `.env` file. The fallback insecure key in `settings.py` must never be used in production.
- **Debug Mode**: Set `DEBUG=False` in your `.env` file. Never expose debug pages publicly.
- **Allowed Hosts**: Set `ALLOWED_HOSTS` in your `.env` file to your exact domain name(s), e.g. `ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com`.
- **Static Files**: Static files are already configured for production. Run `python manage.py collectstatic` to gather all assets into `staticfiles/`. **whitenoise** (`CompressedManifestStaticFilesStorage`) is active via middleware and will serve compressed, fingerprinted static files automatically — no Nginx/CDN required for basic deployments.
- **Database**: Migrate from SQLite to PostgreSQL or MySQL for production workloads. Install `psycopg2-binary` (PostgreSQL) or `mysqlclient` (MySQL) and update the `DATABASES` setting in `settings.py`. You can also add `DATABASE_URL` support via `django-environ`'s `env.db()` helper.
- **Media Files**: User-uploaded files (`uploads/`) are served from the local filesystem in development. For production, use a cloud storage backend (e.g., AWS S3 or Cloudinary) with `django-storages`.
