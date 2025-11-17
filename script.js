const voiceActors = [
  {
    name: 'J.G. Quintel',
    roles: 'Mordecai / Hi-Five Ghost',
    bio: 'Show creator who balances mellow slacker energy with heartfelt storytelling.',
    tags: ['Creator', 'Storyboarder', 'Mordecai Sessions'],
  },
  {
    name: 'William Salyers',
    roles: 'Rigby',
    bio: 'Fast-talking, chaotic improviser that fuels Rigby\'s high-energy tone.',
    tags: ['Comedy shorts', 'Fan shout-outs', 'Game streams'],
  },
  {
    name: 'Sam Marin',
    roles: 'Pops / Benson / Muscle Man',
    bio: 'Switches between wild characters, crooners, and strict park managers.',
    tags: ['Crooner covers', 'Behind-the-scenes', 'Park podcasts'],
  },
  {
    name: 'Mark Hamill',
    roles: 'Skips',
    bio: 'Legendary voice who brings serene wisdom and heroic grit to Skips.',
    tags: ['Jedi jam sessions', 'Documentaries', 'Fan Q&A'],
  },
  {
    name: 'Courtenay Taylor',
    roles: 'Starla',
    bio: 'Powerhouse vocalist with roots in gaming and animated sci-fi.',
    tags: ['Synth ballads', 'Action reels', 'Coach tips'],
  },
  {
    name: 'Minty Lewis',
    roles: 'Eileen',
    bio: 'Chill indie songwriter with cozy ukulele vibes and comic timing.',
    tags: ['Indie zines', 'Cozy livestreams', 'Mixtape clubs'],
  },
  {
    name: 'Janie Haddad Tompkins',
    roles: 'Margaret / CJ',
    bio: 'LA-based actor and podcaster who brings warmth and grounded humor to the park crew.',
    tags: ['Margaret mixtapes', 'Story podcasts', 'Indie collaborations'],
  },
  {
    name: 'Sydney Park',
    roles: 'Morgan / Teen ensemble',
    bio: 'Actor-musician who voiced Morgan and lends bright R&B hooks plus playful improv energy.',
    tags: ['Teen scene anthems', 'R&B hooks', 'Dance challenges'],
  },
];

const leadSelect = document.getElementById('leadSelect');
const backgroundSelects = Array.from(document.querySelectorAll('.background-select'));
const voiceActorGrid = document.getElementById('voiceActorGrid');
const voiceActorTemplate = document.getElementById('voiceActorTemplate');
const arrangementTemplate = document.getElementById('arrangementTemplate');
const arrangementsNode = document.getElementById('arrangements');
const searchInput = document.getElementById('searchInput');
const form = document.getElementById('arrangerForm');
const projectNotes = document.getElementById('projectNotes');
const projectType = document.getElementById('projectType');
const songTitleInput = document.getElementById('songTitle');
const youtubeLinkInput = document.getElementById('youtubeLink');
const shareBanner = document.getElementById('shareBanner');

const STORAGE_KEY = 'regular-show-arrangements';
let arrangements = [];
const encoder = new TextEncoder();
const decoder = new TextDecoder();

function populateSelect(select, { includePlaceholder = false } = {}) {
  const placeholder = includePlaceholder
    ? '<option value="">Select a backing vocalist</option>'
    : '';
  select.innerHTML =
    placeholder +
    voiceActors
      .map((actor, index) => `<option value="${index}">${actor.name}</option>`)
      .join('');
}

function populateAllVoiceSelects() {
  populateSelect(leadSelect);
  backgroundSelects.forEach((select) => populateSelect(select, { includePlaceholder: true }));
}

function updateBackgroundSelectStates() {
  const leadValue = leadSelect.value;
  backgroundSelects.forEach((select) => {
    Array.from(select.options).forEach((option) => {
      option.disabled = option.value === leadValue;
    });
    if (select.value === leadValue) {
      select.value = '';
    }
  });
}

function setDefaultBackgrounds(excludeIndex) {
  const available = voiceActors
    .map((_, idx) => idx)
    .filter((idx) => idx !== excludeIndex);
  backgroundSelects.forEach((select, idx) => {
    select.value = available[idx % available.length]?.toString() ?? '';
  });
  updateBackgroundSelectStates();
}

function renderVoiceActors(list) {
  voiceActorGrid.innerHTML = '';
  list.forEach((actor) => {
    const node = voiceActorTemplate.content.cloneNode(true);
    node.querySelector('h3').textContent = actor.name;
    node.querySelector('.role').textContent = actor.roles;
    node.querySelector('.bio').textContent = actor.bio;
    const tagList = node.querySelector('.tag-list');
    actor.tags.forEach((tag) => {
      const li = document.createElement('li');
      li.textContent = tag;
      tagList.appendChild(li);
    });
    const originalIndex = voiceActors.indexOf(actor);
    node.querySelector('.card').addEventListener('click', () => {
      leadSelect.value = originalIndex.toString();
      setDefaultBackgrounds(originalIndex);
      updateBackgroundSelectStates();
    });
    voiceActorGrid.appendChild(node);
  });
}

function getStoredArrangements() {
  try {
    const data = localStorage.getItem(STORAGE_KEY);
    if (!data) return [];
    return JSON.parse(data);
  } catch (error) {
    console.warn('Unable to parse saved arrangements', error);
    return [];
  }
}

function persistArrangements() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(arrangements));
}

function renderArrangements() {
  arrangementsNode.innerHTML = '';
  if (!arrangements.length) {
    const empty = document.createElement('p');
    empty.textContent = 'No saved songs yet. Build one above!';
    empty.className = 'empty-state';
    arrangementsNode.appendChild(empty);
    return;
  }

  arrangements.forEach((entry) => {
    const node = arrangementTemplate.content.cloneNode(true);
    node.querySelector('.arrangement-title').textContent = entry.songTitle;
    node.querySelector('.arrangement-lead').textContent = `Lead: ${entry.lead}`;
    node.querySelector('.arrangement-type').textContent = `${entry.projectType}`;
    node.querySelector(
      '.arrangement-bgv'
    ).textContent = `Background vocals: ${entry.background.join(', ')}`;
    node.querySelector('.arrangement-notes').textContent = entry.notes
      ? `Notes: ${entry.notes}`
      : 'No additional scene notes yet.';
    const link = node.querySelector('.arrangement-link');
    link.href = entry.youtubeLink;
    const iframe = node.querySelector('.arrangement-embed');
    iframe.src = entry.embedUrl;
    const shareButton = node.querySelector('.arrangement-share');
    shareButton.addEventListener('click', () => handleShareClick(entry, shareButton));
    node.querySelector('.arrangement-delete').addEventListener('click', () => {
      arrangements = arrangements.filter((item) => item.id !== entry.id);
      persistArrangements();
      renderArrangements();
    });
    arrangementsNode.appendChild(node);
  });
}

function encodeSharePayload(entry) {
  const payload = {
    lead: entry.lead,
    songTitle: entry.songTitle,
    background: entry.background,
    projectType: entry.projectType,
    notes: entry.notes,
    youtubeLink: entry.youtubeLink,
  };
  const json = JSON.stringify(payload);
  const binary = encoder.encode(json);
  let binaryString = '';
  binary.forEach((byte) => {
    binaryString += String.fromCharCode(byte);
  });
  const base64 = btoa(binaryString)
    .replace(/\+/g, '-')
    .replace(/\//g, '_')
    .replace(/=+$/, '');
  return base64;
}

function decodeSharePayload(value) {
  const base64 = value.replace(/-/g, '+').replace(/_/g, '/');
  const pad = base64.length % 4 === 0 ? '' : '='.repeat(4 - (base64.length % 4));
  const binaryString = atob(base64 + pad);
  const bytes = Uint8Array.from(binaryString, (char) => char.charCodeAt(0));
  const json = decoder.decode(bytes);
  return JSON.parse(json);
}

function createShareLink(entry) {
  const payload = encodeSharePayload(entry);
  const { origin, pathname } = window.location;
  return `${origin}${pathname}?project=${payload}`;
}

async function handleShareClick(entry, button) {
  const link = createShareLink(entry);
  try {
    await navigator.clipboard.writeText(link);
    button.textContent = 'Link copied!';
    setTimeout(() => {
      button.textContent = 'Copy share link';
    }, 2000);
  } catch (error) {
    window.prompt('Copy this link:', link); // fallback
  }
}

function handleSearch(event) {
  const term = event.target.value.toLowerCase();
  const filtered = voiceActors.filter((actor) => {
    const searchable = `${actor.name} ${actor.roles} ${actor.bio} ${actor.tags.join(' ')}`.toLowerCase();
    return searchable.includes(term);
  });
  renderVoiceActors(filtered);
}

function extractYouTubeId(url) {
  const matcher =
    /(?:youtube\.com\/(?:watch\?v=|embed\/|shorts\/)|youtu\.be\/)([A-Za-z0-9_-]{11})/;
  const match = url.match(matcher);
  return match ? match[1] : null;
}

function handleSubmit(event) {
  event.preventDefault();
  const leadActor = voiceActors[Number(leadSelect.value)];
  const songTitle = songTitleInput.value.trim();
  const background = backgroundSelects.map((select) => {
    const actor = voiceActors[Number(select.value)];
    return actor?.name ?? '';
  });
  const youtubeLink = youtubeLinkInput.value.trim();
  const notes = projectNotes.value.trim();
  const type = projectType.value;

  if (background.some((bg) => !bg)) {
    alert('Please fill all three background vocals.');
    return;
  }

  if (new Set(background).size !== background.length) {
    alert('Please choose three different background vocalists.');
    return;
  }

  const youtubeId = extractYouTubeId(youtubeLink);
  if (!youtubeId) {
    alert('Enter a full YouTube link (watch, share, or shorts URL).');
    return;
  }

  const embedUrl = `https://www.youtube.com/embed/${youtubeId}`;

  arrangements = [
    {
      id: crypto.randomUUID(),
      lead: leadActor.name,
      songTitle,
      background,
      projectType: type,
      notes,
      youtubeLink,
      embedUrl,
    },
    ...arrangements,
  ];

  form.reset();
  populateAllVoiceSelects();
  const leadIndex = Number(leadSelect.value) || 0;
  setDefaultBackgrounds(leadIndex);
  renderArrangements();
  persistArrangements();
  shareBanner.hidden = true;
}

function applySharedProjectFromUrl() {
  const params = new URLSearchParams(window.location.search);
  const shared = params.get('project');
  if (!shared) return false;
  try {
    const payload = decodeSharePayload(shared);
    const leadIndex = voiceActors.findIndex((actor) => actor.name === payload.lead);
    if (leadIndex >= 0) {
      leadSelect.value = leadIndex.toString();
    }
    updateBackgroundSelectStates();
    payload.background.forEach((name, idx) => {
      const actorIndex = voiceActors.findIndex((actor) => actor.name === name);
      if (actorIndex >= 0 && backgroundSelects[idx]) {
        backgroundSelects[idx].value = actorIndex.toString();
      }
    });
    songTitleInput.value = payload.songTitle ?? '';
    youtubeLinkInput.value = payload.youtubeLink ?? '';
    projectNotes.value = payload.notes ?? '';
    if (payload.projectType) {
      projectType.value = payload.projectType;
    }
    shareBanner.hidden = false;
    updateBackgroundSelectStates();
    params.delete('project');
    const newUrl = `${window.location.pathname}${params.toString() ? `?${params}` : ''}`;
    window.history.replaceState({}, '', newUrl);
    return true;
  } catch (error) {
    console.warn('Unable to load shared arrangement', error);
    return false;
  }
}

function init() {
  populateAllVoiceSelects();
  arrangements = getStoredArrangements();
  const sharedLoaded = applySharedProjectFromUrl();
  if (!sharedLoaded) {
    setDefaultBackgrounds(Number(leadSelect.value) || 0);
  }
  renderVoiceActors(voiceActors);
  renderArrangements();
  searchInput.addEventListener('input', handleSearch);
  form.addEventListener('submit', handleSubmit);
  leadSelect.addEventListener('change', updateBackgroundSelectStates);
}

init();
