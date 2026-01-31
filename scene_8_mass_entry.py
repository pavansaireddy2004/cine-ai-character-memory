from prompt_engine import (
    load_character,
    build_mass_entry_prompt
)
from image_generator import generate_image_with_cache


def main():
    character = load_character("hero")

    # ==================================================
    # 🎬 SCENE 8 — MASS ENTRY SEQUENCE
    # SHOT 1 IS LOCKED ❗ DO NOT MODIFY
    # ==================================================

    scene_8_shots = [
        {
            # ✅ SHOT 1 — Car Exit (LOCKED)
            "action": (
                "Hero stepping out of a car slowly, "
                "one door open, hero pauses and looks ahead calmly"
            ),
            "background": (
                "open road with dry terrain, "
                "parked vehicle angled in frame, "
                "wide sky and distant landscape visible"
            ),
            "output": "scene8_shot1_car_exit.png"
        },

        {
            # ✅ SHOT 2 — Rain Mass Entry (NEW)
            "action": (
                "Hero standing alone in heavy rain, "
                "head slightly lowered, fist clenched, "
                "emotion restrained but powerful"
            ),
            "background": (
                "outdoor location in heavy rainfall, "
                "blurred trees and structures behind, "
                "natural environment visible through rain"
            ),
            "output": "scene8_shot2_rain_mass.png"
        }
    ]

    for shot in scene_8_shots:
        prompt = build_mass_entry_prompt(shot, character)
        generate_image_with_cache(prompt, shot["output"])


if __name__ == "__main__":
    main()
