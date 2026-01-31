import os
import json
import hashlib

CACHE_DIR = "cache"
IMAGE_DIR = os.path.join(CACHE_DIR, "images")
META_FILE = os.path.join(CACHE_DIR, "metadata.json")

os.makedirs(IMAGE_DIR, exist_ok=True)

if not os.path.exists(META_FILE):
    with open(META_FILE, "w") as f:
        json.dump({}, f)


def _hash_prompt(prompt: str) -> str:
    return hashlib.sha256(prompt.encode("utf-8")).hexdigest()


def get_cached_image(prompt: str):
    with open(META_FILE, "r") as f:
        data = json.load(f)

    key = _hash_prompt(prompt)
    return data.get(key)


def save_to_cache(prompt: str, image_path: str):
    with open(META_FILE, "r") as f:
        data = json.load(f)

    key = _hash_prompt(prompt)
    data[key] = image_path

    with open(META_FILE, "w") as f:
        json.dump(data, f, indent=2)
