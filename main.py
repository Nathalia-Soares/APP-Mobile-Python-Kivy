# App Import, builder (GUI)

from kivy.app import App
from kivy.lang import Builder
import requests

# Create App

GUI = Builder.loaf_file("tela.kv")

# Create Build Function

class MeuAplicativo(App):
    def build(self):
        return GUI
    
    def on_start(self):
        self.root.ids["moeda1"].text = f"Dólar R${self.cotacao('USD')}"
        self.root.ids["moeda2"].text = f"Euro R${self.cotacao('EUR')}"
        self.root.ids["moeda3"].text = f"Bitcoin R${self.cotacao('BTC')}"
        self.root.ids["moeda4"].text = f"Ethereum R${self.cotacao('ETH')}"

    def cotacao(self, moeda):
       link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
       requisicao = requests.get(link)
       dicio_requisicao = requisicao.json()
       cotacao_atual = dicio_requisicao[f"{moeda}BRL"]["bid"]
       return cotacao_atual

MeuAplicativo().run()