import flet as ft

def main(page: ft.Page):
    page.title = "Conversor Minutos para Horas"
    page.window.width = 400
    page.window.height = 700 # Aumentado para caber a lista
    page.window.resizable = False
    page.window.maximizable = False
    page.bgcolor = "#252526"
    
    #texto
    
    text = ft.Text("Coloque o numero de minutos", color="#E0E0E0", size=20)
    textField = ft.TextField(
        label = "Coloque o numero de minutos",
        color="#E0E0E0",
        width=300,
        keyboard_type=ft.KeyboardType.NUMBER,
        border_radius=10)
    
    text_resultado = ft.Text("Resultado: ", color="#E0E0E0", size=20)
    
    def calcular(e):
        try:
            minutos = int(textField.value)
            horas = minutos / 60
            textField.error_text = None
            text_resultado.value = f"Resultado: {horas:.2f} horas"
        except ValueError:
            textField.error_text = "Coloque um numero valido"
        page.update()
        
    
    
    btn_calcular = ft.ElevatedButton("Calcular", on_click=calcular, color="#E0E0E0", bgcolor="#007acc")
    
    #layout
    
    layout = ft.Container(
        content = ft.Column([
            text,
            textField,
            btn_calcular,
            text_resultado
        ], spacing=15),width=380, 
        height=580, 
        alignment=ft.alignment.center, 
        padding=20, 
        border_radius=10, 
        bgcolor="#3e3e42"
    )
    
    page.add(layout)
    
ft.app(target=main)
    
    