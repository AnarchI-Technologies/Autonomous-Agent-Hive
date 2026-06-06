import requests
import base64
import json
import os
from datetime import datetime

API_URL = "http://127.0.0.1:7860/sdapi/v1/txt2img"

OUTPUT_DIR = r"C:\Lyra_Voss\RAW_Generations"
LOG_DIR = r"C:\Lyra_Voss\METADATA_LOGS"

prompt = "YOUR LYRA VOSS MASTER PROMPT HERE"
negative_prompt = "low quality, blurry, bad anatomy"

payload = {
    "prompt": prompt,
    "negative_prompt": negative_prompt,
    "steps": 30,
    "cfg_scale": 7,
    "width": 768,
    "height": 1024,
    "sampler_name": "DPM++ 2M Karras",
    "seed": -1
}

response = requests.post(API_URL, json=payload)
data = response.json()

image_data = data["images"][0]
info = json.loads(data["info"])

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"lyra_{timestamp}.png"

image_path = os.path.join(OUTPUT_DIR, filename)
log_path = os.path.join(LOG_DIR, filename.replace(".png", ".json"))

# save image
with open(image_path, "wb") as f:
    f.write(base64.b64decode(image_data))

# save metadata
with open(log_path, "w") as f:
    json.dump(info, f, indent=4)

print("Saved:", filename)