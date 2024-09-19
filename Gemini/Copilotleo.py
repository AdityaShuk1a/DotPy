
# Import necessary libraries
import torch
from diffusers import StableDiffusionPipeline

# Load the Stable Diffusion model (download it first if you haven't)
model_id = "CompVis/stable-diffusion-v1-4"  # Choose your desired model
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)

# Move the model to the GPU if available
if torch.cuda.is_available():
  pipe = pipe.to("cuda")

# Define your prompt
prompt = "A photorealistic image of a cat wearing a hat"

# Generate the image
image = pipe(prompt).images[0]

# Save the generated image
image.save("generated_image.png")

print("Image saved to 'generated_image.png'")