/* Name: Weather Observation Station 20
Problem: https://www.hackerrank.com/challenges/weather-observation-station-20/problem
Score: 40
Language: MySQL
*/

SET @rowindex := -1;

SELECT
   ROUND(AVG(s.lat),4)
FROM
   (SELECT @rowindex:=@rowindex + 1 AS rowindex,
           STATION.LAT_N AS lat
    FROM STATION
    ORDER BY STATION.LAT_N) AS s
WHERE
s.rowindex IN (FLOOR(@rowindex / 2) , CEIL(@rowindex / 2));