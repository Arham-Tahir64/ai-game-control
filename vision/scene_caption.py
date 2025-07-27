from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load BLIP
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# Load image and crop center (remove UI)
image = Image.open("cod_ss4.png").convert("RGB")
width, height = image.size
crop_box = (width * 0.2, height * 0.25, width * 0.8, height * 0.85)
cropped = image.crop(crop_box)

# Generate caption
inputs = processor(cropped, return_tensors="pt").to(device)
output = model.generate(**inputs)
caption = processor.decode(output[0], skip_special_tokens=True)

print("🧠 Scene Caption:", caption)
