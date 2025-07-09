-- 코드를 입력하세요
SELECT name, count(name)
from ANIMAL_INS
group by name
having count(name) >=2
order by name;
