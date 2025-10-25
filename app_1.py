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

    def go_to_second_page(e):
        page.go("/second")

    button_main_page = ft.ElevatedButton(
        text="Нажми меня",
        bgcolor=ft.Colors.BLUE_100,
        on_hover=on_hover,
        on_click=go_to_second_page,
        animate_scale=ft.Animation(200, "easeOut"),
        animate_opacity=ft.Animation(200, "easeOut")

    )

    main_page = ft.Container(
        expand=True,
        content=ft.Column(
            [
                ft.Text('Привет!', size=36, text_align=ft.TextAlign.CENTER),
                button_main_page
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        alignment=ft.alignment.center
    )

    def go_back(e):
        page.go('/')

    button_second_page = ft.ElevatedButton(
        text="Нажми меня",
        bgcolor=ft.Colors.BLUE_100,
        on_hover=on_hover,
        on_click=go_back,
        animate_scale=ft.Animation(200, "easeOut"),
        animate_opacity=ft.Animation(200, "easeOut")

    )

    second_page = ft.Container(
        expand=True,
        content=ft.Column(
            [
                ft.Text('Возврат на предыдущую страницу!', size=36, text_align=ft.TextAlign.CENTER),
                button_second_page
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        alignment=ft.alignment.center
    )

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(ft.View(route="/", controls=[main_page]))
        elif page.route == "/second":
            page.views.append(ft.View(route="/second", controls=[second_page]))
        page.update()

    page.on_route_change = route_change
    page.go("/")

ft.app(app)