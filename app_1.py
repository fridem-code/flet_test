import flet as ft


def app(page: ft.Page):
    page.title = 'App1'
    page.add(ft.Text('Привет!'))


ft.app(app)