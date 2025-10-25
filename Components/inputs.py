import flet as ft


class InputFactory:
    @staticmethod
    def create_text_field_with_animate(label: str, text_size=None, width=None, height=None, on_change=None):
        """Фабричная функция для создания текстового поля с эффектом наведения"""

        def on_hover(e: ft.HoverEvent):
            if e.data == "true":
                e.control.border_color = ft.Colors.BLUE_700
                e.control.bgcolor = ft.Colors.BLUE_50
                e.control.scale = 1.05
            else:
                e.control.border_color = ft.Colors.BLUE_300
                e.control.bgcolor = ft.Colors.WHITE
                e.control.scale = 1.0
            e.control.update()

        text_field = ft.TextField(
            label=label,
            border=ft.InputBorder.OUTLINE,
            border_color=ft.Colors.BLUE_300,
            border_radius=8,
            bgcolor=ft.Colors.WHITE,
            text_size=text_size,
            width=width,
            height=height,
            on_change=on_change,
        )

        return ft.Container(
            content=text_field,
            border=ft.border.all(2, ft.Colors.BLUE_300),
            border_radius=8,
            on_hover=on_hover,
            animate_scale=ft.Animation(200, "easeOut"),
        )