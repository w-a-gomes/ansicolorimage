#!/usr/bin/env python3
import pathlib
import sys

base_dir = pathlib.Path(__file__).resolve().parent.parent
sys.path.append(base_dir.as_posix())
from src.ansicolorimage import ImageColorMap

# /usr/share/pixmaps/neon.png
img = ImageColorMap(
    url_image=base_dir.as_posix() + '/examples/data/neon.png',
    contrast=1.3,
    brightness=0.85)
for item in img.ascii_lines:
    print(item)

img = ImageColorMap(url_image=base_dir.as_posix() + '/examples/data/tux.png')
for item in img.ascii_lines:
    print(item)

img = ImageColorMap(
    url_image=base_dir.as_posix() + '/examples/data/debian.png',
    contrast=1.2,
    brightness=0.95,
    ascii_map=[' ', ' ', '*', '&'] + ['#'] * 20)
for item in img.ascii_lines:
    print(item)

img = ImageColorMap(
    url_image=base_dir.as_posix() + '/examples/data/poe.png',
    show_background_color=True,
    hide_foreground_character=True)
for item in img.ascii_lines:
    print(item)
