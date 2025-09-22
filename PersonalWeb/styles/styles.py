import reflex as rx
import PersonalWeb.styles.styles as styles
from enum import Enum
from PersonalWeb.styles.colors import Color, TextColor

# Constants
MAX_WIDTH = "800px"

# Sizes
class Size(Enum):
    SMALL = "0.6em"
    MEDIUM = "1em"
    DEFAULT = "1.2em"
    LARGE = "2em"
    XLARGE = "3.5em"
    XXLARGE = "4.5em"

#Stylesheets

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Nunito:wght@400;700&display=swap"
]

# Styles
BASE_STYLE = {
    "background_color": Color.BACKGROUND.value,
    "font_family": "Nunito, sans-serif",
    rx.button: {
        "width": "100%",
        "height": "100%",
        "cursor": "pointer",
        "display": "block",
        "padding": Size.MEDIUM.value,
        "border_radius": Size.DEFAULT.value,
        "background_color": Color.CONTENT.value,
        "_hover": {"background_color": Color.SECONDARY.value},
        "color": TextColor.HEADER.value,
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {},
        "cursor": "pointer",
    },
    rx.icon: {
        "width": styles.Size.LARGE.value,
        "height": styles.Size.LARGE.value,
        "align_self": "center",
    },
}

title_style = dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
    color=TextColor.HEADER.value
)

button_title_style = dict(
    font_size=Size.DEFAULT.value,
    color=TextColor.HEADER.value,
    font_weight="bold"
)

button_body_style = dict(
    font_size=Size.MEDIUM.value,
    color=TextColor.BODY.value
)