import os
from utils import load_images, pixelate_image, apply_cartoon_effect, create_transition_frames

base_dir = os.getcwd()
folder_path = os.path.join(base_dir, 'Banner', 'paintings')
img_folder = os.path.join(folder_path, 'ind')
name = os.path.join(folder_path, 'pixelated_hopper.gif')

images = load_images(img_folder, desired_size=(1000, 200))
cartoon_images = [apply_cartoon_effect(pixelate_image(img, pixel_size = 5), levels= 10) for img in images]

all_frames = []
for i in range(len(cartoon_images) - 1):
    all_frames += create_transition_frames(cartoon_images[i], cartoon_images[i+1], steps=15)

all_frames += create_transition_frames(cartoon_images[-1], cartoon_images[0], steps=15)
all_frames[0].save(name, save_all=True, append_images=all_frames[1:], optimize=False, duration=150, loop=0)
