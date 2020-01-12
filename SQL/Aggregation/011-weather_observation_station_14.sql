/* Name: Weather Observation Station 14
Problem: https://www.hackerrank.com/challenges/weather-observation-station-14/problem
Score: 10
Language: MySQL
*/

SELECT ROUND(MAX(LAT_N), 4)
FROM STATION
WHERE LAT_N < 137.2345;