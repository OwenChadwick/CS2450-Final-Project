
CREATE DATABASE IF NOT EXISTS final_reservations_db;
USE final_reservations_db;

-- ===========================
-- 1. Customers
-- ===========================
CREATE TABLE IF NOT EXISTS customers (
    cust_id INT AUTO_INCREMENT PRIMARY KEY,
    last_name VARCHAR(100),
    first_name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20)
);

-- ===========================
-- 2. Boats
-- ===========================
CREATE TABLE IF NOT EXISTS boats (
    boat_id VARCHAR(6) PRIMARY KEY,
    cust_id INT NOT NULL,
    length INT NOT NULL,
    FOREIGN KEY (cust_id) REFERENCES customers(cust_id)
);

-- ===========================
-- 3. Slips
-- ===========================
CREATE TABLE IF NOT EXISTS slips (
    slip_number INT PRIMARY KEY,
    availability BOOLEAN DEFAULT TRUE,
    length INT NOT NULL
);

-- ===========================
-- 4. Reservations
-- ===========================
CREATE TABLE IF NOT EXISTS reservations (
    reservation_id INT AUTO_INCREMENT PRIMARY KEY,
    cust_id INT NOT NULL,
    boat_id VARCHAR(6) NOT NULL,
    slip_number INT NOT NULL,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (cust_id) REFERENCES customers(cust_id),
    FOREIGN KEY (boat_id) REFERENCES boats(boat_id),
    FOREIGN KEY (slip_number) REFERENCES slips(slip_number)
);



INSERT INTO slips (slip_number, availability,length)
VALUES
(2, TRUE, 20),
(3, TRUE, 40),
(4, TRUE, 50);
