#!/usr/bin/env python3
import pathlib
import sys
import os
import time

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

    print(
        'accent_color: '
        f'\x1b[38;2;{img.image_accent_color}m{img.image_accent_color}\x1B[0m')


def python_ex():
    img = AnsiColorImage(
        url_image=base_dir.as_posix() + '/examples/data/python.png')
    for line in img.ansi_lines:
        print(line)
    print(
        'accent_color: '
        f'\x1b[38;2;{img.image_accent_color}m{img.image_accent_color}\x1B[0m')


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
        print(
            img_line,
            f'\x1b[38;2;{img.image_accent_color}m{text_line}\x1B[0m')

    # print(
    #     'accent_color: '
    #     f'\x1b[38;2;{img.image_accent_color}m{img.image_accent_color}\x1B[0m')


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

    print(
        'accent_color: '
        f'\x1b[38;2;{img.image_accent_color}m{img.image_accent_color}\x1B[0m')


def gif_ex():
    img_frames = os.listdir(base_dir.as_posix() + '/examples/data/frames/')
    img_frames.sort()
    images = [
        AnsiColorImage(
            url_image=base_dir.as_posix() + '/examples/data/frames/' + fr,
            height=25,
            width=85)
        for fr in img_frames]

    for image in images * 5:
        time.sleep(0.2)
        os.system('clear')

        for line in image.ansi_lines:
            print(line)
        print(
            'accent_color: '
            f'\x1b[38;2;{image.image_accent_color}m{image.image_accent_color}'
            '\x1B[0m')


def accent_color():
    img = AnsiColorImage(
        url_image=base_dir.as_posix() + '/examples/data/debian.png',
        contrast=1.2,
        brightness=0.95,
        chars_map=[' ', ' ', '*', '&'] + ['#'] * 20)
    for line in img.ansi_lines:
        print(line)

    print(
        'accent_color: '
        f'\x1b[38;2;{img.image_accent_color}m{img.image_accent_color}\x1B[0m')

    img.image_accent_color = '85;170;0'
    print(
        'accent_color: '
        f'\x1b[38;2;{img.image_accent_color}m{img.image_accent_color}\x1B[0m')

    img.image_accent_color = None
    print(
        'accent_color: '
        f'\x1b[38;2;{img.image_accent_color}m{img.image_accent_color}\x1B[0m')

    img.url_image = base_dir.as_posix() + '/examples/data/neon.png'
    img.update_ascii_lines()
    print(
        'accent_color: '
        f'\x1b[38;2;{img.image_accent_color}m{img.image_accent_color}\x1B[0m')


if __name__ == '__main__':
    # gif_ex()
    neon_ex()
    python_ex()
    debian_ex()
    poe_ex()
    kali_ex()
    # accent_color()
