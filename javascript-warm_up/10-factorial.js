#!/usr/bin/node
function factorial (n) {
  return n < 2 ? 1 : n * factorial(n - 1);
}
const number = Number(process.argv[2]);
if (Number.isNaN(number) || number < 1) {
  console.log(1);
} else {
  console.log(factorial(number, number));
}
