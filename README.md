# Image Upscaling with SRGAN

This project uses a Super-Resolution Generative Adversarial Network (SRGAN) to upscale images while maintaining their aspect ratio. The script processes all images in an input folder and saves the upscaled images in an output folder.

## Requirements

- Python 3.7 or later
- PyTorch
- Pillow
- SRGAN

## Usage

1. Place your images in the input folder.
2. Run the script with the command `python upscale.py`.
3. The upscaled images will be saved in the output folder.

## Customization

You can customize the script by modifying the following variables at the beginning of the script:

- `model`: The path to your SRGAN model.
- `input_folder`: The path to the folder containing the images you want to upscale.
- `output_folder`: The path to the folder where you want to save the upscaled images.
- `target_size`: The size of the larger dimension (width or height) of the upscaled image.

## Notes

This script uses bicubic interpolation for resizing the images before upscaling. Depending on your specific requirements, you might want to use a different method.

Also, please note that this script assumes that your SRGAN model can handle images of any size. If your model requires a specific input size or other preprocessing steps, you will need to adjust the script accordingly.

## License

This project is licensed under the terms of the MIT license.
