import streamlit as st
from prompt_engine import load_character, build_prompt
from image_generator import generate_image_with_cache

st.set_page_config(page_title="AI Character Memory", layout="wide")

st.title("🎬 AI Character Memory System")
st.write("Generate consistent character images across scenes")

character = load_character("hero")

scene_text = st.text_area(
    "Enter scene description",
    "Hero is running"
)

if st.button("Generate Image"):
    with st.spinner("Generating image..."):

        # 🔧 FIX: wrap text into a scene dictionary
        scene = {
            "action": scene_text,
            "background": "cinematic environment, realistic setting",
            "lighting": "dramatic cinematic lighting",
            "camera": "medium wide shot",
            "costume": "consistent hero outfit"
        }

        prompt = build_prompt(scene, character)
        output_path = "output.png"

        image = generate_image_with_cache(prompt, output_path)

    st.success("Image generated!")
    st.image(image, use_container_width=True)
