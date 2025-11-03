const characterForm = document.getElementById("character-form");
const sceneBeatsContainer = document.getElementById("scene-beats");
const timelineContainer = document.getElementById("timeline-scenes");
const exportTextArea = document.getElementById("export-text");

const beats = [];
const timeline = [];

function renderBeats() {
  sceneBeatsContainer.innerHTML = "";

  if (!beats.length) {
    sceneBeatsContainer.innerHTML =
      '<p class="empty">No beats yet. Add a character moment to kick things off.</p>';
    return;
  }

  beats.forEach((beat, index) => {
    const card = document.createElement("article");
    card.className = "card";
    card.innerHTML = `
      <h3>${beat.character} &mdash; ${beat.emotion}</h3>
      <div class="meta">${beat.backdrop} • ${beat.duration}s</div>
      <p><strong>Action:</strong> ${beat.action || "Freestyling"}</p>
      <p><strong>Clothing:</strong> ${beat.clothing || "Classic look"}</p>
      <p><strong>Accessories:</strong> ${beat.accessories || "None"}</p>
      <p><strong>Shoes:</strong> ${beat.shoes || "Standard kicks"}</p>
      <p><strong>Dialogue/Beat:</strong> ${beat.dialogue || "Silent storytelling"}</p>
      <footer>
        <span>Beat ${index + 1}</span>
        <button data-index="${index}" aria-label="Remove beat ${index + 1}">
          Remove
        </button>
      </footer>
    `;

    const removeBtn = card.querySelector("button");
    removeBtn.addEventListener("click", () => {
      beats.splice(index, 1);
      renderBeats();
    });

    sceneBeatsContainer.appendChild(card);
  });
}

function renderTimeline() {
  timelineContainer.innerHTML = "";

  if (!timeline.length) {
    timelineContainer.innerHTML =
      '<p class="empty">Your timeline is empty. Save a scene to start shaping your short.</p>';
    exportTextArea.value = "";
    return;
  }

  timeline.forEach((scene, index) => {
    const card = document.createElement("article");
    card.className = "card";
    const beatsList = scene.beats
      .map(
        (beat, beatIndex) => `
          <li>
            <strong>Beat ${beatIndex + 1}:</strong> ${beat.character} ${beat.emotion.toLowerCase()} &ndash;
            ${beat.action || "Improvising"} (${beat.duration}s)
          </li>
        `
      )
      .join("");

    card.innerHTML = `
      <h3>Scene ${index + 1}</h3>
      <div class="meta">${scene.location}</div>
      <p>${scene.summary}</p>
      <ul class="scene-list">${beatsList}</ul>
      <footer>
        <span>Total duration: ${scene.totalDuration}s</span>
        <button data-index="${index}" aria-label="Remove scene ${index + 1}">Remove</button>
      </footer>
    `;

    const removeBtn = card.querySelector("button");
    removeBtn.addEventListener("click", () => {
      timeline.splice(index, 1);
      renderTimeline();
      updateExport();
    });

    timelineContainer.appendChild(card);
  });
}

function updateExport() {
  if (!timeline.length) {
    exportTextArea.value = "";
    return;
  }

  const outline = timeline
    .map((scene, index) => {
      const beatsOutline = scene.beats
        .map((beat, beatIndex) => `      Beat ${beatIndex + 1}: ${beat.character} (${beat.emotion})`)
        .join("\n");

      return `Scene ${index + 1} — ${scene.location} (${scene.totalDuration}s)\n    ${scene.summary}\n${beatsOutline}`;
    })
    .join("\n\n");

  exportTextArea.value = outline;
}

characterForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const formData = new FormData(characterForm);
  const beat = {
    character: characterForm["character-select"].value,
    emotion: characterForm["emotion-select"].value,
    action: formData.get("action")?.trim(),
    clothing: formData.get("clothing")?.trim(),
    accessories: formData.get("accessories")?.trim(),
    shoes: formData.get("shoes")?.trim(),
    dialogue: formData.get("dialogue")?.trim(),
    backdrop: characterForm["backdrop-select"].value,
    duration: Number(characterForm["duration-input"].value) || 6,
  };

  if (!beat.character || !beat.emotion) {
    return;
  }

  beats.push(beat);
  characterForm.reset();
  document.getElementById("duration-input").value = 6;
  document.getElementById("backdrop-select").value = beat.backdrop;
  renderBeats();
});

const clearBeatsBtn = document.getElementById("clear-beats");
clearBeatsBtn.addEventListener("click", () => {
  beats.length = 0;
  renderBeats();
});

const saveSceneBtn = document.getElementById("save-scene");
saveSceneBtn.addEventListener("click", () => {
  if (!beats.length) {
    alert("Add at least one beat before saving a scene.");
    return;
  }

  const location = beats[0].backdrop;
  const totalDuration = beats.reduce((sum, beat) => sum + beat.duration, 0);
  const featured = [...new Set(beats.map((beat) => beat.character))].join(", ");
  const summary = `Featuring ${featured}. Highlights ${beats.length} beats with moods from ${beats[0].emotion.toLowerCase()} to ${beats[beats.length - 1].emotion.toLowerCase()}.`;

  timeline.push({
    beats: beats.map((beat) => ({ ...beat })),
    location,
    totalDuration,
    summary,
  });

  beats.length = 0;
  renderBeats();
  renderTimeline();
  updateExport();
});

const clearTimelineBtn = document.getElementById("clear-timeline");
clearTimelineBtn.addEventListener("click", () => {
  timeline.length = 0;
  renderTimeline();
  updateExport();
});

const exportBtn = document.getElementById("export-film");
exportBtn.addEventListener("click", () => {
  if (!timeline.length) {
    alert("Create at least one scene before exporting.");
    return;
  }

  updateExport();
  exportTextArea.focus();
  exportTextArea.select();
  const copied = document.execCommand("copy");
  if (copied) {
    alert("Story outline copied to your clipboard! Share it with the crew.");
  }
});

renderBeats();
renderTimeline();
