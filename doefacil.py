#\n
import os

email_cadastrados = []
senha_cadastradas = []
telefone_cadastrados = []
nome_cadastrados = []
endereco_cadastrados = []
itens_doacao = []
itens_troca = []

#AQUI É A FUNCAO DE LOGIN, ONDE O USUARIO PODE DIGITAR SEU EMAIL E SENHA PARA ACESSAR O SISTEMA E ENTRA NA CONDICAO PARA VERIFICAR SE ESTA CADASTRADO
def login():
    while True:
        os.system('cls')
        print("""
        ╔══════════════════════════════╗
        ║          DOEFACIL            ║
        ╚══════════════════════════════╝
        """)
        print('Digite seu email cadastrado')
        email_cadastrado = input('Email: ')
        print('Digite sua senha cadastrada')
        senha_cadastrada = input('Senha: ')

        usuario_encontrado = False

        for i in range(len(email_cadastrados)):
            if email_cadastrado == email_cadastrados[i] and senha_cadastrada == senha_cadastradas[i]:
                print('Login realizado com sucesso!')
                usuario_logado(i)
                usuario_encontrado = True
                break
        else:
            print('Senha ou email incorretos, tente novamente!')
            print('1- Cadastrar novo usuário')
            print('2- Deseja tentar novamente ')
            opcao = input('Escolha uma opção: ')
            if opcao == '1':
                cadastrar_usuario()
            elif opcao == '2':
                continue
            else:
                break
        break


#FUNCAO DE CADASTRO DE USUARIO PARA LOGIN E SUAS INFORMACOES
def cadastrar_usuario():
    os.system('cls')
    print('=====CADASTRO DE USUÁRIO=====\n')
    print('Digite seu email para cadastro')
    email_cadastrado = input('Email: ')
    email_cadastrados.append(email_cadastrado)
    print('Digite sua senha para cadastro')
    senha_cadastrada = input('Senha: ')
    senha_cadastradas.append(senha_cadastrada)
    print('Digite seu telefone para cadastro')
    telefone_cadastrado = input('Telefone: ')
    telefone_cadastrados.append(telefone_cadastrado)
    print('Digite seu nome para cadastro')
    nome_cadastrado = input('Nome: ')
    nome_cadastrados.append(nome_cadastrado)
    print('Digite seu endereço para cadastro')
    endereco_cadastrado = input('Endereço: ')
    endereco_cadastrados.append(endereco_cadastrado)
    print(f'Usuário {email_cadastrado} cadastrado com sucesso!')
    login()
    

#AQUI É A FUNCAO DE USUARIO LOGADO, ONDE O USUARIO PODE ESCOLHER SUAS OPÇÕES DE PERFIL
def usuario_logado(i):
    os.system('cls')
    print(f'Bem-vindo, {nome_cadastrados[i]}!\n')
    print('1 ver perfil')
    print('2- fazer doação')
    print('3- oferta de trocas')
    print('4- Itens disponíveis para doação')
    print('5- Voltar ao login')
    print('6- Sair do programa')
    opcao = int(input('Escolha uma opção: '))
    opcao_usuario(opcao, i)


def opcao_usuario(opcao, i):
    if opcao == 1:
        perfil_usuario(i)
    elif opcao == 2:
        fazer_doacao(i)
    elif opcao == 3:
        oferta_trocas(i)
    elif opcao == 4:
        intens_disponiveis(i)
    elif opcao == 5:
        login()
    elif opcao == 6:
        fechar_programa()
    else:
        print('Opção inválida!')


#AQUI É A FUNCAO DE PERFIL DO USUARIO, ONDE ELE PODE VER SUAS INFORMACOES CADASTRADAS
def perfil_usuario(i):
    os.system('cls')
    print(f'=====PERFIL DO USUÁRIO {nome_cadastrados[i]}=====\n')
    print(f'Email: {email_cadastrados[i]}')
    print(f'Senha: {senha_cadastradas[i]}')
    print(f'Telefone: {telefone_cadastrados[i]}')
    print(f'Nome: {nome_cadastrados[i]}')
    print(f'Endereço: {endereco_cadastrados[i]}\n')
    input('Pressione Enter para voltar ao menu principal...')
    usuario_logado(i)

#FALTA IMPLEMENTAR A FUNCAO DE TER A OPCAO DE OU LIBERAR PARA DOACAO OU TROCA, OU SEJA, O USUARIO PODER ESCOLHER SE QUER DOAR OU TROCAR O ITEM
def fazer_doacao(i):
    os.system('cls')
    print(f'=====FAZER DOAÇÃO=====\n')
    item_doacao = input('Digite o item que deseja doar: ')
    itens_doacao.append(item_doacao)
    print(f'Item {item_doacao} doado com sucesso!\n')
    input('Pressione Enter para voltar ao menu principal...')
    usuario_logado(i)

#AQUI CONFUNDI OS CODIGOS, MAS BASTA POR ESSA FUNCAO RESPONSAVEL POR CASO O USUARIO QUEIRA VER AS OPCOES DE TROCA
def oferta_trocas(i):
    os.system('cls')
    print(f'=====OFERTA DE TROCAS=====\n')
    item_troca = input('Itens que deseja oferecer para troca: ')
    itens_troca.append(item_troca)
    print(f'Item {item_troca} oferecido para troca com sucesso!\n')
    usuario_logado(i)

#AQUI SERA A VISAO GERAL DE ITENS DISPONIVEIS SEM SER PARA TROCAS
def intens_disponiveis(i):
    os.system('cls')
    print(f'=====ITENS DISPONÍVEIS PARA DOAÇÃO=====\n')
    print('Lista de itens disponíveis:')
    input('Pressione Enter para voltar ao menu principal...')
    usuario_logado(i)

def fechar_programa():
    os.system('cls')
    print('Saindo...')
    exit()


def main():
    login()
main()