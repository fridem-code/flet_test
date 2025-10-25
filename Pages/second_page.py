import flet as ft
from Components.buttons import create_button


class SecondPage(ft.Container):
    def __init__(self):
        super().__init__(
            expand=True,
            alignment=ft.alignment.center
        )

        self.content = ft.Column(
            [
                ft.Text('Возврат на предыдущую страницу!', size=36, text_align=ft.TextAlign.CENTER),
                create_button("Нажми меня", self.go_back)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    def go_back(self, e):
        self.page.go("/")