import os
from datetime import datetime

# 1. PERGUNTA O NOME LOGO DE CARA
funcionario = input("Digite seu nome para começar: ")

ARQUIVO_RELATORIO = "relatorio_hamburgueria.txt"

# 2. ORGANIZAÇÃO POR DEPARTAMENTOS
checklist = {
    "COZINHA": {
        "1": ["Ligar as chapas", False],
        "2": ["Conferir molhos", False]
    },
    "ESTOQUE": {
        "3": ["Conferir pães", False],
        "4": ["Verificar carne", False]
    }
}

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"FUNCIONÁRIO(A): {funcionario}")
    print("="*35)

    # 3. MOSTRANDO CADA DEPARTAMENTO
    for depto, tarefas in checklist.items():
        print(f"\n--- {depto} ---")
        for num, dados in tarefas.items():
            status = "✅ OK" if dados[1] else "[ ] PENDENTE"
            print(f"{num}. {status} - {dados[0]}")

    print("\n" + "="*35)
    escolha = input("Número para marcar ou '0' para SALVAR E SAIR: ")

    if escolha == "0":
        # 4. HORA DE SALVAR O TXT COM TUDO O QUE VOCÊ PEDIU
        agora = datetime.now().strftime("%d/%m/%Y %H:%M")
        
        with open(ARQUIVO_RELATORIO, "a", encoding="utf-8") as f: # Usei "a" de APPEND (acrescentar)
            f.write(f"\n\n=== CHECKLIST REALIZADO EM {agora} ===")
            f.write(f"\nRESPONSÁVEL: {funcionario}\n")
            f.write("-" * 35 + "\n")
            
            for depto, tarefas in checklist.items():
                f.write(f"[{depto}]\n")
                for num, dados in tarefas.items():
                    status = "FEITO" if dados[1] else "NÃO FEITO"
                    f.write(f"- {dados[0]}: {status}\n")
        
        print(f"Relatório salvo em {ARQUIVO_RELATORIO}!")
        break

    # 5. LÓGICA PARA ENCONTRAR O NÚMERO DENTRO DOS DEPARTAMENTOS
    for depto, tarefas in checklist.items():
        if escolha in tarefas:
            tarefas[escolha][1] = not tarefas[escolha][1]