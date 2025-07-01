/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    const lastWord = s.trim().split(" ");
    const lastWordsLength = lastWord[lastWord.length-1].length;
    return lastWordsLength;
};


console.log(lengthOfLastWord('Hello World'));


// var lengthOfLastWord = s => s.trim().split(" ").pop().length;