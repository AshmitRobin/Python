import csv
import os

TEXT_FILE = "songs.txt"
CSV_FILE = "music_catalog.csv"
FIELDS = ["ID", "Title", "Artist", "Genre", "Price", "Duration"]


# Validations

def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Try again.")


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt).strip())
            if value <= 0:
                print("Value must be greater than 0.")
                continue
            return value
        except ValueError:
            print("Invalid number. Try again.")


def get_duration(prompt):
    # expects MM:SS format
    while True:
        value = input(prompt).strip()
        parts = value.split(":")
        if len(parts) == 2 and all(p.isdigit() for p in parts):
            return value
        print("Invalid duration. Use MM:SS format (e.g. 03:45).")


#Text file handling

def create_sample_text_file():
    if not os.path.exists(TEXT_FILE):
        sample = [
            "Blinding Lights,The Weeknd,199",
            "Shape of You,Ed Sheeran,149",
            "Kesariya,Arijit Singh,99",
            "Levitating,Dua Lipa,179",
            "Perfect,Ed Sheeran,129",
        ]
        with open(TEXT_FILE, "w") as f:
            f.write("\n".join(sample))


def read_text_file_and_show_above_average():
    try:
        with open(TEXT_FILE, "r") as f:
            lines = [line.strip() for line in f if line.strip()]

        songs = []
        for line in lines:
            try:
                title, artist, price = line.split(",")
                songs.append((title, artist, float(price)))
            except ValueError:
                print(f"Skipping malformed line: {line}")

        if not songs:
            print("No valid records found in text file.")
            return

        average_price = sum(p for _, _, p in songs) / len(songs)
        print(f"\nAverage Price: {average_price:.2f}")
        print("\nSongs priced above average:")
        print(f"{'Title':<20}{'Artist':<20}{'Price':<10}")
        for title, artist, price in songs:
            if price > average_price:
                print(f"{title:<20}{artist:<20}{price:<10.2f}")

    except FileNotFoundError:
        print("Text file not found.")


# CSV file handling & CRUD

def create_csv_if_missing():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()


def read_all_records():
    with open(CSV_FILE, "r", newline="") as f:
        return list(csv.DictReader(f))


def write_all_records(records):
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(records)


def generate_id(records):
    if not records:
        return 1
    return max(int(r["ID"]) for r in records) + 1


def add_record():
    try:
        records = read_all_records()
        title = get_non_empty("Title: ")
        artist = get_non_empty("Artist: ")
        genre = get_non_empty("Genre: ")
        price = get_positive_float("Price: ")
        duration = get_duration("Duration (MM:SS): ")

        new_record = {
            "ID": generate_id(records),
            "Title": title,
            "Artist": artist,
            "Genre": genre,
            "Price": price,
            "Duration": duration,
        }
        records.append(new_record)
        write_all_records(records)
        print("Record added successfully.")
    except Exception as e:
        print(f"Error adding record: {e}")


def display_all_records():
    try:
        records = read_all_records()
        if not records:
            print("No records found.")
            return
        print(f"\n{'ID':<5}{'Title':<20}{'Artist':<18}{'Genre':<12}{'Price':<10}{'Duration':<10}")
        for r in records:
            print(f"{r['ID']:<5}{r['Title']:<20}{r['Artist']:<18}{r['Genre']:<12}{r['Price']:<10}{r['Duration']:<10}")
    except Exception as e:
        print(f"Error reading records: {e}")


def search_record():
    try:
        records = read_all_records()
        keyword = input("Search by Title or Artist: ").strip().lower()
        results = [r for r in records if keyword in r["Title"].lower() or keyword in r["Artist"].lower()]
        if not results:
            print("No matching records found.")
            return
        for r in results:
            print(r)
    except Exception as e:
        print(f"Error searching records: {e}")


def update_record():
    try:
        records = read_all_records()
        song_id = input("Enter ID of record to update: ").strip()
        for r in records:
            if r["ID"] == song_id:
                r["Title"] = get_non_empty(f"New Title [{r['Title']}]: ") or r["Title"]
                r["Artist"] = get_non_empty(f"New Artist [{r['Artist']}]: ") or r["Artist"]
                r["Genre"] = get_non_empty(f"New Genre [{r['Genre']}]: ") or r["Genre"]
                r["Price"] = get_positive_float("New Price: ")
                r["Duration"] = get_duration("New Duration (MM:SS): ")
                write_all_records(records)
                print("Record updated successfully.")
                return
        print("Record with that ID not found.")
    except Exception as e:
        print(f"Error updating record: {e}")


def delete_record():
    try:
        records = read_all_records()
        song_id = input("Enter ID of record to delete: ").strip()
        updated_records = [r for r in records if r["ID"] != song_id]
        if len(updated_records) == len(records):
            print("Record with that ID not found.")
            return
        write_all_records(updated_records)
        print("Record deleted successfully.")
    except Exception as e:
        print(f"Error deleting record: {e}")


# complexity

def genre_summary_report():
    try:
        records = read_all_records()
        if not records:
            print("No records found.")
            return
        summary = {}
        for r in records:
            genre = r["Genre"]
            price = float(r["Price"])
            if genre not in summary:
                summary[genre] = {"count": 0, "total": 0.0}
            summary[genre]["count"] += 1
            summary[genre]["total"] += price

        print(f"\n{'Genre':<15}{'Count':<10}{'Avg Price':<10}")
        for genre, data in summary.items():
            avg = data["total"] / data["count"]
            print(f"{genre:<15}{data['count']:<10}{avg:<10.2f}")
    except Exception as e:
        print(f"Error generating report: {e}")

def show_menu():
    print("\n----- MUSIC CATALOG MANAGEMENT SYSTEM -----")
    print("1. Read Text File & Show Songs Above Average Price")
    print("2. Add Record")
    print("3. Display All Records")
    print("4. Search Record")
    print("5. Update Record")
    print("6. Delete Record")
    print("7. Genre-wise Summary Report")
    print("8. Exit")


def main():
    create_sample_text_file()
    create_csv_if_missing()

    while True:
        show_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            read_text_file_and_show_above_average()
        elif choice == "2":
            add_record()
        elif choice == "3":
            display_all_records()
        elif choice == "4":
            search_record()
        elif choice == "5":
            update_record()
        elif choice == "6":
            delete_record()
        elif choice == "7":
            genre_summary_report()
        elif choice == "8":
            print("Exiting")
            break
        else:
            print("Invalid choice. Enter a number between 1 and 8.")


if __name__ == "__main__":
    main()
