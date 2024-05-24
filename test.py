import nltk
from nltk import CFG

# Definindo a gramática
gramatica = CFG.fromstring("""
    S -> Pron VP | Pron NP | NP VP | VP NP | 
    Pron -> "quem" | "qual" | "onde"
    NP -> Det Subs | Det Subs Prep NP | Det Subs Prep Subs | Prep Det Subs
    VP -> Verb | Verb NP | Verb Prep Subs | Verb NP Prep NP | Verb Prep NP | Verb Verb | Verb Det Subs Prep Subs
    Prep -> "de" | "o" | "a"
    Det -> "o" | "a" | "um"
    Subs -> "motorista" | "rota" | "valor" | "corrida" | "carro" | "placar" | "forma" | "pagamento" | "destino" 
    Verb -> "ser" | "querer" | "chegar" | "encontrar"
""")

# Criando o parser
parser = nltk.ChartParser(gramatica)

# Frases de exemplo
frases = [
    "quem ser o motorista",
    "qual ser a rota",
    "qual ser o carro",
    "onde ser o destino",
    "onde encontrar o motorista",
    "qual o valor de o corrida",
    "qual o forma de pagamento",
    "qual a placar de o carro",
    "querer um corrida"    
]

# Função para analisar as frases
def analisar_frases(frases, parser):
    for frase in frases:
        sentenca = frase.split()
        print(f"Analisando a frase: '{frase}'")
        try:
            parsed = False
            for arvore in parser.parse(sentenca):
                print('Frase aceita')
                arvore.pretty_print()
                parsed = True
            if not parsed:
                print("A frase não é reconhecida pela gramática.")
        except ValueError:
            print("A frase não é reconhecida pela gramática.")

# Analisando as frases de exemplo
analisar_frases(frases, parser)
