"""Lightweight video generator mock that outputs a production plan."""
from __future__ import annotations

from pathlib import Path
from typing import Iterable

from .movie_maker import MovieProject


def render_ascii_frame(scene_title: str, frame_index: int) -> str:
    """Create a playful ASCII frame banner for a scene."""

    banner = f"[{scene_title.upper()} - FRAME {frame_index:02d}]"
    border = "=" * len(banner)
    return f"{border}\n{banner}\n{border}"


def export_project(project: MovieProject, output_dir: Path) -> Path:
    """Export the project's storyboard and fake video frames to disk."""

    output_dir.mkdir(parents=True, exist_ok=True)
    storyboard_path = output_dir / "storyboard.txt"
    storyboard_path.write_text(project.storyboard())

    frames_dir = output_dir / "frames"
    frames_dir.mkdir(exist_ok=True)

    for index, scene in enumerate(project.scenes, start=1):
        frame_text = render_ascii_frame(scene.title, index)
        frame_path = frames_dir / f"scene_{index:02d}.txt"
        frame_path.write_text(frame_text)

    return storyboard_path


def assemble_video(frames: Iterable[Path], destination: Path) -> None:
    """Combine frame files into a pseudo-video file (a stitched text document)."""

    contents = [frame.read_text() for frame in frames]
    destination.write_text("\n\n".join(contents))
