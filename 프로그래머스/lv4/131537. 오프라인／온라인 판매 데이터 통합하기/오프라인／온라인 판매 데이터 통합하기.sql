-- 코드를 입력하세요
(select to_char(sales_date,'yyyy-mm-dd') as sales_date, product_id, user_id, sales_amount from online_sale
where extract(month from sales_date) = 3)
union all
(select to_char(sales_date,'yyyy-mm-dd') as sales_date, product_id, null as user_id, sales_amount from offline_sale
where extract(month from sales_date) = 3)
order by sales_date, product_id, user_id