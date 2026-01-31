from image_generator import generate_image_with_cache


def build_end_title_prompt():
    """
    FINAL END TITLE CARD
    """

    prompt = """
    cinematic end title card, final frame of a movie,

    environment:
    dark smoky background,
    faint remaining embers floating in the air,
    soft glow from distant dying fire,
    atmosphere of silence and closure,

    text:
    THE END,
    centered in frame,
    bold cinematic serif font,
    subtle gold or off-white lettering,
    slightly weathered texture,
    not glowing too much,

    lighting:
    very low light,
    soft ambient glow,
    no harsh highlights,

    camera:
    static shot,
    perfectly centered composition,

    ultra realistic cinematic frame,
    film grain,
    dramatic but minimal,
    emotional closure,

    16:9 aspect ratio,
    landscape,

    no characters,
    no faces,
    no action,
    no illustration,
    no anime,
    no logo,
    no watermark
    """

    return prompt.strip()


def main():
    prompt = build_end_title_prompt()
    generate_image_with_cache(prompt, "scene10_the_end.png")


if __name__ == "__main__":
    main()
