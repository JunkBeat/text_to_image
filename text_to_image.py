import argparse
from PIL import Image, ImageDraw, ImageFont

def split_text(font, text, max_width):
    lines = []
    paragraphs = text.split('\n') 

    for paragraph in paragraphs:
        words = paragraph.split()
        line = ''
        while words:
            if line:
                test_line = line + ' ' + words[0]
            else:
                test_line = words[0]

            if font.getsize(test_line)[0] <= max_width:
                line = test_line
                words.pop(0)
            else:
                lines.append(line)
                line = ''
        
        if line:
            lines.append(line)

    return lines

def create_image(font_path, font_size, text, max_width, max_height, alignment):
    while True:
        font = ImageFont.truetype(font_path, font_size)
        lines = split_text(font, text, max_width)
        image_height = sum(font.getsize(line)[1] for line in lines if line)
        
        if image_height <= max_height:
            break
        else:
            font_size -= 5  

    image = Image.new('RGBA', (max_width, max_height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    y_text = 0  
    for line in lines:
        if line:  
            line_width, line_height = font.getsize(line)
            if alignment == 'center':
                x_text = (max_width - line_width) / 2 
            else:  # left alignment
                x_text = 0
            draw.text((x_text, y_text), line.strip(), font=font, fill=(0, 0, 0))
            y_text += line_height
        else:
            y_text += font.getsize('A')[1] 

    return image

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate an image with text")
    parser.add_argument('--font-size', type=int, default=80, help='Font size for the text')
    parser.add_argument('--text', type=str, default='This is an example text', help='Text to be rendered')
    parser.add_argument('--alignment', type=str, choices=['left', 'center'], default='center', help='Text alignment (upper left or upper center)')
    parser.add_argument('--font-path', type=str, default='1.ttf', help='Path to the font file')
    parser.add_argument('--width', type=int, default=1700, help='Width of the image')
    parser.add_argument('--height', type=int, default=600, help='Height of the image')
    args = parser.parse_args()

    image = create_image(
        args.font_path, 
        args.font_size, 
        args.text, 
        args.width, 
        args.height, 
        args.alignment
    )

    image.save('text.png')
