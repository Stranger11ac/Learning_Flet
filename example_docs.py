import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="1", text_align=ft.TextAlign.CENTER, width=60, bgcolor=ft.Colors.BLUE_800)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        if int(txt_number.value) == 0:
            txt_number.bgcolor = ft.Colors.GREY_800
        elif int(txt_number.value) < 0:
            txt_number.bgcolor = ft.Colors.RED_800
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        if int(txt_number.value) == 0:
            txt_number.bgcolor = ft.Colors.GREY_800
        elif int(txt_number.value) > 0:
            txt_number.bgcolor = ft.Colors.BLUE_800
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.Icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main)