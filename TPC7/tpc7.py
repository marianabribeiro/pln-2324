from flask import Flask, render_template, request
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
    if designacao in conceitos:
        conceito_atual=conceitos[designacao]
        
        return render_template("descricao.html", conceito=(conceito_atual, designacao))
    else:
        return render_template("erro.html", erro="Conceito não existe na nossa base de dados")

@app.route("/conceitos", methods=["POST"])
def adicionar_Conceitos():
    conceito=request.form.get("conceito")
    traducaoEN=request.form.get("traducaoEN")
    descricao=request.form.get("descricao")

    #if conceito not in conceitos: # faz so o adicionar
    #adiciona e faz update tb
    conceitos[conceito]={"descricao": descricao, "en": traducaoEN}
    
    return render_template("conceitos.html", conceitos=conceitos)


@app.route("/pesquisar_conceito", methods=["POST"])
def pesquisar_conceito():
    palavra = request.form.get("info")
    
    if palavra is not None and palavra.strip():  
        resultados = []
        for conceito in conceitos:
            descricao = conceitos[conceito]["descricao"]  
            if palavra.lower() in conceito.lower() or palavra.lower() in descricao.lower():
                resultados.append({'conceito': conceito, 'descricao': descricao})
        return render_template("conceitos.html", resultados=resultados, palavra=palavra)
    else:
        return render_template("conceitos.html", resultados=[], palavra="")
    

import os
@app.route("/conceitos/<designacao>", methods=["DELETE"])
def delete_conceitos(designacao):
    
    os.rename("conceitosTrad.json", "conceitos_backup.json")

    del conceitos[designacao]
    
    file_out=open("conceitosTrad.json", "w")
    json.dump(conceitos, file_out, indent=4, ensure_ascii=False)
    file_out.close()
    
    return render_template("conceitos.html", conceitos=conceitos)



@app.route("/table")
def table():
    return render_template("table.html", conceitos=conceitos)


app.run(host="localhost", port=4002, debug=True)
