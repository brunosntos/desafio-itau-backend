import json
import datetime
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

memoria = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/transacao", methods=["POST"])
def registrar_transcao():
    valor = request.get_json()
    dataHora = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3))).strftime("%Y-%m-%dT%H:%M:%S%:z")

    try:
        if "," in str(valor):
            valor = str(valor).replace(".", "").replace(",", ".")
            valor = float(valor)
        else:
            valor = float(valor)

        if valor < 0:
            return jsonify({"mensagem": "O valor digitado não pode ser negativo"}), 422
        
        valor = round(valor, 2)
    
    except:
        mensagem = "Erro! O valor digitado não é valido."
        return jsonify({"mensagem": mensagem}), 400

    transacao = {
        "valor": valor,
        "dataHora": dataHora
    }

    memoria.append(transacao)
    return jsonify({"mensagem": "Transção feita com sucesso!"}), 201


if __name__ == "__main__":
    app.run(debug=True)