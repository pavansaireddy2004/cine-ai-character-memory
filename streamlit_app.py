import streamlit as st
from prompt_engine import load_character, build_prompt
from image_generator import generate_image_with_cache

st.set_page_config(page_title="AI Character Memory", layout="wide")

st.title("🎬 AI Character Memory System")
st.write("Generate consistent character images across scenes")

# Load character
character = load_character("hero")

# User input
scene_text = st.text_area(
    "Enter scene description",
    "Hero running through a rainy street at night"
)

if st.button("Generate Image"):
    with st.spinner("Generating image..."):

        scene = {
            "action": scene_text,
            "background": "cinematic realistic environment",
            "lighting": "dramatic cinematic lighting",
            "camera": "wide cinematic shot",
            "costume": "consistent with character design"
        }

        prompt = build_prompt(scene, character)
        output_path = "output.png"

        image = generate_image_with_cache(prompt, output_path)

    st.success("Image generated!")
    st.image(image, use_container_width=True)
