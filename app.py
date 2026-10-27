import requests
from flask import Flask

app = Flask(__name__)

nome = input("Digite o nome do pokemon desejado: ").lower()

url = f"https://pokeapi.co/api/v2/pokemon/{nome}"

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()

    # Extrai o nome de cada tipo na lista 'types'
    tipos = [t['type']['name'] for t in dados['types']]

    print(f"Pokémon: {dados['name']}")
    print(f"Altura: {dados['height']}")
    print(f"Peso: {dados['weight']}")
    print(f"Tipo(s): {', '.join(tipos)}")
else:
    print("Não foi possível encontrar o pokémon")