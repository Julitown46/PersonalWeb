import reflex as rx
from PersonalWeb.components.link_button import link_button
from PersonalWeb.components.title import title

def links() -> rx.Component:
    return rx.vstack(
        title("Professional Links"),
        link_button("github", "GitHub", "View my GitHub Projects!", "https://github.com/Julitown46"),
        link_button("linkedin", "LinkedIn", "Connect on LinkedIn", "https://www.linkedin.com/in/julian-moreno-1408b133a"),
        link_button("mail", "Gmail", "morenojulian4502@gmail.com", "mailto:morenojulian4502@gmail.com"),
        title("Social Links"),
        link_button("instagram", "Instagram", "My main social media account","https://www.instagram.com/julitown46/"),
        link_button("music", "Spotify", "Follow me on Spotify!","https://open.spotify.com/user/1196330141"),
        width="100%",
    )