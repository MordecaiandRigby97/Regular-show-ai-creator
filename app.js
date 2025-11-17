const actors = [
  {
    name: 'J.G. Quintel',
    roles: ['Mordecai', 'High Five Ghost'],
    funFact: 'Storyboards adventures after midnight with gallons of coffee.',
    movies: ['Regular Show: The Movie', 'Close Enough shorts'],
  },
  {
    name: 'William Salyers',
    roles: ['Rigby'],
    funFact: 'Runs improv sessions that inspire new fan scripts every month.',
    movies: ['Regular Show: The Movie'],
  },
  {
    name: 'Mark Hamill',
    roles: ['Skips'],
    funFact: 'Balances Jedi wisdom with immortal yeti sarcasm.',
    movies: ['Star Wars Saga (voice & live action cameo love)', 'Batman: The Animated Series'],
  },
  {
    name: 'Sam Marin',
    roles: ['Benson', 'Pops', 'Muscle Man'],
    funFact: 'Records three characters in a single take for chaotic charm.',
    movies: ['Regular Show: The Movie'],
  },
  {
    name: 'Courtenay Taylor',
    roles: ['Starla'],
    funFact: 'Hosts a podcast for fanfic authors between VO gigs.',
    movies: ['Mass Effect Trilogy', 'OK K.O.! Let\'s Be Heroes'],
  },
  {
    name: 'Minty Lewis',
    roles: ['Eileen'],
    funFact: 'Keeps a sketchbook filled with park critters and donut ideas.',
    movies: ['Regular Show: The Movie'],
  },
];

const stories = [
  {
    title: 'Storyboard to Silver Screen',
    description:
      'A mini documentary charting how the cast prepped for Regular Show: The Movie, blending VO booth footage with hand-drawn story diaries.',
  },
  {
    title: 'Beyond the Park Gates',
    description:
      'Podcast-style stories where the actors reprise roles while exploring sci-fi conventions, music festivals, and heroic road trips.',
  },
  {
    title: 'Sydney\'s Scrapbook',
    description:
      'Our curator Sydney narrates a visual novel that binds every interview into an interactive archive.',
  },
];

const fanEpisodes = [
  {
    title: 'Quantum Slushie Heist',
    focus: 'Mordecai, Rigby, and Sydney patch the time stream after a broken slushie machine starts spitting alternate timelines.',
  },
  {
    title: 'Skips\' Story Stones',
    focus: 'Skips mentors Sydney through cosmic flashbacks featuring cameos from every main actor.',
  },
  {
    title: 'Benson\'s Battle of the Bands',
    focus: 'Sydney plays synth for Eileen and Starla in a fan-animated music showdown judged by Pops.',
  },
];

const actorGrid = document.getElementById('actor-grid');
const storiesContainer = document.getElementById('stories');
const episodesList = document.getElementById('episodes');

actors.forEach((actor) => {
  const card = document.createElement('article');
  card.className = 'card';
  card.innerHTML = `
    <h3>${actor.name}</h3>
    <p><strong>Roles:</strong> ${actor.roles.join(', ')}</p>
    <p>${actor.funFact}</p>
    <p><strong>Movies & Stories:</strong> ${actor.movies.join(', ')}</p>
  `;
  card.addEventListener('click', () => {
    card.classList.toggle('active');
    card.style.borderColor = card.classList.contains('active')
      ? 'rgba(245, 166, 35, 1)'
      : 'rgba(255, 255, 255, 0.05)';
  });
  actorGrid.appendChild(card);
});

stories.forEach((story) => {
  const storyCard = document.createElement('article');
  storyCard.className = 'story';
  storyCard.innerHTML = `
    <h3>${story.title}</h3>
    <p>${story.description}</p>
  `;
  storiesContainer.appendChild(storyCard);
});

fanEpisodes.forEach((episode) => {
  const item = document.createElement('li');
  item.innerHTML = `
    <h3>${episode.title}</h3>
    <p>${episode.focus}</p>
  `;
  episodesList.appendChild(item);
});
