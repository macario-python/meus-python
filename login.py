usuarios = []

while True:
    print("\n" + "="*30)
    print("🔐 SISTEMA DE LOGIN")
    print("="*30)
    print("1 - Cadastrar")
    print("2 - Login")
    print("3 - Sair")

    opcao = input("Escolha: ")

    # CADASTRAR
    if opcao == "1":
        usuario = input("Crie um usuário: ")
        senha = input("Crie uma senha: ")

        usuarios.append((usuario, senha))
        print("✅ Usuário cadastrado!")

    # LOGIN
    elif opcao == "2":
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        encontrado = False

        for u, s in usuarios:
            if u == usuario and s == senha:
                print("✅ Login realizado com sucesso!")
                encontrado = True
                break

        if not encontrado:
            print("❌ Usuário ou senha incorretos")

    # SAIR
    elif opcao == "3":
        print("Saindo...")
        break

    else:
        print("❌ Opção inválida")