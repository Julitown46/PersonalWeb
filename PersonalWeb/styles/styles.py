import reflex as rx
import PersonalWeb.styles.styles as styles
from enum import Enum

# Constants
MAX_WIDTH = "800px"

# Sizes
class Size(Enum):
    SMALL = "0.6em"
    MEDIUM = "1em"
    DEFAULT = "1.2em"
    LARGE = "2em"

# Styles
BASE_STYLE = {
    rx.button: {
        "width": "100%",
        "height": "100%",
        "cursor": "pointer",
        "display": "block",
        "padding": Size.MEDIUM.value,
        "border_radius": Size.DEFAULT.value,
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
)

button_title_style = dict(
    font_size=Size.DEFAULT.value,
)

button_body_style = dict(
    font_size=Size.MEDIUM.value,
)