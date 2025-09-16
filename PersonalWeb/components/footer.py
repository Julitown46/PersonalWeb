import reflex as rx
import datetime
from PersonalWeb.styles.styles import Size as Size

def footer() -> rx.Component:
    return rx.box(
        rx.text("Built with Reflex", font_size=Size.MEDIUM.value),
        rx.text(f"© 2024-{datetime.date.today().year} Julian Moreno. All rights reserved.", font_size=Size.MEDIUM.value),
        text_align="center",
        padding_y="4",
        width="100%",
        border_color="gray.200",
        margin_top="auto",
        margin_bottom=Size.LARGE.value,
    )