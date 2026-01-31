import json


def load_character(character_name="hero"):
    """
    Load character identity from character_memory.json
    This locks the hero's face and identity across all scenes.
    """
    with open("character_memory.json", "r") as f:
        data = json.load(f)
    return data[character_name]


def build_prompt(scene, character):
    """
    Normal cinematic shots
    - Hero is visible
    - NOT a close-up
    - Background is important
    """

    prompt = f"""
    {character['description']},
    same person across scenes,
    consistent facial identity,
    realistic human proportions,

    single male character,
    solo subject,

    cinematic 35mm film look,
    medium-wide shot,
    hero visible from waist-up or wider,

    action:
    {scene['action']},

    background:
    {scene['background']},

    lighting:
    {scene['lighting']},

    camera:
    {scene['camera']},

    environment clearly visible,
    background important to the story,
    grounded, realistic location,

    ultra realistic cinematic movie still,
    natural skin tones,
    realistic film color grading,
    modern digital cinema look,
    16:9 landscape framing,

    no close-up face,
    no portrait framing,
    no anime,
    no illustration,
    no cartoon,
    no fantasy style
    """

    return prompt.strip()


def build_establishing_prompt(scene, character):
    """
    Environment-first establishing shot
    - World first
    - Hero present but secondary
    """

    prompt = f"""
    cinematic wide establishing shot of a realistic environment,

    environment is the primary subject:
    {scene['background']},

    environment occupies at least 70–80% of the frame,
    wide angle lens,
    deep depth of field,
    entire location clearly visible,

    a male character (hero) is present,
    hero visible but small in frame,
    hero positioned away from the camera,
    hero does not dominate the image,
    no facial emphasis,

    hero action:
    {scene['action']},

    lighting:
    {scene['lighting']},

    ultra realistic cinematic movie still,
    natural colors,
    serious grounded film tone,
    environmental storytelling frame,

    16:9 landscape framing,

    no close-up,
    no portrait,
    no anime,
    no illustration,
    no fantasy,
    no exaggerated colors,
    no studio lighting
    """

    return prompt.strip()


def build_action_mass_prompt(scene, character):
    """
    Scene 4 — Mass / Action shots
    Hero present but NOT dominant
    Multiple people, weapons, cinematic chaos
    """

    prompt = f"""
    {character['description']},
    same person across scenes,
    consistent facial identity,

    multiple people present,
    hero is part of a group,
    hero not centered,
    hero not dominant,
    side characters visible clearly,

    some people holding guns or weapons,
    tense action atmosphere,
    serious realistic tone,
    no exaggeration,

    cinematic 35mm film look,
    wide or medium-wide shot,
    group composition,
    hero occupies less than 30% of frame,

    action:
    {scene['action']},

    background:
    {scene['background']},

    lighting:
    {scene['lighting']},

    camera:
    {scene['camera']},

    background clearly visible,
    environment important to storytelling,

    ultra realistic cinematic movie still,
    natural colors,
    film color grading,
    16:9 landscape,

    no anime,
    no illustration,
    no fantasy,
    no portrait,
    no close-up face,
    no hero-only framing
    """

    return prompt.strip()
