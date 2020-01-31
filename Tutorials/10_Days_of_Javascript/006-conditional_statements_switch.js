// Name: Day 2: Conditional Statements: Switch
// Problem: https://www.hackerrank.com/challenges/js10-switch/problem
// Score: 10


function getLetter(s) {
    let letter;
    // Write your code here
    switch (true) {
        case 'aeiou'.includes(s.charAt(0)):
            letter = 'A';
            break;
        case 'bcdfg'.includes(s.charAt(0)):
            letter = 'B';
            break;
        case 'hjklm'.includes(s.charAt(0)):
            letter = 'C';
            break;
        case 'npqrstvwxyz'.includes(s.charAt(0)):
            letter = 'D';
            break;
    }
    return letter;
}
