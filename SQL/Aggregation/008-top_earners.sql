/* Name: Top Earners
Problem: https://www.hackerrank.com/challenges/earnings-of-employees/problem
Score: 20
Language: MySQL
*/

SELECT salary*months AS earnings, count(*)
FROM employee
GROUP BY 1
ORDER BY 1 DESC
LIMIT 1;