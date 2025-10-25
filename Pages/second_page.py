import flet as ft
from Components.buttons import create_button_with_animate
from Components.inputs import InputFactory


class SecondPage(ft.Container):
    def __init__(self):
        super().__init__(
            expand=True,
            alignment=ft.alignment.center
        )

        # Создаем текстовое поле
        def handle_text_change(e):
            print(f"Введено: {e.control.value}")

        self.content = ft.Column(
            [
                ft.Text('Возврат на предыдущую страницу!', size=36, text_align=ft.TextAlign.CENTER),
                InputFactory.create_text_field_with_animate(
                    label='Введите текст',
                    height=40,
                    width=300,
                    text_size=16,
                    on_change=handle_text_change),
                create_button_with_animate("Нажми меня", self.go_back)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    def go_back(self, e):
        self.page.go("/")
