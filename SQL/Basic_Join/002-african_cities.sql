/* Name: African Cities
Problem: https://www.hackerrank.com/challenges/african-cities/problem
Score: 10
Language: MySQL
*/

SELECT CITY.NAME
FROM CITY
JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE
WHERE COUNTRY.CONTINENT = 'Africa';