-- ==========================================
-- Performance Indexes
-- ==========================================

CREATE INDEX idx_orders_customer
ON orders(customer_id);

CREATE INDEX idx_orders_store
ON orders(store_id);

CREATE INDEX idx_order_items_order
ON order_items(order_id);

CREATE INDEX idx_order_items_product
ON order_items(product_id);

CREATE INDEX idx_inventory_product
ON inventory(product_id);

CREATE INDEX idx_inventory_store
ON inventory(store_id);

CREATE INDEX idx_shipments_supplier
ON shipments(supplier_id);