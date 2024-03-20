# Write your MySQL query statement below
select p.product_id, ifnull(round(sum(units*price)/ sum(units),2),0) as average_price
from Prices p
left join UnitsSold us
on p.product_id=us.product_id and (us.purchase_date BETWEEN start_date AND end_date)
group by product_id

