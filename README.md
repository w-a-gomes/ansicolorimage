# ansicolorimage
Python lib to create figures with text characters and ANSI colors from an image file 


https://github.com/w-a-gomes/ansicolorimage

Minimal example.

```python
img = AnsiColorImage(url_image='python.png')
for line in img.ansi_lines:
    print(line)
```
![Image](data/screen-python.png "screenshot")

In addition to the basic adjustments like setting the dimensions and displaying the background color, you can also adjust the brightness and contrast for a better result.
The `float` '**1.3**' is like **30%** and '**0.85**' is like **-15%**.

```python
img = AnsiColorImage(url_image='neon.png', contrast=1.3, brightness=0.85)
for line in img.ansi_lines:
    print(line)
```

![Image](data/screen-neon.png "screenshot")

Each item represents a line, making it easy to enter parallel information.

```python
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
    url_image='poe.jpg',
    height=25,
    width=50,
    show_background_color=True,
    hide_foreground_character=True)

for text_line, img_line in zip(poem.split('\n'), img.ansi_lines):
    print(img_line, text_line)
```
![Image](data/screen-poe.png "screenshot")

Choosing the character map helps to achieve conceptual aesthetic results. For example, using 0 and 1 alluding to hacking in Kali's logo.
Work with a gradient of around **20** characters.

```python
img = AnsiColorImage(
    url_image='kali.jpg',
    height=30,
    width=60,
    contrast=1.2,
    brightness=0.95,
    chars_map=['0', '0'] + ['1'] * 25)
for line in img.ansi_lines:
    print(line)
```
![Image](data/screen-kali.png "screenshot")
