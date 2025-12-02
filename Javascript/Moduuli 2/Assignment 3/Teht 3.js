'use strict';

const dogs = [];

for (let i = 0; i < 6; i++) {
  const dogName = prompt(`Enter name for dog ${i + 1}:`);
  dogs.push(dogName);
}

dogs.sort();
dogs.reverse();

let html = '<ul>';
for (const dog of dogs) {
  html += `<li>${dog}</li>`;
}
html += '</ul>';

document.body.innerHTML += html;
