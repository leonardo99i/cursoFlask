#Importação da biblioteca do framework Flask
from flask import Flask

#Determina a classe
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

#Inicia a instancia se essa for a classe main
if __name__ == "__main__":
    app.run()