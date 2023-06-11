#!/usr/bin/env python3
from rembg import remove
from PIL import Image

input_path = "images.jpeg"
output_path = "images.jpeg"

image_input = Image.open(input_path)
output = remove(image_input)
output.save(output_path)
