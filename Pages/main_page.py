import flet as ft
from Components.buttons import create_button


class MainPage(ft.Container):
    def __init__(self):
        super().__init__(
            expand=True,
            alignment=ft.alignment.center
        )

        self.content = ft.Column(
            [
                ft.Text('Привет!', size=36, text_align=ft.TextAlign.CENTER),
                create_button("Нажми меня", self.go_to_second_page)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    def go_to_second_page(self, e):
        self.page.go("/second")