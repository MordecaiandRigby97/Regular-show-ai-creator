import json
import random

def load_characters(filename="characters.json"):
    """Loads character data from a JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)["characters"]

def generate_interaction(characters):
    """Generates a more dynamic interaction between two random characters."""
    char1, char2 = random.sample(characters, 2)

    char1_name = char1["name"]
    char2_name = char2["name"]

    # Choose a random emotion for each character
    char1_emotion_name = random.choice(list(char1["emotions"].keys()))
    char2_emotion_name = random.choice(list(char2["emotions"].keys()))

    char1_emotion = char1["emotions"][char1_emotion_name]
    char2_emotion = char2["emotions"][char2_emotion_name]

    # Get the action and dialogue
    char1_action = char1_emotion["action"]
    char1_dialogue = random.choice(char1_emotion["dialogue"])

    char2_action = char2_emotion["action"]
    char2_dialogue = random.choice(char2_emotion["dialogue"])

    # Get the audio placeholder
    char1_audio = char1_emotion["audio_placeholder"]
    char2_audio = char2_emotion["audio_placeholder"]

    interaction = f"Scene: {char1_name} and {char2_name} are at the park.\n\n"
    interaction += f"{char1_name} ({char1_emotion_name}): {char1_action}\n"
    interaction += f'"{char1_dialogue}"\n'
    interaction += f"(Audio: {char1_audio})\n\n"

    interaction += f"{char2_name} ({char2_emotion_name}): {char2_action}\n"
    interaction += f'"{char2_dialogue}"\n'
    interaction += f"(Audio: {char2_audio})\n"

    return interaction

if __name__ == "__main__":
    characters = load_characters()
    interaction = generate_interaction(characters)
    print("--- A Regular Show Interaction ---")
    print(interaction)
    print("---------------------------------")