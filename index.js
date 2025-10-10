const fs = require('fs');
const OpenAI = require('openai');

// --- Configuration ---
// IMPORTANT: Replace with your actual OpenAI API key
const API_KEY = process.env.OPENAI_API_KEY || 'YOUR_API_KEY';
const CHARACTERS_FILE = 'characters.json';

// --- Main Function ---
async function generateScene() {
  if (API_KEY === 'YOUR_API_KEY') {
    console.error('ERROR: Please replace "YOUR_API_KEY" with your actual OpenAI API key in index.js');
    return;
  }

  const openai = new OpenAI({ apiKey: API_KEY });

  try {
    const characters = JSON.parse(fs.readFileSync(CHARACTERS_FILE, 'utf8'));
    const scenePrompt = createScenePrompt(characters);

    console.log('Generating scene...');

    const response = await openai.chat.completions.create({
      model: 'gpt-3.5-turbo',
      messages: [{ role: 'user', content: scenePrompt }],
    });

    console.log('\n--- Generated Scene ---\n');
    console.log(response.choices[0].message.content);
    console.log('\n----------------------\n');

  } catch (error) {
    console.error('Error generating scene:', error.message);
  }
}

// --- Helper Function ---
function createScenePrompt(characters) {
  const characterDescriptions = characters.map(c => `
    - Name: ${c.name}
      - Description: ${c.description}
      - Voice: ${c.voice}
      - Current Emotion: ${c.emotion}
      - Wearing: ${c.clothing}
      - Shoes: ${c.shoes}
      - Accessories: ${c.accessories}
  `).join('');

  const scenarioPrompt = `
    Generate a short, funny scene script in the style of the show "Regular Show".
    The scene should feature some of the following characters. Pay close attention to their descriptions, voices, and emotions to ensure the dialogue is authentic.

    Character Details:
    ${characterDescriptions}

    Choose one of the following scenarios for the scene:
    1. The characters get into a ridiculous situation while trying to do a simple task (like setting up chairs or cleaning a fountain).
    2. The characters try a new, mysterious brand of bubble gum. They pop a piece in their mouth, describe the strange flavor, and then the tip of their nose starts turning purple.

    Incorporate their clothing and accessories into the scene description where appropriate.
  `;
  return scenarioPrompt;
}

// --- Run the script ---
generateScene();