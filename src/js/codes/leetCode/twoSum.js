/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

// todo:optimize to O(n) as a revisit

function twoSum(nums, target) {
  console.log(nums, target);

  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        return ([i, j]);
      }
    }
  }
}

console.log(twoSum([3, 3], 6));



// const numbers = [2,3,4,5,5,6,3];
// function showN(){
//     for(let i = 0; i < numbers.length; i++){
//         console.log([numbers.indexOf(numbers[i])], i);
//     }
// }

// showN();
