'use strict';

const diceCount = Number(prompt('Enter number of dice:'));
const desiredSum = Number(prompt('Enter desired sum of eyes:'));

const trials = 10000;
let successCount = 0;

for (let t = 0; t < trials; t++) {
  let sum = 0;

  for (let d = 0; d < diceCount; d++) {
    const die = Math.floor(Math.random() * 6) + 1; // 1–6
    sum += die;
  }

  if (sum === desiredSum) {
    successCount++;
  }
}

const probability = (successCount / trials) * 100;

document.body.innerHTML += `<p>Probability to get sum ${desiredSum} with ${diceCount} dice is ${probability.toFixed(2)}%.</p>`;
 .