/* Name: Weather Observation Station 7
Problem: https://www.hackerrank.com/challenges/weather-observation-station-7/problem
Score: 10
Language: MySQL
*/

SELECT DISTINCT CITY
FROM STATION
WHERE RIGHT(CITY,1) IN ('a','i','e','o','u');