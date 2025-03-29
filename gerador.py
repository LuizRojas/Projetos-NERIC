import secrets
import string
import math


class Gerador():
    def __init__(self):
        self.setores = {
            'Administracao': 20,
            'TI': 30,
            'Producao': 15,
        }
    
    def gerar_senha(self, tamanho):
        if tamanho is None or tamanho <= 0:
            return "Erro: tamanho inválido"

        alfabeto = string.ascii_letters + string.digits + string.punctuation  # Inclui caracteres especiais
        senha = ''.join(secrets.choice(alfabeto) for _ in range(tamanho))
        
        return senha
    
    def verifica_seguranca(self, senha):
        tamanho = len(senha)
    
        # Verificar se a senha contem diferentes tipos de caracteres
        mu, mi, dgt = False, False, False
        for c in senha:
            if c.isupper():
                mu = True
            if c.islower():
                mi = True
            if c.isdigit():
                dgt = True

        # calculo da entropia
        if dgt and not (mi or mu):
            entropia = math.log2(10 ** tamanho)  # Apenas numeros (0-9)
        elif mi and not (mu or dgt):
            entropia = math.log2(26 ** tamanho)  # Apenas minusculas
        elif mu and mi and not dgt:
            entropia = math.log2(52 ** tamanho)  # Maiusculas + Minusculas
        elif mu and mi and dgt:
            entropia = math.log2(94 ** tamanho)  # Maiusculas + Minusculas + Digitos + Simbolos
        else:
            entropia = 0

        return entropia
