"""Support for reading and writing generic data files."""
import json
import pathlib


# Directory I/O

def ensure_path(path):
    """Ensure the existence of the path by making directories as needed."""
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)


# JSON I/O

def dump_json(dictionary, path=None):
    """Save a json object to a file."""
    if path is None:
        return json.dumps(dictionary, indent=2, allow_nan=False)
    with open(path, 'w') as f:
        json.dump(dictionary, f, indent=2, allow_nan=False)
        return None


def load_json(path):
    """Load a json object from a file."""
    with open(path, 'r') as f:
        return json.load(f)


# String I/O

def dump_string(string, path):
    """Save a string to a file."""
    pathlib.Path(path).write_text(string)


def load_string(path):
    """Load a string from a file."""
    return pathlib.Path(path).read_text()


def normalize_line_endings(string):
    """Convert all line endings to newline chars."""
    return string.replace('\r\n', '\n').replace('\r', '\n')
