#Romo Alvarado Luis Angel - 23308060610320 - 6D
import flet as ft
def main(page: ft.Page):
    page.title="Examen final - Registro de estudiantes"
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.add(ft.Text(value="Registro de participantes", size=25, italic=False, text_align=ft.TextAlign.CENTER))
    
    nombre = ft.TextField(
        value="",
        label="Escriba su nombre completo: ",
        color=ft.Colors.BLUE,
        on_change=lambda e: print(e.control.value),
        on_submit=lambda e: print("Enter presionado")
    )
    
    correo = ft.TextField(
        value="",
        label="Escriba su correo electronico",
        color=ft.Colors.BLUE,
    )
    
    page.add(ft.Text("--Taller de interes--"))
    taller = ft.Dropdown(
        value="Taller",
        options=[
            ft.DropdownOption(key="principiantes", text="Python para principiantes."),
            ft.DropdownOption(key="intermedio", text="Flet intermedio."),
            ft.DropdownOption(key="panda", text="Analisis de datos con pandas."),
        ],
    )
    
    page.add(ft.Text("--Modalidad de pago--"))
    pago = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="completo", label="Pago completo"),
            ft.Radio(value="cuotas", label="Pago por cuotas"),
        ])
    )
    
    page.add(ft.Text("--Requiere computadora portatil--"))
    requerimientos = ft.Checkbox(
        label="Si",
        value=False,
        check_color=ft.Colors.WHITE,
        fill_color=ft.Colors.GREEN
    )
    
    page.add(ft.Text("--Nivel de experiencia--"))
    experiencia = ft.Slider(
        value= 1,
        min=0,
        max=5,
        divisions=5
    )
    
    page.add(ft.Column(
    width=220,
    height=120,
    spacing=12,
    controls=[
        ft.Text(nombre),
        ft.Text(correo),
        ft.Text(taller),
        ft.Text(pago),
        ft.Text(requerimientos),
        ft.Text(experiencia)
    ],
))
    
    mostrar_resumen=ft.ElevatedButton(
        content="Mostrar ficha del participante",
        icon=ft.Icons.SAVE,
        color=ft.Colors.BLUE,
        on_click=lambda e: print("Click!")
    )
    
    
    ft.Divider(height=10, thickness=2, color=ft.Colors.GREY_400)
    ft.VerticalDivider(width=10, thickness=2, color=ft.Colors.GREY_400)
    

    page.add(ft.Text("--Ficha del participante--"))
    
    def mostrar_resumen(e):
        ft.Text("Nombre completo: " + nombre.value + "\n",
        "Correo electronico: " + correo.value + "\n",
        "Taller: " + taller.value + "\n",
        "Pago: " + pago.value + "\n",
        "Requerimientos: " + requerimientos.value + "\n",
        "Experiencia: " + experiencia.value + "\n",
        )
        page.update()
    page.add(mostrar_resumen)
    

    page.add(ft.Text("--Gracias por su registro--"))

ft.run(main)