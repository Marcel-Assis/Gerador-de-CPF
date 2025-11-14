# Gerador de CPF (API em Flask)

Este projeto é uma API simples feita com **Python e Flask** que gera um CPF válido usando o cálculo dos dígitos verificadores.  
A ideia é ter uma rota que retorna um CPF aleatório sempre que for acessada.

---

## Como funciona

- Gera os 9 primeiros dígitos de forma aleatória  
- Evita sequências repetidas (ex: 000000000)  
- Calcula o 1º e o 2º dígito verificador  
- Retorna o CPF completo em JSON

---

## Rota disponível

### `GET /cpf`

Retorna algo assim:

```json
"12345678909"
```

---

## Estrutura do arquivo

O código principal está assim:

```
app.py
```

Ele contém:
- A função que gera o CPF
- A validação
- A rota `/cpf`
- A inicialização do Flask

---

## Como rodar

Basta executar:

```bash
python app.py
```

A API ficará disponível em:

```
http://127.0.0.1:5000/cpf
```

---

## Observação

Este projeto é simples e foi feito apenas para estudo e prática com Python, lógica e Flask.

