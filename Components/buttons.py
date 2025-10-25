import flet as ft


def create_button_with_animate(text: str, on_click=None):
    """Фабричная функция для создания кнопки с эффектом наведения"""

    def on_hover(e: ft.HoverEvent):
        if e.data == "true":
            e.control.scale = 1.1
            e.control.bgcolor = ft.Colors.BLUE_200
            e.control.elevation = 5
        else:
            e.control.scale = 1.0
            e.control.bgcolor = ft.Colors.BLUE_100
            e.control.elevation = 1
        e.control.update()

    return ft.ElevatedButton(
        text=text,
        bgcolor=ft.Colors.BLUE_100,
        on_hover=on_hover,
        on_click=on_click,
        animate_scale=ft.Animation(200, "easeOut"),
        animate_opacity=ft.Animation(200, "easeOut")
    )