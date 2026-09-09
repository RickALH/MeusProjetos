import sqlite3

conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT NOT NULL,
    email TEXT NOT NULL
    )
""")

conexao.commit()

def cadastrar_cliente():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    cursor.execute(
        "INSERT INTO clientes (nome, telefone, email) VALUES (?, ?, ?)",
        (nome, telefone, email)
    )

    conexao.commit()
    print("Cliente cadastrado com sucesso!")


def listar_clientes():
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    for cliente in clientes:
        print(f"ID:{cliente[0]}")
        print(f"Nome:{cliente[1]}")
        print(f"Telefone:{cliente[2]}")
        print(f"E-mail:{cliente[3]}")
        print("-" * 30)


def pesquisar_cliente():
    nome = input("Digite o nome do cliente: ")

    cursor.execute(
        "SELECT * FROM clientes WHERE nome LIKE ?",
        (f"%{nome}%")
    )

    clientes = cursor.fetchall()

    if not clientes:
        print("Cliente não encontrado.")
        return
    
    for cliente in clientes:
        print(f"ID:{cliente[0]}")
        print(f"Nome:{cliente[1]}")
        print(f"Telefone:{cliente[2]}")
        print(f"E-mail:{cliente[3]}")
        print("-" * 30)


while True:
    print("\n===SISTEMA DE CLIENTES===")
    print("1 - Cadastrar cliente")
    print("2 - Listar cliente")
    print("3 - Pesquisar cliente")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")


    if opcao == "1":
        cadastrar_cliente()

    elif opcao == "2":
        listar_clientes()

    elif opcao == "3":
        pesquisar_cliente()

    elif opcao == "4":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida")


conexao.close()