#!/usr/bin/node
const args = process.argv.slice(2).map(x => parseInt(x));

if (args.length < 2) {
  console.log(0);
} else {
  // Remove duplicates and sort descending
  const uniqueSorted = [...new Set(args)].sort((a, b) => b - a);
  console.log(uniqueSorted.length < 2 ? 0 : uniqueSorted[1]);
}
