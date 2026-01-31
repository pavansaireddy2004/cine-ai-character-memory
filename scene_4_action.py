from prompt_engine import (
    load_character,
    build_action_mass_prompt
)
from image_generator import generate_image_with_cache


def main():
    # Load hero identity
    character = load_character("hero")

    # ==================================================
    # 🎬 SCENE 4 — ACTION / MASS ENTRY (3 SHOTS)
    # ==================================================
    scene_4_shots = [
        {
            # SHOT 1 — Establishing (world + mass)
            "action": "Hero walking slowly through an open area at night",
            "background": (
                "dimly lit open ground at night, parked vehicles, "
                "street lights casting long shadows, "
                "group of men standing behind the hero"
            ),
            "lighting": "low key night lighting, hard shadows",
            "camera": "wide shot, hero off-center",
            "costume": "dark mass outfit",
            "output": "scene4_shot1_establishing.png"
        },
        {
            # SHOT 2 — Mass attitude
            "action": (
                "Hero standing calmly, holding a cigarette, "
                "slight confident smile on his face"
            ),
            "background": (
                "men beside the hero holding guns casually, "
                "vehicles parked behind, night street atmosphere"
            ),
            "lighting": "dramatic side lighting, cigarette smoke visible",
            "camera": "medium-wide shot",
            "costume": "same dark mass outfit",
            "output": "scene4_shot2_mass.png"
        },
        {
            # SHOT 3 — Tension build-up
            "action": "Hero looks forward calmly as men behind him raise their guns",
            "background": (
                "night street, armed men in aggressive stance, "
                "tense confrontation atmosphere"
            ),
            "lighting": "harsh contrast lighting, deep shadows",
            "camera": "wide shot, hero foreground but not dominant",
            "costume": "same dark mass outfit",
            "output": "scene4_shot3_tension.png"
        }
    ]

    # ✅ GENERATE SCENE 4 SHOTS (MASS PROMPT ONLY)
    for shot in scene_4_shots:
        prompt = build_action_mass_prompt(shot, character)
        generate_image_with_cache(prompt, shot["output"])


if __name__ == "__main__":
    main()
