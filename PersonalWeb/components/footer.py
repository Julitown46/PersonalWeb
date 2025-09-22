import reflex as rx
import datetime
from PersonalWeb.styles.styles import Size as Size
from PersonalWeb.styles.colors import TextColor

def footer() -> rx.Component:
    return rx.box(
        rx.text("Built with Reflex", font_size=Size.MEDIUM.value),
        rx.text(f"© 2024-{datetime.date.today().year} Julian Moreno. All rights reserved.", font_size=Size.MEDIUM.value),
        text_align="center",
        width="100%",
        margin_top="auto",
        padding_bottom=Size.LARGE.value,
        color=TextColor.FOOTER.value,
    )