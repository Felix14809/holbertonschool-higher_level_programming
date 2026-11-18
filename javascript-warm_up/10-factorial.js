#!/usr/bin/node
function factorial (total, number) {
  if (number < 2) {
    return total;
  } else {
    number--;
    total *= number;
    return factorial(total, number);
  }
}
const number = Number(process.argv[2]);
if (Number.isNaN(number) || number < 1) {
  console.log(1);
} else {
  console.log(factorial(number, number));
}
