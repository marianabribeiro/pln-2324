import unicodedata


# Função auxiliar que permite a remoção de acentos das strings
def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

# Abertura e Leitura do ficheiro
filename = "CIH Bilingual Medical Glossary English-Spanish.txt"
file = open(filename,'r', encoding='utf-8')
text = file.read()

# Remover pontuação, carateres
text = text.replace(".", " ")
text = text.replace(",", " ")
text = text.replace("-", " ")
text = text.replace("/", " ")
text = text.replace(")", " ")
text = text.replace("(", " ")
text=remove_accents(text)
# ...

text = text.lower()

# dividir o texto por tokens/termos
# .split() separa por espaços/tabs/paragrafos

tokens = text.split()

# remover repetidos
tokens = list(set(tokens))

# para cada termo do dicionário verifica-se é anagrama das chaves do dicionário
# se o token é um anagrama, é adicionado aos valores do dic da chave (=token ordenado)
# se não é anagrama de nenhuma chave do dicionário, cria-se a chave(=token ordenado) e o valor (=lista com o token)

anagramas = {}
for token in tokens:
    # ordenar o token
    token_ordenado = ''.join(sorted(token))

    # Verificar se a chave já existe no dicionário
    if token_ordenado not in anagramas.keys():
        anagramas[token_ordenado] = [token]
    else:
        anagramas[token_ordenado].append(token)

print(anagramas)