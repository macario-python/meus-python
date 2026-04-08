# Sistema de Checklist - Hamburgueria
print("--- SISTEMA DE CHECKLIST: DEPARTAMENTO COZINHA ---")

# Criamos um dicionário onde a chave é a tarefa e o valor é o status (True para OK, False para Pendente)
checklist_cozinha = {
    "Ligar as chapas": False,
    "Conferir validade dos molhos": False,
    "Abastecer cubas de vegetais": False,
    "Verificar temperatura da geladeira": False
}

# Vamos simular a marcação de uma tarefa
print("\nTarefas pendentes:")
for tarefa, status in checklist_cozinha.items():
    if status == False:
        print(f"[ ] {tarefa}")

print("\n--- ATUALIZANDO STATUS ---")
# Aqui simulamos que você concluiu a primeira tarefa
pergunta = input("Você já ligou as chapas? (sim/nao): ").lower()

if pergunta == "sim":
    checklist_cozinha["Ligar as chapas"] = True
    print("Tarefa marcada como concluída!")
else:
    print("Atenção: Ligue as chapas antes de abrir!")

# Resultado final
print("\nStatus atualizado da Cozinha:")
for tarefa, status in checklist_cozinha.items():
    marcador = "OK" if status else "PENDENTE"
    print(f"{tarefa}: {marcador}")