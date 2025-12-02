'use strict';

function even(arr) {
  const evens = [];
  for (const n of arr) {
    if (n % 2 === 0) {
      evens.push(n);
    }
  }
  return evens;
}

const original = [2, 7, 4, 9, 10, 13, 8];
const evensOnly = even(original);

console.log('Original array:', original);
console.log('Even numbers array:', evensOnly);
