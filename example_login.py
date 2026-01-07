import flet as ft
import requests

API_LOGIN_URL = "http://localhost:8030/login"


def main(page: ft.Page):
    page.title = "Login"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.Colors.SURFACE
    page.window.width = 360
    page.window.center()

    # =========================
    # Alert Dialog
    # =========================
    def show_alert( page: ft.Page, title: str, message: str, icon: ft.Icon, icon_color=ft.Colors.GREEN):
        dialog = ft.AlertDialog(
            # modal=True,
            title=ft.Row(
                # wrap=True,
                spacing=5,
                controls=[
                    ft.Icon(icon, size=32, color=icon_color),
                    ft.Text(title, size=20, weight=ft.FontWeight.BOLD),
                ],
            ),
            content=ft.Text(message, text_align=ft.TextAlign.CENTER),
            actions=[
                ft.TextButton(
                    "Cerrar",
                    on_click=lambda e: page.close(dialog),
                )
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        # page.dialog = dialog
        # page.update()
        page.open(dialog)

    # =========================
    # Inputs
    # =========================
    username = ft.TextField(
        label="Usuario",
        keyboard_type=ft.KeyboardType.EMAIL,
        border_radius=12,
        autofocus=True,
    )

    password = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        border_radius=12,
    )

    # status_text = ft.Text(
    #     "",
    #     size=0,
    #     color=ft.Colors.RED_400,
    #     text_align=ft.TextAlign.CENTER,
    # )

    # =========================
    # Login action
    # =========================
    def do_login(e):
        # status_text.value = "Iniciando sesión..."
        # status_text.color = ft.Colors.BLUE_400
        page.update()

        try:
            response = requests.post(
                API_LOGIN_URL,
                json={
                    "username": username.value,
                    "password": password.value,
                },
                timeout=10,
                verify=False  # ⚠️ SOLO PARA CERTIFICADOS LOCALES
            )

            print(response)
            print(response.json())

            if int(response.status_code) == 200:
                data = response.json()
                token = data.get("access_token")

                # status_text.value = "Login exitoso ✅"
                # status_text.color = ft.Colors.GREEN_400

                # Aquí puedes guardar el token
                page.client_storage.set("token", token)

                print("TOKEN:", token)

            else:
                data = response.json()
                response_msg = data.get("message", "Error desconocido")
                response_msg_color = ft.Colors.RED_400
                show_alert(
                    page,
                    title="Error de inicio de sesión",
                    message=response_msg,
                    icon=ft.Icons.ERROR,
                    icon_color=response_msg_color,
                )

        except Exception as ex:
            # status_text.value = f"Error de conexión"
            # status_text.color = ft.Colors.RED_400
            show_alert(
                    page,
                    title="Error de inicio de sesión",
                    message="Error de conexión al servidor",
                    icon=ft.Icons.ERROR,
                    icon_color=ft.Colors.RED_400,
                )
            print(ex)

        page.update()

    # =========================
    # Card Login
    # =========================
    login_card = ft.Card(
        elevation=8,
        content=ft.Container(
            width=360,  # Mobile-first
            padding=24,
            content=ft.Column(
                spacing=16,
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                controls=[
                    ft.Text(
                        "Iniciar sesión",
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER,
                    ),

                    username,
                    password,

                    ft.ElevatedButton(
                        text="Entrar",
                        height=48,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=12)
                        ),
                        on_click=do_login,
                    ),

                    # status_text,

                    ft.Divider(),

                    ft.TextButton(
                        "¿Olvidaste tu contraseña?",
                        on_click=lambda e: print("Forgot password"),
                    ),
                ],
            ),
        ),
    )

    # =========================
    # Layout principal
    # =========================
    page.add(
        ft.Container(
            # expand=True,
            alignment=ft.alignment.center,
            content=login_card,
        )
    )


ft.app(target=main)
