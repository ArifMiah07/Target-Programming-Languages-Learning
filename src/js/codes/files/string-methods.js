/**
 * ### **String Methods**
1. `charAt()`
2. `charCodeAt()`
3. `concat()`
4. `endsWith()`
5. `includes()`
6. `indexOf()`
7. `lastIndexOf()`
8. `localeCompare()`
9. `match()`
10. `matchAll()`
11. `normalize()`
12. `padEnd()`
13. `padStart()`
14. `repeat()`
15. `replace()`
16. `replaceAll()`
17. `search()`
18. `slice()`
19. `split()`
20. `startsWith()`
21. `substring()`
22. `toLocaleLowerCase()`
23. `toLocaleUpperCase()`
24. `toLowerCase()`
25. `toString()`
26. `toUpperCase()`
27. `trim()`
28. `trimEnd()`
29. `trimStart()`
30. `valueOf()`
 */

//method
//charAt()

//String.prototype.charAt()
// Baseline Widely available
// The charAt() method of String values returns a new string consisting of the single UTF-16 code unit 
// at the given index.

// charAt() always indexes the string as a sequence of UTF-16 code units, so it may return lone 
// surrogates. To get the full Unicode code point at the given index, use String.prototype.codePointAt() 
// and String.fromCodePoint().

// Try it

// Syntax
// js
// Copy to Clipboard
// charAt(index)
// Parameters
// index
// Zero-based index of the character to be returned. Converted to an integer — undefined is converted to 0.

// Return value
// A string representing the character (exactly one UTF-16 code unit) at the specified index. If index is 
// out of the range of 0 – str.length - 1, charAt() returns an empty string.

// Description
// Characters in a string are indexed from left to right. The index of the first character is 0, and 
// the index of the last character in a string called str is str.length - 1.

// Unicode code points range from 0 to 1114111 (0x10FFFF). charAt() always returns a character whose 
// value is less than 65536, because the higher code points are represented by a pair of 16-bit 
// surrogate pseudo-characters. Therefore, in order to get a full character with value greater than 65535,
// it is necessary to retrieve not only charAt(i), but also charAt(i + 1) (as if manipulating a string 
// with two characters), or to use codePointAt(i) and String.fromCodePoint() instead. For information on
// Unicode, see UTF-16 characters, Unicode code points, and grapheme clusters.

// charAt() is very similar to using bracket notation to access a character at the specified index. 
// The main differences are:

// charAt() attempts to convert index to an integer, while bracket notation does not, and directly 
// uses index as a property name.
// charAt() returns an empty string if index is out of range, while bracket notation returns undefined.
// Examples
// Using charAt()
// The following example displays characters at different locations in the string "Brave new world":

// js
// Copy to Clipboard
// const anyString = "Brave new world";
// console.log(`The character at index 0   is '${anyString.charAt()}'`);
// // No index was provided, used 0 as default

// console.log(`The character at index 0   is '${anyString.charAt(0)}'`);
// console.log(`The character at index 1   is '${anyString.charAt(1)}'`);
// console.log(`The character at index 2   is '${anyString.charAt(2)}'`);
// console.log(`The character at index 3   is '${anyString.charAt(3)}'`);
// console.log(`The character at index 4   is '${anyString.charAt(4)}'`);
// console.log(`The character at index 999 is '${anyString.charAt(999)}'`);
// These lines display the following:

// The character at index 0   is 'B'

// The character at index 0   is 'B'
// The character at index 1   is 'r'
// The character at index 2   is 'a'
// The character at index 3   is 'v'
// The character at index 4   is 'e'
// The character at index 999 is ''
// charAt() may return lone surrogates, which are not valid Unicode characters.

// js
// Copy to Clipboard
// const str = "𠮷𠮾";
// console.log(str.charAt(0)); // "\ud842", which is not a valid Unicode character
// console.log(str.charAt(1)); // "\udfb7", which is not a valid Unicode character
// To get the full Unicode code point at the given index, use an indexing method that splits by Unicode 
// code points, such as String.prototype.codePointAt() and spreading strings into an array of Unicode 
// code points.

// js
// Copy to Clipboard
// const str = "𠮷𠮾";
// console.log(String.fromCodePoint(str.codePointAt(0))); // "𠮷"
// console.log([...str][0]); // "𠮷"
// Note: Avoid re-implementing the solutions above using charAt(). The detection of lone surrogates 
// and their pairing is complex, and built-in APIs may be more performant as they directly use the
// internal representation of the string. Install a polyfill for the APIs mentioned above if necessary.

// const say = "Hello, Word! Im leaning a new programming language name Red"
// console.log(`say length is : ${say.length}`,'random length here:',Math.ceil(Math.random() * say.length)); 

// console.log(`The character at index ${Math.floor(Math.random() * say.length)} is ${say.charAt(Math.floor(Math.random() * say.length))}`);

const text = "Hello, Word! Im learning a new programming language name Red. I am a beginner.";

function strContent(str = "hi there"){
    console.log(`str length is :`, str.length);
    for(let i = 0; i < str.length; i++){
        console.log(`fr: ${i} is ${str.charAt(i)}`);
        console.log(`charAt: ${str.charCodeAt(i)} is ${str.charAt(i)}`);

        // console.log(str[i] + 1);
    }
    return str;
}

console.log(strContent(text));

//charCodeAt()
//"ABC".charCodeAt(0); // returns 65

const word = "ABCD";
const ranIn = Math.floor(Math.random() * word.length);
console.log(`charAt ranIn:  ${word.charCodeAt(ranIn)} is ${word.charAt(ranIn)}`);

//concat()
const letters = ["a", "b", "c"];
const numbers = [1, 2, 3];

const alphaNumeric = letters.concat(numbers);
console.log(alphaNumeric);
// results in ['a', 'b', 'c', 1, 2, 3]


//endsWith()
const str = "To be, or not to be, that is the question.";

console.log(str.endsWith("question.")); // true
console.log(str.endsWith("to be")); // false
console.log(str.endsWith("to be", 19)); // true


//includes()
const arr = ["a", "b", "c"];

arr.includes("c", 3); // false
arr.includes("c", 100); // false


