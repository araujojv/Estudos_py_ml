login = "joqo"
senha = "123"

while True:
    usuario_login = input("digite seu usuario")
    usuario_senha = input("digite sua senha")
    
    if usuario_login == login and usuario_senha == senha: 
        print ("logado com sucesso")
        break 
    else: 
        print("usuario ou senha invalida ")    
        