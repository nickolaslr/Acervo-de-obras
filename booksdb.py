import sqlite3


# -- search the db --
# by title

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
    #Colocar not found se não encontrar

cursor.close()
conn.close()


# -- search the db --
# by author

# -- insert new itens in the db --
