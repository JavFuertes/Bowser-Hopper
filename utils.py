import os
import numpy as np
from PIL import Image, ImageFilter

def load_images(folder_path, desired_size=(500, 300)):
    images = []
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            img = Image.open(os.path.join(folder_path, filename))
            img = crop_to_aspect(img, desired_width=desired_size[0], desired_height=desired_size[1])
            images.append(img)
    return images

def crop_to_aspect(image, desired_width=500, desired_height=300):
    """ Crop the image to the desired aspect ratio without stretching it. """
    original_width, original_height = image.size
    target_ratio = desired_width / desired_height
    original_ratio = original_width / original_height

    if target_ratio > original_ratio:
        new_height = int(original_width / target_ratio)
        offset = (original_height - new_height) // 2
        resized_image = image.crop((0, offset, original_width, original_height - offset))
    else:
        # Image is too wide: cut off the sides
        new_width = int(original_height * target_ratio)
        offset = (original_width - new_width) // 2
        resized_image = image.crop((offset, 0, original_width - offset, original_height))

    return resized_image.resize((desired_width, desired_height), Image.ANTIALIAS)

def pixelate_image(image, pixel_size=15):
    """ Create a pixelated effect on the image by resizing down and then up. """
    image_small = image.resize((image.width // pixel_size, image.height // pixel_size), Image.BILINEAR)
    return image_small.resize(image.size, Image.NEAREST)

def apply_cartoon_effect(image, levels=5):
    """ Apply a cartoon effect to the image using edge enhancement and quantization. """
    
    quantized = image.quantize(colors=levels, method=0)
    converted_img = quantized.convert('RGB')
    edge_enhanced = converted_img.filter(ImageFilter.EDGE_ENHANCE_MORE)

    return edge_enhanced

def create_transition_frames(start_img, end_img, steps=10):
    """ Generate frames that transition from start_img to end_img. """
    start_pixels = np.array(start_img)
    end_pixels = np.array(end_img)
    frames = []
    for t in range(steps):
        temp_pixels = (1 - t / steps) * start_pixels + (t / steps) * end_pixels
        temp_img = Image.fromarray(np.uint8(temp_pixels))
        frames.append(temp_img)
    return frames


