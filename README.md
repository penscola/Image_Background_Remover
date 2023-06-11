### Background remover

#### 1. Importing the Required Libraries:
To get started, we need to import the necessary libraries. We import `remove` from the `rembg` library and `Image` from the `PIL` library.

```
from rembg import remove
from PIL import Image
```

#### 2. Defining the Input and Output Paths:
Next, we define the paths for the input and output images. In the given code snippet, “Input_Path” and “Output_Path” are placeholders. You should replace them with the actual paths to your input and output image files.

```
input_path = “path/to/input/image.png”
output_path = “path/to/output/image.png”
```

Ensure that you provide the correct file extension, such as “.png”, “.jpg”, or “.jpeg”, depending on the format of your images.

#### 3. Opening the Input Image:
We use the `Image.open()` method from the PIL library to open the input image. The `Image.open()` method reads the image file located at the specified input path and returns an Image object.

`image_input = Image.open(input_path)`

#### 4. Removing the Background:
The `remove()` function from the Rembg library is the core component that performs the background removal. We pass the `image_input` object, which represents the input image, as an argument to the `remove()` function.

`output = remove(image_input)`

The `remove()` function processes the image and returns a new image with the background removed. This new image is stored in the `output` variable.

#### 5. Saving the Output Image:
Finally, we use the `save()` method from the PIL library to save the output image to the specified output path. The `save()` method takes the output path as an argument.

`output.save(output_path)`

### How to run it
```
./app.py
```