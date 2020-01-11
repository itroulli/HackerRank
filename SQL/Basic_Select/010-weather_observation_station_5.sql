/* Name: Weather Observation Station 5
Problem: https://www.hackerrank.com/challenges/weather-observation-station-5/problem
Score: 30
Language: MySQL
*/

(SELECT `CITY`, CHAR_LENGTH(CITY)
FROM STATION
ORDER BY CHAR_LENGTH(CITY) DESC
LIMIT 1)
UNION
(SELECT CITY, CHAR_LENGTH(CITY)
FROM STATION
ORDER BY CHAR_LENGTH(CITY) ASC, CITY ASC
LIMIT 1);