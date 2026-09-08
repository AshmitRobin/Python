class MusicTrack:

    platform_name = "TuneWave Music"
    total_tracks = 0
 
    def __init__(self, track_id, title, artist, genre, streams):  #Constructor
       
        self.track_id = track_id
        self.title = title
        self.artist = artist
        self.genre = genre
        self.streams = streams
        self.royalty = 0


        MusicTrack.total_tracks += 1
        print(f"\n[Added] '{self.title}' by {self.artist} uploaded to {MusicTrack.platform_name}")

    def calculate_royalty(self):                       # Complexity          
        if self.streams >= 1000000:
            rate = 0.05
        elif self.streams >= 100000:
            rate = 0.03
        else:
            rate = 0.01


        self.royalty = self.streams * rate


    def popularity_status(self):
        if self.streams >= 1000000:
            return "Hit Song"
        elif self.streams >= 100000:
            return "Trending"
        else:
            return "New Release"


    def display_info(self):
        print("\n----- Track Details -----")
        print("Platform     :", MusicTrack.platform_name)
        print("Track ID     :", self.track_id)
        print("Title        :", self.title)
        print("Artist       :", self.artist)
        print("Genre        :", self.genre)
        print("Streams      :", self.streams)
        print("Status       :", self.popularity_status())
        print("Royalty (₹)  :", round(self.royalty, 2))


    def __del__(self):
        print(f"[Removed] Track '{self.title}' deleted from {MusicTrack.platform_name}")    #Destructor


tracks = []


def add_track():
    track_id = input("Enter Track ID: ")


    title = input("Enter Song Title: ")
    while title.strip() == "":
        title = input("Title cannot be empty. Enter Song Title: ")         #Validation


    artist = input("Enter Artist Name: ")
    while artist.strip() == "":
        artist = input("Artist cannot be empty. Enter Artist Name: ")          #Validation


    genre = input("Enter Genre (Pop/Rock/Classical/etc): ")
    while genre.strip() == "":
        genre = input("Genre cannot be empty. Enter Genre: ")              #Validation


    while True:
        try:
            streams = int(input("Enter Total Streams: "))
            if streams >= 0:
                break
            print("Streams cannot be negative!")                   #Validation
        except ValueError:
            print("Please enter a valid number.")

    track = MusicTrack(track_id, title, artist, genre, streams)
    track.calculate_royalty()
    track.display_info()
    tracks.append(track)

def view_all_tracks():
    if not tracks:
        print("\nNo tracks available.")
        return
    for t in tracks:
        t.display_info()

def delete_track():
    if not tracks:
        print("\nNo tracks to delete.")
        return


    track_id = input("Enter Track ID to delete: ")
    for t in tracks:
        if t.track_id == track_id:
            tracks.remove(t)
            del t
            return
    print("Track ID not found.")

def show_total_tracks():
    print(f"\nTotal Tracks on {MusicTrack.platform_name}: {MusicTrack.total_tracks}")


while True:                                              #Main Menu
    print("\n===== Music Track Management =====")
    print("1. Add New Track")
    print("2. View All Tracks")
    print("3. Delete a Track")
    print("4. Show Total Tracks")
    print("5. Exit")


    choice = input("Enter your choice (1-5): ")


    if choice == '1':
        add_track()
    elif choice == '2':
        view_all_tracks()
    elif choice == '3':
        delete_track()
    elif choice == '4':
        show_total_tracks()
    elif choice == '5':
        print("\nExiting program...")
        break
    else:
        print("Invalid choice! Please enter 1-5.")

print("\nProgram ended. Remaining track objects will now be destroyed.")
