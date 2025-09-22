import reflex as rx
from PersonalWeb.styles.styles import Size as Size
from PersonalWeb.styles.styles import Color, TextColor

def navbar() -> rx.Component:
    return rx.hstack(
        rx.image(
            src="logo.png",
            height=Size.XXLARGE.value,
            width=Size.XXLARGE.value,
            alt="Logo",
        ),
        rx.text(
            "Welcome to my Personal Website!",
            color=Color.PRIMARY.value,
            ),
            bg=Color.CONTENT.value,
            padding_x=Size.LARGE.value,
            padding_y=Size.DEFAULT.value,
            z_index="999",
            top="0",
            font_size=Size.DEFAULT.value,
            align="center",
    )