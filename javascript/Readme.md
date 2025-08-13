### DOM Manipulation Example

The `DOM` folder contains a simple example of manipulating the DOM using JavaScript:

- **index.html**: Basic HTML file with a heading and a paragraph. Links to `style.css` and `script.js`.
- **script.js**: Changes the content of the heading using JavaScript (`getElementById` and `innerHTML`).
- **style.css**: (Add your styles here if needed.)

#### How to Run HTML/JS Files

To view the DOM example or any HTML file:
1. Make sure you are on a system with a graphical desktop environment.
2. Open the HTML file in your browser by double-clicking it or using your browser's "Open File" option.
3. If you use the terminal, you can run:
	```bash
	xdg-open index.html
	```
	or manually open the file in your browser.

If you encounter permission errors, check your system environment and user permissions.

## JavaScript Self-Study Workspace

This repository contains various JavaScript files and practice questions designed to help you learn and master different looping constructs and basic programming concepts in JavaScript.

### Folder Structure

```
.
├── doWhile_loop.js
├── for_loop.js
├── forIn_loop.js
├── forOF_loop.js
├── while_loop.js
├── Readme.md
└── practice-Questions/
	├── index.html
	├── Ques1.js
	├── Ques2.js
	└── Ques3.js
```

### File Descriptions

#### Loop Examples
- **for_loop.js**: Demonstrates the use of a `for` loop to calculate the sum of the first 10 natural numbers.
- **while_loop.js**: Uses a `while` loop for the same sum calculation.
- **doWhile_loop.js**: Shows a `do...while` loop, which runs at least once before checking the condition.
- **forIn_loop.js**: Iterates over the properties of an object using `for...in`.
- **forOF_loop.js**: Iterates over elements of an array using `for...of` and calculates their sum.

#### Practice Questions (`practice-Questions/`)
- **Ques1.js**: Prints the sum of all even numbers from 1 to 100 using both `for` and `while` loops.
- **Ques2.js**: Implements a number guessing game where the user tries to guess a randomly generated number between 1 and 100.
- **Ques3.js**: Calculates the total price of items in an array after applying a 10% discount to each item.
- **index.html**: Simple HTML file that loads `Ques2.js` for browser-based interaction.

---

Feel free to explore each file to understand how different loops and basic logic are implemented in JavaScript. This workspace is ideal for beginners looking to strengthen their fundamentals.

---

## Additional Notes

- For DOM manipulation, ensure you open HTML files in a browser, not in Node.js.
- If you face issues opening files from the terminal, try opening them directly from your file manager or browser.
