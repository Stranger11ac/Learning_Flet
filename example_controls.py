import flet as ft
import time

class MyButton(ft.ElevatedButton):
    def __init__(self, text):
        super().__init__()
        self.bgcolor = ft.Colors.ORANGE_300
        self.color = ft.Colors.GREEN_800
        self.text = text     

def main(page: ft.Page):
    page.title = "Controles iniciales de Flet"
    page.window.width = 600
    page.window.height = 800

    label = ft.Text(value="Hello, world!", color="green")
    page.add(label)

    text_range = ft.Text(value="Initial Value", color="blue")
    page.add(text_range) # it's a shortcut for page.controls.append(t) and then page.update()

    for i in range(4):
        text_range.value = f"Step {i}"
        page.update()
        time.sleep(1)
    
    page.add(ft.Text("A"))
    page.add(ft.Text("B"))
    page.add(ft.Text("C"))

    page.add(
        ft.Row(controls=[
            ft.Text("D"),
            ft.Text("E"),
            ft.Text("F")
        ])
    )

    page.add(
        ft.Row(controls=[
            ft.TextField(label="Your name"),
            ft.ElevatedButton(text="Say my name!")
        ])
    )

    for i in range(1, 4):
        page.controls.append(ft.Text(f"Line {i}"))
        if i > 1:
            page.controls.pop(2)
        page.update()
        time.sleep(2)

    def button_clicked(e):
        page.add(ft.Text("Clicked!"))
    
    page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))

    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="What's needs to be done?", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))

    def button_clicked(e):
        output_text.value = f"Dropdown value is:  {color_dropdown.value}"
        page.update()

    output_text = ft.Text()
    submit_btn = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    color_dropdown = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ],
    )
    page.add(ft.Row([color_dropdown, submit_btn]), output_text)
    page.add(MyButton(text="OK"), MyButton(text="Cancel"))

    page.update()

ft.app(target=main, assets_dir="assets")