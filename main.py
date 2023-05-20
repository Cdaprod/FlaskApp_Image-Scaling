# DOWNLOAD SRGAN Model from web
# place in root of foldee

import os
from PIL import Image
import torch
from torchvision.transforms import ToTensor, ToPILImage

model = torch.load('path_to_your_model.pt')  # Load your model
model.eval()

input_folder = 'path_to_input_folder'
output_folder = 'path_to_output_folder'

target_size = 3840  # Target size (for 4K resolution)

for filename in os.listdir(input_folder):
    if filename.endswith('.png') or filename.endswith('.jpg'):  # Check if the file is an image
        img = Image.open(os.path.join(input_folder, filename))  # Open the image file
        width, height = img.size
        scaling_factor = max(width, height) / target_size
        new_width = int(width / scaling_factor)
        new_height = int(height / scaling_factor)
        img = img.resize((new_width, new_height), Image.BICUBIC)  # Resize the image to maintain aspect ratio
        img_t = ToTensor()(img).unsqueeze(0)  # Convert the image to a tensor
        with torch.no_grad():
            upscaled_img_t = model(img_t)  # Upscale the image
        upscaled_img = ToPILImage()(upscaled_img_t.squeeze(0))  # Convert the tensor to an image
        upscaled_img.save(os.path.join(output_folder, filename))  # Save the upscaled image

print('Upscaling completed.')
