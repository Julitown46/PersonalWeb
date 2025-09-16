import reflex as rx
from PersonalWeb.components.link_icon import link_icon
from PersonalWeb.components.info_text import info_text

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="JMC", size="8"),
            rx.vstack(
                rx.text("Julian Moreno Cuenca", size="7", font_weight="bold"),
                rx.text("FullStack Developer", size="5"),
                rx.hstack(
                    link_icon("https://hola.com"),
                    link_icon("https://hola.com"),
                    link_icon("https://hola.com"),
                ),
                width="100%",
                spacing="2",
            ), 
            spacing="4",
        ),
        rx.flex(
            info_text("+3","years of acedemic training"),
            rx.spacer(),
            info_text("+2","years working with Angular & Java"),
            rx.spacer(),
            info_text("+1","year with Python & Django"),
            width="100%",
        ),
        rx.text("Hello world! I am Julián Moreno Cuenca, a recent graduate in Web Application Development, with hands-on experience in Python, Django, and JavaScript, and a solid academic background in Java and Angular, which have been the core technologies throughout my training and projects. " \
        "My goal is to grow as a web developer, contribute value to innovative technology projects, and continue expanding my knowledge in the IT sector."),
        spacing="4",
        align_items="start",
    )