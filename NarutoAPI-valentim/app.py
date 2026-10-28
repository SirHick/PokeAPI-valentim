import requests
from flask import Flask

app = Flask(__name__)

nome = input("Digite o nome do personagem desejado: ").strip()

url = f"https://dattebayo-api.onrender.com/characters"

resposta = requests.get(url)

dados = resposta.json()

if resposta.status_code == 200:
    dados = resposta.json()

    print(f"Personagem: {dados.get['name']}")
    print(f"ID: {dados.get['id']}")
    print(f"Altura: {dados.get['height']}")
    print(f"Peso: {dados.get['weight']}")
else:
    print("Nenhum personagem encontrado com esse nome.")