# RetailSphere - Database Design

## Entity Relationship Overview

The PostgreSQL database follows a relational model.

Main Tables

Customers
│
├── Orders
│      │
│      └── Order_Items
│
Products
│
├── Categories
│
Stores
│
Inventory
│
Suppliers
│
Employees
│
Shipments

---

## Relationships

Customers
→ One customer can place multiple orders.

Orders
→ One order contains multiple order items.

Products
→ One product belongs to one category.

Stores
→ Stores maintain inventory and process orders.

Suppliers
→ Suppliers provide products.

Employees
→ Employees work in stores.

Shipments
→ Shipments deliver customer orders.

---

## Primary Keys

- customer_id
- order_id
- product_id
- category_id
- store_id
- supplier_id
- employee_id
- shipment_id

---

## Foreign Keys

Orders.customer_id → Customers.customer_id

Order_Items.order_id → Orders.order_id

Order_Items.product_id → Products.product_id

Products.category_id → Categories.category_id

Inventory.product_id → Products.product_id

Inventory.store_id → Stores.store_id

Employees.store_id → Stores.store_id

Shipments.order_id → Orders.order_id

---

This schema represents a simplified enterprise retail database for analytics and reporting.