'use strict';

const count = Number(prompt('How many participants?'));
const participants = [];

for (let i = 0; i < count; i++) {
  const name = prompt(`Name for participant ${i + 1}:`);
  participants.push(name);
}

participants.sort();

let html = '<ol>';
for (const name of participants) {
  html += `<li>${name}</li>`;
}
html += '</ol>';

document.body.innerHTML += html;
