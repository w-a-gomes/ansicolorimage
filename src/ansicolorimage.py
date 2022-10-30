#!/usr/bin/env python3
from PIL import Image, ImageEnhance
import warnings


class AnsiColorImage(object):
    """..."""
    def __init__(
            self,
            url_image: str,
            # Defaults
            brightness: float = 1.0,
            chars_map: list = None,
            contrast: float = 1.0,
            height: int = 20,
            hide_foreground_character: bool = False,
            show_background_color: bool = False,
            width: int = 40) -> None:
        """..."""
        self.__default_chars_map = [
            ' ', '´', '.', ':', ';', 'i', '/', 'l', 'j', 'h',
            'N', 'S', 'k', 'W', 'M', 'G', '0', '@', '#', '#']
        self.__ansi_lines = []
        self.__brightness = brightness
        self.__chars_map = chars_map if chars_map else self.__default_chars_map
        self.__contrast = contrast
        self.__height = height
        self.__hide_foreground_character = hide_foreground_character
        self.__show_background_color = show_background_color
        self.__url_image = url_image
        self.__width = width

        self.update_ascii_lines()

    @property
    def ansi_lines(self) -> list:
        """..."""
        return self.__ansi_lines

    @ansi_lines.setter
    def ansi_lines(self, ansi_lines: list) -> None:
        """..."""
        if ansi_lines:
            self.__ansi_lines = ansi_lines

    @property
    def brightness(self) -> float:
        """..."""
        return self.__brightness

    @brightness.setter
    def brightness(self, brightness: float) -> None:
        """..."""
        self.__brightness = brightness if brightness else 1.0

    @property
    def chars_map(self) -> list:
        """..."""
        return self.__chars_map

    @chars_map.setter
    def chars_map(self, chars_map: list) -> None:
        """..."""
        self.__chars_map = chars_map if chars_map else self.__default_chars_map

    @property
    def contrast(self) -> float:
        """..."""
        return self.__contrast

    @contrast.setter
    def contrast(self, contrast: float) -> None:
        """..."""
        self.__contrast = contrast if contrast else 1.0

    @property
    def height(self) -> int:
        """Get height in number of lines"""
        return self.__height

    @height.setter
    def height(self, height: int) -> None:
        """Set height in number of lines
        
        Use None to reset. Default is 20.

        :param height: number of lines
        """
        self.__height = height if height else 20

    @property
    def hide_foreground_character(self) -> bool:
        """..."""
        return self.__hide_foreground_character

    @hide_foreground_character.setter
    def hide_foreground_character(self, hide: bool) -> None:
        """..."""
        self.__hide_foreground_character = hide if hide else False

    @property
    def show_background_color(self) -> bool:
        """..."""
        return self.__show_background_color

    @show_background_color.setter
    def show_background_color(self, show: bool) -> None:
        """..."""
        self.__show_background_color = show if show else False

    @property
    def url_image(self) -> str:
        """..."""
        return self.__url_image

    @url_image.setter
    def url_image(self, url_image: str) -> None:
        """..."""
        if url_image:
            self.__url_image = url_image

    @property
    def width(self) -> int:
        """Get width in number of columns"""
        return self.__width

    @width.setter
    def width(self, width: int) -> None:
        """Set width in number of columns

        Use None to reset. Default is 40.

        :param width: number of columns
        """
        self.__width = width if width else 40

    def update_ascii_lines(self):
        # Image
        image = Image.open(self.__url_image, 'r')
        if image.mode != 'RGB':
            warnings.filterwarnings('ignore')  # Fix RGBA warning
            image = image.convert('RGB')

        # Resize
        h, w = image.size
        if h != self.__height or w != self.__width:
            image = image.resize(
                (self.__width, self.__height),
                Image.Resampling.BICUBIC)  # type: ignore

        # Adjust color
        if self.__contrast != 1.0:
            contrast = ImageEnhance.Contrast(image)
            image = contrast.enhance(self.__contrast)
        if self.__brightness != 1.0:
            brightness = ImageEnhance.Brightness(image)
            image = brightness.enhance(self.__brightness)

        # Map
        ascii_line = ''
        loop_count = 0
        line_count = 0
        for pixel in list(image.getdata()):
            # RGB
            if len(pixel) == 3:
                r, g, b = pixel
            else:
                r, g, b, _a = pixel

            # Foreground:
            #     set brightness to find ascii_map char index
            pixel_brightness = (  # brightness: github.com/EbonJaeger/asciifyer
                    (0.2126 * r) + (0.7152 * g) + (0.0722 * b))

            ascii_map_char_index = int(
                    (pixel_brightness / 255.0) * (len(self.__chars_map)))

            foreground_character = ' '
            if not self.__hide_foreground_character:
                foreground_character = self.__chars_map[ascii_map_char_index]

            # Background:
            #     \x1b[48... for background or \x1b[38... for hidden background
            bg_color = 48 if self.__show_background_color else 38
            ascii_line += '{}{}'.format(
                f'\x1b[{bg_color};2;{r};{g};{b}m',
                foreground_character)

            # Loop config
            if loop_count + 1 == self.__width:
                # Update line
                self.__ansi_lines.append(ascii_line + '\x1B[0m')
                line_count += 1

                # Reset
                ascii_line = ''
                loop_count = 0
            else:
                loop_count += 1


if __name__ == '__main__':
    pass
