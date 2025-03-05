select distinct id, email, first_name, last_name
from developers
join skillcodes on skillcodes.code & developers.skill_code=skillcodes.code
where skillcodes.name in ('C#','Python')
order by id