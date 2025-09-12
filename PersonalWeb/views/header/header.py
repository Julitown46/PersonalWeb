import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback="JM", size="6"),
        rx.text("Julian Moreno", font_size="2xl", font_weight="bold"),
        rx.text("Full Stack Developer", font_size="lg", color="gray.500"),
        spacing="4",
        align_items="center",
    )