select category, price, product_name from food_product
where category in ('과자','국','김치','식용유') and price in (select max(price) from food_product group by category)
group by category, product_name
order by price desc