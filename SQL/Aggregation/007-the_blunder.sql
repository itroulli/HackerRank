/* Name: The Blunder
Problem: https://www.hackerrank.com/challenges/the-blunder/problem
Score: 15
Language: MySQL
*/

SELECT CEIL(AVG(Salary)-AVG(REPLACE(Salary,'0','')))
FROM EMPLOYEES;