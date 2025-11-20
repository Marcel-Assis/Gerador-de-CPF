# Gerador de CPF (API)

Um projeto simples em Python usando Flask para gerar CPFs válidos aleatórios através de uma API.
O objetivo principal é estudar lógica, expressões regulares, criação e exposição de APIs e praticar conceitos básicos de backend.

---

## Como funciona

A API possui um único endpoint:

GET /cpf

Ele retorna um CPF válido em formato JSON, por exemplo:
"58301924780"

O cálculo segue as regras oficiais dos dígitos verificadores.

---

## Dependências

Arquivo requirements.txt:

flask
gunicorn

---

## Rodando localmente

Para testar o projeto no seu computador, siga exatamente estes passos:

1) Criar o ambiente virtual:
python -m venv venv

2) Ativar o ambiente virtual:
- Windows:
  venv\Scripts\activate
- Linux/Mac:
  source venv/bin/activate

3) Instalar as dependências dentro do venv:
pip install -r requirements.txt

(Importante: certifique-se de que o venv está ativado antes de instalar.)

4) Rodar a API:
python Gerador_de_CPF.py

Se tudo deu certo, você verá algo como:
Running on http://127.0.0.1:5000

5) Testar no navegador:
http://127.0.0.1:5000/cpf

---

## Rodando publicamente

Este projeto também foi pensado para funcionar como uma pequena API pública.
Ao acessá-lo, qualquer pessoa pode fazer requisições ao endpoint `/cpf` e receber um CPF válido como resposta.

A API está hospedada gratuitamente no Render:
https://gerador-de-cpf.onrender.com

https://gerador-de-cpf.onrender.com/cpf


---

## Detalhes da lógica

1. Gera 9 dígitos aleatórios.
2. Evita sequências repetidas (ex.: 111111111).
3. Calcula o primeiro dígito verificador.
4. Calcula o segundo dígito verificador.
5. Monta o CPF final (11 dígitos).

---

## Observação

Este é um projeto de estudo, feito para treinar Python, lógica e conceitos básicos de Flask e APIs.
