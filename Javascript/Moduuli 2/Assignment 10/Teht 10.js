'use strict';

const candidateCount = Number(prompt('Number of candidates:'));
const candidates = [];

for (let i = 0; i < candidateCount; i++) {
  const name = prompt(`Name for candidate ${i + 1}:`);
  candidates.push({ name: name, votes: 0 });
}

const voterCount = Number(prompt('Number of voters:'));

for (let i = 0; i < voterCount; i++) {
  const voteName = prompt(`Voter ${i + 1}, who do you vote for? (empty = empty vote)`);

  if (voteName === null || voteName === '') {
    continue; // tyhjä ääni
  }

  const candidate = candidates.find(c => c.name === voteName);
  if (candidate) {
    candidate.votes++;
  } else {
    console.log(`Invalid vote for "${voteName}"`);
  }
}

candidates.sort((a, b) => b.votes - a.votes);

const winner = candidates[0];

console.log(`The winner is ${winner.name} with ${winner.votes} votes.`);
console.log('results:');
for (const c of candidates) {
  console.log(`${c.name}: ${c.votes} votes`);
}
