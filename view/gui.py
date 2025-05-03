"""
Contains settings to customize the GUI view
"""

colors = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "green": (0, 200, 0),
    "red": (200, 0, 0),
    "grey": (200, 200, 200),
}

style_settings = {
    "window_width": 800,
    "window_height": 600,
    "window_caption": "Type Racer",
    "font_path": "view/fonts/Hack-Regular.ttf",  # Must be monospaced
    "font_size": 32,
    "background_color": colors["black"],
    "prompt_text_color": colors["grey"],
    "typed_text_color": (255, 255, 255),
    "red_line": (255, 0, 0)
}
