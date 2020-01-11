/* Name: Revising Aggregations - The Count Function
Problem: https://www.hackerrank.com/challenges/revising-aggregations-the-count-function/problem
Score: 10
Language: MySQL
*/

SELECT COUNT(NAME)
FROM CITY
WHERE POPULATION > 100000;