-- FREE THEMED DATABASE TOPIC: Simple Kendama Shop
DROP KEYSPACE cbd_112169_ex4;
CREATE KEYSPACE cbd_112169_ex4 WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
USE cbd_112169_ex4;
-- pretty output (uncomment)
-- EXPAND ON;

create table user(
    user_name text,
    email text,
    created_date timestamp,
    primary key((user_name))
);

create table product (
    product_name text,
    producer text,
    price int,
    color text,
    description text,
    release_date timestamp,
    primary key((product_name), release_date)
)
WITH CLUSTERING ORDER BY (release_date DESC);

create table purchase (
    user_name text,
    total double,
    products map<text, text>,
    purchased_date timestamp,
    status text,
    primary key ((user_name), purchased_date)
)
WITH CLUSTERING ORDER BY (purchased_date DESC);

create table opinion (
    user_name text,
    product_name text,
    content text,
    avg_rating int,
    votes int,
    ratings list<int>,
    created_date timestamp,
    primary key ((product_name), created_date)
)
WITH CLUSTERING ORDER BY (created_date DESC);
-- ddls for additional queries
-- 6,7
CREATE MATERIALIZED VIEW purchases_by_status 
    AS SELECT status, total, user_name, purchased_date
    FROM purchase
    WHERE user_name IS NOT NULL AND purchased_date IS NOT NULL AND status IS NOT NULL
PRIMARY KEY ((status), purchased_date, user_name);
-- 8 
CREATE MATERIALIZED VIEW opinions_by_user 
    AS SELECT user_name, product_name, content, avg_rating, votes, ratings, created_date
    FROM opinion
    WHERE product_name IS NOT NULL AND user_name IS NOT NULL AND created_date IS NOT NULL
PRIMARY KEY ((user_name), created_date, product_name);

 -- create some secondary indexes 
-- 9 select all users that opinioned with a rating 5. They would be be rewarded with a promo code.
create index on opinion(ratings);

-- 10 select all purchases that cointains a given product
create index on purchase(products);

