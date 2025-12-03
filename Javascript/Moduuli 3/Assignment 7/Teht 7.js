'use strict';

function rollDieSides(sides) {
  return Math.floor(Math.random() * sides) + 1;
}

const sides = Number(prompt('Enter number of sides on the dice:'));

let r;
let html = '<ul>';

do {
  r = rollDieSides(sides);
  html += `<li>${r}</li>`;
} while (r !== sides);

html += '</ul>';

document.body.innerHTML += html;
