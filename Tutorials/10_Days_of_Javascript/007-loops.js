// Name: Day 2: Loops
// Problem: https://www.hackerrank.com/challenges/js10-loops/problem
// Score: 10


function vowelsAndConsonants(s) {
    let vowels = ['a', 'e', 'i', 'o', 'u'];
    for (let v of s) {
        if (vowels.includes(v)) {
            console.log(v);
        }
    }
    for (let c of s) {
        if (!vowels.includes(c)) {
            console.log(c);
        }
    }
}
