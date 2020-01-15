/* Name: Weather Observation Station 19
Problem: https://www.hackerrank.com/challenges/weather-observation-station-19/problem
Score: 30
Language: MySQL
*/

SELECT ROUND(SQRT(POW(MAX(LAT_N) - MIN(LAT_N), 2) + POW(MAX(LONG_W) - MIN(LONG_W), 2)), 4)
FROM STATION