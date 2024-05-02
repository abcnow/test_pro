import flet as ft

def set_fonts(page):
    page.fonts = {
        "roboto": "/fonts/Roboto-Regular.ttf",
        "roboto_bold": "/fonts/Roboto-Bold.ttf",
        "nexa": "/fonts/Nexa-Light.ttf",
        "nexa_bold": "/fonts/Nexa-Bold.ttf",
    }

def main(page: ft.Page):
    set_fonts(page)
    # Continue with other setup for this page

def home(page: ft.Page):
    set_fonts(page)
    # Continue with other setup for this page

def apptheme(page: ft.Page):
    set_fonts(page)

# Initialize the Flet app with the assets directory specified
ft.app(target=main, assets_dir='assets')
