from prompt_engine import load_character, build_prompt
from image_generator import generate_image

def main():
    # Load character memory (identity stays locked)
    character = load_character("hero")

    # Story-based scenes
    scenes = [
        {
            "action": "Hero recording a podcast alone",
            "background": (
                "dark apartment living room, sofa against the wall, "
                "podcast microphone on table, bookshelf in background, "
                "dim lamp light, closed curtains"
            ),
            "lighting": "low key lighting, eerie night mood",
            "camera": "static medium-wide shot, eye level",
            "costume": "dark casual clothing",
            "output": "scene_1.png"
        },
        {
            "action": "Hero burying a body in a graveyard",
            "background": (
                "graveyard at night, visible tombstones, stone crosses, "
                "mist near the ground, iron gate in distance, old trees"
            ),
            "lighting": "moonlight, dramatic shadows",
            "camera": "wide shot, slightly low angle",
            "costume": "traditional clothing with dirt stains",
            "output": "scene_2.png"
        },
        {
            "action": "Hero standing inside a police station during investigation",
            "background": (
                "Hyderabad police station interior, wooden desks with files, "
                "FIR registers on the table, police emblem on the wall, "
                "notice board with case papers, barred windows, ceiling fan"
            ),
            "lighting": "bright indoor daylight, fluorescent lighting",
            "camera": "medium-wide shot, side angle",
            "costume": "simple shirt and trousers",
            "output": "scene_3.png"
        }
    ]

    for scene in scenes:
        prompt = build_prompt(scene, character)
        generate_image(prompt, scene["output"])


if __name__ == "__main__":
    main()
