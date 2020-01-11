/* Name: Weather Observation Station 4
Problem: https://www.hackerrank.com/challenges/weather-observation-station-4/problem
Score: 10
Language: MySQL
*/

SELECT COUNT(CITY) - COUNT(DISTINCT(CITY))
FROM STATION;