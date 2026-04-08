# Checklist Hamburgueria - Versão Seleção Livre
checklist = {
    "1": ["Ligar as chapas", False],
    "2": ["Conferir validade dos molhos", False],
    "3": ["Abastecer cubas de vegetais", False],
    "4": ["Verificar temperatura da geladeira", False],
    "5": ["Limpar bancadas de inox", False],
    "6": ["Organizar embalagens", False]
}

while True:
    print("\n" + "="*30)
    print("   CHECKLIST DA COZINHA")
    print("="*30)
    
    # Mostra a lista completa com o status atual
    for tecla, dados in checklist.items():
        status = "✅ OK" if dados[1] else "[  ] PENDENTE"
        print(f"{tecla}. {status} - {dados[0]}")
    
    print("="*30)
    escolha = input("Digite o número para marcar/desmarcar (ou '0' para sair): ")

    if escolha == "0":
        print("Saindo do sistema... Até logo!")
        break
    
    if escolha in checklist:
        # Aqui acontece a "mágica": ele inverte o valor de True para False ou vice-versa
        checklist[escolha][1] = not checklist[escolha][1]
    else:
        print("\n⚠️ Opção inválida! Escolha um número da lista.")