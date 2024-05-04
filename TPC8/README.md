# TPC8

Processamento de Linguagem Natural - 4º ano Informática Médica

O objetivo do TPC8 foi a exploração das funções most_similar, doesnt_match e similarity e também a criação de analgias. Em primeiro lugar foi treinado o modelo com diferentes hiperparametros:
- epochs=20, vector_size=300
- epochs=20, vector_size=250
- epochs=20, vector_size=100
- epochs=15, vector_size=100
- epochs=5, vector_size=100

O melhor modelo desenvolvido parece ser o modelo treinado com epochs=5 e vector_size=100 uma vez que uma vez que o relaciona a palavra "harry" com outras personagens e não com palavras "random".

Posteriormenete, o melhor modelo foi guardado através da função save e carregado através da função load.

Assim, foi possível testar as diferentes funções para diferentes palavras nomeadamente, testou-se as palavras "most similar" a "harry", "potter", "magia", "trouxas", "grifinória", "sonserina" e "hagrid". Foram feitas analogias através da função analogias que faz o cálculo entre 3 palavras: model.wv.most_similar(positive=[y1, x2], negative=[x1]), isto é, y1+x2-x1.

Foram feitas então, analogias para os seguintes conjuntos de palavras:
- "harry", "hermione", "rony"
- "grifinória", "sonserina", "corvinal"
- "harry", "snape", "corvinal"
- "draco", "sonserina", "hermione"
- "harry", "sonserina", "dumbledore"
- "poção", "mione", "harry"

Para averiguar a similaridade de algumas palavras utilizou-se a função similarity, obtendo os seguintes resultados:
 Par de Palavras | Resultado de similaridade 
 ------- | -----
  "dumbledore", "harry" | 0.86465895 |
  "mione", "harry" | 0.9385708
  "potter", "harry" | 0.73286885
  "hermione", "rony" | 0.94747347
  "sonserina", "grifinória" | 0.98014
  "magia", "trouxas"   | 0.8559123
  "trouxas", "hermione" | 0.70220184
  "snape", "harry" | 0.8754602
  "snape", "hermione" | 0.88800305

Por fim, foi utilizada a função doesnt_match (que retorna a palavra mais afastada) para os seguintes conjuntos de palavras:
- "harry", "rony", "draco"
- "harry", "rony", "lúcio"
- "harry", "dudley", "draco"
- "dumbledore", "snape", "hagrid"
- "dumbledore", "grifinória", "hagrid"