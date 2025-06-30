CREATE DATABASE financesight;

USE financesight;

CREATE TABLE invoices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vendor VARCHAR(100),
    amount DECIMAL(10,2),
    invoice_date DATE,
    category VARCHAR(50)
);

CREATE TABLE ratios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    month VARCHAR(10),
    current_ratio DECIMAL(5,2),
    quick_ratio DECIMAL(5,2),
    burn_rate DECIMAL(10,2),
    profit_margin DECIMAL(5,2)
);
CREATE TABLE IF NOT EXISTS ratios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    month VARCHAR(7),
    current_ratio DECIMAL(5, 2),
    quick_ratio DECIMAL(5, 2),
    burn_rate DECIMAL(10, 2),
    profit_margin DECIMAL(5, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
