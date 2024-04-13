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
