/* Name: Revising Aggregations - The Sum Function
Problem: https://www.hackerrank.com/challenges/revising-aggregations-sum/problem
Score: 10
Language: MySQL
*/

SELECT SUM(POPULATION)
FROM CITY
WHERE DISTRICT = 'California';