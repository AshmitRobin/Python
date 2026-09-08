from abc import ABC, abstractmethod


class Music(ABC):
    def __init__(self, title, artist):
        self.title = title
        self._artist = artist
        self.__streams = 0

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

    @abstractmethod
    def calculate_royalty(self):
        pass


class Album(Music):
    def calculate_royalty(self):
        streams = self.get_streams()
        if streams >= 1000000:
            return streams * 0.05
        elif streams >= 100000:
            return streams * 0.03
        else:
            return streams * 0.01


title = input("Enter Song Title: ").strip()
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

song = Album(title, artist)
song.set_streams(streams)
song.display()
print("Royalty : Rs.", song.calculate_royalty())
