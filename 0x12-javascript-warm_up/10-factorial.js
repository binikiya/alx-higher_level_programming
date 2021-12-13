#!/usr/bin/node
const arg = process.argv[2];
function factorial (arg) {
  if (isNaN(arg)) {
    return (1);
  } else {
    if (arg > 1) {
      return (arg * factorial(arg - 1));
    } else {
      return (1);
    }
  }
}

console.log(factorial(arg));
