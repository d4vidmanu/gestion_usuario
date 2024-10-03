-- Conéctate a la base de datos 'postgres' antes de intentar eliminar 'gestion_usuarios'
\c postgres;

-- Elimina la base de datos si existe
DROP DATABASE IF EXISTS gestion_usuarios;

-- Crea la base de datos nuevamente
CREATE DATABASE gestion_usuarios;

-- Conéctate a la base de datos recién creada
\c gestion_usuarios;

-- Elimina las tablas si existen y crea nuevas
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);

DROP TABLE IF EXISTS subscriptions;
CREATE TABLE subscriptions (
    id SERIAL PRIMARY KEY,
    subscription_type VARCHAR(10) NOT NULL,
    start_date DATE DEFAULT CURRENT_DATE,
    end_date DATE,
    user_id INT REFERENCES users(id)
);

DROP TABLE IF EXISTS reviews;
CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    rating INT NOT NULL,
    created_at DATE DEFAULT CURRENT_DATE,
    ride_id INT,
    user_id INT REFERENCES users(id)
);
