'use strict';

const form = document.getElementById('tv-form');
const queryInput = document.getElementById('query');
const resultsDiv = document.getElementById('results');

// default-kuva jos sarjalla ei ole kuvaa
const DEFAULT_IMG = 'https://placehold.co/210x295?text=Not%20Found';

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

    // tulosta myös konsoliin kuten tehtävä sanoo
    console.log('Search results:', data);

    // tyhjennetään vanhat tulokset
    resultsDiv.innerHTML = '';

    // käydään läpi kaikki hakutulokset
    data.forEach(item => {
      const show = item.show;

      const article = document.createElement('article');

      // nimi <h2>
      const h2 = document.createElement('h2');
      h2.textContent = show.name;
      article.appendChild(h2);

      // linkki <a>, target="_blank"
      if (show.url) {
        const link = document.createElement('a');
        link.href = show.url;
        link.target = '_blank';
        link.textContent = 'Details';
        article.appendChild(link);
      }

      // kuva <img> – käytetään ternaryä default-kuvaan
      const img = document.createElement('img');
      const imgUrl = show.image && show.image.medium
        ? show.image.medium
        : DEFAULT_IMG;
      img.src = imgUrl;
      img.alt = show.name || 'TV show image';
      article.appendChild(img);

      // summary <div> (ei <p>, koska summary sisältää jo <p>-tageja)
      const summaryDiv = document.createElement('div');
      summaryDiv.innerHTML = show.summary || 'No summary available.';
      article.appendChild(summaryDiv);

      resultsDiv.appendChild(article);
    });

    if (data.length === 0) {
      resultsDiv.innerHTML = '<p>Ei tuloksia.</p>';
    }

  } catch (err) {
    console.error('Error fetching TV data:', err);
    resultsDiv.innerHTML = '<p>Virhe haussa.</p>';
  }
});
