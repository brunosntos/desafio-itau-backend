import json
import datetime
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

memoria = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/transacao")
def carregar_transacoes():
    return jsonify({"dados": memoria}), 201


@app.route("/transacao", methods=["POST"])
def registrar_transcao():
    valor = request.get_json()
    dataHora = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3))).strftime("%Y-%m-%dT%H:%M:%S%:z")

    try:
        if valor is None:
            return jsonify({"mensagem": "O valor não pode estar vazio."}), 422

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

    data_formatada = str(dataHora).split("T")[0]
    data_formatada = data_formatada.split("-")
    data_formatada = f"{data_formatada[2]}/{data_formatada[1]}/{data_formatada[0]}"

    transacao = {
        "valor": valor,
        "dataHora": data_formatada
    }

    memoria.append(transacao)
    print(memoria)
    return jsonify({"dados": memoria,
                    "mensagem": "Transção feita com sucesso!"}), 201

@app.route("/transacao", methods=["DELETE"])
def limpar_transacoes():
    memoria.clear()
    print(memoria)

    return jsonify({"dados": memoria,
                    "mensagem": "Todas as transações foram apagadas!"}), 200

@app.route("/estatistica")
def estatistica():
    if len(memoria) == 0:
        dados = {
            "count": 0,
            "sum": 0,
            "avg": 0,
            "min": 0,
            "max": 0,
        }

        return jsonify({"dados": dados,
                        "mensagem": "Estatísticas exibidas com sucesso!"}), 200
    
        
    valores = [item["valor"] for item in memoria]

    dados = {
        "count": len(valores),
        "sum": sum(valores),
        "avg": round(float(sum(valores) / len(valores)), 2),
        "min": min(valores),
        "max": max(valores),
    }

    return jsonify({"dados": dados,
                    "mensagem": "Estatísticas exibidas com sucesso!"}), 200



if __name__ == "__main__":
    app.run(debug=True)