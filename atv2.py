import flet as ft

def main(page: ft.Page):
    
    #configurações da janela
    page.title = "Tacógrafo"
    page.window.width = 400
    page.window.height = 700 # Aumentado para caber a lista
    page.window.resizable = False
    page.window.maximizable = False
    page.bgcolor = "#252526"
    
    #Textos e Campos de texto
    
    text_tempo = ft.Text("Adicione o tempo: ", color="#E0E0E0", size=20)
    
    textField_tempo = ft.TextField(
        label = "Coloque o tempo",
        color="#E0E0E0",
        width=300,
        keyboard_type=ft.KeyboardType.NUMBER,
        border_radius=10)
    
    text_velocidade = ft.Text("Adicione a velocidade: ", color="#E0E0E0", size=20)
    
    textField_velocidade = ft.TextField(
        label = "Coloque a velocidade",
        color="#E0E0E0",    
        width= 300,
        keyboard_type=ft.KeyboardType.NUMBER,
        border_radius=10)

    #Função on_click
    
    text_resultado = ft.Text("Resultado: ", color="#E0E0E0", size=20)
    lista_de_entradas = ft.ListView(expand=1, spacing=5, auto_scroll=True)
    
    
    entradas = [] # CORREÇÃO: Usar colchetes [] para criar uma lista modificável
    
    def adicionar(e):
        try:

            tempo = float(textField_tempo.value)
            velocidade = int(textField_velocidade.value)
            entradas.append({"tempo": tempo, "velocidade": velocidade})

            # Adiciona a nova entrada na lista visual
            nova_entrada_texto = ft.Text(f"Tempo: {tempo}h, Velocidade: {velocidade} km/h", color="#E0E0E0")
            lista_de_entradas.controls.append(nova_entrada_texto)

            # Limpa os campos para a próxima entrada (melhora a usabilidade)
            textField_tempo.value = ""
            textField_velocidade.value = ""
            textField_tempo.focus() # Coloca o foco de volta no primeiro campo
        except ValueError: # CORREÇÃO: Captura o erro específico
            textField_tempo.error_text = "Coloque um numero valido"
            textField_velocidade.error_text = "Coloque um numero valido"
        page.update()
    
    def calcular(e):
        resultado = 0 # CORREÇÃO: Inicializa a variável resultado
        for entrada in entradas:
            tempo = entrada["tempo"]
            velocidade = entrada["velocidade"]
            resultado += velocidade * tempo
        
        text_resultado.value = f"Resultado: {resultado} km"
        page.update()
    
    #criação dos botões
    
    btn_adicionar = ft.ElevatedButton("Adicionar", on_click=adicionar, color="#000000", bgcolor="#ffffff")
    btn_calcular = ft.ElevatedButton("Calcular", on_click=calcular, color="#000000", bgcolor="#ffffff")
    
    #layout da página
    
    layout = ft.Container(
        content = ft.Column([
            text_tempo,
            textField_tempo,
            text_velocidade,
            textField_velocidade,
            ft.Row([
                btn_adicionar,
                btn_calcular
            ], alignment=ft.MainAxisAlignment.CENTER),
            ft.Text("Entradas Adicionadas:", color="#E0E0E0", weight=ft.FontWeight.BOLD),
            ft.Container(
                content=lista_de_entradas,
                border=ft.border.all(1, ft.Colors.WHITE30),
                border_radius=10,
                height=150,
                padding=10
            ),
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

    
        
    

    
    