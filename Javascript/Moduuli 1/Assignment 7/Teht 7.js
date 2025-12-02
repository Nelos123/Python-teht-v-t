'use strict';

const rolls = Number(prompt('How many dice rolls?'));
let total = 0;

for (let i = 0; i < rolls; i++) {
  const die = Math.floor(Math.random() * 6) + 1; // 1–6
  total += die;
}

document.body.innerHTML += `<p>Sum of ${rolls} dice rolls is ${total}.</p>`;
