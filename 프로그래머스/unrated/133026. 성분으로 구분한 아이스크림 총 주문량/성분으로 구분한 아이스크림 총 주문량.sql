-- 코드를 입력하세요
SELECT i.ingredient_type, sum(h.total_order) as total_order from first_half h inner join icecream_info i on (h.flavor = i.flavor)
group by i.ingredient_type
order by total_order