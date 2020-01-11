/* Name: Weather Observation Station 10
Problem: https://www.hackerrank.com/challenges/weather-observation-station-10/problem
Score: 10
Language: MySQL
*/

SELECT DISTINCT CITY
FROM STATION
WHERE RIGHT(CITY,1) NOT IN ('a','i','e','o','u');