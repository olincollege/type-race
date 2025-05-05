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
    # Window settings
    "window_width": 800,
    "window_height": 600,
    "window_caption": "Type Racer",
    # Background
    "background_color": colors["black"],
    # Text
    "font_path": "view/fonts/Hack-Regular.ttf",  # Must be monospaced
    "font_size": 32,
    "text_color": colors["grey"],
    "alternate_text_color": colors["red"],
    # Cursor
    "cursor_color": colors["white"],
    # Underlines
    "mistake_underline": colors["red"],
    "correct_underline": colors["white"],
}
