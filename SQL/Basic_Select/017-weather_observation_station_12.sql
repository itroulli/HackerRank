/* Name: Weather Observation Station 12
Problem: https://www.hackerrank.com/challenges/weather-observation-station-12/problem
Score: 15
Language: MySQL
*/

SELECT DISTINCT CITY
FROM STATION
WHERE LEFT(CITY,1) NOT IN ('a','i','e','o','u')
AND RIGHT(CITY,1) NOT IN ('a','i','e','o','u');