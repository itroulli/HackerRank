/* Name: Weather Observation Station 16
Problem: https://www.hackerrank.com/challenges/weather-observation-station-16/problem
Score: 10
Language: MySQL
*/

SELECT ROUND(MIN(LAT_N), 4)
FROM STATION
WHERE LAT_N > 38.7780;