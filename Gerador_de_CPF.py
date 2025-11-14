import re
import random
from flask import Flask, jsonify, render_template


def gerar_cpf_valido():
    """Gera um CPF válido aleatório."""

    # Gerando os 9 dígitos base (primeira parte do CPF)
    cpf_base = ''.join(str(random.randint(0, 9)) for _ in range(9))

    cpf_numeros = re.sub(r'[^0-9]', '', cpf_base)
    
    # Previne sequências raras de números repetidos
    if cpf_numeros == cpf_numeros[0] * len(cpf_numeros):
        return gerar_cpf_valido() 

    # --- Cálculo do 1º Dígito ---
    
    nove_digitos = cpf_numeros[:9]
    soma_1 = 0
    
    # Loop para aplicar os pesos de 10 a 2
    for i, digito in enumerate(nove_digitos):
        soma_1 += int(digito) * (10 - i)
        
    digito_1 = (soma_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0
    
    # --- Cálculo do 2º Dígito ---

    dez_digitos = cpf_numeros + str(digito_1)
    soma_2 = 0
    
    # Loop para aplicar os pesos de 11 a 2
    for i, digito in enumerate(dez_digitos):
        soma_2 += int(digito) * (11 - i)
        
    digito_2 = (soma_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    return f'{cpf_numeros}{digito_1}{digito_2}'

# --- API e Frontend ---

app = Flask(__name__)

# NOVA ROTA: Serve o Frontend na raiz (/)
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cpf", methods=['GET'])
def cpf_endpoint():
    # Rota da API que retorna o CPF em formato JSON
    return jsonify(gerar_cpf_valido())

# Para rodar localmente
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)