import flet as ft


def main(page: ft.Page):
    # --- DEFININDO O TAMANHO DA JANELA ---
    page.window.width = 400    # Largura em pixels (típico de celular)
    page.window.height =  620    # Altura em pixels (típico de celular)
    page.window.resizable = False  # Impede que o usuário redimensione
    page.window.maximizable = False # Impede que o usuário maximize
    page.bgcolor = "#252526"

    page.title = "Calculo de entradas"
    page.horizontal_alignment= ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    
    text = ft.Text("Coloque o numero de acessos do 3º link", color="#E0E0E0", size=20)
    
    textField = ft.TextField(
        label = "Coloque o numero de acessos",
        color="#E0E0E0",
        width=300,
        keyboard_type=ft.KeyboardType.NUMBER,
        border_radius=10)
    
    acessos_primeiro_link = ft.Text("Pessoas que clicaram no primeiro link: 0",color="#E0E0E0")
    acessos_segundo_link = ft.Text("Pessoas que clicaram no segundo link: 0",color="#E0E0E0")
    
    
    def calcular(e):
        try:
            acessos_terceiro_link = int(textField.value)
            segundo_link = acessos_terceiro_link * 2
            primeiro_link = segundo_link * 2
            acessos_primeiro_link.value = f"Pessoas que clicaram no primeiro link: {primeiro_link}"
            acessos_segundo_link.value = f"Pessoas que clicaram no segundo link: {segundo_link}"
            textField.error_text = None
            
        except ValueError:
            textField.error_text = "Coloque um numero valido"
        page.update()
                
    btn_calcular = ft.ElevatedButton("Calcular", on_click=calcular, color="#E0E0E0", bgcolor="#007acc")
    
    
    container = ft.Container(
    content = ft.Column( [
        text,
        textField,
        btn_calcular,
        acessos_primeiro_link,
        acessos_segundo_link
    ]), 
    width=350, 
    height=400, # Aumentando a altura do container para preencher melhor a janela
    alignment=ft.alignment.center, 
    padding=20, 
    border_radius=10,
    bgcolor="#3e3e42")
    
    page.add(container)
    
    
ft.app(target=main)
    
