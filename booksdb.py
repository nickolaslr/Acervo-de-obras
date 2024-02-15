import sqlite3


def display_menu(): 
    print("Bem vindo ao seu acervo:")
    print("1 - Procurar por alguma obra")
    print("2 - Inserir nova obra")

def search_book():
    print("Procurar por obra:")
    print("1 - Procurar pelo título")
    print("2 - Procurar pelo nome do autor")


def user_choice():
    while True:
        try:
            choice = int(input("Digite o número de sua opção (1 ou 2) e pressione a tecla \"Enter: "))
            if choice in [1, 2]:
                return choice
            else:
                print("Opcão inválida. Por favor digite apenas 1 ou 2 e tecle \"Enter.")
        except ValueError: #caso o usuário digite algo não numérico
            print("Opcão inválida. Por gentileza digitar apenas o número desejado seguido pela tecla \"Enter.")

def main():
    display_menu()
    menu_choice = user_choice()

    if menu_choice == 1:
        print("Você escolheu a opção 1 - Procurar por obra.")
        search_book()
        search_choice = user_choice()
        if search_choice == 1:
            print("Você escolheu a opção 1 - Procurar pelo  título.")
            
            conn = sqlite3.connect('booksdb.db')
            cursor = conn.cursor()

            search_value = input("Qual o nome da obra? ")
            # Lembrando que o input recebe uma string

            search_query = "SELECT * FROM books WHERE title = ?"

            cursor.execute(search_query, (search_value,))
            # Virgula para criar uma tupla

            results = cursor.fetchall()

            for row in results:
                print(row)
                #Melhorar o layout das informações exibidas
                #Deixar pesquisar por parte do nome ou obra
                #Colocar not found se não encontrar
                #Posso colocar esse bloco dentro de uma função?
            

        elif search_choice == 2:
            print("Você escolheu a opção 2 - Procurar pelo nome do autor.")
            # 
        else:
            print("Opção inválida.")
        # 
    elif menu_choice == 2:
        print("Você escolheu a opção 2 - Inserir obra.")
        # 

#if __name__ == "__main__": #boa prática, mas desnecessário?
main()




# ---BELOW, BLOCK OF CODE TO SEARCH THE DB---

# conn = sqlite3.connect('booksdb.db')
# cursor = conn.cursor()

# search_value = input("Qual o nome da obra? ")
# # Lembrando que o input recebe uma string

# search_query = "SELECT * FROM books WHERE title = ?"

# cursor.execute(search_query, (search_value,))
# # Virgula para criar uma tupla

# results = cursor.fetchall()

# for row in results:
#     print(row)
#     #Melhorar o layout das informações exibidas
#     #Colocar not found se não encontrar

# cursor.close()
# conn.close()