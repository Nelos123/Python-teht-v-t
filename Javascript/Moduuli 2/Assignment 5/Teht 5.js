'use strict';

const inputs = [];

while (true) {
  const value = Number(prompt('Enter a number:'));

  if (inputs.includes(value)) {
    alert('The number has already been given!');
    break;
  }

  inputs.push(value);
}

inputs.sort((a, b) => a - b);

console.log('All given numbers in ascending order:');
for (const n of inputs) {
  console.log(n);
}
