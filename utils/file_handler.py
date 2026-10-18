import json
import os

DATA_FILE = "data/storage.json"

def load_data():
    """Loads all application data from the local JSON file."""
    if not os.path.exists(DATA_FILE):
        return {"users": [], "projects": [], "tasks": []}
    
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        # Handle malformed data or read errors gracefully
        print("[Warning] Storage file is corrupted or unreadable. Resetting data.")
        return {"users": [], "projects": [], "tasks": []}

def save_data(data):
    """Saves application data back to the local JSON file."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        print(f"[Error] Could not save data: {e}")