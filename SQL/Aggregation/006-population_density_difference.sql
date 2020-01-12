/* Name: Population Density Difference
Problem: https://www.hackerrank.com/challenges/population-density-difference/problem
Score: 10
Language: MySQL
*/

SELECT MAX(POPULATION) - MIN(POPULATION)
FROM CITY;