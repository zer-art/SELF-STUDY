// create a game where you start with a random number . ask user to keep guessing the number

let randomNumber = Math.floor(Math.random() * 100) + 1; 
let input = prompt("Guess the number between 1 and 100:");

while(input != randomNumber) {
    if (input < randomNumber) {
        console.log("Too low! Try again.");
    } else if (input > randomNumber) {
        console.log("Too high! Try again.");
    }
    input = prompt("Guess the number between 1 and 100:");
}

console.log("Congratulations! You've guessed the number: " + randomNumber);
