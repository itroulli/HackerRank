/* Name: Weather Observation Station 6
Problem: https://www.hackerrank.com/challenges/weather-observation-station-6/problem
Score: 10
Language: MySQL
*/

SELECT DISTINCT city
FROM station
WHERE city REGEXP "^[aeiou].*";