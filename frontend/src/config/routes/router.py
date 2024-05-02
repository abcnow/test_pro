import re
#from typing import Any, Dict
from config.routes.routes import Routes
from features.home.pages.home_view import Home
from features.settings.pages.settings_view import Settings
from features.profile.pages.profile_view import Profile
from features.news.pages.news_view import News
from features.auth.login.pages.login_view import Login
from features.auth.join.pages.join_view import Join
#import flet as ft


ROUTER = {
    Routes.HOME_ROUTE: Home,
    Routes.LOGIN_ROUTE: Login,
    Routes.JOIN_ROUTE: Join,
    Routes.PROFILE_ROUTE: Profile,
    Routes.NEWS_ROUTE: News,
    Routes.PROFILE_ROUTE: Profile,
    Routes.SETTINGS_ROUTE: Settings,
    Routes.NOT_FOUND_ROUTE: "404 Not Found",
}


def dynamic_router(path: str):
    for route, page in ROUTER.items():
        if route == path:
            return page
        if isinstance(route, re.Pattern):
            match = route.match(path)
            if match:
                return page
    return None