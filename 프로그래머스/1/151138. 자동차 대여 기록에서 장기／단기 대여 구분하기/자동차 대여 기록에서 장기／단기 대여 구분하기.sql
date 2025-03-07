
select history_id, car_id,
date_format(start_date,'%Y-%m-%d') as start_date,
date_format(end_date,'%Y-%m-%d') as end_date,
if(datediff(end_date,start_date)<29,'단기 대여','장기 대여') as rent_type
from car_rental_company_rental_history
where date_format(start_date,'%Y-%m') = '2022-09'
order by 1 desc;