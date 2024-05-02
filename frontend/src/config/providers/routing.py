import re
import flet as ft
from typing import List #Callable, List, Dict, Union, Pattern
from common.theme.colors import Colors

class Home(ft.View):

    def __init__(self, **kwargs):
        super().__init__(route="/home")

        self.appbar = ft.AppBar(
            bgcolor=Colors.BACKGROUND,
            title=ft.Text(
                "Home",
                size=32,
                weight=ft.FontWeight.BOLD,
            ),
        )


class News(ft.View):
    def __init__(self, **kwargs):
        super().__init__(route="/news/:id")

        self.appbar = ft.AppBar(
            title=ft.Text("News"),
            actions=[ft.IconButton(icon="logout")],
        )

        self.controls = [
            ft.Text("News:   "),
        ]


class Settings(ft.View):

    def __init__(self, **kwargs):
        super().__init__(route="/settings")

        self.appbar = ft.AppBar(
            title=ft.Text("Settings"),
            actions=[ft.IconButton(icon="logout")],
        )

        self.controls = [
            ft.Text("Settings"),
        ]


class Route:
    def __init__(self, path: str, view: ft.View) -> None:
        self.path: str = path
        self.view: ft.View = view
        self.pattern = (
            re.compile(
                self._convert_path_to_regex(path),
            )
            if ":" in path
            else path
        )

    def _convert_path_to_regex(self, path: str) -> str:
        return re.sub(r":(\w+)", r"(?P<\1>[^/]+)", path)


class Router:
    def __init__(self, page, routes: List[Route]) -> None:
        self.routes: List[Route] = routes

    # def handle_route_change(self, route: str) -> ft.View:
    #     for r in self.routes:
    #         if isinstance(r.pattern, Pattern):
    #             match = r.pattern.match(route)
    #             if match:
    #                 return r.view(**match.groupdict())
    #         elif r.path == route:
    #             return r.view()
    #     return ft.View(route="/404", controls=[ft.Text("404 Not Found")])
    def push(self, route: Route) -> None:
        self.routes.append(route)


router = Router(
    page=ft.Page,
    routes=[
        Route(path="/home", view=Home),
        Route(path="/news/:id", view=News),
        Route(path="/news/:source/:news_id", view=News),
    ],
)


print(router.handle_route_change("/home"))
# print(router.handle_route_change("/movie/123"))
# print(router.handle_route_change("/movie/john_doe/456"))