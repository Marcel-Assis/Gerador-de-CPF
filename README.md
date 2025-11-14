# Gerador de CPF (API)

Um projeto simples em Python usando Flask para gerar CPFs válidos de forma aleatória através de uma API.
O objetivo é treinar lógica, expressões regulares e desenvolvimento de API.

---

## Como funciona

A API possui um único endpoint:

GET /cpf

Ele retorna um CPF válido em formato JSON, exemplo:

"58301924780"

O algoritmo calcula corretamente os dois dígitos verificadores seguindo as regras oficiais.

---

## Estrutura do Projeto

/
├── Gerador_de_CPF.py       # Arquivo principal com Flask e gerador de CPF
├── requirements.txt        # Dependências do projeto
├── README.md               # Este arquivo
└── venv/                   # Ambiente virtual (não deve ser enviado para o GitHub)

---

## Dependências

Conteúdo do requirements.txt:

flask
gunicorn

---

## Rodando localmente

Para testar o projeto localmente:

python Gerador_de_CPF.py

A API ficará disponível em:

http://127.0.0.1:5000/cpf

---

## Sobre a API

Quando acessado, o endpoint retorna um CPF totalmente válido.  
O algoritmo funciona assim:

1. Gera 9 dígitos aleatórios.
2. Evita sequências repetidas (ex.: 111111111).
3. Calcula o primeiro dígito verificador.
4. Calcula o segundo dígito verificador.
5. Retorna o CPF final (11 dígitos).
