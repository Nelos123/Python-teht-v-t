'use strict';

const doCalc = confirm('Should I calculate the square root?');

if (doCalc) {
  const num = Number(prompt('Enter a number:'));
  if (num < 0) {
    document.body.innerHTML += '<p>The square root of a negative number is not defined.</p>';
  } else {
    const root = Math.sqrt(num);
    document.body.innerHTML += `<p>The square root of ${num} is ${root}.</p>`;
  }
} else {
  document.body.innerHTML += '<p>The square root is not calculated.</p>';}