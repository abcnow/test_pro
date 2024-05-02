import flet as ft
from common.theme.apptheme import AppTheme
from common.components.sidebar import Sidebar
from common.theme.colors import Colors
#from common.providers.navigator import Navigator
from config.routes import Routes

class Home:
    def __init__(self, page: ft.Page):
        super().__init__(route=Routes.HOME_ROUTE)
        self.page = page
        self.page.theme = AppTheme
        self.page.on_resize = self.show_app_bar
        self.page.bgcolor = ft.colors.WHITE
        self.main()
        self.show_app_bar()

    def toggle_sidebar(self, e):
        self.sidebar.col['xs'] = 12 if self.sidebar.col['xs'] == 0 else 0
        self.content.col['xs'] = 0 if self.content.col['xs'] == 12 else 12
        self.page.update()


    def show_app_bar(self, e = None):
        if self.page.width < 768:
            self.page.appbar = ft.AppBar(
                leading=ft.IconButton(
                    icon=ft.icons.MENU,
                    icon_color= Colors.PRIMARY500,
                    on_click=self.toggle_sidebar
                ),
                bgcolor= Colors.BACKGROUND,
            )
            self.layout.spacing = 0
            self.page.bgcolor = Colors.BACKGROUND
        else:
            self.page.appbar = None
            self.layout.spacing = 10
            self.page.bgcolor = Colors.BACKGROUND

        self.page.update()

    def main(self):
        self.sidebar = Sidebar(col={'xs': 0, 'md': 5, 'lg': 4, 'xxl': 3})
        #self.content = MainContent(col={'xs': 12, 'md': 7, 'lg': 8, 'xxl': 9})

        self.layout = ft.ResponsiveRow(
            columns=12,
            controls=[
                self.sidebar,
                self.content,
            ],
            expand=True,
        )

        self.page.add(self.layout)



if __name__ == '__main__':
    ft.app(target=Home, assets_dir='assets')