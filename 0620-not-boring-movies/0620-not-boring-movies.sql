# Write your MySQL query statement below
SELECT * FROM Cinema
WHERE Description != 'boring'
HAVING (id%2)<>0
ORDER BY rating DESC