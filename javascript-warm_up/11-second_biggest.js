#!/usr/bin/node
const list = process.argv.slice(2);
if (isNaN(list[1])) {
  console.log(0);
} else {
  let biggest = Number(list[0]);
  let second = -Infinity;
  for (const number of list) {
    const temp = Number(number);
    if (temp > biggest) {
      second = biggest;
      biggest = temp;
    }
    if (temp > second && temp < biggest) {
      second = temp;
    }
  }
  console.log(second);
}
