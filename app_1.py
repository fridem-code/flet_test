import flet as ft
from PIL.ImageOps import scale


def app(page: ft.Page):
    page.title = 'App1'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def on_hover(e: ft.HoverEvent):
        # При наведении увеличиваем масштаб и меняем цвет
        if e.data == "true":
            e.control.scale = 1.1
            e.control.bgcolor = ft.Colors.BLUE_200
            e.control.elevation = 5
        else:
            e.control.scale = 1.0
            e.control.bgcolor = ft.Colors.BLUE_100
            e.control.elevation = 1
        e.control.update()

    button = ft.ElevatedButton(
        text="Нажми меня",
        bgcolor=ft.Colors.BLUE_100,
        on_hover=on_hover,
        animate_scale=ft.Animation(200, "easeOut"),
        animate_opacity=ft.Animation(200, "easeOut")

    )

    body = ft.Container(
        expand=True,
        content=ft.Column(
            [
                ft.Text('Привет!', size=36, text_align=ft.TextAlign.CENTER),
                button
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        alignment=ft.alignment.center
    )

    page.add(body)


ft.app(app)