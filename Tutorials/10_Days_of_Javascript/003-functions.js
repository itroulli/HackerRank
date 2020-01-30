// Name: Day 1: Functions
// Problem: https://www.hackerrank.com/challenges/js10-function/problem
// Score: 10


/*
 * Create the function factorial here
 */
function factorial(n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n-1);

}
