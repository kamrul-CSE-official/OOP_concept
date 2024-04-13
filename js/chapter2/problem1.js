// -------------
// => this key word
// -------------

console.log(this);
// console.log(this === window);

function unNamed() {
  this.name = "Zonayed Ahmed";
  this.address = "Dhaka, Bangladesh";
}
unNamed();
console.log(name, address);

// const name = "Kamrul";
// console.log(name);

// -------------
// 1. Call method
// -------------

var myCustomObj = {
  name: "MD.Kamrul Hasan",
  age: 21,
  job: "Student",
  anotherObj: {
    name: "MD.Maksudul Rahman",
    value: function () {
      console.log("My name is " + this.name);
    },
  },
};

myCustomObj.anotherObj.value();
myCustomObj.anotherObj.value.call(myCustomObj);

var karim = {
  name: "MD.Kamrul Hasan",
  dob: 1996,
  age: function (currentYear) {
    console.log(this.name + " is " + (currentYear - this.dob) + " years old!");
  },
};

karim.age(2024);

var karim = {
  name: "MD.Kamrul Hasan",
  dob: 1996,
  age: function (currentYear) {
    console.log(this.name + " is " + (currentYear - karim.dob) + " years old!");
  },
};

karim.age(2024);

// -------------
// 2. apply method
// -------------

var myCustomObj = {
  name: "Zonayed Ahmed",
  age: 21,
  job: "Student",
  anotherObj: {
    name: "Ahmed Zonayed",
    value: function () {
      console.log("My name is " + this.name);
    },
  },
};
myCustomObj.anotherObj.value.apply(myCustomObj);
myCustomObj.anotherObj.value();


