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

def build_heroine_prompt(scene, character):
    """
    Hero + Heroine cinematic shots (balanced, environment visible)
    """

    prompt = f"""
    {character['description']},
    same hero identity across scenes,

    two main characters present:
    hero and female lead,

    both characters visible,
    natural human proportions,
    realistic appearance,

    cinematic wide or medium-wide shot,
    environment clearly visible,
    background dominant over faces,

    action:
    {scene['action']},

    background:
    {scene['background']},

    lighting:
    {scene['lighting']},

    camera:
    {scene['camera']},

    ultra realistic cinematic movie still,
    natural skin tones,
    serious film look,
    16:9 landscape framing,

    no anime,
    no illustration,
    no fantasy,
    no beauty shot,
    no close-up face,
    no portrait framing
    """

    return prompt.strip()




def build_mass_hero_prompt(scene, character):
    """
    SCENE 6 ONLY
    Mythic / Mass elevation shot
    Environment and scale dominate the frame
    """

    prompt = f"""
    epic cinematic wide shot, mythic scale, theatrical elevation moment,

    environment is the primary subject,
    vast dramatic landscape,
    towering storm clouds, heavy rain, lightning tearing the sky,
    massive symbolic elements dominating the background,
    environment occupies at least 75–80% of the frame,

    hero presence:
    {character['description']},
    hero standing firm and powerful,
    hero small relative to the environment,
    full body or long shot only,
    face visible but NOT emphasized,
    no portrait framing,

    hero action:
    {scene['action']},

    background details:
    {scene['background']},

    lighting:
    extreme high-contrast cinematic lighting,
    lightning backlight,
    strong rim light outlining hero silhouette,
    dark clouds, rain-filled atmosphere,

    ultra realistic cinematic movie still,
    epic Indian mythic tone,
    grounded realism,
    serious theatrical color grading,
    large-scale cinema poster quality,

    camera:
    extreme wide angle lens,
    low-angle perspective looking up at the hero,
    deep depth of field,
    background razor sharp and dominant,

    16:9 aspect ratio,
    widescreen landscape framing,

    no close-up,
    no medium shot,
    no portrait,
    no studio lighting,
    no beauty lighting,
    no anime,
    no illustration,
    no fantasy art style
    """

    return prompt.strip()




def build_mass_entry_prompt(scene, character):
    """
    Grounded modern mass entry shot
    Environment dominates, hero powerful but realistic
    """

    prompt = f"""
    ultra realistic cinematic wide shot,

    environment is the primary subject,
    real-world location, grounded realism,
    open terrain, road, vehicles, sky visible,
    environment occupies at least 70% of the frame,

    hero presence:
    {character['description']},
    hero stepping out of a vehicle,
    confident and intense body language,
    calm but dangerous expression,
    hero visible from thighs-up or full body,
    face visible but NOT dominating the frame,

    action:
    {scene['action']},

    background:
    {scene['background']},

    lighting:
    natural daylight,
    strong directional sunlight,
    realistic shadows,
    cinematic contrast without stylization,

    camera:
    wide cinematic lens,
    eye-level or slightly low angle,
    deep depth of field,

    ultra realistic movie still,
    modern Indian action cinema tone,
    natural colors,
    serious and grounded mood,

    16:9 aspect ratio,
    landscape framing,

    no fantasy,
    no mythology,
    no anime,
    no illustration,
    no close-up portrait,
    no stylized VFX
    """

    return prompt.strip()


def build_mass_entry_prompt(scene, character):
    """
    Grounded mass hero entry — realistic, emotional, environment-first
    """

    prompt = f"""
    ultra realistic cinematic wide shot,

    environment dominates the frame,
    real-world outdoor location,
    rain visible clearly across the scene,
    background textures readable,
    environment occupies at least 70% of the frame,

    hero:
    {character['description']},
    hero present with strong body language,
    hero NOT posing,
    hero NOT centered,
    hero seen from medium-long to full body,
    face visible but not the focus,

    action:
    {scene['action']},

    background:
    {scene['background']},

    lighting:
    natural overcast daylight,
    rain-diffused light,
    soft shadows,
    realistic contrast,

    camera:
    cinematic wide lens,
    eye-level framing,
    deep depth of field,

    grounded Indian action cinema look,
    natural colors,
    serious emotional tone,

    16:9 aspect ratio,
    landscape framing,

    no close-up,
    no portrait,
    no fantasy,
    no mythology,
    no anime,
    no illustration,
    no dramatic VFX
    """

    return prompt.strip()
