'use strict';

const nums = [];

while (true) {
  const value = Number(prompt('Enter a number (0 to stop):'));
  if (value === 0) {
    break;
  }
  nums.push(value);
}

nums.sort((a, b) => b - a);

console.log('Numbers from largest to smallest:');
for (const n of nums) {
  console.log(n);
}
