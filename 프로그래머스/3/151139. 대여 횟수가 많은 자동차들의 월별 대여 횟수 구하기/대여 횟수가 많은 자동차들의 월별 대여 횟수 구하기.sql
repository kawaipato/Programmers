with mm as (
select extract(month from start_date) as MONTH,
    car_id,
    history_id
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where to_char(start_date,'YYYY-MM') between '2022-08' and '2022-10'
and car_id in (
select car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where to_char(start_date,'YYYY-MM') between '2022-08' and '2022-10'
group by car_id having count(*) > 4
    )
)

select MONTH, car_id, count(*) as records
from mm
group by month, car_id
order by month asc, car_id desc;