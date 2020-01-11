/* Name: The PADS
Problem: https://www.hackerrank.com/challenges/the-pads/problem
Score: 30
Language: MySQL
*/

SELECT CONCAT(Name,'(', SUBSTRING(OCCUPATION,1,1),')') AS name
FROM OCCUPATIONS
ORDER BY name;
SELECT CONCAT('There are a total of ',' ',COUNT(OCCUPATION), ' ', LOWER(OCCUPATION), 's.') AS total
FROM OCCUPATIONS
GROUP BY OCCUPATION
ORDER BY total;