// Name: Day 2: Conditional Statements: If-Else
// Problem: https://www.hackerrank.com/challenges/js10-if-else/problem
// Score: 10


function getGrade(score) {
    let grade;
    // Write your code here
    if (score > 25) {
        grade = 'A';
    } else if (score > 20) {
        grade = 'B';
    } else if (score > 15) {
        grade = 'C';
    } else if (score > 10) {
        grade = 'D';
    } else if (score > 5) {
        grade = 'E';
    } else {
        grade = 'F';
    }
    return grade;
}
