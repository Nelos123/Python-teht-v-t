'use strict';

function concat(arr) {
  let result = '';
  for (const item of arr) {
    result += item;
  }
  return result;
}

const names = ['Johnny', 'DeeDee', 'Joey', 'Marky'];
const concatenated = concat(names);

document.body.innerHTML += `<p>${concatenated}</p>`;
