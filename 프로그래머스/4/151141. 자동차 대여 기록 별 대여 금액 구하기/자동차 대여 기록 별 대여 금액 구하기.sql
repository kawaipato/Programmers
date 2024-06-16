with carr as (select H.*, C.car_type, (end_date - start_date + 1) days, (end_date - start_date + 1) * C.daily_fee all_fee
from CAR_RENTAL_COMPANY_RENTAL_HISTORY H inner join CAR_RENTAL_COMPANY_CAR C
on H.car_id = C.car_id and C.car_type = '트럭')

select history_id, (all_fee * (100 - NVL(discount_rate,0))/100) fee
from carr C left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN P
on C.car_type = P.car_type and
case when end_date - start_date + 1 between 7 and 29 then 7
    when end_date - start_date + 1 between 30 and 89 then 30
    when end_date - start_date + 1 >= 90 then 90 end = REPLACE(DURATION_TYPE(+),'일 이상')
order by 2 desc, 1 desc;