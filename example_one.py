import flet as ft

def main(page: ft.Page):
    page.title = "Ejemplo básico"

    nombre = ft.TextField(label="Nombre")

    def enviar(e):
        page.add(ft.Text(f"Hola {nombre.value}", size=20))

    btn_menu = ft.IconButton(ft.icons.MENU, on_click=lambda e: setattr(page.drawer, "open", True))

    page.drawer = ft.NavigationDrawer(
        controls=[
            ft.Text("Menú"),
            ft.Divider(),
            ft.TextButton("Inicio"),
            ft.TextButton("Perfil")
        ]
    )

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME, label="Inicio"),
            ft.NavigationDestination(icon=ft.icons.SETTINGS, label="Config"),
        ]
    )

    page.add(
        btn_menu,
        ft.Text("Bienvenido", size=30, weight="bold"),
        nombre,
        ft.ElevatedButton("Enviar", on_click=enviar),
    )


ft.app(target=main)
