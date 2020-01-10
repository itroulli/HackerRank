/* Name: Revising the Select Query II
Problem: https://www.hackerrank.com/challenges/revising-the-select-query-2/problem
Score: 10
Language: MySQL
*/

SELECT NAME
FROM CITY
WHERE COUNTRYCODE = 'USA'
AND POPULATION > 120000;