import flet as ft


class AppRouter:
    def __init__(self, page: ft.Page):
        self.page = page
        self.routes = {}

    def register_page(self, route: str, page_component):
        """Регистрация маршрута и соответствующей ему страницы"""
        self.routes[route] = page_component

    def route_change(self, route):
        """Обработчик смены маршрута"""
        self.page.views.clear()
        route_path = self.page.route

        if route_path in self.routes:
            self.page.views.append(
                ft.View(
                    route=route_path,
                    controls=[self.routes[route_path]]
                )
            )
        else:
            # Можно добавить страницу 404
            self.page.views.append(
                ft.View(
                    route=route_path,
                    controls=[ft.Container(
                        content=ft.Text("404 - Page Not Found"),
                        alignment=ft.alignment.center
                    )]
                )
            )
        self.page.update()