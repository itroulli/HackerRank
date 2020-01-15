/* Name: The Report
Problem: https://www.hackerrank.com/challenges/the-report/problem
Score: 20
Language: MySQL
*/

SELECT (CASE WHEN g.Grade <8 THEN 'NULL' ELSE s.Name END), g.Grade, s.Marks
FROM Students as s
JOIN Grades as g
ON  s.Marks BETWEEN g.Min_Mark AND g.Max_Mark
ORDER BY g.Grade DESC, s.Name, s.Marks;