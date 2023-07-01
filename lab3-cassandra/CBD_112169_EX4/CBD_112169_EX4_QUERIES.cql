-- JSON SELECTS
select json * from user;
select json * from purchase;
select json * from product;
select json * from opinion;

-- SELECTS
-- 1 select all users
select * from user;

-- 2 select all purchases by given user
select * from purchase where user_name='justwatchin';

-- 3 select all purchases by given user order by oldest purchases
select * from purchase where user_name='justwatchin' order by purchased_date desc;

-- 4 select all product opinions
select * from opinion where product_name='Extra-Long - linki zapasowe - Kendama';

-- 5 select product by given name
select * from product where product_name='Extra-Long - linki zapasowe - Kendama';

-- 6 select all purchases by given order status
select * from purchases_by_status where status='AWAITING_PAYMENT';

-- 7 select all not paid purchases with the oldest date
select * from purchases_by_status where status='AWAITING_PAYMENT' order by purchased_date asc;

-- 8 select all opinions by a given user
select * from opinions_by_user where user_name='super_user';

-- 9 select all users that have been opinioned a given rating 5
select user_name from opinion where ratings contains 5;

-- 10 select all purchases that cointains a given product
select * from purchase where products contains 'Extra-Long - linki zapasowe - Kendama';


-- UPDATES
-- 1 change email for user
update user set email='user_new_email@email.xyz' where user_name='justwatchin';

-- 2 change status of a purchase
update purchase set status='FINISHED' where user_name='justwatchin' and purchased_date='2022-08-21';

-- 3 update product data
update product set price=200, color='red', description='descritpion', producer='YEPPA' where product_name='BIG BROTHER BAMBOO' and release_date='2021-11-11';

-- 4 add ratings to opinion
UPDATE opinion SET ratings = [1,1,1] + ratings WHERE product_name='Krom Pop' AND created_date='2020-09-10 09:54:21';


-- DELETES
-- 1 delete user
delete from user where user_name='super_user';

-- 2 delete user purchases
delete from purchase where user_name='super_user';

-- 3 delete product by its name
delete from product where product_name='Waldo Bamboo Tacky';

-- 4 delete opinion
delete from opinion where product_name='Waldo Bamboo Tacky';
