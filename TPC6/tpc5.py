from flask import Flask, render_template
import json

file=open(r'C:\Users\Mariana Ribeiro\Desktop\ProcLingNat\pln-2324\TPC5\conceitosTrad.json', 'r', encoding="utf-8")
conceitos=json.load(file)
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/conceitos")
def listar_Conceitos():
    return render_template("conceitos.html", conceitos=conceitos)



@app.route("/conceitos/<designacao>")
def consultar_Conceitos(designacao):
    conceito_atual=conceitos[designacao]
    return render_template("descricao.html", conceito=(conceito_atual, designacao))

#@app.route("/conceitos/<designacao>", methods=["PUT"])
#def editar_Conceitos(designacao):


app.run(host="localhost", port=4002, debug=True)
