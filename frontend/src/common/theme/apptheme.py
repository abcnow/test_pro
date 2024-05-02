import flet as ft
from common.theme.colors import Colors
from common.theme.fonts import set_fonts

class AppTheme:
    def __init__(self):
        super().__init__()
        # The Theme does not accept a 'fonts' parameter; instead, set fonts directly on the Page.
        self.theme = ft.Theme(
            text_theme=ft.TextTheme(
                body_large=ft.TextStyle(
                    font_family="roboto_bold",
                    weight=ft.FontWeight.BOLD,
                    color=Colors.FONT500,
                    size=14,
                ),
                body_medium=ft.TextStyle(
                    font_family="roboto",
                    weight=ft.FontWeight.NORMAL,
                    color=Colors.FONT400,
                    size=14,
                ),
                headline_large=ft.TextStyle(
                    font_family="roboto",
                    weight=ft.FontWeight.W_900,
                    color=Colors.FONT500,
                    size=50,
                ),
                label_large=ft.TextStyle(
                    font_family="roboto",
                    weight=ft.FontWeight.W_700,
                    color=Colors.FONT500,
                    size=16,
                ),
                headline_medium=ft.TextStyle(
                    font_family="roboto",
                    weight=ft.FontWeight.W_700,
                    color=Colors.FONT500,
                    size=30,
                ),
            ),
            scrollbar_theme=ft.ScrollbarTheme(
                track_visibility=False,
                thumb_visibility=False,
                track_color={
                    ft.MaterialState.DEFAULT: ft.colors.TRANSPARENT,
                },
                thumb_color={
                    ft.MaterialState.HOVERED: ft.colors.TRANSPARENT,
                    ft.MaterialState.DEFAULT: ft.colors.TRANSPARENT,
                }
            )
        )

def main(page: ft.Page):

    app_theme = AppTheme()
    page.theme = app_theme.theme
    page.update()
    set_fonts(page)

# Initialize the Flet app with the assets directory specified
ft.app(target=main, assets_dir='assets')
