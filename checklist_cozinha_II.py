# Sistema de Checklist Contínuo
checklist_cozinha = {
    "Ligar as chapas": False,
    "Conferir validade dos molhos": False,
    "Abastecer cubas de vegetais": False,
    "Verificar temperatura da geladeira": False
}

# O comando 'for' vai percorrer CADA item do dicionário, um por um
for tarefa in checklist_cozinha:
    pergunta = input(f"Você já concluiu: {tarefa}? (s/n): ").lower()
    
    if pergunta == "s":
        checklist_cozinha[tarefa] = True
        print(f"✅ {tarefa} marcado como OK!")
    else:
        print(f"❌ {tarefa} continuará como PENDENTE.")

# Só depois que o 'for' passar por todos, ele mostra o resultado final
print("\n--- RESUMO FINAL DO TURNO ---")
for tarefa, status in checklist_cozinha.items():
    marcador = "OK" if status else "PENDENTE"
    print(f"{tarefa}: {marcador}")