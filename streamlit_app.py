import streamlit as st
import json
import os
from prompt_engine import load_character, build_prompt
from image_generator import generate_image_with_cache

# ==================================================
# 🎛️ STREAMLIT CONFIG
# ==================================================
st.set_page_config(
    page_title="AI Character Memory (Hybrid Mode)",
    layout="wide"
)

st.title("🎬 AI Character Memory — Hybrid Mode")
st.caption(
    "• Simple text OR director-style description"
)

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
# 🔍 SMART KEYWORD MATCH (HYBRID)
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
# ✍️ USER INPUT
# ==================================================
user_input = st.text_area(
    "Describe the scene (simple OR director-style):",
    placeholder=(
        "Example:\n"
        "Hero running through heavy rain at night, wide shot, "
        "stormy background, dramatic lighting"
    ),
    height=140
)

reuse_images = st.checkbox(
    "Reuse existing images",
    value=True
)

# ==================================================
# 🎬 ACTION BUTTON
# ==================================================
if st.button("Generate / Load Image", type="primary"):
    if not user_input.strip():
        st.warning("Please enter a scene description.")
    else:
        with st.spinner("Processing scene..."):

            # 🔍 Try keyword-based recall
            matched_image, match_score = find_matching_image(user_input)

            if reuse_images and matched_image and os.path.exists(matched_image):
                st.image(matched_image, use_container_width=True)

            else:
                st.info("🎨 No strong match found — generating new image")

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
                st.caption("⚠️ New image generated (credits used)")


st.divider()
st.subheader("🎬 Story Preview Video")

video_path = "videos/final_story_video.mp4"

if os.path.exists(video_path):
    st.video(video_path)
    with open(video_path, "rb") as file:
        st.download_button(
            label="⬇️ Download Story Video",
            data=file,
            file_name="final_story_video.mp4",
            mime="video/mp4"
        )
else:
    st.warning("Story video not found.")


# ==================================================
# 📘 HELP SECTION
# ==================================================
with st.expander("ℹ️ How Hybrid Mode Works"):
    st.markdown(
        """
**This app understands BOTH:**

### 🧑‍💻 Simple input
`hero running`

### 🎥 Director-style input
`Hero walking through stormy rain, wide angle shot, low camera`

If keywords match existing scenes → **image is reused**  
If no match → **new image is generated once**

You stay in control of credits.
        """
    )