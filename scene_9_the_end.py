from prompt_engine import load_character
from image_generator import generate_image_with_cache


def build_mass_hero_prompt(scene, character):
    """
    FINAL END SHOT — Environment dominates, hero as silhouette
    """

    prompt = f"""
    epic cinematic wide shot, final scene, end title mood,

    environment is the primary subject,
    massive burning battlefield,
    ground covered in fire,
    flames spread across the horizon,
    thick smoke and embers in the air,
    destruction everywhere,
    environment occupies at least 80% of the frame,

    hero presence:
    {character['description']},
    hero standing alone facing the fire,
    hero seen from behind or silhouette,
    full body visible,
    hero small compared to environment,
    face NOT visible or not readable,
    no portrait framing,

    hero action:
    {scene['action']},

    lighting:
    intense fire backlight,
    hero in dark silhouette,
    high contrast,
    glowing flames illuminating smoke,

    camera:
    extreme wide shot,
    low angle perspective,
    deep depth of field,

    ultra realistic cinematic movie still,
    grounded realism,
    serious dramatic tone,
    no fantasy art,
    no stylized illustration,

    16:9 aspect ratio,
    landscape framing,

    no close-up,
    no face focus,
    no soft lighting,
    no beauty shot,
    no anime
    """

    return prompt.strip()


def main():
    character = load_character("hero")

    # ==================================================
    # 🎬 SCENE 9 — THE END (FINAL IMAGE)
    # ==================================================
    scene_9_end = {
        "action": (
            "Hero standing still, holding a weapon loosely at his side, "
            "watching the burning battlefield silently, "
            "calm after destruction"
        ),
        "output": "scene9_the_end.png"
    }

    prompt = build_mass_hero_prompt(scene_9_end, character)
    generate_image_with_cache(prompt, scene_9_end["output"])


if __name__ == "__main__":
    main()
