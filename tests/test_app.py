from pathlib import Path

from regular_show_app.characters import default_characters, list_voice_actors
from regular_show_app.movie_maker import create_default_project
from regular_show_app.story import babysitting_story
from regular_show_app.video_generator import assemble_video, export_project


def test_default_characters_include_sydney_details():
    characters = default_characters()
    sydney = next(character for character in characters if character.name == "Sydney")
    assert sydney.hair_color == "orange"
    assert sydney.eye_color == "green"
    assert any("Movie-Maker Mode" == outfit.name for outfit in sydney.outfits)


def test_voice_actor_list_contains_regular_show_cast():
    actors = list_voice_actors()
    assert "J. G. Quintel" in actors
    assert "William Salyers" in actors


def test_babysitting_story_has_required_scenes():
    scenes = babysitting_story()
    titles = [scene.title for scene in scenes]
    assert "Sydney's Pitch" in titles
    assert "Director's Return" in titles


def test_movie_project_exports(tmp_path: Path):
    project = create_default_project()
    export_dir = tmp_path / "export"
    storyboard_path = export_project(project, export_dir)

    assert storyboard_path.exists()
    frames_dir = export_dir / "frames"
    frame_files = sorted(frames_dir.glob("scene_*.txt"))
    assert len(frame_files) == len(project.scenes)

    destination = export_dir / "stitched_video.txt"
    assemble_video(frame_files, destination)
    assert destination.exists()
