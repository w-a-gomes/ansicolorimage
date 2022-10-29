#!/usr/bin/env python3
import pathlib
import sys

base_dir = pathlib.Path(__file__).resolve().parent.parent
sys.path.append(base_dir.as_posix())
from src.ansicolorimage import AnsiColorImage


# /usr/share/pixmaps/neon.png
def neon_ex():
    img = AnsiColorImage(
        url_image=base_dir.as_posix() + '/examples/data/neon.png',
        contrast=1.3,
        brightness=0.85)
    for line in img.ansi_lines:
        print(line)


def python_ex():
    img = AnsiColorImage(
        url_image=base_dir.as_posix() + '/examples/data/python.png')
    for line in img.ansi_lines:
        print(line)


def debian_ex():
    img = AnsiColorImage(
        url_image=base_dir.as_posix() + '/examples/data/debian.png',
        contrast=1.2,
        brightness=0.95,
        chars_map=[' ', ' ', '*', '&'] + ['#'] * 20)
    for line in img.ansi_lines:
        print(line)


def poe_ex():
    poem = """
    
    The Raven
    
    ...
     Then this ebony bird beguiling my sad fancy into smiling,
    By the grave and stern decorum of the countenance it wore,
    “Though thy crest be shorn and shaven, thou,” I said, “art sure no craven,
    Ghastly grim and ancient Raven wandering from the Nightly shore—
    Tell me what thy lordly name is on the Night’s Plutonian shore!”
                Quoth the Raven “Nevermore.”
    ...
    But the Raven still beguiling all my fancy into smiling,
    Straight I wheeled a cushioned seat in front of bird, and bust and door;
        Then, upon the velvet sinking, I betook myself to linking
        Fancy unto fancy, thinking what this ominous bird of yore—
    What this grim, ungainly, ghastly, gaunt, and ominous bird of yore
                Meant in croaking “Nevermore.”
    ...
    
    
    (By Edgar Allan Poe)
    
    """
    img = AnsiColorImage(
        url_image=base_dir.as_posix() + '/examples/data/poe.jpg',
        height=25,
        width=50,
        show_background_color=True,
        hide_foreground_character=True)
    for text_line, img_line in zip(poem.split('\n'), img.ansi_lines):
        print(img_line, text_line)


def kali_ex():
    img = AnsiColorImage(
        url_image=base_dir.as_posix() + '/examples/data/kali.jpg',
        height=30,
        width=60,
        contrast=1.2,
        brightness=0.95,
        chars_map=['0', '0'] + ['1'] * 25)
    for line in img.ansi_lines:
        print(line)


if __name__ == '__main__':
    neon_ex()
    python_ex()
    debian_ex()
    poe_ex()
    kali_ex()
