#!/usr/bin/node
const size = Number(process.argv[2]);
if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  const row = 'X'.repeat(size);
  let y = 0;
  while (y < size) {
    console.log(row);
    y++;
  }
}
