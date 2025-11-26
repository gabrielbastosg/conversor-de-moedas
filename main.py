import customtkinter
from pegar_moedas import nomes_moedas, conversoes_disponiveis
from pegar_cotacao import pegar_cotacao_moeda

# -----------------------------------------------------------
# * CONFIGURAÇÃO INICIAL DA JANELA
# -----------------------------------------------------------

# Define o tema escuro da interface
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Cria a janela principal
janela = customtkinter.CTk()
janela.geometry("600x600")  # Define o tamanho da janela

# Carrega as conversões possíveis (ex: USD -> EUR, BRL -> USD, etc.)
dic_conversoes_disponiveis = conversoes_disponiveis()

# -----------------------------------------------------------
# * CRIAÇÃO DOS ELEMENTOS VISUAIS (Labels, Botões, Menus)
# -----------------------------------------------------------

# Título principal
titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=("",20))

# Labels explicativos
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem")
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino")


# -----------------------------------------------------------
# * FUNÇÃO: Atualiza as moedas de destino conforme a moeda de origem selecionada
# -----------------------------------------------------------

def carregar_moedas_destino(moeda_selecionada):
    # Obtém a lista de moedas possíveis para conversão daquela moeda
    lista_moedas_destino = dic_conversoes_disponiveis[moeda_selecionada]

    # Atualiza o OptionMenu de destino com as novas opções
    campo_moeda_destino.configure(values=lista_moedas_destino)

    # Define a primeira moeda como padrão
    campo_moeda_destino.set(lista_moedas_destino[0])


# Menu de seleção da moeda de origem
campo_moeda_origem = customtkinter.CTkOptionMenu(
    janela,
    values=list(dic_conversoes_disponiveis.keys()),
    command=carregar_moedas_destino
)

# Menu de seleção da moeda de destino (inicialmente com mensagem)
campo_moeda_destino = customtkinter.CTkOptionMenu(
    janela,
    values=["Selecione uma moeda de origem"]
)

# -----------------------------------------------------------
# * FUNÇÃO: Converte a moeda selecionada ao clicar no botão
# -----------------------------------------------------------

def converter_moeda():
    moeda_origem = campo_moeda_origem.get()
    moeda_destino = campo_moeda_destino.get()

    # Só converte se ambos estiverem selecionados
    if moeda_origem and moeda_destino:
        # Chama a função que consulta a API (ou arquivo) e retorna a cotação
        cotacao = pegar_cotacao_moeda(moeda_origem, moeda_destino)

        # Atualiza o texto exibindo a cotação
        texto_cotacao_moeda.configure(
            text=f"1 {moeda_origem} = {cotacao} {moeda_destino}"
        )

# Botão que executa a conversão
botao_converter = customtkinter.CTkButton(
    janela, text="Converter", command=converter_moeda
)

# Frame rolável que mostrará a lista de moedas existentes
lista_moedas = customtkinter.CTkScrollableFrame(janela)

# Label que exibirá o resultado da conversão
texto_cotacao_moeda = customtkinter.CTkLabel(janela, text="")

# -----------------------------------------------------------
# * LISTA DE TODAS AS MOEDAS DISPONÍVEIS
# -----------------------------------------------------------

moedas_disponiveis = nomes_moedas()  # Dicionário { "USD": "Dólar Americano", ... }

# Cria um label para cada moeda dentro do frame rolável
for codigo_moeda in moedas_disponiveis:
    nome_moeda = moedas_disponiveis[codigo_moeda]
    texto_moeda = customtkinter.CTkLabel(
        lista_moedas,
        text=f"{codigo_moeda}: {nome_moeda}"
    )
    texto_moeda.pack()

# -----------------------------------------------------------
# * ORGANIZAÇÃO DOS ELEMENTOS NA TELA
# -----------------------------------------------------------

titulo.pack(padx=10, pady=10)
texto_moeda_origem.pack(padx=10, pady=10)
campo_moeda_origem.pack(padx=10)
texto_moeda_destino.pack(padx=10, pady=10)
campo_moeda_destino.pack(padx=10)
botao_converter.pack(padx=10, pady=10)
texto_cotacao_moeda.pack(padx=10, pady=10)
lista_moedas.pack(padx=10, pady=10)

# -----------------------------------------------------------
# * INICIALIZA A INTERFACE
# -----------------------------------------------------------
janela.mainloop()
