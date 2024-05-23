class Automato:
    def __init__(self):
        self.transitions = {
            'q0': {'quem': 'q1', 'qual': 'q1', 'quanto': 'q1', 'onde': 'q1'},
            'q1': {'ser': 'q2', 'o': 'q3', 'a': 'q3'},
            'q2': {'motorista': 'q4', 'rota': 'q5', 'valor': 'q6', 'corrida': 'q7',
                   'carro': 'q8', 'placa': 'q9', 'forma': 'q10', 'pagamento': 'q11',
                   'tempo': 'q12', 'viagem': 'q13', 'querer': 'q14', 'chegar': 'q15',
                   'encontrar': 'q16'},
            'q3': {'motorista': 'q4', 'rota': 'q5', 'valor': 'q6', 'corrida': 'q7',
                   'carro': 'q8', 'placa': 'q9', 'forma': 'q10', 'pagamento': 'q11',
                   'tempo': 'q12', 'viagem': 'q13', 'destino': 'q17', 'querer': 'q14',
                   'chegar': 'q15', 'encontrar': 'q16'},
            'q4': {},
            'q5': {},
            'q6': {},
            'q7': {},
            'q8': {},
            'q9': {},
            'q10': {},
            'q11': {},
            'q12': {},
            'q13': {},
            'q14': {'um': 'q18'},
            'q15': {},
            'q16': {'o': 'q19'},
            'q17': {'ser': 'q20'},
            'q18': {'corrida': 'q7'},
            'q19': {'motorista': 'q4'},
            'q20': {'o': 'q3'}
        }
        self.start_state = 'q0'
        self.accept_states = ['q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q18', 'q19', 'q20']
        
    def process_input(self, tokens):
        current_state = self.start_state
        for token in tokens:
            if token in self.transitions[current_state]:
                current_state = self.transitions[current_state][token]
            else:
                return False
        return current_state in self.accept_states

# Criando o autômato
automato = Automato()

# Testando com algumas frases de exemplo
frases = [
    ["quem", "ser", "o", "motorista"],
    ["qual", "ser", "a", "rota"],
    ["qual", "o", "valor", "de", "o", "corrida"],
    ["qual", "ser", "o", "carro"],
    ["qual", "a", "placa", "de", "o", "carro"],
    ["qual", "o", "forma", "de", "pagamento"],
    ["querer", "um", "corrida"],
    ["onde", "encontrar", "o", "motorista"],
    ["onde", "ser", "o", "destino"]
]

for frase in frases:
    print(f"Analisando a frase: {frase}")
    print(automato.process_input(frase))
