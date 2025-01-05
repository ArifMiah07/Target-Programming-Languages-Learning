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

const say = "Hello, Word! Im leaning a new programming language name Red"
console.log(`say length is : ${say.length}`,'random length here:',Math.ceil(Math.random() * say.length)); 

console.log(`The character at index ${Math.floor(Math.random() * say.length)} is ${say.charAt(Math.floor(Math.random() * say.length))}`);

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

