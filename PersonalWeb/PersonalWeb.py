import reflex as rx
from PersonalWeb.components.navbar import navbar
from PersonalWeb.views.header.header import header
from PersonalWeb.views.links.links import links
from PersonalWeb.components.footer import footer
import PersonalWeb.styles.styles as styles
from PersonalWeb.styles.styles import Size as Size

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                align_items="center",
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_bottom=Size.LARGE.value,
                padding=Size.LARGE.value,
            )
        ),
        footer()
    )
        
app = rx.App(
    style=styles.BASE_STYLE,
)
app.add_page(index)
app._compile()