CREATE DATABASE ai_tdv_finacle;
USE ai_tdv_finacle;

CREATE TABLE daily_transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_date DATE,
    customer_id INT,
    amount DECIMAL(10, 2),
    category VARCHAR(50),
    location VARCHAR(100),
    payment_method VARCHAR(50)
);
