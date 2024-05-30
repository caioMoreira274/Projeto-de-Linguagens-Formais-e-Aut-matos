from lematizar import lematizacao
from gramatica import analisar_frase
from automato_gramatica import Automato_Gramatica 
from automato_intencao import Automato_Intencao

automato_intencao = Automato_Intencao()
automato_gramatica = Automato_Gramatica()

frase = input("Digite uma frase: ")

lista_lematizada = lematizacao(frase)

frase_lematizada = " ".join(lista_lematizada)

print(f"A frase lematizada: {frase_lematizada}")
print()

#   Construa autômatos para extrair as palavras (tokens) da entrada
# que forma as frases e suas respectivas categorias. 
# Por exemplo, na "qual é o preço?", teríamos 4 tokens:
# qual (Pron), ser (Verb), o (Det), preço (Subs).
#   Depois de extraído o token o mesmo deve ser “tratado”,
# retornando o seu radical (processo conhecido como stemming) e categorizado.
#   Cabe ao grupo pesquisar alternativas para este tratamento.

print(f"A lista com os tokens: {lista_lematizada}")
print()

#Uma vez que os tokens tenham sido extraídos eles devem ser confrontados
# com a gramática para verificar se formam uma frase válida de acordo com as regras gramaticais.

print(f"Analisando a frase em relação à gramatica")
automato_gramatica.analisar_tokens_de_entrada(frase_lematizada)
analisar_frase(frase_lematizada)
print()

# Construa autômatos que representem intenções. 
#   Esses autômatos receberão como entrada os tokens
# da frases gramaticalmente corretas. 
# 'Uma outra possibilidade é já reconhecer as frases corretas
# e os estados finais já serem as “intenções”

print(f"Frase pelo autômato: ")
automato_intencao.analisar_frase(frase_lematizada)