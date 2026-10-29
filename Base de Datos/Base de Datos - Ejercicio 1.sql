CREATE TABLE "Products"(
    "product_id" INT NOT NULL,
    "product_name" VARCHAR(255) NOT NULL,
    "product_price" DECIMAL(8, 2) NOT NULL,
    "product_entry_date" DATE NOT NULL,
    "product_brand" VARCHAR(255) NOT NULL,
    "product_stock_available" DECIMAL(8, 2) NOT NULL,
    "is_active" CHAR(255) NOT NULL
);
ALTER TABLE
    "Products" ADD CONSTRAINT "products_product_id_primary" PRIMARY KEY("product_id");
CREATE TABLE "Invoices"(
    "invoice_id" INT NOT NULL,
    "invoice_number" VARCHAR(255) NOT NULL,
    "buyer_id" INT NOT NULL,
    "invoice_date" DATE NOT NULL,
    "status" CHAR(255) NOT NULL,
    "tax_amount" DECIMAL(8, 2) NOT NULL,
    "total_amount" DECIMAL(8, 2) NOT NULL,
    "created_at" INT NOT NULL,
    "notes" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Invoices" ADD CONSTRAINT "invoices_invoice_id_primary" PRIMARY KEY("invoice_id");
CREATE UNIQUE INDEX "invoices_invoice_number_unique" ON
    "Invoices"("invoice_number");
CREATE TABLE "Inventory movements"(
    "movement_id" INT NOT NULL,
    "product_Id" INT NOT NULL,
    "movement_date" INT NOT NULL,
    "movement_type" VARCHAR(255) NOT NULL,
    "quantity" INT NOT NULL,
    "reference_type" VARCHAR(255) NOT NULL,
    "reference_id" VARCHAR(255) NOT NULL,
    "notes" VARCHAR(255) NOT NULL,
    "created_by" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Inventory movements" ADD CONSTRAINT "inventory movements_movement_id_primary" PRIMARY KEY("movement_id");
CREATE TABLE "Shopping Cart"(
    "cart_id" INT NOT NULL,
    "buyer_id" INT NOT NULL,
    "created_at" INT NOT NULL,
    "updated_at" INT NOT NULL,
    "cart_status" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Shopping Cart" ADD CONSTRAINT "shopping cart_cart_id_primary" PRIMARY KEY("cart_id");
CREATE TABLE "Buyers"(
    "buyer_id" INT NOT NULL,
    "buyer_name" VARCHAR(255) NOT NULL,
    "buyer_phone" VARCHAR(255) NOT NULL,
    "buyer_email" VARCHAR(255) NOT NULL,
    "buyer_tax_id" VARCHAR(255) NOT NULL,
    "buyer_address" VARCHAR(255) NOT NULL,
    "created_at" INT NOT NULL,
    "is_active" CHAR(255) NOT NULL
);
ALTER TABLE
    "Buyers" ADD CONSTRAINT "buyers_buyer_id_primary" PRIMARY KEY("buyer_id");
CREATE TABLE "Shopping Cart items"(
    "cart_item_id" INT NOT NULL,
    "cart_id" INT NOT NULL,
    "product_id" INT NOT NULL,
    "quantity" INT NOT NULL,
    "unit_price" DECIMAL(8, 2) NOT NULL,
    "created_at" INT NOT NULL
);
ALTER TABLE
    "Shopping Cart items" ADD CONSTRAINT "shopping cart items_cart_item_id_primary" PRIMARY KEY("cart_item_id");
CREATE TABLE "Invoices items"(
    "invoice_item_id" INT NOT NULL,
    "invoice_id" INT NOT NULL,
    "product_id" INT NOT NULL,
    "quantity" INT NOT NULL,
    "unit_price" DECIMAL(8, 2) NOT NULL,
    "discount" DECIMAL(8, 2) NOT NULL,
    "total" DECIMAL(8, 2) NOT NULL
);
ALTER TABLE
    "Invoices items" ADD CONSTRAINT "invoices items_invoice_item_id_primary" PRIMARY KEY("invoice_item_id");
ALTER TABLE
    "Inventory movements" ADD CONSTRAINT "inventory movements_product_id_foreign" FOREIGN KEY("product_Id") REFERENCES "Products"("product_id");
ALTER TABLE
    "Shopping Cart items" ADD CONSTRAINT "shopping cart items_cart_id_foreign" FOREIGN KEY("cart_id") REFERENCES "Shopping Cart"("cart_id");
ALTER TABLE
    "Shopping Cart" ADD CONSTRAINT "shopping cart_buyer_id_foreign" FOREIGN KEY("buyer_id") REFERENCES "Buyers"("buyer_id");
ALTER TABLE
    "Products" ADD CONSTRAINT "products_product_price_foreign" FOREIGN KEY("product_price") REFERENCES "Invoices items"("product_id");
ALTER TABLE
    "Invoices" ADD CONSTRAINT "invoices_buyer_id_foreign" FOREIGN KEY("buyer_id") REFERENCES "Buyers"("buyer_id");
ALTER TABLE
    "Shopping Cart items" ADD CONSTRAINT "shopping cart items_product_id_foreign" FOREIGN KEY("product_id") REFERENCES "Products"("product_id");
ALTER TABLE
    "Invoices items" ADD CONSTRAINT "invoices items_invoice_id_foreign" FOREIGN KEY("invoice_id") REFERENCES "Invoices"("invoice_id");