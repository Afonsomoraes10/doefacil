#\n
email_geral = 'doefacil@admin.com'
senha_geral = 'admin'

def login(email_geral, senha_geral):
    while True:
        print('=====DOEFACIL=====\n')
        print('Digite seu email cadastrado')
        email_cadastrado = input('Email: ')
        print('Digite sua senha cadastrada')
        senha_cadastrada = input('Senha: ')

        if email_cadastrado != email_geral or senha_cadastrada != senha_geral:
            print('Senha ou email incorretos, tente novamente!')
            print('1- Cadastrar novo usuário')
            print('2- Deseja tentar novamente ')
            opcao = input('Escolha uma opção: ')
            if opcao == '1':
                email_geral, senha_geral = cadastrar_usuario()
            elif opcao == '2':
                continue
            else:
                break
        else:
            print('Login realizado com sucesso!')
            usuario_logado(email_cadastrado)
            break

def cadastrar_usuario():
    print('=====CADASTRO DE USUÁRIO=====\n')
    print('Digite seu email para cadastro')
    email_cadastrado = input('Email: ')
    print('Digite sua senha para cadastro')
    senha_cadastrada = input('Senha: ')
    print(f'Usuário {email_cadastrado} cadastrado com sucesso!')
    return email_cadastrado, senha_cadastrada

def usuario_logado(email_cadastrado):
    print(f'Bem-vindo, {email_cadastrado}!')
    # Aqui você pode adicionar funcionalidades adicionais para o usuário logado
def main():
    login(email_geral, senha_geral)
main()
