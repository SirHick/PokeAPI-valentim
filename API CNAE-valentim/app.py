import requests
from flask import Flask, jsonify

app = Flask(__name__)


url = "https://servicodados.ibge.gov.br/api/v2/cnae"


@app.route("/classes")
def obter_classe():
    resposta = requests.get(f"{url}/classes")
    return jsonify(resposta.json()), resposta.status_code

@app.route("/classes/<string:classe_id>")
def obter_id_classe(classe_id):
    resposta = requests.get(f"{url}/classes/{classe_id}")
    return jsonify(resposta.json()), resposta.status_code

@app.route("/subclasses")
def obter_subclasses():
    resposta = requests.get(f"{url}/subclasses")
    return jsonify(resposta.json()), resposta.status_code

@app.route("/subclasses/<string:subclasse_id>")
def obter_id_subclasse(subclasse_id):
    resposta = requests.get(f"{url}/subclasses/{subclasse_id}")
    return jsonify(resposta.json()), resposta.status_code

@app.route("/secoes")
def obter_secao():
    resposta = requests.get(f"{url}/secoes")
    return jsonify(resposta.json()), resposta.status_code

@app.route("/secoes/<string:secao_id>")
def obter_id_secao(secao_id):
    secao_formatada = secao_id.upper()
    resposta = requests.get(f"{url}/secoes/{secao_formatada}")
    return jsonify(resposta.json()), resposta.status_code


if __name__ == '__main__':
    app.run(debug=True)