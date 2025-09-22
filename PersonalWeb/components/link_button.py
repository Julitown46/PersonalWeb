import reflex as rx
import PersonalWeb.styles.styles as styles
from PersonalWeb.styles.styles import Size

def link_button(icon: str, title: str, body: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.stack(
                rx.icon(
                    icon
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    spacing="0",
                ),
            ),
        ),
        href=url,
        is_external=True,
        width="100%",
    )