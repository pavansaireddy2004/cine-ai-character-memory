import streamlit as st
from prompt_engine import load_character, build_prompt
from image_generator import generate_image

st.set_page_config(page_title="AI Character Memory", layout="wide")

st.title("🎬 AI Character Memory System")
st.write("Generate consistent character images across scenes")

# Load character
character = load_character("hero")

# User input
scene_text = st.text_area(
    "Enter scene description",
    "Hero standing inside a police station during investigation"
)

if st.button("Generate Image"):
    with st.spinner("Generating image..."):
        prompt = build_prompt(scene_text, character)
        output_path = "output.png"
        generate_image(prompt, output_path)

    st.success("Image generated!")
    st.image(output_path, use_container_width=True)
