DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS designers;



CREATE TABLE designers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    status VARCHAR(255)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255),
    description TEXT,
    quantity INT,
    cost INT,
    price INT,
    designer_id INT REFERENCES designers(id) ON DELETE CASCADE
);