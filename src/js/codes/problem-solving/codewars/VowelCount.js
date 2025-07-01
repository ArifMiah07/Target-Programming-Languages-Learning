// Return the number (count) of vowels in the given string.

// We will consider a, e, i, o, u as vowels for this Kata (but not y).

// The input string will only consist of lower case letters and/or spaces.

function getCount(str) {
  let number = 0;

  const vowel = ["a", "e", "i", "o", "u"];
  str.split("").forEach((char) => {
    if (vowel.includes(char)) {
      //
      number += 1;
    }
  });
  return number;
}

const sen = "hello, world";
console.log(getCount("hello, world"));
