from prompt_engine import (
    load_character,
    build_mass_hero_prompt   # ✅ IMPORTANT
)
from image_generator import generate_image_with_cache


def main():
    # Load hero identity
    character = load_character("hero")

    # ==================================================
    # 🎬 SCENE 6 — MASS / PEAK HERO IMAGE (SINGLE SHOT)
    # ==================================================
    scene_6_mass_shot = {
        "action": (
            "Hero walking forward powerfully through a violent storm, "
            "holding a heavy iron chain in one hand, "
            "calm and fearless expression, unstoppable presence"
        ),

        "background": (
            "massive storm clouds filling the sky, "
            "lightning striking behind the hero, "
            "heavy rain falling diagonally, "
            "vast rocky open ground, "
            "epic scale environment dominating the frame"
        ),

        "lighting": (
            "intense lightning backlight, "
            "strong rim light outlining the hero’s body, "
            "dark cinematic shadows, "
            "high contrast dramatic lighting"
        ),

        "camera": (
            "extreme wide cinematic shot, "
            "low angle perspective, "
            "hero full body visible, "
            "environment occupying most of the frame"
        ),

        "costume": (
            "rugged warrior-style traditional clothing, "
            "wet fabric clinging to body, "
            "battle-worn, raw and realistic"
        ),

        "output": "scene6_mass_hero.png"
    }

    # ✅ USE MASS PROMPT (THIS IS THE KEY)
    prompt = build_mass_hero_prompt(scene_6_mass_shot, character)
    generate_image_with_cache(prompt, scene_6_mass_shot["output"])


if __name__ == "__main__":
    main()
