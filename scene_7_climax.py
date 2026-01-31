from prompt_engine import (
    load_character,
    build_prompt
)
from image_generator import generate_image_with_cache


def main():
    # Load hero identity
    character = load_character("hero")

    # ==================================================
    # 🎬 SCENE 7 — CLIMAX INTRO (HERO MEETS HEROINE)
    # Environment + Emotion Dominant
    # ==================================================
    scene_7_climax_shots = [
        {
            # SHOT 1 — Establishing (Environment first)
            "action": (
                "Hero and female lead standing face to face in silence, "
                "intense emotional tension, no dialogue"
            ),
            "background": (
                "open outdoor area, muted cloudy sky, "
                "parked vehicle behind hero, "
                "empty space around them, "
                "calm before the storm feeling"
            ),
            "lighting": (
                "soft natural daylight, "
                "overcast sky, "
                "realistic cinematic tones"
            ),
            "camera": (
                "wide cinematic shot, "
                "both characters fully visible, "
                "background dominant, "
                "no close-up"
            ),
            "costume": (
                "hero wearing rugged casual clothing, "
                "female lead in simple elegant outfit"
            ),
            "output": "scene7_climax_shot1_establishing.png"
        },
        {
            # SHOT 2 — Emotional Face-Off
            "action": (
                "Hero looks at the female lead with restrained anger and pain, "
                "female lead looks back with concern and strength"
            ),
            "background": (
                "same open environment, "
                "vehicle partially visible, "
                "soft blurred background"
            ),
            "lighting": (
                "natural soft light, "
                "subtle shadows on faces"
            ),
            "camera": (
                "medium-wide two shot, "
                "side angle composition, "
                "balanced focus on both characters"
            ),
            "costume": (
                "same clothing as previous shot"
            ),
            "output": "scene7_climax_shot2_emotion.png"
        },
        {
            # SHOT 3 — Turn Toward Violence (Bridge to Fight)
            "action": (
                "Hero slowly turns away from the female lead, "
                "jaw clenched, fists tightening, "
                "decision made to face the enemy"
            ),
            "background": (
                "open space stretching ahead, "
                "road or empty ground leading forward, "
                "stormy mood building"
            ),
            "lighting": (
                "slightly darker natural light, "
                "dramatic clouds forming"
            ),
            "camera": (
                "wide shot from behind hero, "
                "hero moving forward, "
                "female lead remaining behind"
            ),
            "costume": (
                "same clothing"
            ),
            "output": "scene7_climax_shot3_turn.png"
        }
    ]

    for shot in scene_7_climax_shots:
        prompt = build_prompt(shot, character)
        generate_image_with_cache(prompt, shot["output"])


if __name__ == "__main__":
    main()
