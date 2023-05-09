senha = input('Digite sua senha:')
confirmSenha = input('Confirme sua senha:')
if (senha != confirmSenha) :
    print('uma das senhas está incorreta')
    senha =input('Digite sua senha:')
    confirmSenha =input('Confirme sua senha:')
if (senha == confirmSenha) :
    print ('Senha registrada')
