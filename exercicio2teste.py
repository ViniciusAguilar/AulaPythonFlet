import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 400
    page.window.height = 700   
    
    page.window.resizable = False
    page.window.maximizable = False 
    
    page.bgcolor = "#252526"
    page.title = "Exercício"
    
    
    text = ft.Text("Escolha um número de 0 à 60", size= 16,color = ft.Colors.WHITE)
    numero_textField = ft.TextField(label = "Escreva aqui o numero!", width=250,color=ft.Colors.WHITE, keyboard_type= ft.KeyboardType.NUMBER)
    resultado = ft.Text("Numero de Fibonacci correspondente: ", size= 16,color= ft.Colors.WHITE)
    
    def gerar_sequencia(n):
        sequencia = [0,1]
        for i in range(2,n+1):
            sequencia.append(sequencia[i-1] + sequencia[i-2])
        return sequencia
    
    def verificar_posicao(e):
        try:
            numero = int(numero_textField.value)
            if not (0 <= numero <= 60):
                page.snack_bar = ft.SnackBar(ft.Text("Digite um número entre 0 e 60"))
                page.snack_bar.open = True
                page.update()
                return
            else:
                seq = gerar_sequencia(60)
                resultado.value = f"Numero de Fibonacci correspondente: {seq[numero]}"
                page.update()

        except:
            page.snack_bar = ft.SnackBar(ft.Text("Digite um número válido"))
            page.snack_bar.open = True
            page.update()

    sequencia_completa = gerar_sequencia(60)
    
    sequencia_text = ft.Text(
        f"Sequencia completa: \n" + ", ".join(map(str, sequencia_completa)),
        size = 12,
        color = ft.Colors.WHITE,
        visible= False)
    def mostar_esconder_sequencia(e):
        sequencia_text.visible = not sequencia_text.visible
        if sequencia_text.visible == True:
            btn_esconder.text = "Esconder Sequencia"
        else:
            btn_esconder.text = "Mostrar Sequencia"
        page.update()
        
    btn_esconder = ft.ElevatedButton(
        "Mostrar Sequencia",
        on_click= mostar_esconder_sequencia,
        color = ft.Colors.WHITE,
        bgcolor= "#007acc")
    
    btn_verificar = ft.ElevatedButton(
        "Verificar", 
        on_click= verificar_posicao,
        color = ft.Colors.WHITE,
        bgcolor= "#007acc")
    
    sequencia_scroll = ft.Container(
        content=ft.Column([sequencia_text],spacing=10,expand= True,scroll = ft.ScrollMode.ALWAYS),
        border=ft.border.all(1,ft.Colors.WHITE),
        expand=True,
    )
    
    layout = ft.Container(
        content = ft.Column(
            [
                text,
                numero_textField,
                btn_verificar,
                resultado,
                btn_esconder,
                sequencia_scroll
            ],
            horizontal_alignment= ft.CrossAxisAlignment.CENTER
        ),
        width= 350,
        height= 300,
        bgcolor= "#252526",
        border_radius= 10
    )
    
    page.add(layout)
    
ft.app(target=main)
                
    