import reflex as rx
from PersonalWeb.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("GitHub", "https://github.com/Julitown46"),
        link_button("LinkedIn", "www.linkedin.com/in/julian-moreno-1408b133a"),
        link_button("Gmail", ""),
        link_button("Instagram", "https://www.instagram.com/julitown46/")
    )