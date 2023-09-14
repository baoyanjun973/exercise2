import sqlite3

def create_database(filename):
    # Read the file and copy content to a list
    with open(filename, 'r') as file:
        stephen_king_adaptations_list = [line.strip().split(',') for line in file]

    # Establish a connection with the database
    conn = sqlite3.connect('stephen_king_adaptations.db')
    c = conn.cursor()

    # Create the table
    c.execute('''CREATE TABLE IF NOT EXISTS stephen_king_adaptations_table
                 (movieID text, movieName text, movieYear text, imdbRating real)''')

    # Insert the content into the table
    c.executemany('INSERT INTO stephen_king_adaptations_table VALUES (?,?,?,?)', stephen_king_adaptations_list)

    # Commit the transaction
    conn.commit()

    # Close the connection
    conn.close()

def search_movie_by_name(movie_name):
    # Establish a connection with the database
    conn = sqlite3.connect('stephen_king_adaptations.db')
    c = conn.cursor()

    # Search for movies by name
    c.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieName=?", (movie_name,))
    rows = c.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No such movie exists in our database.")

    # Close the connection
    conn.close()

def search_movie_by_year(movie_year):
    # Establish a connection with the database
    conn = sqlite3.connect('stephen_king_adaptations.db')
    c = conn.cursor()

    # Search for movies by year
    c.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieYear=?", (movie_year,))
    rows = c.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No movies were found for that year in our database.")

    # Close the connection
    conn.close()

def search_movie_by_rating(min_rating):
    # Establish a connection with the database
    conn = sqlite3.connect('stephen_king_adaptations.db')
    c = conn.cursor()

    # Search for movies by rating
    c.execute("SELECT * FROM stephen_king_adaptations_table WHERE imdbRating >= ?", (min_rating,))
    rows = c.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No movies with a rating equal to or above", min_rating, "were found in the database.")

    # Close the connection
    conn.close()

def stop_search():
    print("Exiting the program.")


def menu():
    while True:
        print("1.Movie name")
        print("2.Movie year")
        print("3.Movie rating")
        print("4. STOP")
        choice = input("Choose an option: ")

        if choice == '1':
            movie_name = input("Enter the movie name: ")
            search_movie_by_name(movie_name)
        elif choice == '2':
            movie_year = input("Enter the movie year: ")
            search_movie_by_year(movie_year)
        elif choice == '3':
            min_rating = float(input("Enter the minimum movie rating: "))
            search_movie_by_rating(min_rating)
        elif choice == '4':
            stop_search()
            break
        else:
            print("Invalid option.")

# Create the database
# create_database('stephen_king_adaptations.txt')

# Start the menu loop
menu()