🪙 Conversor de Moedas com Python + CustomTkinter

Este projeto é um conversor de moedas feito em Python utilizando:

CustomTkinter (interface moderna)

AwesomeAPI (cotações em tempo real)

XML para armazenar:

Lista de moedas disponíveis

Conversões possíveis entre moedas

O objetivo é fornecer uma interface simples, intuitiva e elegante para converter valores entre diferentes moedas.

🚀 Funcionalidades

✔ Interface moderna usando CustomTkinter
✔ Cotação em tempo real usando a AwesomeAPI
✔ Atualização automática da lista de moedas de destino
✔ Lista rolável com todas as moedas disponíveis
✔ Arquivos XML para configurar moedas e conversões
✔ Código organizado e totalmente comentado

🖥 Pré-requisitos

Antes de executar, instale as dependências:

pip install requests
pip install customtkinter
pip install xmltodict

📂 Estrutura dos Arquivos
/
├── main.py                  # Interface principal (CustomTkinter)
├── pegar_cotacao.py         # Função que consulta a API
├── pegar_moedas.py          # Leitor dos arquivos XML
├── moedas.xml               # Lista de moedas disponíveis
├── conversoes.xml           # Lista de pares de conversão
└── README.md


🧩 Funcionamento do Sistema
🔹 1. moedas.xml

Arquivo contendo todas as moedas disponíveis.

Exemplo:

<xml>
    <USD>Dólar Americano</USD>
    <BRL>Real Brasileiro</BRL>
    <EUR>Euro</EUR>
</xml>

🔹 2. conversoes.xml

Define quais conversões são possíveis.

Exemplo:

<xml>
    <USD-BRL/>
    <BRL-USD/>
    <USD-EUR/>
</xml>

🔹 3. pegando cotação

A cotação é obtida pela URL:

https://economia.awesomeapi.com.br/last/USD-BRL

📸 Print da Interface (opcional)

Se quiser, posso gerar uma imagem de preview e adicionar aqui. :)

▶ Como executar

No terminal, execute:

python main.py


E a interface irá abrir automaticamente.

🧠 Lógica Interna
Conversões disponíveis

Cria um dicionário assim:

{
  "USD": ["BRL", "EUR"],
  "BRL": ["USD"]
}

Conversão de moeda

A aplicação faz:

cotacao = pegar_cotacao_moeda("USD", "BRL")


E exibe:

1 USD = 5.12 BRL
