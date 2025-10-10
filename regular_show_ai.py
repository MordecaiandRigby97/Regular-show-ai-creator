import json

def load_characters():
    with open('characters.json', 'r') as f:
        return json.load(f)

def save_characters(characters):
    with open('characters.json', 'w') as f:
        json.dump(characters, f, indent=2)

def create_character(characters):
    name = input("Enter the character's name: ")
    new_character = {
        "name": name,
        "clothing": [],
        "emotions": [],
        "actions": [],
        "is_blueberry": False
    }
    characters["characters"].append(new_character)
    save_characters(characters)
    print(f"Character '{name}' created successfully!")

def transform_to_blueberry(characters):
    print("Select a character to transform into a blueberry:")
    for i, char in enumerate(characters["characters"]):
        print(f"{i + 1}. {char['name']}")

    choice = input("Enter the number of the character: ")
    try:
        char_index = int(choice) - 1
        if 0 <= char_index < len(characters["characters"]):
            character = characters["characters"][char_index]
            character["is_blueberry"] = True
            save_characters(characters)
            print(f"{character['name']} has been turned into a blueberry!")
        else:
            print("Invalid character number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def manage_character(characters):
    print("Select a character to manage:")
    for i, char in enumerate(characters["characters"]):
        print(f"{i + 1}. {char['name']}")

    choice = input("Enter the number of the character: ")
    try:
        char_index = int(choice) - 1
        if 0 <= char_index < len(characters["characters"]):
            character = characters["characters"][char_index]
            while True:
                print(f"\nManaging {character['name']}:")
                print("1. Add clothing")
                print("2. Add emotion")
                print("3. Add action")
                print("4. Back to main menu")
                sub_choice = input("Enter your choice: ")

                if sub_choice == '1':
                    item = input("Enter the clothing item: ")
                    character["clothing"].append(item)
                    save_characters(characters)
                    print("Clothing item added.")
                elif sub_choice == '2':
                    emotion = input("Enter the emotion: ")
                    character["emotions"].append(emotion)
                    save_characters(characters)
                    print("Emotion added.")
                elif sub_choice == '3':
                    action = input("Enter the action: ")
                    character["actions"].append(action)
                    save_characters(characters)
                    print("Action added.")
                elif sub_choice == '4':
                    break
                else:
                    print("Invalid choice.")
        else:
            print("Invalid character number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == '__main__':
    characters_data = load_characters()
    print("Welcome to the Regular Show AI creator!")
    while True:
        print("\nWhat would you like to do?")
        print("1. Create a new character")
        print("2. Transform a character into a blueberry")
        print("3. Manage a character")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_character(characters_data)
        elif choice == '2':
            transform_to_blueberry(characters_data)
        elif choice == '3':
            manage_character(characters_data)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")