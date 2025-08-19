import flet as ft

def main(page: ft.Page):
    page.window.width = 500
    page.window.height = 600
    page.window.resizable = False
    page.window.maximizable = False 
    
    page.bgcolor = "#252526"
    page.title = "Exercício"
    
    texto = ft.Text("Coloque um número: ",size=20,color = ft.Colors.WHITE)
    
    text_field = ft.TextField(label="Escreva aqui seu numero",border_radius=10,width=250,color="#E0E0E0",keyboard_type=ft.KeyboardType.NUMBER)
    tabela = ft.DataTable(columns=[
        ft.DataColumn(ft.Text("i", color = ft.Colors.WHITE)),
        ft.DataColumn(ft.Text("i**2", color = ft.Colors.WHITE)),
        ft.DataColumn(ft.Text("i**3", color = ft.Colors.WHITE)),
        
    ], rows=[])
    def calcular(e):
        try:
            n = int(text_field.value)
            if not (1<n<1000):
                page.snack_bar = ft.SnackBar(ft.Text("Digite um número entre 1 e 9999"))
                page.snack_bar.open = True
                page.update()
                return

            tabela.rows.clear()
            
            for i in range(1,n+1):
                tabela.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(i), color = ft.Colors.WHITE)),
                            ft.DataCell(ft.Text(str(i**2), color = ft.Colors.WHITE)),
                            ft.DataCell(ft.Text(str(i**3), color = ft.Colors.WHITE)),
                    ]))
                tabela.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(i), color=ft.Colors.WHITE)),
                            ft.DataCell(ft.Text(str(i**2 + 1), color=ft.Colors.WHITE)),
                            ft.DataCell(ft.Text(str(i**3 + 1), color=ft.Colors.WHITE)),
                        ]
                    )
                )
            page.update()
            
        except:
            page.snack_bar = ft.SnackBar(ft.Text("Digite um número válido"))
            page.snack_bar.open = True
            page.update()
    
    btn_calcular = ft.ElevatedButton(
        "Calcular", 
        color = ft.Colors.WHITE,
        on_click= calcular,
        bgcolor= "#007acc")
    
    tabela_scroll = ft.Container(
        content=ft.Column([tabela],spacing=10,expand= True,scroll = ft.ScrollMode.ALWAYS),
        border=ft.border.all(1,ft.Colors.WHITE),
        expand=True,
        bgcolor="#2d2d30",
        border_radius=10,
        padding=10,
        alignment=ft.alignment.top_center,
        )

    
    layout = ft.Container(
        content = ft.Column([
            texto,
            text_field,
            btn_calcular,
            tabela_scroll
        ],spacing=15,expand= True, scroll=ft.ScrollMode.ALWAYS),
        width= 400,
        alignment= ft.alignment.center,
        padding= 20,
        border_radius=10,
        expand= True)
    
    page.add(layout)
    
ft.app(target=main)
        
        