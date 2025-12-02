'use strict';

const startYear = Number(prompt('Enter start year:'));
const endYear = Number(prompt('Enter end year:'));

let listHtml = '<ul>';

for (let y = startYear; y <= endYear; y++) {
  let isLeapYear = false;

  if (y % 4 === 0) {
    if (y % 100 === 0) {
      if (y % 400 === 0) {
        isLeapYear = true;
      } else {
        isLeapYear = false;
      }
    } else {
      isLeapYear = true;
    }
  }

  if (isLeapYear) {
    listHtml += `<li>${y}</li>`;
  }
}

listHtml += '</ul>';
document.body.innerHTML += listHtml;
