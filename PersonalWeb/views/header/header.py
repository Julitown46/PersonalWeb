import reflex as rx
from PersonalWeb.components.link_icon import link_icon
from PersonalWeb.components.info_text import info_text
from PersonalWeb.styles.styles import Size
from PersonalWeb.styles.colors import Color, TextColor

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="JMC",
                      src="avatar.jpg",
                      height=Size.XXXLARGE.value,
                      width=Size.XXXLARGE.value,
                      color= TextColor.BODY.value,
                      bg= Color.CONTENT.value
                      ),
            rx.vstack(
                rx.heading("Julian Moreno Cuenca", size="8", 
                        font_weight="bold",
                        color= TextColor.HEADER.value),
                rx.text("FullStack Developer", 
                        size="6",
                        color= Color.SECONDARY.value),
                width="100%",
                spacing="3",
            ), 
            spacing="4",
            align_items="center",
        ),
        rx.flex(
                link_icon("icons/python.svg", "https://www.python.org/", "Python"),
                rx.spacer(),
                link_icon("icons/java.svg", "https://www.java.com/es/" , "Java"),
                rx.spacer(),
                link_icon("icons/angular.svg", "https://angular.dev/" , "Angular"),
                rx.spacer(),
                link_icon("icons/docker.svg", "https://www.docker.com/" , "Docker"),
                width="100%",
                margin_y=Size.MEDIUM.value,
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
        "My goal is to grow as a web developer, contribute value to innovative technology projects, and continue expanding my knowledge in the IT sector.",
        color= TextColor.BODY.value),
        spacing="4",
        align_items="start",
    )