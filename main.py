import os
from utils import load_images, pixelate_image, apply_cartoon_effect, create_transition_frames, create_steady_frames

base_dir = os.getcwd()
folder_path = os.path.join(base_dir, 'paintings', 'ind')
name = os.path.join(base_dir, 'pixelated_hopper.gif')

images = load_images(folder_path= folder_path, desired_size=(1000, 200))
cartoon_images = [apply_cartoon_effect(pixelate_image(img, pixel_size = 8), levels= 7) for img in images]

all_frames = []
for i in range(len(cartoon_images) - 1):
    all_frames += create_transition_frames(cartoon_images[i], cartoon_images[i+1], steps= 20)
    all_frames += create_steady_frames(cartoon_images[i+1], steps=20) 

all_frames += create_transition_frames(cartoon_images[-1], cartoon_images[0], steps= 20)
all_frames[0].save(name, save_all=True, append_images=all_frames[1:], optimize=False, duration= 150, loop=0)
