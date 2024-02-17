import sqlite3
import time


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
        print()
        print("Você escolheu a opção 1 - Procurar por obra.")
        search_book()
        search_choice = user_choice()
        if search_choice == 1:
            print("Você escolheu a opção 1 - Procurar pelo  título.")
            
            conn = sqlite3.connect('booksdb.db')
            cursor = conn.cursor()

            search_value = input("Qual o nome da obra? ")
            # Lembrando que o input recebe uma string

            search_query = """
                                SELECT books.id, books.title, authors.name AS author_name, category.name AS category_name, genre.name AS genre_name, books.description, books.pages, books.isbn
                                FROM books
                                JOIN authors ON books.author_id = authors.id
                                JOIN category ON books.category_id = category.id
                                JOIN genre ON books.genre_id = genre.id
                                WHERE books.title LIKE ?
                            """
                                                     


            cursor.execute(search_query, ('%' + search_value + '%',)) #wildcard para aceitar qualquer sequencia de char
            # Virgula para criar uma tupla

            results = cursor.fetchall()

            if  not results:
                print()
                print("Não foi encontrado nenhum resultado para sua busca.")
                print()
                time.sleep(3)               
                main()
            
            else:
                print()
                print("Foram encontradas as seguintes obras:")
                for row in results:
                    id, title, author, category, genre, description, pages, isbn = row
                    print(f"ID: {id}, Título: {title}, Autor: {author}, Categoria: {category}, Gênero: {genre}, Descrição: {description}, Número de Páginas: {pages}, ISBN: {isbn}")
                    print()
                    time.sleep(3)                    
                    main()              
                    
            

        elif search_choice == 2:
            print("Você escolheu a opção 2 - Procurar pelo nome do autor.")
            
            conn = sqlite3.connect('booksdb.db')
            cursor = conn.cursor()

            search_value = input("Qual o nome do autor? ")
            # Lembrando que o input recebe uma string

            #search_query = "SELECT * FROM books WHERE title = ?" --> Query antigo que funciona

            search_query = """
                                SELECT books.id, books.title, authors.name AS author_name, category.name AS category_name, genre.name AS genre_name, books.description, books.pages, books.isbn
                                FROM books
                                JOIN authors ON books.author_id = authors.id
                                JOIN category ON books.category_id = category.id
                                JOIN genre ON books.genre_id = genre.id
                                WHERE authors.name LIKE ?
                            """
                                                     


            cursor.execute(search_query, ('%' + search_value + '%',)) #wildcard para aceitar qualquer sequencia de char
            # Virgula para criar uma tupla

            results = cursor.fetchall()

            if  not results:
                print()
                print("Não foi encontrado nenhum resultado para sua busca.")
                print()
                time.sleep(3)               
                main()
            
            else:
                print()
                print("Foram encontradas as seguintes obras:")
                for row in results:
                    id, title, author, category, genre, description, pages, isbn = row
                    print(f"ID: {id}, Título: {title}, Autor: {author}, Categoria: {category}, Gênero: {genre}, Descrição: {description}, Número de Páginas: {pages}, ISBN: {isbn}")
                    print()
                    time.sleep(3)                    
                    main()

        else:
            print("Opção inválida.")
        # 
    elif menu_choice == 2:
        print("Você escolheu a opção 2 - Inserir obra.")
        # Não deixar inserir obra duplicada!








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