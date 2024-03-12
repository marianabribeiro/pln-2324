import json
import re

file_conceitos=open(r'C:\Users\Mariana Ribeiro\Desktop\ProcLingNat\pln-2324\TPC5\conceitos.json', encoding='utf-8')
file_livro=open(r"C:\Users\Mariana Ribeiro\Desktop\ProcLingNat\pln-2324\TPC5\LIVRO-Doenças-do-Aparelho-Digestivo.txt", encoding='utf-8')
file_traduzidos=open(r'C:\Users\Mariana Ribeiro\Desktop\ProcLingNat\pln-2324\TPC5\termos_traduzidos.txt', encoding='utf-8')
texto=file_livro.read()
conceitos=json.load(file_conceitos)


conc_trad={}
textoTrad=file_traduzidos.read()
textoTrad=re.findall(r'\n?(.+)\s@\s(.+)', textoTrad)

#conceitos traduzidos={conceito:traducao}
dictrad={tuple[0]:tuple[1] for tuple in textoTrad}


#conceitos_min={}
conceitos_min={}
for palavra in conceitos:
    if palavra in dictrad.keys():
        conceitos_min[palavra.lower()]={'descricao': conceitos[palavra], 'en':dictrad[palavra]} 
    else:
        conceitos_min[palavra.lower()]={'descricao': conceitos[palavra], 'en':""} 


blacklist=['para', 'de', 'pelos', 'por', 'e', 'Este']
def etiquetador(matched):
    palavra=matched[0]
    original=palavra
    palavra=palavra.lower()
    if palavra in conceitos_min and palavra not in blacklist:
        descricao=conceitos_min[palavra]['descricao']
        traducao="EN: "+conceitos_min[palavra]['en']+" - Descrição: "
        etiqueta=f"<a href='' title='{traducao}{descricao}'>{original}</a>"
        return etiqueta
    else: return original


expressao=r'[\wáçãêíúâ]+'
texto=re.sub(expressao, etiquetador, texto) #etiquetador recebe o que o padrao encontra commo uma lista
texto=re.sub(r'\n', '<br>', texto)
texto=re.sub(r'\f', '<hr>', texto)

file_out=open(r"C:\Users\Mariana Ribeiro\Desktop\ProcLingNat\pln-2324\TPC5\livro.html", "w", encoding='utf-8')
file_out.write(texto)

file_out2=open(r"C:\Users\Mariana Ribeiro\Desktop\ProcLingNat\pln-2324\TPC5\conceitosTrad.json", 'w')
json.dump(conceitos_min, file_out2, indent=4, ensure_ascii=False)

file_out3=open(r"C:\Users\Mariana Ribeiro\Desktop\ProcLingNat\pln-2324\TPC5\dic_Trad.json", 'w')
json.dump(dictrad, file_out3, indent=4, ensure_ascii=False)
