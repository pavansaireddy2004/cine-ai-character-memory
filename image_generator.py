import requests
import os
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO

# Load environment variables
load_dotenv()

API_KEY = os.getenv("HF_API_KEY")

if not API_KEY:
    raise Exception("HF_API_KEY not found in .env file")

# ✅ CORRECT Hugging Face router URL
API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

def generate_image(prompt, output_path):
    payload = {
        "inputs": prompt,
        "parameters": {
            # ✅ 16:9 cinematic resolution
            "width": 1344,
            "height": 768,

            # ✅ Stronger scene adherence
            "guidance_scale": 8.5,

            # ✅ More realism (don’t go above 50)
            "num_inference_steps": 40,



            # ✅ VERY IMPORTANT: negative prompts
            "negative_prompt": (
                "black and white, monochrome, grayscale, "
                "studio portrait, plain background, empty background, "
                "headshot, face only, close up face, cropped face, "
                "blurred background, bokeh background, "
                "extra people, duplicate person, twin, clone, "
                "cartoon, illustration, painting, anime, "
                "over smooth skin, plastic skin, unrealistic face"
            )
        }
    }

    print("Generating image...")
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"API Error {response.status_code}: {response.text}")

    image = Image.open(BytesIO(response.content))
    image.save(output_path)
    print(f"Image saved as {output_path}")


