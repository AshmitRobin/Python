class MusicPlaylist:


    def __init__(self):
        self.songs = {}


    def welcome(self):                                            # Single Method
        print("\nWelcome to Music Playlist Manager")


    def add_song(self, name, artist, rating):                     # Multiple Methods


        if name in self.songs:
            print("Song already exists.")
            return


        self.songs[name] = {
            "artist": artist,
            "rating": rating
        }


        print("Song Added Successfully.")


    def display_songs(self):


        if len(self.songs) == 0:
            print("No Songs Available.")
        else:
            print("\nSong List")
            for song, details in self.songs.items():
                print(song, "-", details)


    def search_song(self, name):


        if name in self.songs:
            print(self.songs[name])
        else:
            print("Song Not Found.")


    def delete_song(self, name):


        if name in self.songs:
            del self.songs[name]
            print("Song Deleted.")
        else:
            print("Song Not Found.")


    def update_song(self, name, rating=None):                    # Method Overloading


        if name not in self.songs:
            print("Song Not Found.")
            return


        if rating is None:
            print("Artist :", self.songs[name]["artist"])
            print("Rating :", self.songs[name]["rating"])
        else:
            self.songs[name]["rating"] = rating
            print("Rating Updated.")


    def top_song(self):                                           # Complexity


        if len(self.songs) == 0:
            print("Playlist Empty.")
            return


        top = max(self.songs, key=lambda x: self.songs[x]["rating"])


        print("\nTop Rated Song")
        print("Song   :", top)
        print("Artist :", self.songs[top]["artist"])
        print("Rating :", self.songs[top]["rating"])




obj = MusicPlaylist()
obj.welcome()


while True:


    print("\n------ MENU ------")
    print("1. Add Song")
    print("2. Display Songs")
    print("3. Search Song")
    print("4. Update Song Rating")
    print("5. Delete Song")
    print("6. Show Song Details (Method Overloading)")
    print("7. Top Rated Song")
    print("8. Exit")


    try:
        choice = int(input("Enter Choice: "))


        if choice < 1 or choice > 8:
            print("Enter choice between 1 and 8.")
            continue


    except ValueError:
        print("Enter numbers only.")
        continue


    if choice == 1:


        name = input("Song Name: ").title()


        while name == "":
            print("Song name cannot be empty.")
            name = input("Song Name: ").title()


        artist = input("Artist Name: ").title()


        while artist == "":
            print("Artist name cannot be empty.")
            artist = input("Artist Name: ").title()


        while True:


            try:
                rating = float(input("Rating (1-5): "))


                if 1 <= rating <= 5:
                    break
                else:
                    print("Rating should be between 1 and 5.")


            except ValueError:
                print("Enter valid rating.")


        obj.add_song(name, artist, rating)


    elif choice == 2:


        obj.display_songs()


    elif choice == 3:


        name = input("Enter Song Name: ").title()
        obj.search_song(name)


    elif choice == 4:


        name = input("Song Name: ").title()


        try:
            rating = float(input("New Rating: "))


            if 1 <= rating <= 5:
                obj.update_song(name, rating)
            else:
                print("Rating should be between 1 and 5.")


        except ValueError:
            print("Invalid Rating.")


    elif choice == 5:


        name = input("Song Name: ").title()
        obj.delete_song(name)


    elif choice == 6:


        name = input("Song Name: ").title()


        obj.update_song(name)


    elif choice == 7:


        obj.top_song()


    elif choice == 8:


        print("Exit")
        break

