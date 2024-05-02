import flet as ft


class SidebarHeader(ft.UserControl):
    def build(self):
        def close_anchor(e):
            text = f"Color {e.control.data}"
            print(f"closing view from {text}")
            anchor.close_view(text)

        def handle_change(e):
            print(f"handle_change e.data: {e.data}")

        def handle_submit(e):
            print(f"handle_submit e.data: {e.data}")

        def handle_tap(e):
            print("handle_tap")

        anchor = ft.SearchBar(
            view_elevation=4,
            divider_color=ft.colors.AMBER,
            bar_hint_text="Search colors...",
            view_hint_text="Choose a color from the suggestions...",
            on_change=handle_change,
            on_submit=handle_submit,
            on_tap=handle_tap,
            controls=[
                ft.ListTile(title=ft.Text(f"Color {i}"), on_click=close_anchor, data=i)
                for i in range(10)
            ],
        )


class SidebarContent(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.expand = True

    def build(self):
        location = ft.Column(
            
        ),
        
        return ft.Container(
            bgcolor=ft.accent2_color4,
            padding=ft.padding.all(20),
            content=ft.Column(
                scroll=ft.ScrollMode.HIDDEN,
                controls=[
                    location,
                    ft.Divider(height=30),
                ]
            )
        )

class SidebarFooter(ft.UserControl):
    def build(self):
        return ft.Container(
            padding = ft.padding.symmetric(vertical=10),
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        content=ft.Image(src='icons/001-instagram.png', height=15, color='white'),
                        url='https://www.instagram.com/programadoraventureiro/',
                    ),
                    ft.IconButton(
                        content=ft.Image(src='icons/002-linkedin.png', height=15, color='white'),
                        url='https://www.linkedin.com/company/66876059',
                    ),
                    ft.IconButton(
                        content=ft.Image(src='icons/003-github.png', height=15, color='white'),
                        url='https://github.com/Programador-Aventureiro',
                    ),
                    ft.IconButton(
                        content=ft.Image(src='icons/004-youtube.png', height=15, color='white'),
                        url='https://www.youtube.com/@ProgramadorAventureiro',
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

class Sidebar(ft.UserControl):
    def build(self):
        return ft.Container(
            expand=True,
            content=ft.Column(
                controls=[
                    SidebarHeader(),
                    SidebarContent(),
                    SidebarFooter(),
                ]
            ),
            bgcolor=ft.accent2_color4,
        )