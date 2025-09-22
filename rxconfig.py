import reflex as rx

config = rx.Config(
    app_name="PersonalWeb",
    frontend_only=True,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)