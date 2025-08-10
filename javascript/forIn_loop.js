// used for iterating over object properties

let student = {
    name: "Pawan",
    age: 25,
    course: "AI"
};

for (let key in student) {
    console.log(key + ": " + student[key]);
}