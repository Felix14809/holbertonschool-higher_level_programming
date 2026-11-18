#!/usr/bin/node
const args = process.argv.slice(2);
if (isNaN(args[0])) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
