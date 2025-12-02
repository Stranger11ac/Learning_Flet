import flet as ft

def main(page: ft.Page):
    page.title = "Ejemplo básico"
    page.window.icon = "assets/favicon.png"

    # ---------------- MENÚ LATERAL (DRAWER) ----------------
    drawer = ft.NavigationDrawer(
        controls=[
            ft.Text("Menú", size=20, weight="bold"),
            ft.Divider(),
            ft.TextButton("Inicio"),
            ft.TextButton("Perfil"),
            ft.TextButton("Configuración"),
        ]
    )
    page.drawer = drawer

    # ---- Botón para abrir el menú ----
    def abrir_menu(e):
        page.drawer.open = True
        page.update()

    btn_menu = ft.IconButton(ft.Icons.MENU, on_click=abrir_menu)

    # ---------------- CAMPO DE TEXTO + BOTÓN ----------------
    nombre = ft.TextField(label="Nombre", width=300)

    def enviar(e):
        page.add(ft.Text(f"Hola {nombre.value}", size=20))
        page.update()

    btn_enviar = ft.ElevatedButton("Enviar", on_click=enviar)

    # ---------------- NAVIGATION BAR (INFERIOR) ----------------
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Inicio"),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label="Config"),
        ]
    )

    # ---------------- DISEÑO PRINCIPAL ----------------
    page.add(
        btn_menu,
        ft.Text("Bienvenido", size=30, weight="bold"),
        nombre,
        btn_enviar,
    )

ft.app(target=main, assets_dir="assets")
# ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER)
