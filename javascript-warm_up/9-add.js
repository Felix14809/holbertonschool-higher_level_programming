#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}
const numbers = process.argv.slice(2);
add(Number(numbers[0]), Number(numbers[1]));
