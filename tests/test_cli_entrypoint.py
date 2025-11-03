import os
import subprocess
import sys
from pathlib import Path


def test_module_entrypoint_runs_without_export(tmp_path, monkeypatch):
    # Ensure the command uses a temp directory for exports to avoid polluting the repo
    monkeypatch.chdir(tmp_path)
    project_root = Path(__file__).resolve().parents[1]
    env = os.environ.copy()
    env["PYTHONPATH"] = str(project_root)
    result = subprocess.run(
        [sys.executable, "-m", "regular_show_app", "--skip-export"],
        check=True,
        capture_output=True,
        text=True,
        env=env,
    )
    assert "Voice Actors Featured" in result.stdout
    assert "Movie Maker Storyboard" in result.stdout
