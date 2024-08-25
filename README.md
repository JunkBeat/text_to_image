# Text-to-Image Generator

This utility generates an image with text using the Python Pillow library. The script allows you to specify the text, font, alignment, and dimensions of the output image.

## Installation

Before using the utility, make sure you have Python installed. You also need to install the Pillow library if it's not already installed:

```bash
pip install Pillow
```

## Usage
You can run the script directly from the command line with various options:
```bash
python text_to_image.py --font-path "path/to/font.ttf" --width 1920 --height 1080 --font-size 100 --text "Your custom text" --alignment center
```

## Command-line Arguments
- --font-size: Font size for the text (default: 80).
- --text: The text to be rendered in the image (default: "This is an example text").
- --alignment: Text alignment, either left or center (default: center).
- --font-path: Path to the font file to be used (default: "1.ttf").
- --width: Width of the generated image (default: 1700).
- --height: Height of the generated image (default: 600).
