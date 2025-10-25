import flet as ft
from Router.router import AppRouter
from Pages.main_page import MainPage
from Pages.second_page import SecondPage


def main(page: ft.Page):
    page.title = 'App1'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Инициализация роутера
    router = AppRouter(page)

    # Регистрация страниц
    router.register_page("/", MainPage())
    router.register_page("/second", SecondPage())

    # Установка обработчика маршрутов
    page.on_route_change = router.route_change
    page.go("/")


if __name__ == "__main__":
    ft.app(main)