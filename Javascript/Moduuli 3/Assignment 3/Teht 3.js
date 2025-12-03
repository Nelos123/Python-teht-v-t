'use strict';

const names = ['John', 'Paul', 'Jones'];
let html = '';

for (const name of names) {
  html += `<li>${name}</li>`;
}

document.getElementById('target').innerHTML = html;
