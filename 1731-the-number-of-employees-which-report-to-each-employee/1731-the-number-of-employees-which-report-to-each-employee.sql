# Write your MySQL query statement below
select mngr.employee_id, mngr.name, count(emp.employee_id) as reports_count, round(avg(emp.age)) as average_age
from Employees emp
join Employees mngr
on emp.reports_to=mngr.employee_id
group by employee_id
order by employee_id