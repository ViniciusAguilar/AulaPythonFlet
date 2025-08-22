import flet as ft

def main(page: ft.Page):
    
    #Configurações de página
    page.window.width = 400
    page.window.height = 600
    page.window.resizable = False
    page.window.maximizable = False
    page.bgcolor = "#252526"
    page.title = "Sistema de controle de acessos"
    #Elementos da página
    
    titulo = ft.Text(
        "Sistema de controle de acessos", 
        size = 20, 
        text_align= ft.TextAlign.CENTER, 
        color = ft.Colors.WHITE)
    
    texto1 = ft.Text(
        "Coloque seu cargo",
        size = 14,
        color = ft.Colors.WHITE)
    
    cargo_textField = ft.TextField(
        width= 250,
        label = "Escreva aqui seu cargo!", 
        color= "#E0E0E0",
        border_radius= 10)
    
    texto2 = ft.Text(
        "Coloque o dia da semana:",
        size = 14,
        color = ft.Colors.WHITE)
    
    dia_textField = ft.TextField(
        width= 250,
        label = "Escreva aqui o dia da semana!", 
        color= "#E0E0E0",
        border_radius= 10)
    
    acesso = ft.Text("Verificando acesso", size = 16, color = ft.Colors.WHITE)    
    
    #Função para o botão
    dias_analista = ["segunda", "terça", "quarta", "quinta", "sexta","segunda-feira","terça-feira","quarta-feira","quinta-feira","sexta-feira"]
    dias_suporte = ["segunda", "quarta", "sexta","segunda-feira","quarta-feira","sexta-feira"]
    dias_estagiario = ["segunda", "terça", "quarta", "quinta", "sexta","segunda-feira","terça-feira","quarta-feira","quinta-feira","sexta-feira"]
    
    def verificar(e):
        cargo = cargo_textField.value
        dia = dia_textField.value
        
        if cargo == "analista":
            if dia in dias_analista:
                acesso.value = "Acesso Permitido"
                acesso.color = ft.Colors.GREEN
            else:
                acesso.value = "Acesso Negado"
                acesso.color = ft.Colors.RED
        elif cargo == "suporte":
            if dia in dias_suporte:
                acesso.value = "Acesso Permitido"
                acesso.color = ft.Colors.GREEN
            else:
                acesso.value = "Acesso Negado"
                acesso.color = ft.Colors.RED
        elif cargo == "estagiario":
            if dia in dias_estagiario:
                acesso.value = "Acesso Permitido"
                acesso.color = ft.Colors.GREEN
            else:
                acesso.value = "Acesso Negado"
                acesso.color = ft.Colors.RED
        elif cargo == "gerente":
            acesso.value = "Acesso Permitido"
            acesso.color = ft.Colors.GREEN
        else:
            acesso.value = "Cargo não encontrado"
            acesso.color = ft.Colors.RED
        
        page.update()
    
    btn_verificar = ft.ElevatedButton(
        "Verificar", 
        color = ft.Colors.WHITE,
        on_click= verificar,
        bgcolor= "#007acc")
    
    #layout da página
    
    layout = ft.Container(
        content= ft.Column([
            titulo,
            texto1,
            cargo_textField,
            texto2,
            dia_textField,
            btn_verificar,
            acesso
        ], spacing= 15),
        width= 350,
        alignment= ft.alignment.center,
        padding= 20,
        border_radius=10    
    )
    
    page.add(layout)

ft.app(target=main)