"""Storyboarding utilities for Regular Show inspired video projects."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, List

from .cast import CastMember, get_cast


@dataclass
class Scene:
    """A storyboard scene featuring a subset of the cast."""

    description: str
    featured_characters: List[str]


@dataclass
class VideoMaker:
    """Simple helper for assembling short-form videos."""

    title: str
    premise: str
    cast: List[CastMember] = field(default_factory=get_cast)
    scenes: List[Scene] = field(default_factory=list)

    def add_scene(self, description: str, featured_characters: Iterable[str]) -> None:
        """Append a storyboard scene to the video."""

        self.scenes.append(Scene(description=description, featured_characters=list(featured_characters)))

    def build_outline(self) -> str:
        """Return a formatted outline of the video including cast and scenes."""

        lines = [f"Title: {self.title}", f"Premise: {self.premise}", "Cast:"]
        for member in self.cast:
            lines.append(f"  - {member.character} (voice: {member.voice_actor})")
        if not self.scenes:
            lines.append("No scenes have been added yet.")
        else:
            lines.append("Scenes:")
            for index, scene in enumerate(self.scenes, start=1):
                featured = ", ".join(scene.featured_characters)
                lines.append(f"  {index}. {scene.description} [{featured}]")
        return "\n".join(lines)


__all__ = ["Scene", "VideoMaker"]
