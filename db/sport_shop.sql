DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS sports;

CREATE TABLE sports (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    active BOOLEAN
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    stock_quantity INT,
    buying_cost INT,
    selling_price INT,
    product_type VARCHAR(255),
    sport_id INT REFERENCES sports(id)
);