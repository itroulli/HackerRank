/* Name: Asian Population
Problem: https://www.hackerrank.com/challenges/asian-population/problem
Score: 10
Language: MySQL
*/

SELECT SUM(CITY.POPULATION)
FROM CITY
JOIN COUNTRY ON CITY.CountryCode = COUNTRY.Code
WHERE COUNTRY.CONTINENT = 'Asia';