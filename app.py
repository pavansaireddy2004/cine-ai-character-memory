from prompt_engine import (
    load_character,
    build_prompt,
    build_establishing_prompt,
    build_heroine_prompt
)
from image_generator import generate_image_with_cache


def main():
    # ==================================================
    # Load hero identity ONCE
    # ==================================================
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
            prompt = build_establishing_prompt(shot, character)
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
            "camera": "wide establishing shot",
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

    # ==================================================
    # 🎬 SCENE 3 — POLICE STATION (3 SHOTS)
    # ==================================================
    scene_3_shots = [
        {
            "action": "Hero seated quietly inside a police station while officers work",
            "background": (
                "realistic Indian police station interior, wooden desks, "
                "files, notice board, officers moving in background"
            ),
            "lighting": "flat indoor fluorescent lighting",
            "camera": "wide establishing shot",
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
            "costume": "same clothing",
            "output": "scene3_shot2_interrogation.png"
        },
        {
            "action": "Hero standing silently, thinking, under pressure",
            "background": "police station interior, officers blurred in background",
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

    # ==================================================
    # 🎬 SCENE 4 — ACTION / TRANSITION (3 SHOTS)
    # ==================================================
    scene_4_shots = [
        {
            "action": "Hero walking alone slowly along the road",
            "background": (
                "Indian city street at night, dim street lights, "
                "passing vehicles with motion blur, closed shops, "
                "wet road reflecting lights"
            ),
            "lighting": "natural street lighting",
            "camera": "wide establishing shot",
            "costume": "dark casual clothing",
            "output": "scene4_shot1_city_walk.png"
        },
        {
            "action": "Hero driving a car quietly through the city at night",
            "background": (
                "city road seen through car windows, dashboard lights glowing"
            ),
            "lighting": "street light and dashboard glow",
            "camera": "wide exterior shot",
            "costume": "dark casual clothing",
            "output": "scene4_shot2_driving.png"
        },
        {
            "action": "Hero standing beside a friend, smoking quietly",
            "background": (
                "roadside tea stall at night, dim bulb light, smoke in air"
            ),
            "lighting": "warm practical lighting",
            "camera": "medium-wide shot",
            "costume": "dark casual clothing",
            "output": "scene4_shot3_friend.png"
        }
    ]

    for i, shot in enumerate(scene_4_shots):
        if i == 0:
            prompt = build_establishing_prompt(shot, character)
        else:
            prompt = build_prompt(shot, character)

        generate_image_with_cache(prompt, shot["output"])

    # ==================================================
    # 🎬 SCENE 5 — HEROINE INTRO (FIXED ✅)
    # ==================================================
    scene_5_shots = [
        {
            "action": "Hero and female lead walking slowly together",
            "background": (
                "large public park at evening, tall trees, walking paths, "
                "park benches, street lights turning on"
            ),
            "lighting": "natural evening light",
            "camera": "very wide establishing shot",
            "costume": "casual evening clothing",
            "output": "scene5_shot1_park_establishing.png"
        },
        {
            "action": "Hero and female lead walking side by side calmly",
            "background": (
                "quiet park path at night, trees on both sides"
            ),
            "lighting": "soft park lighting",
            "camera": "medium-wide shot",
            "costume": "same clothing",
            "output": "scene5_shot2_walk.png"
        },
        {
            "action": "Hero driving the car, female lead in passenger seat",
            "background": (
                "city road at night, street lights reflecting on windshield"
            ),
            "lighting": "street lights and dashboard glow",
            "camera": "wide interior car shot",
            "costume": "same clothing",
            "output": "scene5_shot3_car_drive.png"
        },
        {
            "action": "Hero glances at female lead with a slight smile",
            "background": (
                "parked car on quiet roadside, night atmosphere"
            ),
            "lighting": "soft ambient night lighting",
            "camera": "medium-wide two shot",
            "costume": "same clothing",
            "output": "scene5_shot4_smile.png"
        }
    ]

    for shot in scene_5_shots:
        prompt = build_heroine_prompt(shot, character)
        generate_image_with_cache(prompt, shot["output"])


if __name__ == "__main__":
    main()