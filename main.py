import math
import string
import secrets

def gerar_senha(tamanho):
    if tamanho is None or tamanho <= 0:
        return "Erro: tamanho inválido"

    alfabeto = string.ascii_letters + string.digits + string.punctuation  # Inclui caracteres especiais
    senha = ''.join(secrets.choice(alfabeto) for _ in range(tamanho))
    
    return senha

def verifica_seguranca(senha):
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

def main():
    setores = {
        'Administracao': 20,
        'TI': 30,
        'Producao': 15,
    }

    rodando = True
    while rodando:
        print('\n\t<--- GERADOR DE SENHAS --->')
        print('Digite o numero do setor correspondente:')

        setor_nomes = list(setores.keys())  # Lista com os nomes dos setores
        for count, key in enumerate(setor_nomes):
            print(f'\t{count + 1} - {key}')

        try:
            setor_index = int(input('-> ')) - 1  # Ajustando indice
            if setor_index not in range(len(setor_nomes)):
                print('Setor inválido! Escolha um numero válido.')
                continue
        except ValueError:
            print('Digite um valor inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('O usuário decidiu sair...')
            return

        # Obtendo o nome correto do setor
        setor_nome = setor_nomes[setor_index]
        tamanho_senha = setores[setor_nome]

        print('Gerando sua senha...')
        super_secret_password = gerar_senha(tamanho_senha)

        if super_secret_password.startswith("Erro"):
            print(super_secret_password)
            continue

        print('Deseja visualizar sua senha? (s/n)')
        visualizar = input('').strip().lower()
        if visualizar == 's':
            print(f'Sua senha e:\n-> {super_secret_password}')
        
        print('Deseja saber o nivel de segurança dela? (s/n)')
        visualizar = input('').strip().lower()
        if visualizar == 's':
            print(f"O nivel de segurança de sua senha:\n-> {verifica_seguranca(super_secret_password)} bits de entropia")

if __name__ == '__main__':
    main()
