MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by little, or 'q' to quit: "
movies = []


def add_movie():
    title = input("Tell the title of the movie.\n")
    director = input("Tell the director of the movie.\n")
    release_year = input("Tell the release year of the movie.\n")

    movies.append({
        "title": title, 
        "director": director, 
        "year": release_year
    })


def show_movies():
    for movie in movies:
        print_movie(movie)


def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")


def find_movie():
    search_title = input("Enter movie title you're looking for: ")

    for movie in movies:
        if movie["title"] == search_title:
            print_movie(movie)


user_options = {
    "a": add_movie,
    "l": show_movies,
    "f": find_movie
}

def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        # First Class function
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print('Unknown command. Please try again.')
        selection = input(MENU_PROMPT)
        
menu()