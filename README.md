# Regular Show Voice Actor Creator

A playful Regular Show studio where you can browse the cast, assemble musical or movie concepts, and save the project ideas locally. Each arrangement captures the lead, three background vocals, a YouTube backing track, project type, and scene notes so you can draft full productions.

## Run the app (working link)
1. From the project root run a lightweight static server: `python3 -m http.server 4173`.
2. Visit the local link that serves the studio: [http://localhost:4173](http://localhost:4173).
3. Open `index.html` if you prefer to double-click it directly — all scripts are client-side only.

## Sharing arrangements
- After saving an arrangement, use the **Copy share link** button to grab a URL containing the arrangement data.
- Send the link to a collaborator; when they open it, the arranger form pre-fills with the shared settings so they can immediately tweak or re-save the idea.

## Development notes
- Voice actor data lives in `script.js` within the `voiceActors` array.
- Arrangements persist in `localStorage` under the key `regular-show-arrangements`.
- Styles rely on `styles.css` and a single Changa font import.
