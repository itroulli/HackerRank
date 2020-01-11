/* Name: Weather Observation Station 3
Problem: https://www.hackerrank.com/challenges/weather-observation-station-3/problem
Score: 10
Language: MySQL
*/

SELECT DISTINCT(CITY)
FROM STATION
WHERE (ID%2) = 0;