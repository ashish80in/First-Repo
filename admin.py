print("WELCOME TO MOIVE MANAGMENT ")
movies = [
    {"name": "Forrest Gump", "year": 1994, "duration": 142, "genres": ["Drama", "Romance"]},
    {"name": "Avengers: Endgame", "year": 2019, "duration": 181, "genres": ["Action", "Adventure", "Drama"]},
    {"name": "Back to the Future", "year": 1985, "duration": 114, "genres": ["Adventure", "Comedy", "Sci-Fi"]}
]

for index, movie in enumerate(movies, start=1):
    print(f"{index}) {movie['name']} ({movie['year']})")

while True:

    choose = input("Choose from [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit: ").lower()
    print("You chose:", choose)

    if choose == 'l':
        if len(movies) == 0:
            print("No movies saved")
        else:
            for index, movie in enumerate(movies, start=1):
                print(f"{index}) {movie['name']} ({movie['year']})")

    elif choose == 'a':
        name = input("Enter your movie name: ")
        year = int(input("Enter your movie year: "))
        duration = float(input("Enter your duration: "))
        genres = list(input("Enter your genres :").split(","))

        new_movie = {
            "name": name,
            "year": year,
            "duration": duration,
            "genres": genres,  
        }

        movies.append(new_movie)
        print("Movie added successfully!")

    elif choose == 's':

        if len(movies) == 0:
            print("No movies saved")
        else:
            search = input("Enter the film you want to search: ").lower()
            found = False
            if search in movie["name"].lower():
                    print(f"{index}) {movie['name']} ({movie['year']})")
                    found = True

            if not found:
                print("Movie not found")

    elif choose == 'd':

        if len(movies) == 0:
            print("No movies saved")
        else:
            index = int(input("Enter movie index to delete: "))

            if 1 <= index <= len(movies):
                deleted_movie = movies.pop(index - 1)
                print(f"{deleted_movie['name']} deleted successfully!")
            else:
                print("Invalid index number")

    elif choose == 'v':

        if len(movies) == 0:
            print("No movies saved")
        else:
            index = int(input("Enter your index value: "))

            if 1 <= index <= len(movies):
                movie = movies[index - 1]
                print(
                    f"{index}) {movie['name']} - Year: {movie['year']}, "
                    f"Duration: {movie['duration']} mins, "
                    f"Genres: {', '.join(movie['genres'])}"
                )
            else:
                print("Invalid index number")

    elif choose == 'q':
        print("Goodbye!")
        break

    else:
        print("Invalid choice")

         
      
    
    
        


            
            





             