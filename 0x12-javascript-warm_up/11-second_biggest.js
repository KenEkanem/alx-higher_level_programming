#!/usr/bin/node
const myVar = process.argv.length;
if (myVar <= 3) {
  console.log(0);
} else {
  const args = process.argv.slice(2).map(x => parseInt(x));
  const sorted = args.sort((a, b) => a < b);
  console.log(sorted[1]);
}
