/* Name: Higher Than 75 Marks
Problem: https://www.hackerrank.com/challenges/more-than-75-marks/problem
Score: 15
Language: MySQL
*/

SELECT Name
FROM STUDENTS
WHERE Marks > 75
ORDER BY RIGHT(Name, 3) ASC, ID ASC;