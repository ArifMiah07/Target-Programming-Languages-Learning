// /**
//  * @param {number} x
//  * @return {boolean}
//  */
// var isPalindrome = function (x) {
//   let px = x.toString();
//   let arr1 = [];
//   let arr2 = [];

//   let isPalindrome = [];

//   for (let p of px) {
//     arr1.push(p);
//   }

//   for (let z of px) {
//     arr2.push(z);
//   }

//   const reArr = arr2.reverse();

//   for(let i = 0; i < arr1.length; i++){
//     //   console.log([arr1[i] === reArr[i]])
//       isPalindrome.push(arr1[i] === reArr[i]);
//   }
// if (isPalindrome.includes(false)){
//     // console.log('this is not a palindrome number')
//     return false;
// }
// else{
//     // console.log('yes this is a palindrome number')
//     return true;
// }
// //   console.log(arr1);
// //   console.log(reArr);
// //   console.log(isPalindrome);

// //   return px;
// };

console.log(isPalindrome(-121));
/**
//  * @param {number} x
//  * @return {boolean}
//  */
var isPalindrome = function (x) {
  let original = x.toString();
  let reversed = original.split("").reverse().join("");
  return original === reversed;
};

console.log(isPalindrome(4121));
