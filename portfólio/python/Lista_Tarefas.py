lista = []
add_tarefa = []
while True:
    print(
    "1. Adicionar Tarefa\n"
    "2. Ver tarefas\n"
    "3. Concluir tarefa\n"
    "4.Remover tarefa\n"
    "5.Sair\n"
    )
    escolha = int(input("Escolha uma opção: \n"))

    if escolha == 1:
        add_tarefa = input("Digite sua tarefa: \n")
        lista.append(add_tarefa)
        print(f"Sua nova tarefa foi adicionada!\n")
        print(lista)
        continue
    elif escolha == 2:
        print(lista)
        continue
    elif escolha == 3:
        print(lista)
        Conc_Tarefa = input("Qual tarefa foi concluida?: \n")
        lista.remove(Conc_Tarefa)
        print(f"A tarefa {Conc_Tarefa} foi Concluida e excluida da lista!\n")
        continue
    elif escolha == 4:
        print(lista)
        remover_tarefa = input("Qual tarefa deseja remover? \n")
        lista.remove(remover_tarefa)
        continue
    elif escolha == 5:
        break
print("Usuario saiu!\n")
