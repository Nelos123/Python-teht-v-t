'use strict';

const form = document.getElementById('tv-form');
const queryInput = document.getElementById('query');

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const query = queryInput.value.trim();
  if (!query) return;

  const url = `https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`;

  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error('Network error');
    }
    const data = await response.json();

    // Tulostetaan koko hakutulos konsoliin
    console.log('Search results:', data);
  } catch (err) {
    console.error('Error fetching TV data:', err);
  }
});
