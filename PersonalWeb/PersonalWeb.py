import reflex as rx
from PersonalWeb.components.navbar import navbar
from PersonalWeb.views.header.header import header
from PersonalWeb.views.links.links import links
from PersonalWeb.components.footer import footer

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        links(),
        footer(),
        align_items="center",
    )
        
app = rx.App()
app.add_page(index)
app._compile()