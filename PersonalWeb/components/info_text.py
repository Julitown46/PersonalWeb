import reflex as rx
from PersonalWeb.styles.styles import Size as Size

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(title, as_="span", font_size=Size.MEDIUM.value, font_weight="bold", color="blue"),
        f" {body}", font_size=Size.MEDIUM.value,
    )