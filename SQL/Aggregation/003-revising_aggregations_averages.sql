/* Name: Revising Aggregations - Averages
Problem: https://www.hackerrank.com/challenges/revising-aggregations-the-average-function/problem
Score: 10
Language: MySQL
*/

SELECT AVG(POPULATION)
FROM CITY
WHERE DISTRICT = 'California';