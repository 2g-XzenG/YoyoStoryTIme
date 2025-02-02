import json
from pathlib import Path

# Define the path to the elements.json file
ELEMENTS_FILE = Path(__file__).parent.parent.parent / "config" / "elements.json"

def load_elements():
    """
    Load predefined characters and scenes from elements.json.
    """
    with open(ELEMENTS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)
