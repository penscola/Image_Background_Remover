#!/usr/bin/env python3
from rembg import remove
from PIL import Image

input_path = "unremoved_bg/images.png"
output_path = "removed_bg/images.png"

image_input = Image.open(input_path)
output = remove(image_input)
output.save(output_path)
