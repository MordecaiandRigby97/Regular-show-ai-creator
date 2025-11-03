"""Simple movie maker utilities that stitch story scenes together."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from .characters import Character
from .story import Scene


@dataclass
class VoiceLine:
    """Represents a spoken line recorded by a Regular Show voice actor."""

    text: str
    performed_by: Character

    def render(self) -> str:
        return f"{self.performed_by.name} ({self.performed_by.voice_actor}): {self.text}"


@dataclass
class MovieProject:
    """Keeps track of scenes, outfits, and voice lines."""

    title: str
    scenes: List[Scene] = field(default_factory=list)
    voice_lines: List[VoiceLine] = field(default_factory=list)

    def add_scene(self, scene: Scene) -> None:
        self.scenes.append(scene)

    def add_voice_line(self, voice_line: VoiceLine) -> None:
        self.voice_lines.append(voice_line)

    def storyboard(self) -> str:
        """Create a textual storyboard overview."""

        lines: List[str] = [f"Movie Project: {self.title}"]
        lines.append("Scenes:")
        for index, scene in enumerate(self.scenes, start=1):
            lines.append(f"  {index}. {scene.title} - cast: {', '.join(ch.name for ch in scene.characters)}")
            lines.append(f"     {scene.description}")
        if self.voice_lines:
            lines.append("Voice Lines:")
            for line in self.voice_lines:
                lines.append(f"  - {line.render()}")
        else:
            lines.append("Voice Lines: (none recorded yet)")
        return "\n".join(lines)


def create_default_project() -> MovieProject:
    """Build a movie project around the babysitting story arc."""

    project = MovieProject(title="Sydney's Babysitting Adventure")

    from .story import babysitting_story

    for scene in babysitting_story():
        project.add_scene(scene)

    def find_character(name: str) -> Character:
        for scene in project.scenes:
            for character in scene.characters:
                if character.name == name:
                    return character
        raise ValueError(f"Character {name!r} not found in project scenes")

    sydney = find_character("Sydney")
    janie = find_character("Janie")
    emily = find_character("Emily Rose")
    mordecai = find_character("Mordecai")
    rigby = find_character("Rigby")
    jayla = find_character("Jayla")

    # Sample voice lines using the Regular Show actors
    project.add_voice_line(
        VoiceLine(
            text="Janie, could you watch Emily while I wrangle Mordecai and Rigby?",
            performed_by=sydney,
        )
    )
    project.add_voice_line(
        VoiceLine(
            text="Don't worry, Sydney! Emily and I will make the cutest behind-the-scenes video ever!",
            performed_by=janie,
        )
    )
    project.add_voice_line(
        VoiceLine(
            text="Rigby, keep that mic steady! Emily's laugh is gold!",
            performed_by=mordecai,
        )
    )
    project.add_voice_line(
        VoiceLine(
            text="What? A little mud never hurt a storyboard!",
            performed_by=jayla,
        )
    )
    project.add_voice_line(
        VoiceLine(
            text="Hey Jayla, how about using that energy to help me rebuild the set?",
            performed_by=rigby,
        )
    )
    project.add_voice_line(
        VoiceLine(
            text="Group hug! Let's film a make-up montage before Mom gets back!",
            performed_by=emily,
        )
    )

    return project
