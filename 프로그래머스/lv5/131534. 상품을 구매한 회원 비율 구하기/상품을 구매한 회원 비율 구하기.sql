-- 코드를 입력하세요
SELECT to_char(o.sales_date,'yyyy') as year, extract(month from o.sales_date) as month, count(distinct o.user_id) as purchased_users, round(1.00 * count(distinct o.user_id)/(select count(distinct user_id) from user_info where to_char(joined,'yyyy') = 2021),1)
from user_info u inner join online_sale o on (u.user_id = o.user_id)
where to_char(u.joined,'yyyy') = 2021
group by to_char(o.sales_date,'yyyy'), extract(month from o.sales_date)
order by year, month