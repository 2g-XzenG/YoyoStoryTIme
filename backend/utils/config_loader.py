import json
from pathlib import Path

# Define the path to the elements.json file
BASE_DIR = Path(__file__).resolve().parent.parent
ELEMENTS_FILE = BASE_DIR / "config" / "elements.json"

def load_elements():
    """
    Load predefined characters and scenes from elements.json.
    """
    if not ELEMENTS_FILE.exists():
        raise FileNotFoundError(f"Configuration file not found: {ELEMENTS_FILE}")

    with open(ELEMENTS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)