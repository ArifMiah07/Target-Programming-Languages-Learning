//Using test()
// The test() method is a RegExp expression method.
// It searches a string for a pattern, and returns true or false, depending on the result.
// The following example searches a string for the character "e":
// https://www.w3schools.com/jsref/jsref_obj_regexp.asp
// https://www.w3schools.com/js/js_regexp.asp
const pattern = /e/;
console.log(pattern.test("The best things in life are free!"));
console.log(/e/.test("The best things in life are free!"));
console.log(/e/.exec("The best things in life are free!"));

