# Bowser Hopper

![Pixelated_hopper](pixelated_hopper.gif)

## Description

Edward Hopper (1882-1967) was an iconic American painter known for capturing the solitude and alienation inherent in modern life. His most famous piece, **Nighthawks**, showcases people in a diner late at night, close yet distant in their personal bubbles, a perfect metaphor for modern isolation.

Hopper was a quiet guy who liked to observe. His personal life, especially his experiences in New York City and his introspective nature, heavily influenced his art. Edward Hopper's personal life, particularly his complex relationship with his wife Josephine Nivison, profoundly influenced his art. Josephine, also an artist and his frequent model, embodied the figures often depicted in Hopper's paintings. Their reclusive lifestyle and the emotional dynamics of their marriage—marked by mutual artistic passion despite frequent conflicts—deeply informed his themes of introspection. This connection fostered Hopper's exploration of alienation and the human condition, echoing through his use of light, shadow, and architectural forms in his artwork.

Hopper’s paintings, such as **Nighthawks**, reveal the quiet, often overlooked moments of personal solitude that saturate American life. His art not only critiques the urban experience but also explores deeper emotions like melancholy, yearning, and introspection. This exploration resonates with modern audiences, reflecting ongoing issues of connectivity, psychological impact of urban environments, and the paradoxical loneliness of crowded spaces. His legacy continues to inspire and provoke thought about the architecture of loneliness and the intimate moments of human experience amidst the ever-present crowd.

Today, Edward Hopper's themes of solitude and disconnection still resonate, now more than ever with our daily lives dominated by computers. The rise of augmented reality and the creation of online personas on social media have introduced new ways to escape reality, which often leads to superficial connections. In this context, the `Bowser Hopper` project aims to produce pixelated banners that not only reflect the ongoing issues of urban life as seen through Hopper's eyes but also adapt these themes for the modern digital era. This artistic endeavor bridges the gap between Hopper’s time-tested insights and the contemporary landscape shaped by digital technology.

## Use

Make use of this repo's main.py file and define your parameters to your liking 

```python
folder_path = os.path.join(base_dir, 'paintings', 'ind')
name = os.path.join(base_dir, 'pixelated_hopper.gif')

images = load_images(folder_path= folder_path, desired_size=(1000, 200))
cartoon_images = [apply_cartoon_effect(pixelate_image(img, pixel_size = 5), levels= 10) for img in images]

all_frames = []
for i in range(len(cartoon_images) - 1):
    all_frames += create_transition_frames(cartoon_images[i], cartoon_images[i+1], steps=15)

all_frames += create_transition_frames(cartoon_images[-1], cartoon_images[0], steps=15)
all_frames[0].save(name, save_all=True, append_images=all_frames[1:], optimize=False, duration=150, loop=0)
```

Make sure to fork and share any ideas!