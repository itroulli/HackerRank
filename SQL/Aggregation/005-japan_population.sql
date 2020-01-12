/* Name: Japan Population
Problem: https://www.hackerrank.com/challenges/japan-population/problem
Score: 10
Language: MySQL
*/

SELECT SUM(POPULATION)
FROM CITY
WHERE COUNTRYCODE = 'JPN';