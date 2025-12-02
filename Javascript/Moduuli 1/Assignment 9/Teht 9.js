'use strict';

const n = Number(prompt('Enter an integer:'));
let isPrime = true;

if (n <= 1) {
  isPrime = false;
} else {
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
      isPrime = false;
      break;
    }
  }
}

if (isPrime) {
  document.body.innerHTML += `<p>${n} is a prime number.</p>`;
} else {
  document.body.innerHTML += `<p>${n} is not a prime number.</p>`;
}
