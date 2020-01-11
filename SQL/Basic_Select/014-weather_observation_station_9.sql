/* Name: Weather Observation Station 9
Problem: https://www.hackerrank.com/challenges/weather-observation-station-9/problem
Score: 10
Language: MySQL
*/

SELECT DISTINCT CITY
FROM STATION
WHERE LEFT(CITY,1) NOT IN ('a','i','e','o','u');