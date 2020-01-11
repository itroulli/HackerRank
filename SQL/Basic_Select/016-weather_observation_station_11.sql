/* Name: Weather Observation Station 11
Problem: https://www.hackerrank.com/challenges/weather-observation-station-11/problem
Score: 15
Language: MySQL
*/

SELECT DISTINCT CITY
FROM STATION
WHERE LEFT(CITY,1) NOT IN ('a','i','e','o','u')
OR RIGHT(CITY,1) NOT IN ('a','i','e','o','u');