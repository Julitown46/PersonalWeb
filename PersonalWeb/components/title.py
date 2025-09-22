import reflex as rx
import PersonalWeb.styles.styles as styles
from PersonalWeb.styles.colors import TextColor

def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        size="7",
        style=styles.title_style,
        color=TextColor.HEADER.value
    )