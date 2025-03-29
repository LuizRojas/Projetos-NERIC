from gerador import Gerador
import secrets
import string
import math


def main():

    gdr = Gerador()

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
        super_secret_password = gdr.gerar_senha(tamanho_senha)

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
            print(f"O nivel de segurança de sua senha:\n-> {gdr.verifica_seguranca(super_secret_password)} bits de entropia")

if __name__ == '__main__':
    main()
