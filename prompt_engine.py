import json

def load_character(character_name="hero"):
    """
    Loads character data from character_memory.json
    """
    with open("character_memory.json", "r") as f:
        data = json.load(f)

    return data[character_name]


def build_prompt(scene, character):
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

    lighting: {scene['lighting']},

    cinematic wide shot,
    subject placed using rule of thirds,
    visible environment around the character,
    camera positioned as {scene['camera']},

    ultra realistic cinematic movie still,
    full color photography,
    natural skin tones,
    realistic color grading,
    modern digital cinema look,
    16:9 aspect ratio, landscape framing,

    --no studio lighting,
    --no plain background,
    --no portrait photography,
    --no headshot,
    --no close-up only face,
    --no black and white,
    --no monochrome,
    --no sketch,
    --no illustration,
    --no anime,
    --no comic style
    """
    return prompt.strip()


