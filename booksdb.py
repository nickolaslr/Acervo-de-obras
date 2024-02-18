import sqlite3
import time


def display_menu(): 
    print("\nBem vindo ao seu acervo:")
    print("1 - Procurar por alguma obra")
    print("2 - Inserir nova obra")

def search_book():
    print("\nProcurar por obra:")
    print("1 - Procurar pelo título")
    print("2 - Procurar pelo nome do autor")

def user_choice(): #bloco separado pois será utilizado mais de uma vez
    while True:
        user_input = input("\nDigite o número de sua opção (1 ou 2) e pressione a tecla \"Enter: ")
         
        if user_input.isdigit():
            number = int(user_input)
            if 1 <= number <= 2:
                return number
            else:
                print("\nOpcão inválida. Por favor digite apenas 1 ou 2 e tecle \"Enter.")
        

def get_category_input():
    print("\nSelecione uma categoria:")
    print("1. Livro")
    print("2. Quadrinho")
    print("3. Mangá")

    while True:
        user_input = input("\nDigite um número e pressione a tecla \"Enter\": ")

        if user_input.isdigit():
            number = int(user_input)
            if 1 <= number <= 3:
                return number
            else:
                print("\nNúmero inválido. Por favor selecione um número de 1 and 3.")
        else:
            print("\nPor favor selecione um número de 1 and 3.")


def get_genre_input():
    print("\nSelecione um gênero:")
    print("1. Romance")
    print("2. Ficção")
    print("3. Fantasia")
    print("4. Biografia")
    print("5. Autoajuda")
    print("6. Religioso")
    print("7. Ação")
    print("8. Suspense")
    print("9. Terror")

    while True:
        user_input = input("\nDigite um número e pressione a tecla \"Enter\": ")

        if user_input.isdigit():
            number = int(user_input)
            if 1 <= number <= 9:
                return number
            else:
                print("\nNúmero inválido. Por favor selecione um número de 1 and 9.")
        else:
            print("\nPor favor selecione um número de 1 and 9.")

    
def main():
    display_menu()
    menu_choice = user_choice()

    if menu_choice == 1:
        print("\nVocê escolheu a opção 1 - Procurar por obra.")
        search_book()
        search_choice = user_choice()
        
        if search_choice == 1:
            print("\nVocê escolheu a opção 1 - Procurar pelo  título.")
            
            conn = sqlite3.connect('booksdb.db')
            cursor = conn.cursor()

            search_value = input("\nQual o nome da obra? ")

            search_query = """
                                SELECT books.id, books.title, authors.name AS author_name, category.name AS category_name, genre.name AS genre_name, books.description, books.pages, books.isbn
                                FROM books
                                JOIN authors ON books.author_id = authors.id
                                JOIN category ON books.category_id = category.id
                                JOIN genre ON books.genre_id = genre.id
                                WHERE books.title LIKE ?
                            """

            cursor.execute(search_query, ('%' + search_value + '%',)) #aceitar qualquer sequencia de char
            # Virgula para criar uma tupla

            results = cursor.fetchall()

            print("Debug:", results)

            if  not results:
                print("\nNão foi encontrado nenhum resultado para sua busca.")
                time.sleep(3)               
            
            else:
                print("\nForam encontradas as seguintes obras:") #Só encontra uma obra, tem que mostrar todas!!!
                for row in results:
                    id, title, author, category, genre, description, pages, isbn = row
                    print(f"ID: {id}, Título: {title}, Autor: {author}, Categoria: {category}, Gênero: {genre}, Descrição: {description}, Número de Páginas: {pages}, ISBN: {isbn}")
                    time.sleep(3)                    
                    
            main()              
                  
            
        elif search_choice == 2:
            print("\nVocê escolheu a opção 2 - Procurar pelo nome do autor.")
            
            conn = sqlite3.connect('booksdb.db')
            cursor = conn.cursor()

            search_value = input("\nQual o nome do autor? ")
            
            search_query = """
                                SELECT books.id, books.title, authors.name AS author_name, category.name AS category_name, genre.name AS genre_name, books.description, books.pages, books.isbn
                                FROM books
                                JOIN authors ON books.author_id = authors.id
                                JOIN category ON books.category_id = category.id
                                JOIN genre ON books.genre_id = genre.id
                                WHERE authors.name LIKE ?
                            """                                          

            cursor.execute(search_query, ('%' + search_value + '%',))
            # Virgula para criar uma tupla

            results = cursor.fetchall()

            if  not results:
                print("\nNão foi encontrado nenhum resultado para sua busca.")
                cursor.close()
                conn.close()
                time.sleep(3)               
                main()
            
            else:
                print("\nForam encontradas as seguintes obras: ")
                for row in results:
                    id, title, author, category, genre, description, pages, isbn = row
                    print(f"ID: {id}, Título: {title}, Autor: {author}, Categoria: {category}, Gênero: {genre}, Descrição: {description}, Número de Páginas: {pages}, ISBN: {isbn}")
                    cursor.close()
                    conn.close()
                    time.sleep(3)                    
                    main()

        else:
            print("Opção inválida.")

        cursor.close()
        conn.close()
         
    elif menu_choice == 2:
        print("\nVocê escolheu a opção 2 - Inserir obra.")
        
        conn = sqlite3.connect('booksdb.db')
        cursor = conn.cursor()

        author_name = input("\nNome do autor: ")
        author_id = None

        check_query = "SELECT id FROM authors WHERE name LIKE ?"
        cursor.execute(check_query, ('%' + author_name + '%',))
        existing_author = cursor.fetchone()

        if existing_author:
            author_id = existing_author[0]
            print(f"\nO autor {author_name} já está cadastrado em nosso sistema com o ID {author_id}.")
        else:
            insert_query = "INSERT INTO authors (name) VALUES (?)"
            cursor.execute(insert_query, (author_name,))
            conn.commit()
            author_id = cursor.lastrowid
            print(f"\nAutor {author_name} cadastrado com sucesso. ID: {author_id}")

        title = input("\nPor favor insira o nome da obra: ")
                
        check_query = "SELECT COUNT(*) FROM books WHERE title = ?"
        cursor.execute(check_query, (title,))
        existing_records = cursor.fetchone()[0]

        if existing_records > 0:
            cursor.close()
            conn.close()
            print("\nEssa obra já está cadastrada em nosso sistema.")
            time.sleep(3)                    
            main()

        else:
            insert_query = """
            INSERT INTO books (title, author_id, category_id, genre_id, description, pages, isbn)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """

            category_id = get_category_input()
            print("\nVocê selecionou:", category_id)
         
            genre_id = get_genre_input()
            print("\nVocê selecionou:", genre_id)
        
            description = input("\nQue tal inserir uma breve descrição: ")

            pages = input("\nQual o número de páginas: ")

            isbn = input("\nQual o ISBN (International Standard Book Number/ Padrão Internacional de Numeração de Livro): ")

            values = (title, author_id, category_id, genre_id, description, pages, isbn)

            cursor.execute(insert_query, values)
            conn.commit()
            cursor.close()
            conn.close()
            print("\nObra inserida com sucesso!")
            time.sleep(3)                    
            main() 

#if __name__ == "__main__": #boa prática, mas desnecessário?
main()
