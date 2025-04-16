DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;

CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    created_at TEXT,
    FOREIGN KEY(customer_id) REFERENCES customers(id),
    FOREIGN KEY(product_id) REFERENCES products(id)
);

-- Insert sample customers
INSERT INTO customers (name, email) VALUES
('Philip Hickman', 'sarah91@gmail.com'),
('Karina Wilkins', 'natashavalencia@yahoo.com'),
('Tiffany Marshall', 'fhenry@king.com'),
('Megan Jones', 'francisdarin@yahoo.com'),
('Darlene Williams', 'uflores@tran-brennan.biz'),
('Matthew Lee', 'angelaadams@mason-bonilla.com'),
('Eric Bishop', 'laura47@wilson-ritter.com'),
('Juan Kent', 'joseph04@thompson-bryant.com'),
('Michelle Joseph', 'leahlopez@yahoo.com'),
('Barbara Porter', 'rodneygarcia@hotmail.com'),
('Christopher Moore', 'chughes@grant-peters.com'),
('Mary Ward', 'dominguezrobert@gmail.com'),
('Brianna Gray', 'michael60@cooper.com'),
('Zachary Fuller', 'moralesheidi@ramos-johnson.com'),
('Valerie Jones', 'youngangela@richardson.net'),
('Timothy Reid', 'downspamela@flores.com'),
('Erin Harris', 'potteramanda@cook.com'),
('Kelly Rojas', 'zachary32@fitzgerald-johnson.com'),
('Rebecca Garcia', 'abigailwinters@dorsey.com'),
('John Hart', 'bryandickerson@watts.com');

-- Insert sample products
INSERT INTO products (name, price) VALUES
('Laptop', 999.99),
('Phone', 599.49),
('Headphones', 199.95),
('Monitor', 249.99),
('Keyboard', 89.99),
('Mouse', 49.99),
('Tablet', 329.99),
('Charger', 29.99),
('Webcam', 139.99),
('Speaker', 159.95);

-- Insert sample orders
INSERT INTO orders (customer_id, product_id, quantity, created_at) VALUES
(6, 4, 4, '2025-03-20'),
(1, 3, 3, '2024-12-31'),
(4, 7, 5, '2024-06-28'),
(5, 2, 1, '2024-07-22'),
(8, 6, 3, '2024-08-11'),
(11, 8, 4, '2024-10-16'),
(19, 5, 4, '2024-08-09'),
(20, 7, 5, '2024-04-21'),
(15, 4, 2, '2024-06-03'),
(2, 3, 3, '2024-11-13'),
(12, 1, 5, '2024-04-24'),
(17, 1, 4, '2024-09-24'),
(3, 6, 3, '2024-10-10'),
(7, 8, 4, '2024-06-20'),
(14, 5, 3, '2024-06-08'),
(9, 9, 5, '2025-02-28'),
(10, 10, 3, '2024-05-19'),
(13, 2, 2, '2025-02-03'),
(18, 2, 4, '2024-07-07'),
(16, 7, 1, '2024-06-15');
