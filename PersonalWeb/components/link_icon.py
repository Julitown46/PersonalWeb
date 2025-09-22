import reflex as rx
from PersonalWeb.styles import styles
from PersonalWeb.styles.styles import Size

def link_icon(src: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=src,
            height=Size.XLARGE.value,
            alt=alt
        ),
        href=url,
        is_external=True,
    )