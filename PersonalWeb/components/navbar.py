import reflex as rx
from PersonalWeb.styles.styles import Size as Size

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text("Julian Moreno Cuenca"),
                position="sticky",
                bg="blue",
                padding_x=Size.DEFAULT.value,
                padding_y=Size.MEDIUM.value,
                z_index="999",
                top="0",
    )