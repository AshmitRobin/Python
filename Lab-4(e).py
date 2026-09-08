import re


def validate_song_title(title):
    return bool(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9 '\-]{1,49}", title))


def validate_artist_name(name):
    return bool(re.fullmatch(r"[A-Z][a-z]+(?: [A-Z][a-z]+)*", name))


def validate_duration(duration):
    return bool(re.fullmatch(r"[0-5]?\d:[0-5]\d", duration))


def validate_release_date(date):
    return bool(re.fullmatch(r"(0[1-9]|[12]\d|3[01])-(0[1-9]|1[0-2])-\d{4}", date))


def extract_hashtags(caption):
    return re.findall(r"#\w+", caption)


def search_genre(text, genre):
    return re.search(r"\b" + re.escape(genre) + r"\b", text, re.IGNORECASE)


def censor_lyrics(lyrics, banned_words):
    pattern = r"\b(" + "|".join(banned_words) + r")\b"
    return re.sub(pattern, lambda m: m.group()[0] + "*" * (len(m.group()) - 1),
                   lyrics, flags=re.IGNORECASE)


def split_lyrics(lyrics):
    return [line.strip() for line in re.split(r"[.\n]+", lyrics) if line.strip()]


def validate_email(email):
    return bool(re.fullmatch(r"[\w.\-]+@[\w\-]+\.[a-zA-Z]{2,}", email))


def match_genre_code(filename):
    return re.match(r"[A-Z]{3}\d{3}", filename)


def validate_password(password):
    if len(password) < 8:
        return False, "Minimum 8 characters required."
    if not re.search(r"[A-Z]", password):
        return False, "At least one uppercase letter required."
    if not re.search(r"[a-z]", password):
        return False, "At least one lowercase letter required."
    if not re.search(r"\d", password):
        return False, "At least one digit required."
    if not re.search(r"[@#$%&*]", password):
        return False, "At least one special character (@ # $ % & *) required."
    return True, "Strong password."


def extract_credits(text):
    pattern = r"Produced by (?P<producer>[A-Za-z ]+), Written by (?P<writer>[A-Za-z ]+)"
    match = re.search(pattern, text)
    return match.groupdict() if match else None


def word_frequency(lyrics, top_n=5):
    words = re.findall(r"[a-zA-Z]+", lyrics.lower())
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return dict(sorted(freq.items(), key=lambda x: -x[1])[:top_n])


def menu():
    print("""
------ MUSIC REGEX VALIDATOR ------
1.  Validate Song Title
2.  Validate Artist Name
3.  Validate Track Duration (mm:ss)
4.  Validate Release Date (dd-mm-yyyy)
5.  Extract Hashtags from Caption
6.  Search Genre Tag in Text
7.  Censor Explicit Words in Lyrics
8.  Split Lyrics into Lines
9.  Validate Artist Email
10. Match Genre Code at Start of Filename
11. Validate Artist Account Password
12. Extract Song Credits (Producer/Writer)
13. Lyrics Word Frequency Analyzer
0.  Exit
------------------------------------""")


BANNED_WORDS = ["damn", "hell", "curse"]

while True:
    menu()
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        title = input("Enter Song Title: ")
        print("Valid" if validate_song_title(title) else "Invalid Song Title")

    elif choice == "2":
        name = input("Enter Artist Name: ")
        print("Valid" if validate_artist_name(name) else "Invalid Artist Name")

    elif choice == "3":
        duration = input("Enter Track Duration (mm:ss): ")
        print("Valid" if validate_duration(duration) else "Invalid Duration")

    elif choice == "4":
        date = input("Enter Release Date (dd-mm-yyyy): ")
        print("Valid" if validate_release_date(date) else "Invalid Date")

    elif choice == "5":
        caption = input("Enter Song Caption/Description: ")
        tags = extract_hashtags(caption)
        print("Hashtags found:", tags if tags else "None")

    elif choice == "6":
        text = input("Enter Text: ")
        genre = input("Enter Genre to Search: ")
        result = search_genre(text, genre)
        print(f"'{genre}' found at position {result.start()}" if result else "Genre not found")

    elif choice == "7":
        lyrics = input("Enter Lyrics: ")
        print("Censored Lyrics:", censor_lyrics(lyrics, BANNED_WORDS))

    elif choice == "8":
        lyrics = input("Enter Lyrics (use '.' to separate lines): ")
        print("Lines:", split_lyrics(lyrics))

    elif choice == "9":
        email = input("Enter Artist Email: ")
        print("Valid" if validate_email(email) else "Invalid Email")

    elif choice == "10":
        filename = input("Enter Filename (e.g. POP101_track.mp3): ")
        result = match_genre_code(filename)
        print(f"Genre code detected: {result.group()}" if result else "No genre code at start")

    elif choice == "11":
        password = input("Enter Artist Account Password: ")
        valid, message = validate_password(password)
        print(message)

    elif choice == "12":
        text = input("Enter Credit Line (e.g. Produced by John Doe, Written by Jane Roe): ")
        credits_found = extract_credits(text)
        print("Credits:", credits_found if credits_found else "No credits found")

    elif choice == "13":
        lyrics = input("Enter Full Lyrics: ")
        print("Top Words:", word_frequency(lyrics))

    elif choice == "0":
        print("Exiting Music Regex Validator.")
        break

    else:
        print("Invalid choice. Try again.")
