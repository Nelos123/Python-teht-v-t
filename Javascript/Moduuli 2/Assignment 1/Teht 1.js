'use strict';

const numbers = [];

for (let i = 0; i < 5; i++) {
  const n = Number(prompt(`Enter number ${i + 1}:`));
  numbers.push(n);
}

for (let i = numbers.length - 1; i >= 0; i--) {
  console.log(numbers[i]);
}
