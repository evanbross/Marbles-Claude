-- Art Glass Marble Collection Database Schema

CREATE DATABASE IF NOT EXISTS marble_collection;
USE marble_collection;

-- Artists table
CREATE TABLE artists (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    bio TEXT,
    website VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Styles table
CREATE TABLE styles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Vendors/Sources table
CREATE TABLE vendors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255),
    website VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Marbles table
CREATE TABLE marbles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    artist_id INT,
    style_id INT,
    size_mm DECIMAL(5,2) NOT NULL,
    price DECIMAL(10,2),
    purchase_date DATE,
    vendor_id INT,
    description TEXT,
    image_url VARCHAR(500),
    ai_identified_style VARCHAR(100),
    ai_confidence DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (artist_id) REFERENCES artists(id) ON DELETE SET NULL,
    FOREIGN KEY (style_id) REFERENCES styles(id) ON DELETE SET NULL,
    FOREIGN KEY (vendor_id) REFERENCES vendors(id) ON DELETE SET NULL
);

-- Indexes for faster searches
CREATE INDEX idx_artist ON marbles(artist_id);
CREATE INDEX idx_style ON marbles(style_id);
CREATE INDEX idx_size ON marbles(size_mm);
CREATE INDEX idx_price ON marbles(price);
