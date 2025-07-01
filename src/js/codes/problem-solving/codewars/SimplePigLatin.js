// Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

// Examples
// pigIt('Pig latin is cool'); // igPay atinlay siay oolcay
// pigIt('Hello world !');     // elloHay orldway !

/**
 *
 * @param {get} str
 *
 * 1st get each word
 */

function pigIt(str) {
  const punctuationMarks = [
    ".",
    ",",
    "!",
    "?",
    ";",
    ":",
    "-",
    "–",
    "—",
    "'",
    '"',
    "(",
    ")",
    "[",
    "]",
    "{",
    "}",
    "<",
    ">",
    "/",
    "\\",
    "|",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "_",
    "~",
    "`",
    "=",
    "+",
  ];

return str.split(" ").map((word)=> {
    if(punctuationMarks.includes(word)){
        return word;
    }else{
        return word.slice(1)+word[0]+'ay'
    }
}).join(" ")
}

const word1 = "Pig latin is cool";
const word2 = "Hello world !";
console.log(pigIt(word2));