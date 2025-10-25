import flet as ft


def app(page: ft.Page):
    page.title = 'App1'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    body = ft.Container(
        content=ft.Column(
            [
                ft.Text('Привет!', size=36, text_align=ft.TextAlign.CENTER),
                ft.Button('Нажми меня')
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        alignment=ft.alignment.center
    )

    page.add(body)


ft.app(app)