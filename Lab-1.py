artist_id = 101                  
song_duration = 3.5              
artist_name = "Arijit Singh"    
is_available = True              
song_list = ["Kesariya", "Tum Hi Ho", "Agar Tum Saath Ho"]  
album_details = ("Romantic", 2025)                          




print("----- Data Types -----")


print(artist_id, type(artist_id))
print(song_duration, type(song_duration))
print(artist_name, type(artist_name))
print(is_available, type(is_available))
print(song_list, type(song_list))
print(album_details, type(album_details))


total_songs = 10
album_price = 250


print("\n----- Arithmetic Operations -----")


print("Addition:", total_songs + album_price)
print("Subtraction:", album_price - total_songs)
print("Multiplication:", total_songs * album_price)
print("Division:", album_price / total_songs)
print("Floor Division:", album_price // total_songs)
print("Modulus:", album_price % total_songs)
print("Exponentiation:", total_songs ** 2)


print("\n----- Enter Song Details -----")


artist = input("Enter artist name: ")


while artist.strip() == "":
    print("Artist name cannot be empty!")
    artist = input("Enter artist name again: ")




song = input("Enter song name: ")


while song.strip() == "":
    print("Song name cannot be empty!")
    song = input("Enter song name again: ")




while True:
    duration = float(input("Enter song duration (minutes): "))


    if duration > 0:
        break
    else:
        print("Duration must be positive!")




while True:
    rating = float(input("Enter song rating (1-5): "))


    if rating >= 1 and rating <= 5:
        break
    else:
        print("Rating should be between 1 and 5")




while True:
    plays = int(input("Enter number of plays: "))


    if plays >= 0:
        break
    else:
        print("Plays cannot be negative")


print("\n----- Song Analysis -----")




if rating >= 4 and plays >= 1000:
    print("Song Status: Highly Popular")


elif rating >= 4 or plays >= 1000:
    print("Song Status: Trending")


else:
    print("Song Status: New Release")




print("Rating greater than 3:", rating > 3)
print("Rating less than 5:", rating < 5)
print("Rating equal to 5:", rating == 5)
print("Rating not equal to 1:", rating != 1)
print("Rating greater/equal 4:", rating >= 4)
print("Rating less/equal 5:", rating <= 5)




print("\n----- Assignment Operators -----")




song_count = 1


song_count += 2
print("After += :", song_count)


song_count -= 1
print("After -= :", song_count)


song_count *= 3
print("After *= :", song_count)


song_count /= 2
print("After /= :", song_count)




print("\n===== Music Catalog Entry =====")


print("Artist:", artist)
print("Song:", song)
print("Duration:", duration, "minutes")
print("Rating:", rating)
print("Total Plays:", plays)


if rating >= 4.5 and plays > 5000:
    recommendation = "Recommended for Playlist Promotion"


elif rating >= 3.5 or plays > 2000:
    recommendation = "Good Song - Add to Trending Section"

else:
    recommendation = "Needs More Audience Reach"


print("Recommendation:", recommendation)
