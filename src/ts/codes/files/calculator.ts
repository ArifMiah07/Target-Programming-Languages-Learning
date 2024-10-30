import * as readline from 'readline';

// Create an interface for reading input from the terminal
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Function to calculate the average
const calculateAverage = (num1: number, num2: number, num3: number): number => {
    const sum = num1 + num2 + num3;
    return sum / 3;
};

// Prompt the user for input
rl.question("Enter three numbers (separated by space): ", (input) => {
    // Split the input string into an array of numbers
    const numbers = input.split(' ').map(Number);
    
    // Check if the user provided exactly three numbers
    if (numbers.length !== 3 || numbers.some(isNaN)) {
        console.log("Please enter exactly three valid numbers.");
    } else {
        const [num1, num2, num3] = numbers;
        const avg = calculateAverage(num1, num2, num3);
        console.log(`Average: ${avg}`);
    }

    // Close the readline interface
    rl.close();
});

//power by chatgpt o| copy from chatgpt 