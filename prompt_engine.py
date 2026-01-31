import json

def load_character(character_name="hero"):
    """
    Loads character data from character_memory.json
    """
    with open("character_memory.json", "r") as f:
        data = json.load(f)
    return data[character_name]


def build_prompt(scene, character):
    """
    Builds prompt from:
    - scene DICT (story-based scenes)
    - OR plain TEXT (Streamlit user input)
    """

    # 🔹 CASE 1: Scene is plain text (Streamlit input)
    if isinstance(scene, str):
        prompt = f"""
        {character['description']},
        same person, same face, same facial structure,
        same jawline, same beard style, same hairstyle,

        single male character only,
        only one person in the frame,
        solo subject,

        cinematic 35mm lens look,
        medium-wide framing, waist-up or wider,

        scene description: {scene},

        realistic environment matching the scene,
        environment must be visible and story-relevant,

        camera distance is long shot or wide shot,
        full upper body visible,
        subject occupies only 30–40% of the frame,
        environment occupies majority of the frame,
        background clearly visible and detailed,

        background must be clearly readable,
        background is as important as the character,
        environment storytelling shot,

        cinematic lighting,
        ultra realistic cinematic movie still,
        full color photography,
        natural skin tones,
        realistic color grading,
        modern digital cinema look,
        16:9 aspect ratio, landscape framing,

        no close-up face,
        no extreme close-up,
        no tight portrait,
        no face filling the frame
        """
        return prompt.strip()

    # 🔹 CASE 2: Scene is dictionary
    prompt = f"""
    {character['description']},
    same person, same face, same facial structure,
    same jawline, same beard style, same hairstyle,

    single male character only,
    only one person in the frame,
    solo subject,

    consistent cinematic lens, 35mm film lens look,
    medium-wide framing, subject visible from waist-up or wider,

    wearing {scene['costume']},

    scene action: {scene['action']},
    background: {scene['background']},
    environment is clearly visible,
    background is dominant and story-relevant,

    background must be clearly readable,
    background is as important as the character,
    environment storytelling shot,

    lighting: {scene['lighting']},

    cinematic wide shot,
    subject placed using rule of thirds,
    visible environment around the character,
    camera positioned as {scene['camera']},

    camera distance is long shot or wide shot,
    full upper body visible,
    subject occupies only 30–40% of the frame,
    environment occupies majority of the frame,
    background clearly visible and detailed,

    ultra realistic cinematic movie still,
    full color photography,
    natural skin tones,
    realistic color grading,
    modern digital cinema look,
    16:9 aspect ratio, landscape framing,

    no studio lighting,
    no plain background,
    no portrait photography,
    no headshot,
    no close-up only face,
    no extreme close-up,
    no tight portrait,
    no face filling the frame,
    no black and white,
    no monochrome,
    no sketch,
    no illustration,
    no anime,
    no comic style
    """
    return prompt.strip()


def build_prompt_with_co_character(scene, character, co_role="side"):
    """
    Builds prompt for scenes with a co-character.
    co_role:
      - "side"    → hero dominant, side character secondary
      - "heroine" → hero and heroine share equal importance
    """

    if co_role == "heroine":
        people_block = """
        two main characters present,
        hero and heroine share the frame equally,
        balanced cinematic two-shot composition,
        both characters clearly visible,
        both faces in focus,
        equal lighting on both characters,
        emotional connection implied between them
        """
    else:
        people_block = """
        hero is the clear primary subject,
        one side character present as supporting role,
        hero occupies majority of the frame,
        side character positioned to the side or background,
        hero in sharp focus, side character slightly out of focus,
        lighting emphasizes hero
        """

    prompt = f"""
    {character['description']},
    same person, same face, same facial structure,
    same jawline, same beard style, same hairstyle,

    {people_block},

    cinematic 35mm film lens look,
    medium-wide or wide shot,
    full upper body visible,
    subject occupies only 30–40% of the frame,
    environment occupies majority of the frame,

    wearing {scene['costume']},

    scene action: {scene['action']},
    background: {scene['background']},
    environment must be clearly visible,
    background is dominant and story-relevant,

    lighting: {scene['lighting']},

    camera composition: {scene['camera']},
    rule of thirds composition,
    environment storytelling shot,

    ultra realistic cinematic movie still,
    full color photography,
    natural skin tones,
    realistic color grading,
    modern digital cinema look,
    16:9 aspect ratio, landscape framing,

    no studio lighting,
    no plain background,
    no portrait photography,
    no headshot,
    no extreme close-up,
    no face filling the frame,
    no black and white,
    no monochrome,
    no sketch,
    no illustration,
    no anime,
    no comic style
    """

    return prompt.strip()
