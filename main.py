CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    hire_date DATE
);

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10, 2),
    stock_quantity INT
);

CREATE TABLE customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    city VARCHAR(50)
);

CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10, 2)
);

INSERT INTO employees (first_name, last_name, department, hire_date) VALUES
('John', 'Doe', 'Sales', '2020-01-15'),
('Jane', 'Smith', 'Marketing', '2018-07-20'),
('Alice', 'Johnson', 'Sales', '2019-03-30');

INSERT INTO products (name, price, stock_quantity) VALUES
('Laptop', 1200.00, 30),
('Smartphone', 800.00, 50),
('Tablet', 400.00, 70);

INSERT INTO customers (first_name, last_name, city) VALUES
('Emily', 'Clark', 'New York'),
('Michael', 'Brown', 'Los Angeles'),
('Sarah', 'Wilson', 'New York');

INSERT INTO orders (customer_id, order_date, total_amount) VALUES
(1, '2023-02-15', 1500.00),
(2, '2023-03-10', 800.00),
(3, '2023-01-05', 400.00);

SELECT * FROM employees ORDER BY last_name ASC;
SELECT * FROM products ORDER BY price DESC;

SELECT * FROM customers WHERE city = 'New York';
SELECT * FROM orders WHERE order_date >= '2023-01-01';

SELECT * FROM employees WHERE department = 'Sales' ORDER BY hire_date DESC;
SELECT * FROM products WHERE stock_quantity > 50 ORDER BY price ASC;
