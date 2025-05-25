// const readline = require('readline');

// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// });

// rl.question('Enter three numbers separated by spaces: ', (input) => {
//     const numbers = input.split(' ').map(Number);
//     // Check for invalid inputs

//     if(numbers.length !== 3 || numbers.some(isNaN)){
//         console.log("Error: Please enter exactly three valid numbers separated by spaces.");
//     } else{
//         const [num1, num2, num3] = numbers;

//         const sum = num1 + num2 + num3;
//         const avg = sum / 3;

//         console.log(`Sum: ${sum}\n`);
//         console.log(`Avg: ${avg}\n`);
//     }

//     rl.close();
// });

// advance

// const readline = require('readline');

// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// });

// rl.question('Enter three numbers separated by spaces: ', (input) => {
//     // Trim the input to handle extra leading/trailing spaces, then split and filter out empty strings
//     const numbers = input.trim().split(/\s+/).filter(val => val !== '').map(Number);

//     // Check for invalid input cases
//     if (input.trim() === '') {
//         console.log("Error: Input cannot be empty. Please enter exactly three numbers separated by spaces.");
//     } else if (numbers.length !== 3) {
//         console.log("Error: Please enter exactly three numbers.");
//     } else if (numbers.some(isNaN)) {
//         console.log("Error: All inputs must be valid numbers.");
//     } else if (numbers.some(num => !Number.isInteger(num))) {
//         console.log("Error: Only integer numbers are allowed.");
//     } else {
//         const [num1, num2, num3] = numbers;

//         const sum = num1 + num2 + num3;
//         const avg = sum / 3;

//         console.log(`Sum: ${sum}`);
//         console.log(`Average: ${avg}`);
//     }

//     rl.close();
// });

// const name_ = 'ariful'

// const mainFunction = (name_) => {
//     console.log('my name is', name_);

// }

// mainFunction('arif');

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
function twoSum(nums, target) {
  console.log(nums, target);

    for(let row = 0; row < nums.length; row++){
        for(let column=0; column < nums.length; column++){
            // for(let time = 0; time < nums.length; time++){
            //     console.log([nums[row], nums[column], nums[time]]);
            // }
            if(nums[row]+nums[column] == target){
                console.log(nums.indexOf(nums[column]), nums.indexOf(nums[row]))
            }

            console.log(nums[row]+nums[column] == target);
        }
    }







//    const myArray = ["key1", "key2", "key3"];
//    const myObject = {};

//    for (const key of nums) {
//        myObject[key] = nums.indexOf(nums[key]); // Assign a value to each key
//    }
//    console.log(myObject);




  // for(let i= 0; i < nums.length; i++){
  //     console.log(nums[i]);

  //     // if(target === nums[i] + nums[i+1]){
  //     //     // console.log('yes', nums.indexOf(nums[i]), nums.indexOf(nums[i+1]));

  //     // }
  //     // else{
  //     //     console.log('no');
  //     // }
  // }

}

twoSum([2, 7, 11, 15], 17);
