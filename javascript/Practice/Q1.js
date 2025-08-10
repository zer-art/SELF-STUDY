// print the sum all even numbers from 1 to 100

let sum = 0 ; 
for(let i = 1 ; i <= 100 ; i++) {
    if(i%2===0){ 
        sum += i ;
    }
}
console.log("Sum of all even numbers from 1 to 100 is: " + sum) ;

// Using while loop to achieve the same

let i= 1;
while (i<=100){
    if(i%2===0){ 
        sum += i ;
    }
    i++ ;
}

console.log("Sum of all even numbers from 1 to 100 using while loop is: " + sum) ;