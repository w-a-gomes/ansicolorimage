#!/usr/bin/env python3
from PIL import Image, ImageEnhance
import warnings


class ImageColorMap(object):
    def __init__(
            self,
            url_image: str,
            height: int = 20,
            width: int = 40,
            contrast: float = 1.0,
            brightness: float = 1.0,
            show_background_color: bool = False,
            hide_foreground_character: bool = False,
            ascii_map: list = None):

        self.__url_image = url_image
        self.__height = height
        self.__width = width
        self.__contrast = contrast
        self.__brightness = brightness
        self.__show_background_color = show_background_color
        self.__hide_foreground_character = hide_foreground_character
        self.__ascii_lines = []
        self.__ascii_map = ascii_map if ascii_map else [
            ' ', '´', '.', ':', ';', 'i', '/', 'l', 'j', 'h',
            'N', 'S', 'k', 'W', 'M', 'G', '0', '@', '#', '#']

    @property
    def ascii_lines(self) -> list:
        if not self.__ascii_lines:
            self.__set_ascii_lines()
        return self.__ascii_lines

    def __set_ascii_lines(self):
        """
        print(im.format, im.size, im.mode)
        PPM (512, 512) RGB
        """
        # Image
        warnings.filterwarnings('ignore')  # Fix RGBA warning
        image = Image.open(self.__url_image, 'r')
        image = image.convert('RGB')

        # Resize
        image = image.resize(
            (self.__width, self.__height),
            Image.Resampling.BICUBIC)  # type: ignore

        # Adjust colors
        if self.__contrast != 1.0:
            contrast = ImageEnhance.Contrast(image)
            image = contrast.enhance(self.__contrast)
        if self.__brightness != 1.0:
            brightness = ImageEnhance.Brightness(image)
            image = brightness.enhance(self.__brightness)

        ascii_line = ''
        loop_count = 0
        line_count = 0
        for pixel in list(image.getdata()):
            if len(pixel) == 3:
                r, g, b = pixel
            else:
                r, g, b, _a = pixel

            # github.com/EbonJaeger/asciifyer
            pixel_brightness = ((0.2126 * r) + (0.7152 * g) + (0.0722 * b))

            ascii_str_index = int(
                    (pixel_brightness / 255.0) * (len(self.__ascii_map)))

            foreground_character = ' '
            if not self.__hide_foreground_character:
                foreground_character = self.__ascii_map[ascii_str_index]

            ascii_line += '{}{}'.format(
                self.rgb_to_ansi(r, g, b, self.__show_background_color),
                foreground_character)

            # Loop config
            if loop_count + 1 == self.__width:
                # Update line
                self.__ascii_lines.append(ascii_line + '\x1B[0m')
                line_count += 1

                # Reset
                ascii_line = ''
                loop_count = 0

            else:
                loop_count += 1

    @staticmethod
    def rgb_to_ansi(r: int, g: int, b: int, background: bool) -> str:
        return f"\x1b[{48 if background else 38};2;{r};{g};{b}m"


if __name__ == '__main__':
    pass
