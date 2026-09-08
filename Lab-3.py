songs = {
    "Kesariya": {"artist": "Arijit Singh", "rating": 4.8},
    "Perfect": {"artist": "Ed Sheeran", "rating": 4.7},
    "Believer": {"artist": "Imagine Dragons", "rating": 4.6}
}


def display_menu():
    print("\n========== MUSIC PLAYLIST ==========")
    print("1. Add Song")
    print("2. Display Songs")
    print("3. Search Song")
    print("4. Find Top Rated Song")
    print("5. Exit")


def add_song(name, artist, rating):


    if name in songs:
        print("Song already exists.")
        return


    songs[name] = {
        "artist": artist,
        "rating": rating
    }


    print("Song added successfully.")


def search_song(name):


    if name in songs:
        return songs[name]


    return None


def find_top_rated():                             #Complexity


    top_song = max(songs, key=lambda x: songs[x]["rating"])
    return top_song


while True:


    display_menu()


    while True:
        try:
            choice = int(input("Enter your choice: "))


            if 1 <= choice <= 5:                             #Validation
                break
            else:
                print("Enter a number between 1 and 5.")


        except ValueError:
            print("Invalid input! Enter numbers only.")


    if choice == 1:


        name = input("Enter Song Name: ").title()


        while name == "":
            print("Song name cannot be empty.")                 #Validation
            name = input("Enter Song Name: ").title()


        artist = input("Enter Artist Name: ").title()


        while artist == "":
            print("Artist name cannot be empty.")              #Validation
            artist = input("Enter Artist Name: ").title()


        while True:


            try:
                rating = float(input("Enter Rating (1-5): "))


                if 1 <= rating <= 5:
                    break
                else:
                    print("Rating must be between 1 and 5.")


            except ValueError:
                print("Enter a valid rating.")


        add_song(name, artist, rating)


    elif choice == 2:


        print("\n------ SONG LIST ------")


        if len(songs) == 0:
            print("No songs available.")


        else:
            for song, details in songs.items():
                print(song, "-", details)


    elif choice == 3:


        name = input("Enter Song Name: ").title()


        result = search_song(name)


        if result:
            print("Song Found")
            print("Artist :", result["artist"])
            print("Rating :", result["rating"])
        else:
            print("Song not found.")


    elif choice == 4:


        top = find_top_rated()

        print("\nTop Rated Song")
        print("Song   :", top)
        print("Artist :", songs[top]["artist"])
        print("Rating :", songs[top]["rating"])


    elif choice == 5:
          print("Exit")
          break
