
import re

# Abertura do ficheiro previamente convertido para txt
f=open("pln-2324\TPC3\dicionario_medico.txt",'r',encoding='utf-8')
texto=f.read()

# Tratamento dos dados - retirar os \f
#texto=re.sub(r"\f",'',texto)  # esta solução não cobre todos os problemas

texto=re.sub(r"(\f|\n\f)", "",texto) # Corrige a ocorrência de \f a meio das descrições dos termos

# Marcar designações com @
texto=re.sub(r"\n\n(.+)",r"\n\n@\1",texto)
texto=re.sub(r"@(.+)\n\n@",r"@\1\n",texto)


# Uma solução para a divisão dos termos e descricoes seria através de um dicionário
# no qual cada chave seria um termo e os valors os seus significados/descricoes
blocos=re.split(r"@", texto)
dic={}
td=[]
for bloco in blocos:
    td=re.split(r"\n", bloco, maxsplit=1)  
    designacao=td[1]
    dic[td[0]]=designacao
print(dic)
# para utilizar para gerar html seria apenas necessário correr o dicionário e para cada par chave, valor 
# e adicioná-lo ao body do html

# Outra solução mais interessante em termos de expressões regulares é a seguinte
termos=[]
termos= re.findall(r"@(.+)\n([^@]+)\n\n", texto) ## os 2 grupos de captura retorna ums lista de tuplo dá as termos e as descricoes


############################
# Gerar HTML 0 - Básico
############################
html_content=""
html_content += "<h1>Dicionário Médico</h1>\n"
html_content+="<body>"
for termo in termos:
    html_content+=f"<h5>{termo[0]}</h5>"
    html_content+=f"<p>{termo[1]}</p>"
html_content+="</body>"


html_content += "</body>\n</html>"
file_out=open("pln-2324\TPC3\html0.html", "w")
file_out.write(html_content)
file_out.close()

############################
# Gerar HTML 1 - Simples
############################

titulo1="<h3> Dicionário Médico </h3>"
descricao1= "<p> Este é um dicionário médico desenvolvido na unidade curricular PLN </p>"
body1="<body>"
for termo in termos:
   body1 += f"<h5> {termo[0]}</h5>"
   body1 += f"<p> {termo[1]} </p>"
   body1 += "<hr/>"
body1 +="</body>"

html1= titulo1 + descricao1+body1
file_out1=open("pln-2324\TPC3\html1.html","w",encoding='utf-8')
file_out1.write(html1)
file_out1.close()

############################
# Gerar HTML 2 - Tabela
############################

titulo2 = "<h3> Dicionário Médico </h3>"
descricao2 = "<p> Este é um dicionário médico desenvolvido na unidade curricular PLN </p>"
body2 = "<body><table border='1'><tr><th>Termo</th><th>Descrição</th></tr>"
for termo in termos:
    body2 += f"<tr><td>{termo[0]}</td><td>{termo[1]}</td></tr>"
body2 += "</table></body>"

html2 = titulo2 + descricao2 + body2

file_out2 = open("pln-2324\TPC3\html2.html", "w", encoding='utf-8')
file_out2.write(html2)
file_out2.close()

############################
# Gerar HTML 3 -  Utilização os estilos CSS
############################

titulo3 = "<h3 style='color:#cc9900; text-align:center;'> Dicionário Médico </h3>"
descricao3 = "<p style='color:black;'> Este é um dicionário médico desenvolvido na unidade curricular PLN </p>"
body3 = "<body style='background-color:#ffffcc;'><table border='1' style='border-collapse: collapse;'><tr><th style='color:#cc9900; background-color:black; padding: 10px;'>Termo</th><th style='color:#cc9900; background-color:black; padding: 10px;'>Descrição</th></tr>"
for termo in termos:
    body3 += f"<tr><td style='color:black; padding: 10px;'>{termo[0]}</td><td style='color:black; padding: 10px;'>{termo[1]}</td></tr>"
body3 += "</table></body>"

html3 = titulo3 + descricao3 + body3

file_out3 = open("pln-2324\TPC3\html3.html", "w", encoding='utf-8')
file_out3.write(html3)
file_out3.close()

############################
#Gerar HTML 4 - 
#Tentativa de Utilização de ficheiro de estilos CSS
############################

titulo4 = "<h3> Dicionário Médico </h3>"
descricao4 = "<p> Este é um dic médico desenvolvido na unidade curricual PLEB </p>"
body4 = "<body><table border='1'><tr><th>Termo</th><th>Descrição</th></tr>"
for termo in termos:
    body4 += f"<tr><td>{termo[0]}</td><td>{termo[1]}</td></tr>"
body4 += "</table></body>"

css_link = "<link rel='stylesheet' type='text/css' href='pln-2324\TPC3\styles.css'>"

html4 = f"<html><head>{css_link}</head><body>{titulo4}{descricao4}{body4}</body></html>"


file_out4 = open("pln-2324\TPC3\html4.html", "w", encoding='utf-8')
file_out4.write(html4)
file_out4.close()

