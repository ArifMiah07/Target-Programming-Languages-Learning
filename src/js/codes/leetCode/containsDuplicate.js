/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  // console.log(nums);

  const counts = {};

  // Count
  for (let num of nums) {
    counts[num] = (counts[num] || 0) + 1;
    // if (counts[num] === undefined) {
    //   counts[num] = 1;
    // } else {
    //   counts[num] += 1;
    // }
    console.log(counts[num], counts);
    // console.log(num)
  }
  //check twins
  for (let num of nums) {
    if (counts[num] > 1) {
      return true;
    }
  }
  return false;
};

console.log(containsDuplicate([1, 2, 3, 3, 1]));
