#Base Class
class Music:
    def __init__(self, title, artist):
        self.title = title              #Public
        self._artist = artist           #Protected
        self.__streams = 0              #Private


    def set_streams(self, streams):
        if streams >= 0:
            self.__streams = streams
        else:
            print("Streams cannot be negative!")


    def get_streams(self):
        return self.__streams


    def display(self):
        print("\nSong :", self.title)
        print("Artist :", self._artist)
        print("Streams :", self.__streams)


#Single Inheritance
class Album(Music):


    def add_song(self, song_name, duration=None):
        if duration is None:
            print(f"Song '{song_name}' added.")
        else:
            print(f"Song '{song_name}' ({duration} mins) added.")


#Multilevel Inheritance
class PremiumAlbum(Album):


    # Method Overriding
    def display(self):
        print("\n--- Premium Album ---")
        super().display()

#Hierarchical Inheritance
class Podcast(Music):


    # Method Overriding
    def display(self):
        print("\n--- Podcast ---")
        super().display()


#Multiple Inheritance
class DownloadFeature:


    def download(self):
        print("Song downloaded successfully.")

class OfflinePlayer(PremiumAlbum, DownloadFeature):
    pass

#Runtime Polymorphism
def show_details(obj):
    obj.display()

title = input("Enter Song Title: ").strip()                #Validations
while title == "":
    print("Title cannot be empty.")
    title = input("Enter Song Title: ").strip()


artist = input("Enter Artist Name: ").strip()
while artist == "":
    print("Artist cannot be empty.")
    artist = input("Enter Artist Name: ").strip()


while True:
    try:
        streams = int(input("Enter Total Streams: "))
        if streams >= 0:
            break
        else:
            print("Streams must be positive.")
    except ValueError:
        print("Enter a valid number.")


song = OfflinePlayer(title, artist)
song.set_streams(streams)


#Complexity
if streams >= 1000000:
    royalty = streams * 0.05
    status = "Hit Song"
elif streams >= 100000:
    royalty = streams * 0.03
    status = "Trending Song"
else:
    royalty = streams * 0.01
    status = "New Release"


# Method Overloading
song.add_song(title)
song.add_song(title, 4)


# Runtime Polymorphism
show_details(song)


print("Popularity :", status)
print("Royalty : ₹", royalty)

song.download()
