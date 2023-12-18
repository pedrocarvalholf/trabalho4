from flask import Flask, request, jsonify
import os

app = Flask(__name__)

def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

def calcular_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = [0, 1]
        while len(fib_series) < n:
            fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

@app.route('/api/calculos', methods=['POST'])
def realizar_calculos():
    try:
        # Obtemos os dados de entrada do corpo da solicitação como JSON
        dados_entrada = request.get_json()

        # Verificamos se o campo 'tipo' está presente e é válido
        if 'tipo' not in dados_entrada or dados_entrada['tipo'] not in ['fatorial', 'fibonacci']:
            raise ValueError('Tipo de cálculo inválido. Escolha entre "fatorial" ou "fibonacci".')

        tipo_calculo = dados_entrada['tipo']

        # Se o tipo de cálculo for fatorial
        if tipo_calculo == 'fatorial':
            # Verificamos se o campo 'numero' está presente
            if 'numero' not in dados_entrada:
                raise ValueError('O campo "numero" é obrigatório para o cálculo fatorial.')
            numero = dados_entrada['numero']
            resultado = calcular_fatorial(numero)
            return jsonify({'resultado': resultado})

        # Se o tipo de cálculo for Fibonacci
        elif tipo_calculo == 'fibonacci':
            # Verificamos se o campo 'quantidade' está presente
            if 'quantidade' not in dados_entrada:
                raise ValueError('O campo "quantidade" é obrigatório para o cálculo Fibonacci.')
            quantidade = dados_entrada['quantidade']
            resultado = calcular_fibonacci(quantidade)
            return jsonify({'resultado': resultado})

    # Capturamos exceções para lidar com possíveis erros durante a execução
    except Exception as e:
        # Retornamos uma resposta JSON indicando o erro ocorrido
        return jsonify({'erro': str(e)}), 400

if __name__ == '__main__':
    # Use uma chave secreta única para assinar os cookies da sessão
    app.secret_key = os.urandom(24)
    # Iniciamos o aplicativo Flask em modo de depuração
    app.run(debug=True)
