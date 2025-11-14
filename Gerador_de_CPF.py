import re
import sys
import random
from fastapi import FastAPI

def gerarCPF():
    # Gerar um CPF aleatório
    cpf_input = ''
    for i in range(9):
      cpf_input += str(random.randint(0, 9))
    # Retirar tudo o que não for números usando expressão regular
    cpf = re.sub(
      r'[^0-9]',
      '',
      cpf_input
    )
    # Verificar se é uma sequência de caracteres. Ex: 111111111
    entrada_eh_sequencial = cpf_input == cpf_input[0] * len(cpf_input)
    if entrada_eh_sequencial:
      print("Você enviou dados sequenciais.")
      sys.exit()
    # Gerar o primeiro dígito
    nove_digitos = cpf[:9]
    contador_regressivo_1 = 10
    soma_1 = 0
    for digito in range(0, 9):
      soma_1 += int(nove_digitos[digito]) * contador_regressivo_1
      contador_regressivo_1 -= 1
    digito_1 = (soma_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0
    # Gerar o segundo dígito
    dez_digitos = cpf + str(digito_1)
    contador_regressivo_2 = 11
    soma_2 = 0
    for digito in range(0, 10):
      soma_2 += int(dez_digitos[digito]) * contador_regressivo_2
      contador_regressivo_2 -= 1
    digito_2 = (soma_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0
    # Mostrar o CPF na tela
    cpf_final = f'{cpf}{digito_1}{digito_2}'
    return cpf_final


  

# Criar rota api
app = FastAPI()
@app.get("/cpf")
async def cpf():
  return gerarCPF()

# comando pra abrir o servidor -> uvicorn Gerador_de_CPF:app --reload
# rota -> http://127.0.0.1:8000/cpf
# Swagger UI -> http://127.0.0.1:8000/docs#