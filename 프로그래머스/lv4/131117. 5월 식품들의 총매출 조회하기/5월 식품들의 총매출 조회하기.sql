-- 코드를 입력하세요
SELECT p.product_id, p.product_name, sum(p.price * o.amount) as total_price from food_product p inner join food_order o on (p.product_id = o.product_id) 
where to_char(o.produce_date,'mm') = 05
group by p.product_id, p.product_name
order by total_price desc, p.product_id asc