from prompt_engine import (
    load_character,
    build_prompt,
    build_establishing_prompt
)
from image_generator import generate_image_with_cache


def main():
    # Load hero identity
    character = load_character("hero")

    # ==================================================
    # 🎬 SCENE 1 — PODCAST (3 SHOTS)
    # ==================================================
    scene_1_shots = [
        {
            "action": "Hero recording a podcast alone",
            "background": (
                "dark apartment living room, sofa against the wall, "
                "coffee table, bookshelf filled with books, "
                "standing lamp switched on, warm yellow light, "
                "curtains closed, nighttime interior"
            ),
            "lighting": "low key cinematic lighting, moody night ambience",
            "camera": "wide establishing shot",
            "costume": "dark casual clothing",
            "output": "scene1_shot1_establishing.png"
        },
        {
            "action": "Hero speaking calmly into a podcast microphone",
            "background": "same apartment interior, podcast setup visible",
            "lighting": "soft cinematic lighting",
            "camera": "medium-wide shot, eye level",
            "costume": "dark casual clothing",
            "output": "scene1_shot2_medium.png"
        },
        {
            "action": "Hero pauses thoughtfully during the podcast",
            "background": "same apartment interior, warm lamp glow",
            "lighting": "dramatic shadows",
            "camera": "side angle medium-wide shot",
            "costume": "dark casual clothing",
            "output": "scene1_shot3_mood.png"
        }
    ]

    for i, shot in enumerate(scene_1_shots):
        if i == 0:
            prompt = build_establishing_prompt(shot , character)
        else:
            prompt = build_prompt(shot, character)

        generate_image_with_cache(prompt, shot["output"])

    # ==================================================
    # 🎬 SCENE 2 — GRAVEYARD (3 SHOTS)
    # ==================================================
    scene_2_shots = [
        {
            "action": "Hero standing silently in a graveyard at night",
            "background": (
                "realistic Indian graveyard at night, uneven ground, "
                "old tombstones with faded inscriptions, stone crosses, "
                "dry trees, iron gate in distance, light mist near ground"
            ),
            "lighting": "natural moonlight, low visibility, soft shadows",
            "camera": "wide establishing shot, hero small in frame",
            "costume": "dark traditional clothing",
            "output": "scene2_shot1_establishing.png"
        },
        {
            "action": "Hero digging soil near a grave quietly",
            "background": (
                "same graveyard location, open soil, tombstones behind, "
                "mist around feet, dark trees forming silhouettes"
            ),
            "lighting": "moonlight mixed with weak torch light",
            "camera": "medium-wide shot, slightly low angle",
            "costume": "traditional clothing with dirt stains",
            "output": "scene2_shot2_action.png"
        },
        {
            "action": "Hero pauses and looks down, breathing heavily",
            "background": (
                "graveyard at night, mist drifting, blurred tombstones, "
                "dark trees in background"
            ),
            "lighting": "low moonlight, deep shadows",
            "camera": "side angle medium-wide shot",
            "costume": "same dirt-stained traditional clothing",
            "output": "scene2_shot3_emotion.png"
        }
    ]

    for i, shot in enumerate(scene_2_shots):
        if i == 0:
            prompt = build_establishing_prompt(shot, character)
        else:
            prompt = build_prompt(shot, character)

        generate_image_with_cache(prompt, shot["output"])


if __name__ == "__main__":
    main()


    # Load hero identity
    character = load_character("hero")

    # ==================================================
    # 🎬 SCENE 3 — POLICE STATION
    # ==================================================
    scene_3_shots = [
        {
            "action": "Hero seated quietly inside a police station while officers work",
            "background": (
                "realistic Indian police station interior, wooden desks, "
                "files, notice board, officers moving in background"
            ),
            "lighting": "flat indoor fluorescent lighting",
            "camera": "wide establishing shot, hero small in frame",
            "costume": "simple dark shirt and trousers",
            "output": "scene3_shot1_establishing.png"
        },
        {
            "action": "Hero questioned by a police officer across a desk",
            "background": (
                "police desk with open case files, "
                "police emblem on wall, other officers nearby"
            ),
            "lighting": "soft indoor lighting",
            "camera": "medium-wide shot",
            "costume": "same dark shirt and trousers",
            "output": "scene3_shot2_interrogation.png"
        },
        {
            "action": "Hero standing silently, thinking, under pressure",
            "background": (
                "police station interior, officers blurred in background"
            ),
            "lighting": "subdued indoor lighting",
            "camera": "side angle medium-wide shot",
            "costume": "same clothing",
            "output": "scene3_shot3_pressure.png"
        }
    ]

    for i, shot in enumerate(scene_3_shots):
        if i == 0:
            prompt = build_establishing_prompt(shot, character)
        else:
            prompt = build_prompt(shot, character)

        generate_image_with_cache(prompt, shot["output"])


# ❗ NOTHING BELOW THIS ❗
if __name__ == "__main__":
    main()