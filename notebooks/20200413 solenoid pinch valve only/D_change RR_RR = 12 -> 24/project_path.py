"""Utilities for working with python paths from within Jupyter notebooks."""
import pathlib
import shutil
import sys


def add_parent(levels):
    """Add parent directory the specified number of levels above to the pyton path."""
    path = pathlib.Path.cwd()
    for level in range(levels):
        path = path.parent
    if path not in sys.path:
        sys.path.append(str(path))
    return path


def duplicate_to(target_path):
    """Copy this project_path.py script to the target path."""
    target_path = pathlib.Path(target_path)
    target_path.mkdir(parents=True, exist_ok=True)
    shutil.copy(pathlib.Path(__file__).resolve(), str(target_path))
