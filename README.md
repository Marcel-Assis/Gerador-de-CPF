# Gerador de CPF (API)

Um projeto simples em Python usando Flask para gerar CPFs válidos aleatórios através de uma API.
O objetivo principal é estudar lógica, expressões regulares, criação e exposição de APIs e praticar conceitos de backend.

---

## Como funciona

A API possui um único endpoint:

GET /cpf

Ele retorna um CPF válido em formato JSON, por exemplo:

"58301924780"

O cálculo segue exatamente as regras oficiais dos dígitos verificadores.

---

## Dependências

Conteúdo do requirements.txt:

flask
gunicorn

---

## Rodando localmente

Para testar localmente antes de expor a API:

python Gerador_de_CPF.py

A API ficará disponível em:

http://127.0.0.1:5000/cpf

---

## Rodando publicamente

Este projeto foi pensado também para ser exposto publicamente como um pequeno serviço backend.
Ao disponibilizar a API online, qualquer pessoa pode fazer requisições ao endpoint `/cpf` e receber um CPF válido como resposta, facilitando testes, estudos ou integrações simples.

Ele também foi hospedado com a ajuda do Render através do plano gratuito:
https://gerador-de-cpf.onrender.com/

---

## Detalhes da lógica

A lógica de geração funciona assim:

1. Gera 9 dígitos aleatórios.
2. Evita sequências repetidas (ex.: 111111111).
3. Calcula o primeiro dígito verificador.
4. Calcula o segundo dígito verificador.
5. Retorna o CPF final (11 dígitos).

---

## Observação

Este projeto é simples e foi feito apenas para estudo e prática com Python, lógica e Flask.

