import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.box(
        rx.text(f"© 2024-{datetime.date.today().year} Julian Moreno. All rights reserved.", font_size="sm", color="gray.500"),
        text_align="center",
        padding_y="4",
        width="100%",
        border_color="gray.200",
        margin_top="auto",
    )