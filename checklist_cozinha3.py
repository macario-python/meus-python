# Sistema de Checklist 2.0
checklist = {
    "1": ["Ligar as chapas", False],
    "2": ["Conferir molhos", False],
    "3": ["Limpar bancada", False]
}

while True:
    print("\n--- CHECKLIST DA COZINHA ---")
    for num, dados in checklist.items():
        # Se for True, mostra o símbolo de OK, se False, mostra o espaço vazio
        marcador = "[OK]" if dados[1] else "[  ]"
        print(f"{num}. {marcador} {dados[0]}")

    print("\nDigite o número da tarefa para marcar/desmarcar (ou 'sair' para finalizar):")
    escolha = input("Ação: ")

    if escolha.lower() == 'sair':
        break
    
    if escolha in checklist:
        # Isso aqui inverte o status: se era False vira True, se era True vira False
        checklist[escolha][1] = not checklist[escolha][1]
    else:
        print("Opção inválida! Digite um número da lista.")

print("Sistema encerrado. Bom trabalho!")