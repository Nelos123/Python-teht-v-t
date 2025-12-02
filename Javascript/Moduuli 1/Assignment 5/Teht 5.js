'use strict';

const year = Number(prompt('Enter a year:'));
let isLeap = false;

if (year % 4 === 0) {
  if (year % 100 === 0) {
    if (year % 400 === 0) {
      isLeap = true;
    } else {
      isLeap = false;
    }
  } else {
    isLeap = true;
  }
}

if (isLeap) {
  document.body.innerHTML += `<p>${year} is a leap year.</p>`;
} else {
  document.body.innerHTML += `<p>${year} is not a leap year.</p>`;
}
