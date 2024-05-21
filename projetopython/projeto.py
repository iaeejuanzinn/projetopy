import tkinter as tk
from tkinter import messagebox 

def main(page: tk.Page):
    # O código principal da nossa aplicação será inserido aqui
    pass

tk.app(target=main)

def main(page: tk.Page):

    # Função para fechar o banner de notificação
    def close_banner(e):
        page.banner.open = False
        page.update()

    # Configurações da página
    page.appbar = tk.AppBar(
        leading=tk.Icon(tk.icons.MULTILINE_CHART),
        leading_width=40,
        title=tk.Text("Calculadora IMC"),
        center_title=False,
        bgcolor=tk.colors.SURFACE_VARIANT
    )

    page.window_width = 400
    page.window_height = 550

    # Configuração do banner de notificação
    page.banner = tk.Banner(
        bgcolor=tk.colors.AMBER_100,
        leading=tk.Icon(tk.icons.WARNING_AMBER_ROUNDED, color=tk.colors.AMBER, size=40),
        content=tk.Text("Ops, preencha todos os campos?"),
        actions=[
            tk.TextButton("Ok", on_click=close_banner),
        ],
    )
  # Layout da página
    layout =tk.ResponsiveRow(
        [  
            tk.Container(
                padding=5,
                col={"sm":4, "md": 4, "xl": 4},
                alignment=tk.alignment.center,
            ),
            tk.Container(
                padding=5,
                bgcolor=tk.colors.WHITE,
                col={"sm": 12, "md": 3, "xl": 3},
            ),
            tk.Container(
                padding=5,
                bgcolor=tk.colors.WHITE,
                col={"sm": 12, "md": 3, "xl": 3},
            ),
            tk.Container(
                padding=5,
                bgcolor=tk.colors.WHITE,
                col={"sm": 12, "md": 3, "xl": 3},
            ),
            tk.Container(
                padding=5,
                bgcolor=tk.colors.WHITE,
                col={"sm": 12, "md": 3, "xl": 3},
            ),
        ],
    )

    # Adicionar o layout à página
    page.add(layout)

    # Entrada de altura, peso e gênero
    altura = tk.TextField(label="Altura", hint_text="Por favor insira sua altura")
    peso = tk.TextField(label="Peso", hint_text="Por favor insira seu peso")
    genero = tk.Dropdown(
        label="Gênero",
        hint_text="Escolha seu gênero?",
        options=[
            tk.dropdown.Option("Masculino"),
            tk.dropdown.Option("Feminino"),
        ],
        #autofocus=True,
    )

    # Botão para calcular o IMC
    b_calcular = tk.ElevatedButton(text="Calcular IMC")

    # Exibição do IMC e resultados
    IMC = tk.Text("Seu IMC é ...", size=30)
    detalhes = tk.Text("Insira seus dados", size=20)

    img_capa = tk.Image(
        src=f"logo.png",
        width=100,
        height=100,
        fit=tk.ImageFit.CONTAIN,
    )

    info_app_resultado = tk.Column(
        controls=[
            IMC,
            detalhes,
        ])

    img_resultado = tk.Image(
        src=f"logo.png",
        width=100,
        height=100,
        fit=tk.ImageFit.CONTAIN,
    )

    info = tk.Row(
        controls=[
            info_app_resultado,
            img_resultado,
        ])
    # Layout da página
    layout = tk.ResponsiveRow(
        [  
            tk.Container(
                info,
                padding=5,
                col={"sm":4, "md": 4, "xl": 4},
                alignment=tk.alignment.center,
            ),

            tk.Container(
                altura,
                padding=5,
                bgcolor=tk.colors.WHITE,
                col={"sm": 12, "md": 3, "xl": 3},
            ),
            tk.Container(
                peso,
                padding=5,
                bgcolor=tk.colors.WHITE,
                col={"sm": 12, "md": 3, "xl": 3},
            ),
            tk.Container(
                genero,
                padding=5,
                bgcolor=tk.colors.WHITE,
                col={"sm": 12, "md": 3, "xl": 3},
            ),
            tk.Container(
                b_calcular,
                padding=5,
                bgcolor=tk.colors.WHITE,
                col={"sm": 12, "md": 3, "xl": 3},
            ),
        ],
    )

    # Adicionar o layout à página
    page.add(layout)
    def calcular(e):
    # Verificar se os campos de peso, altura e gênero estão preenchidos
     if peso.value == "" or altura.value == "" or genero.value == "":
        # Mostrar notificação de erro
        page.banner.open = True
        page.update()
     else:
        valor_peso = float(peso.value)
        valor_altura = float(altura.value)

        # Calcular o IMC
        imc = valor_peso / (valor_altura * valor_altura)
        imc = float(f"{imc:.2f}")

        # Exibir o valor do IMC
        IMC.value = f"Seu IMC é {imc}"

        # Determinar a imagem correspondente ao resultado do IMC e fornecer detalhes
        if genero.value == "Feminino":
            if imc < 18.5:
                img_resultado.src= f"magraM.png"
                detalhes.value = 'Abaixo do peso'
            elif 18.5 <= imc < 24.9:
                img_resultado.src = f"8.png"
                detalhes.value = 'Peso Saudável'
            elif 25 <= imc < 29.9:
                img_resultado.src = f"6.png"
                detalhes.value = 'Sobrepeso ou Pré-Obeso'
            elif 30 <= imc < 34.9:
                img_resultado.src = f"4.png"
                detalhes.value = 'Obeso'
            else:
                img_resultado.src = f"2.png"
                detalhes.value = 'Severamente obeso'
        else:
            if imc < 18.5:
                img_resultado.src = f"9.png"
                detalhes.value = 'Abaixo do peso'
            elif 18.5 <= imc < 24.9:
                img_resultado.src = f"7.png"
                detalhes.value = 'Peso Saudável'
            elif 25 <= imc < 29.9:
                img_resultado.src = f"5.png"
                detalhes.value = 'Sobrepeso ou Pré-Obeso'
            elif 30 <= imc < 34.9:
                img_resultado.src = f"3.png"
                detalhes.value = 'Obeso'
            else:
                img_resultado.src = f"1.png"
                detalhes.value = 'Severamente obeso'

        # Limpar os campos de entrada
        peso.value = ""
        altura.value = ""
        genero.value = ""

        # Atualizar a página
        page.update()