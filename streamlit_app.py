import streamlit as st
import json
import os
from prompt_engine import load_character, build_prompt
from image_generator import generate_image_with_cache

# ==================================================
# 🎛️ STREAMLIT CONFIG
# ==================================================
st.set_page_config(
    page_title="CINE PERSONA - AI Character Memory",
    layout="wide"
)

# ==================================================
# 🎨 CINEMATIC UI STYLES (SAFE)
# ==================================================
st.markdown("""
<style>
html, body, [class*="css"] {
    background-color: #0e0f13;
    color: #e6e6e6;
    font-family: 'Inter', sans-serif;
}

.main-title {
    font-size: 44px;
    font-weight: 800;
    margin-bottom: 4px;
}

.subtitle {
    color: #9aa0a6;
    margin-bottom: 28px;
}

.card {
    background: linear-gradient(180deg, #15161c, #0f1014);
    border-radius: 18px;
    padding: 24px;
    margin-bottom: 28px;
    box-shadow: 0 0 0 1px rgba(255,255,255,0.05);
}

textarea {
    background-color: #0f1014 !important;
    border-radius: 14px !important;
}

.stButton>button {
    background: linear-gradient(135deg, #ff4b4b, #ff1f1f);
    color: white;
    border-radius: 14px;
    height: 52px;
    font-size: 16px;
    font-weight: 700;
    border: none;
}

.stButton>button:hover {
    transform: scale(1.02);
    transition: 0.2s;
}

video {
    border-radius: 16px;
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# 🎬 HEADER
# ==================================================
st.markdown('<div class="main-title">🎬 CINE PERSONA</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI Character Memory for Filmmakers & Creators</div>', unsafe_allow_html=True)

# ==================================================
# 📦 LOAD CHARACTER
# ==================================================
character = load_character("hero")

# ==================================================
# 📂 LOAD SCENE KEYWORDS JSON
# ==================================================
@st.cache_data
def load_scene_keywords():
    with open("scene_keywords.json", "r") as f:
        return json.load(f)

scene_data = load_scene_keywords()

# ==================================================
# 🔍 SMART KEYWORD MATCH
# ==================================================
def find_matching_image(user_text: str):
    text = user_text.lower()
    best_match = None
    highest_score = 0

    for scene in scene_data.values():
        score = 0
        for keyword in scene["keywords"]:
            if keyword.lower() in text:
                score += 1

        if score > highest_score:
            highest_score = score
            best_match = scene

    if best_match and highest_score > 0:
        return best_match["image"], highest_score

    return None, 0

# ==================================================
# 🎥 INPUT CARD
# ==================================================
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    user_input = st.text_area(
        "🎥 Describe the scene",
        placeholder="Hero running through heavy rain at night, wide shot, stormy background, dramatic lighting",
        height=150
    )

    col1, col2 = st.columns([1, 2])
    with col1:
        reuse_images = st.checkbox("Reuse existing images", value=True)
    with col2:
        generate = st.button("🎨 Generate / Load Image")

    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# 🖼️ IMAGE OUTPUT
# ==================================================
if generate:
    if not user_input.strip():
        st.warning("Please enter a scene description.")
    else:
        with st.spinner("🎬 Processing scene..."):
            matched_image, match_score = find_matching_image(user_input)

            if reuse_images and matched_image and os.path.exists(matched_image):
                st.success("✅ Loaded from character memory")
                st.image(matched_image, use_container_width=True)
            else:
                st.info("🎨 Generating new cinematic frame")

                prompt = build_prompt(
                    {
                        "action": user_input,
                        "background": user_input,
                        "lighting": "cinematic lighting",
                        "camera": "wide cinematic shot",
                        "costume": "consistent with hero identity"
                    },
                    character
                )

                output_path = "generated_from_streamlit.png"
                image = generate_image_with_cache(prompt, output_path)
                st.image(image, use_container_width=True)

# ==================================================
# 🎞️ STORY VIDEO SECTION
# ==================================================
st.divider()
st.markdown("## 🎞️ Story Preview")

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    video_path = "videos/final_story_video.mp4"

    if os.path.exists(video_path):
        st.video(video_path)
        with open(video_path, "rb") as f:
            st.download_button(
                "⬇️ Download Final Story Video",
                data=f,
                file_name="cine_persona_story.mp4",
                mime="video/mp4"
            )
    else:
        st.warning("Story video not found.")

    st.markdown('</div>', unsafe_allow_html=True)

# ==================================================
# 📘 HELP
# ==================================================
with st.expander("ℹ️ How CINE PERSONA Works"):
    st.markdown("""
- Type **simple text** or **director-style instructions**
- System checks **character memory**
- Existing images are reused (no credits)
- New scenes generate once and are saved
- Preview the **full story video** instantly
    """)
