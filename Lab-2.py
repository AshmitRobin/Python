

songs = {
    "Kesariya": {"artist": "Arijit Singh", "rating": 4.8},
    "Tum Hi Ho": {"artist": "Arijit Singh", "rating": 4.9},
    "Perfect": {"artist": "Ed Sheeran", "rating": 4.7},
    "Believer": {"artist": "Imagine Dragons", "rating": 4.6},
    "Apna Bana Le": {"artist": "Arijit Singh", "rating": 4.5}
}


print("Artist:", songs["Kesariya"]["artist"])


# Add
songs["Shape Of You"] = {"artist": "Ed Sheeran", "rating": 4.8}


# Update
songs["Perfect"]["rating"] = 5


# Delete
del songs["Believer"]


print("Keys:", songs.keys())
print("Values:", songs.values())




playlist1 = {"Kesariya", "Perfect", "Tum Hi Ho"}
playlist2 = {"Perfect", "Shape Of You", "Apna Bana Le"}


playlist1.add("Believer")
playlist1.remove("Believer")


print("\nUnion:", playlist1 | playlist2)
print("Intersection:", playlist1 & playlist2)
print("Difference:", playlist1 - playlist2)
print("Symmetric Difference:", playlist1 ^ playlist2)


while True:

    print("\n------ MENU ------")
    print("1.Add Song")
    print("2.Display Songs")
    print("3.Search Song")
    print("4.Update Rating")
    print("5.Delete Song")
    print("6.Top Rated Song")
    print("7.Exit")


    choice = int(input("Enter Choice: "))


    if choice == 1:


        name = input("Song Name: ").title()


        if name in songs:
            print("Song already exists.")
            continue


        artist = input("Artist Name: ").title()


        rating = float(input("Rating (1-5): "))


        if rating < 1 or rating > 5:
            print("Invalid Rating")
            continue


        songs[name] = {"artist": artist, "rating": rating}
        print("Song Added")


    elif choice == 2:


        for song, details in songs.items():
            print(song, "-", details)


    elif choice == 3:


        name = input("Enter Song: ").title()


        if name in songs:
            print(songs[name])
        else:
            print("Song Not Found")


    elif choice == 4:


        name = input("Song Name: ").title()


        if name in songs:
            songs[name]["rating"] = float(input("New Rating: "))
            print("Updated")
        else:
            print("Song Not Found")


    elif choice == 5:


        name = input("Song Name: ").title()


        if name in songs:
            del songs[name]
            print("Deleted")
        else:
            print("Song Not Found")


    elif choice == 6:                                                      # Complexity


        top_song = max(songs, key=lambda x: songs[x]["rating"])
        print("Top Rated Song:", top_song)


    elif choice == 7:
        break

    else:
        pass
        print("Invalid Choice")
