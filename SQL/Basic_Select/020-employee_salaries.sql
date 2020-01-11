/* Name: Employee Salaries
Problem: https://www.hackerrank.com/challenges/salary-of-employees/problem
Score: 10
Language: MySQL
*/

SELECT name
FROM Employee
WHERE salary > 2000 AND months < 10;