-- ==========================================
-- Foreign Key Constraints
-- ==========================================

ALTER TABLE employees
ADD CONSTRAINT fk_employee_store
FOREIGN KEY (store_id)
REFERENCES stores(store_id);

ALTER TABLE orders
ADD CONSTRAINT fk_order_customer
FOREIGN KEY (customer_id)
REFERENCES customers(customer_id);

ALTER TABLE orders
ADD CONSTRAINT fk_order_store
FOREIGN KEY (store_id)
REFERENCES stores(store_id);

ALTER TABLE orders
ADD CONSTRAINT fk_order_employee
FOREIGN KEY (employee_id)
REFERENCES employees(employee_id);

ALTER TABLE order_items
ADD CONSTRAINT fk_orderitem_order
FOREIGN KEY (order_id)
REFERENCES orders(order_id);

ALTER TABLE order_items
ADD CONSTRAINT fk_orderitem_product
FOREIGN KEY (product_id)
REFERENCES products(product_id);

ALTER TABLE inventory
ADD CONSTRAINT fk_inventory_store
FOREIGN KEY (store_id)
REFERENCES stores(store_id);

ALTER TABLE inventory
ADD CONSTRAINT fk_inventory_product
FOREIGN KEY (product_id)
REFERENCES products(product_id);

ALTER TABLE shipments
ADD CONSTRAINT fk_shipment_supplier
FOREIGN KEY (supplier_id)
REFERENCES suppliers(supplier_id);

ALTER TABLE shipments
ADD CONSTRAINT fk_shipment_product
FOREIGN KEY (product_id)
REFERENCES products(product_id);

ALTER TABLE shipments
ADD CONSTRAINT fk_shipment_store
FOREIGN KEY (store_id)
REFERENCES stores(store_id);