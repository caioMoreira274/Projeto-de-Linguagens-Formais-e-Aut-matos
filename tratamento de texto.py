import spacy
import string

texto = "Quais as formas de pagamento?"


# Carregar o modelo do spaCy para o português
nlp = spacy.load("pt_core_news_sm")

def lematizacao(texto):
    texto = texto.lower()
    # Remove a pontuação
    texto = texto.translate(str.maketrans('', '', string.punctuation))

    lista_de_palavras = texto.split()
    # Lista de palavras para lematização (retirar seu sentido puro)
    lista_de_palavras_lematizadas = []
    # Lematizar as lista_de_palavrasas
    for palavra in lista_de_palavras:
        doc = nlp(palavra)
        for token in doc:
            lista_de_palavras_lematizadas.append(token.lemma_)
    # retorne a lista de palavras lematizadas
    return lista_de_palavras_lematizadas



def excluir_palavras_repetidas_de_uma_lista():
    lista_para_analise = separar_texto_em_lista_de_palavras(texto)
    lista_para_analise = lematizacao(lista_para_analise)
    lista_nova = []
    for palavra in lista_para_analise:
        if palavra not in lista_nova:
            lista_nova.append(palavra)
        
    #lista_nova.sort()
        
    return lista_nova
   




print(lematizacao(texto))


