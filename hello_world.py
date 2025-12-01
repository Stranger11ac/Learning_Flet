import flet as ft

def main(page: ft.Page):
    page.title = "Hola Mundo con Flet"
    page.add(
        ft.Text("¡Hola Mundo!", size=30, color="blue")
    )

# Ejecutar en una ventana de escritorio:
ft.app(target=main)

# Ejecutar en el navegador web:
# ft.app(target=main, view=ft.WEB_BROWSER) 