/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    sqrtNumber = x ** 0.5;
     return Number(sqrtNumber.toString().split(".").shift());
};

console.log(mySqrt(81));