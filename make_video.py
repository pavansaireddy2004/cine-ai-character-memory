import os

from moviepy import (
    ImageClip,
    AudioFileClip,
    concatenate_videoclips
)

from moviepy.video.fx import FadeIn, FadeOut
from moviepy.audio.AudioClip import CompositeAudioClip
from moviepy.audio.fx import AudioLoop


# ==================================================
# 🎬 IMAGE ORDER (STORY FLOW)
# ==================================================
images = [
    "scene1_shot1_establishing.png",
    "scene1_shot2_medium.png",
    "scene1_shot3_mood.png",

    "scene2_shot1_establishing.png",
    "scene2_shot2_action.png",
    "scene2_shot3_emotion.png",

    "scene3_shot1_establishing.png",
    "scene3_shot2_interrogation.png",
    "scene3_shot3_pressure.png",

    "scene4_shot1_city_walk.png",
    "scene4_shot2_driving.png",
    "scene4_shot3_friend.png",

    "scene6_mass_hero.png",
    "scene9_the_end.png"
]

# ==================================================
# 🎞️ CREATE IMAGE CLIPS
# ==================================================
clips = []

for img in images:
    if os.path.exists(img):
        clip = (
            ImageClip(img)
            .with_duration(2.5)
            .with_effects([
                FadeIn(0.4),
                FadeOut(0.4)
            ])
        )
        clips.append(clip)
    else:
        print(f"⚠️ Missing image: {img}")

# ==================================================
# 🎬 COMBINE INTO FINAL VIDEO (IMPORTANT)
# ==================================================
final_video = concatenate_videoclips(clips, method="compose")


# ==================================================
# 🎵 AUDIO (BACKGROUND + VOICE OVER) — FINAL FIX
# ==================================================
from moviepy.audio.AudioClip import CompositeAudioClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.audio.AudioClip import concatenate_audioclips

bg_path = "background_music/bg_music.mp3"
voice_path = "background_music/voice_over.wav"

audio_layers = []

# ---------- BACKGROUND MUSIC ----------
if os.path.exists(bg_path):
    bg_music = AudioFileClip(bg_path)

    # repeat music to cover full video
    loops = int(final_video.duration // bg_music.duration) + 1
    bg_music = concatenate_audioclips([bg_music] * loops)

    # trim to exact duration
    bg_music = bg_music.subclipped(0, final_video.duration)

    # reduce volume
    bg_music = bg_music.with_volume_scaled(0.3)

    audio_layers.append(bg_music)

# ---------- VOICE OVER ----------
if os.path.exists(voice_path):
    voice = AudioFileClip(voice_path)
    voice = voice.with_volume_scaled(1.0)
    audio_layers.append(voice)

# ---------- MERGE AUDIO ----------
if audio_layers:
    final_audio = CompositeAudioClip(audio_layers)
    final_video = final_video.with_audio(final_audio)





# ==================================================
# 🎥 EXPORT FINAL VIDEO
# ==================================================
final_video.write_videofile(
    "final_story_video.mp4",
    fps=24,
    codec="libx264",
    audio_codec="aac"
)

print("✅ Final cinematic video created: final_story_video.mp4")
