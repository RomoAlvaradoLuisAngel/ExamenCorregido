#Romo Alvarado Luis Angel - 23308060610320 - 6D
import flet as ft
def main(page: ft.Page):
    page.title="Examen final - Registro de estudiantes"
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
    
    taller = ft.Dropdown(
        label="Taller",
        options=[
            ft.DropdownOption(key="principiantes", text="Python para principiantes."),
            ft.DropdownOption(key="intermedio", text="Flet intermedio."),
            ft.DropdownOption(key="panda", text="Analisis de datos con pandas."),
        ],
    )
    
    pago = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="completo", label="Pago completo"),
            ft.Radio(value="cuotas", label="Pago por cuotas"),
        ])
    )
    
    requerimientos = ft.Checkbox(
        label="Si",
        value=False,
        check_color=ft.Colors.WHITE,
        fill_color=ft.Colors.GREEN
    )
    
    experiencia = ft.Slider(
        value= 1,
        min=0,
        max=5,
        divisions=5
    )
    resultado = ft.Text("")
    
    def mostrar_resumen(e):
        resultado.value=(
        "Nombre completo: " + nombre.value + "\n"
        "Correo electronico: " + correo.value + "\n"
        "Taller: " + str(taller.value) + "\n"
        "Pago: " + str(pago.value) + "\n"
        "Requerimientos: " + str(requerimientos.value) + "\n"
        "Experiencia: " + str(experiencia.value) + "\n"
        )
        page.update()
        
    boton=ft.ElevatedButton(
        content=ft.Text("Mostrar ficha del participante"),
        icon=ft.Icons.SAVE,
        color=ft.Colors.BLUE,
        on_click=mostrar_resumen
    )
    
    page.add(ft.Column(
    width=220,
    spacing=12,
    controls=[
        ft.Text("--Nombre completo--"),
        nombre,
        ft.Text("--Correo electronico--"),
        correo,
        ft.Text("--Taller--"),
        taller,
        ft.Text("--Modalidad de pago--"),
        pago,
        ft.Text("--Requiere una laptop?--"),
        requerimientos,
        ft.Text("--Nivel de experiencia--"),
        experiencia,
        boton,
        ft.Text("--Ficha del participante--"),
        resultado,
        ft.Text("--Gracias por su registro--")
    ],
))

ft.run(main)