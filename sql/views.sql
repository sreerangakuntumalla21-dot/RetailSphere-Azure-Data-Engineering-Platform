-- ==========================================
-- Sales Summary View
-- ==========================================

CREATE VIEW sales_summary AS
SELECT
    o.order_id,
    o.order_date,
    c.first_name,
    c.last_name,
    s.store_name,
    oi.product_id,
    oi.quantity,
    oi.total_price
FROM orders o
JOIN customers c
ON o.customer_id = c.customer_id
JOIN stores s
ON o.store_id = s.store_id
JOIN order_items oi
ON o.order_id = oi.order_id;