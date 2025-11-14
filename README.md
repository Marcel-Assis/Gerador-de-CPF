# Gerador de CPF com FastAPI

Este projeto é uma API simples desenvolvida em **Python** utilizando **FastAPI** para gerar números de **CPF válidos**.  
O algoritmo implementa todas as regras oficiais de validação, incluindo cálculo dos dois dígitos verificadores.

---

## 🚀 Tecnologias utilizadas

- **Python 3**
- **FastAPI**
- **Uvicorn**
- **Regex (re)**
- **Random**

---

## 📌 Funcionalidades

- Gera um CPF aleatório válido.
- Remove caracteres indesejados com regex.
- Evita CPFs compostos por números repetidos (ex: `11111111111`).
- Expõe uma rota HTTP para consumo da API.
- Disponibiliza documentação automática via Swagger UI.

---

## 📂 Estrutura

```text
📁 seu_projeto/
 ├── main.py        # Código principal da aplicação
 └── README.md      # Documentação
```

---

## 🧠 Lógica resumida

O algoritmo:

1. Gera 9 dígitos aleatórios.
2. Verifica se os dígitos formam uma sequência repetida.
3. Calcula o **1º dígito verificador** usando multiplicação regressiva de 10 a 2.
4. Calcula o **2º dígito verificador** usando multiplicação regressiva de 11 a 2.
5. Retorna o CPF final no formato:  
   ```
   NNNNNNNNNDD
   ```

---

## 🛠️ Como executar o projeto

### 1️⃣ Instale as dependências

```bash
pip install fastapi uvicorn
```

### 2️⃣ Rode o servidor

```bash
uvicorn Gerador_de_CPF:app --reload
```

> Certifique-se de que o arquivo principal se chama `Gerador_de_CPF.py`  
> ou ajuste o comando conforme o nome do seu arquivo.

---

## 🌐 Rotas disponíveis

### 📄 Gerar CPF

**GET**
```
http://127.0.0.1:8000/cpf
```

### 📘 Documentação automática (Swagger)

```
http://127.0.0.1:8000/docs
```

### 📙 Documentação alternativa (ReDoc)

```
http://127.0.0.1:8000/redoc
```

---

## 🧪 Exemplo de resposta

```json
{
  "cpf": "12345678909"
}
```

---

## 📜 Licença

Este projeto é de uso livre para estudo, modificação e distribuição.
