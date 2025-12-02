'use strict';

function rollDie() {
  return Math.floor(Math.random() * 6) + 1;
}

let result;
let listHtml = '<ul>';

do {
  result = rollDie();
  listHtml += `<li>${result}</li>`;
} while (result !== 6);

listHtml += '</ul>';

document.body.innerHTML += listHtml;
