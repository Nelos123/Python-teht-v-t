'use strict';

const button = document.getElementById('random-btn');

button.addEventListener('click', async () => {
  try {
    const response = await fetch('https://api.chucknorris.io/jokes/random');
    if (!response.ok) {
      throw new Error('Network error');
    }
    const data = await response.json();

    // tulostetaan vain 'value' kenttä
    console.log('Random Chuck Norris joke:', data.value);
  } catch (err) {
    console.error('Error fetching joke:', err);
  }
});
