'use strict';

const form = document.getElementById('joke-form');
const termInput = document.getElementById('term');
const resultsSection = document.getElementById('results');

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const term = termInput.value.trim();
  if (!term) return;

  const url = `https://api.chucknorris.io/jokes/search?query=${encodeURIComponent(term)}`;

  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error('Network error');
    }
    const data = await response.json();

    // tyhjennä vanhat
    resultsSection.innerHTML = '';

    if (data.result.length === 0) {
      resultsSection.innerHTML = '<p>Ei vitsejä tällä haulla.</p>';
      return;
    }

    // jokainen vitsi article/p
    data.result.forEach(jokeObj => {
      const article = document.createElement('article');
      const p = document.createElement('p');
      p.textContent = jokeObj.value;
      article.appendChild(p);
      resultsSection.appendChild(article);
    });

  } catch (err) {
    console.error('Error fetching jokes:', err);
    resultsSection.innerHTML = '<p>Virhe haussa.</p>';
  }
});
