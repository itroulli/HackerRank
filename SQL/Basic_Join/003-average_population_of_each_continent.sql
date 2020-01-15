/* Name: Average Population of Each Continent
Problem: https://www.hackerrank.com/challenges/average-population-of-each-continent/problem
Score: 10
Language: MySQL
*/

SELECT COUNTRY.Continent, FLOOR(AVG(CITY.POPULATION))
FROM COUNTRY
JOIN CITY
ON CITY.CountryCode = COUNTRY.Code
GROUP BY COUNTRY.Continent;