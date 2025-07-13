-- Create tables

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    location VARCHAR(50)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price INT
);

CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    sale_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Queries

-- Top 5 products by revenue
SELECT p.product_name, SUM(s.quantity * p.price) AS total_revenue
FROM sales s
JOIN products p ON s.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_revenue DESC
LIMIT 5;

-- Top 5 customers
SELECT c.customer_name, SUM(s.quantity * p.price) AS total_spent
FROM sales s
JOIN customers c ON s.customer_id = c.customer_id
JOIN products p ON s.product_id = p.product_id
GROUP BY c.customer_name
ORDER BY total_spent DESC
LIMIT 5;

-- Monthly sales trend
SELECT DATE_TRUNC('month', sale_date) AS month, SUM(s.quantity * p.price) AS monthly_revenue
FROM sales s
JOIN products p ON s.product_id = p.product_id
GROUP BY month
ORDER BY month;

-- Revenue by location
SELECT c.location, SUM(s.quantity * p.price) AS total_revenue
FROM sales s
JOIN customers c ON s.customer_id = c.customer_id
JOIN products p ON s.product_id = p.product_id
GROUP BY c.location
ORDER BY total_revenue DESC;

-- Revenue by category
SELECT p.category, SUM(s.quantity * p.price) AS category_revenue
FROM sales s
JOIN products p ON s.product_id = p.product_id
GROUP BY p.category
ORDER BY category_revenue DESC;
