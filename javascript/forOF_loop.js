// Used to iterate over iterable objects like arrays, strings, etc.

const array = [1, 2, 3, 4, 5];
let sum = 0;
for (const value of array) {
    sum += value;
}
console.log("Sum of array elements is: " + sum);