/* Name: Weather Observation Station 17
Problem: https://www.hackerrank.com/challenges/weather-observation-station-17/problem
Score: 15
Language: MySQL
*/

SELECT ROUND(LONG_W, 4)
FROM STATION
WHERE LAT_N = (SELECT MIN(LAT_N) FROM STATION WHERE LAT_N > 38.7780);