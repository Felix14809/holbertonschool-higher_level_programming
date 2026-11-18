#!/usr/bin/node
const times = process.argv[2];
if (Number.isNaN(Number(times))) {
  console.log('Missing number of occurences');
} else {
  let i = 0;
  while (i < times) {
    console.log('C is fun');
    i++;
  }
}
