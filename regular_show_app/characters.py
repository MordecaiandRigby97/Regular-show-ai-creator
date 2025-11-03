"""Character and outfit models for the Regular Show inspired creator app."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class ClothingItem:
    """A single article of clothing or accessory."""

    name: str
    description: str


@dataclass
class Outfit:
    """A themed collection of clothing items."""

    name: str
    clothing_items: List[ClothingItem] = field(default_factory=list)

    def describe(self) -> str:
        items = ", ".join(item.name for item in self.clothing_items) or "no items"
        return f"{self.name}: {items}"


@dataclass
class Character:
    """Represents a character in the creator app."""

    name: str
    voice_actor: str
    hair_color: str
    eye_color: str
    outfits: List[Outfit] = field(default_factory=list)

    def add_outfit(self, outfit: Outfit) -> None:
        self.outfits.append(outfit)

    def describe(self) -> str:
        outfit_descriptions = "\n".join(f"  - {outfit.describe()}" for outfit in self.outfits)
        return (
            f"{self.name} (voiced by {self.voice_actor})\n"
            f"Hair: {self.hair_color}, Eyes: {self.eye_color}\n"
            f"Outfits:\n{outfit_descriptions or '  - No outfits yet.'}"
        )


def default_characters() -> List[Character]:
    """Create the default characters used by the app."""

    sydney = Character(
        name="Sydney",
        voice_actor="Courtenay Taylor",  # fan casting with Regular Show talent vibes
        hair_color="orange",
        eye_color="green",
    )
    sydney.add_outfit(
        Outfit(
            name="Park Day Chic",
            clothing_items=[
                ClothingItem("Denim Jacket", "Classic blue denim with custom park patches."),
                ClothingItem("Striped Tee", "Orange and white stripes to highlight Sydney's hair."),
                ClothingItem("High-Top Sneakers", "Emerald laces to mirror her eye color."),
                ClothingItem("Walkie Talkie", "For coordinating with the crew in style."),
            ],
        )
    )
    sydney.add_outfit(
        Outfit(
            name="Movie-Maker Mode",
            clothing_items=[
                ClothingItem("Director's Headset", "Keeps her connected to the sound stage."),
                ClothingItem("Utility Belt", "Packed with storyboards and voice notes."),
                ClothingItem("Flowy Scarf", "A pop of teal to contrast the orange hair."),
            ],
        )
    )

    janie = Character(
        name="Janie",
        voice_actor="Linda Cardellini",
        hair_color="brown",
        eye_color="hazel",
    )
    janie.add_outfit(
        Outfit(
            name="Babysitting Ready",
            clothing_items=[
                ClothingItem("Cozy Cardigan", "Soft knit with hidden snack pockets."),
                ClothingItem("Storytime Satchel", "Filled with comic books and crayons."),
                ClothingItem("Comfy Flats", "Great for quick park adventures."),
            ],
        )
    )

    emily = Character(
        name="Emily Rose",
        voice_actor="Ashley Johnson",
        hair_color="auburn",
        eye_color="blue",
    )
    emily.add_outfit(
        Outfit(
            name="Imagination Explorer",
            clothing_items=[
                ClothingItem("Star Hoodie", "Glow-in-the-dark constellations for bedtime stories."),
                ClothingItem("Mini Backpack", "Stuffed with plushies and art supplies."),
                ClothingItem("Sparkle Sneakers", "Light-up soles for dance breaks."),
            ],
        )
    )

    mordecai = Character(
        name="Mordecai",
        voice_actor="J. G. Quintel",
        hair_color="blue feathers",
        eye_color="brown",
    )
    mordecai.add_outfit(
        Outfit(
            name="Classic Blue Jay",
            clothing_items=[
                ClothingItem("Feathered Hoodie", "Matches his animated style."),
                ClothingItem("Retro Cap", "Embroidered with the park logo."),
            ],
        )
    )

    rigby = Character(
        name="Rigby",
        voice_actor="William Salyers",
        hair_color="striped fur",
        eye_color="black",
    )
    rigby.add_outfit(
        Outfit(
            name="Arcade Champ",
            clothing_items=[
                ClothingItem("Fingerless Gloves", "Improve gaming grip."),
                ClothingItem("Pixelated Hoodie", "Shows off an 8-bit coffee mug."),
            ],
        )
    )

    return [sydney, janie, emily, mordecai, rigby]


def list_voice_actors() -> List[str]:
    """Return a list of the Regular Show voice actors featured in the app."""

    return [
        "J. G. Quintel",
        "William Salyers",
        "Mark Hamill",
        "Sam Marin",
        "Linda Cardellini",
        "Courtenay Taylor",
        "Ashley Johnson",
    ]

