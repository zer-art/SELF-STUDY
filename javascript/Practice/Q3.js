// Question 3: Write a program that calculates the total price of items in an array after applying a 10% discount to each item.

let prices = [250 ,345 , 600 , 900 , 50 ]
let afterDiscount = [];

for (const price of prices) {
    afterDiscount.push(price - (price * 0.1));
}
console.log("Prices after 10% discount: " + afterDiscount);
