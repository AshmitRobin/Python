import re
import tkinter as tk
from tkinter import ttk, messagebox

songs = []

def validate_title(title):
    return bool(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9 '\-]{1,49}", title))

def validate_artist(artist):
    return bool(re.fullmatch(r"[A-Z][a-z]+(?: [A-Z][a-z]+)*", artist))

def validate_duration(duration):
    return bool(re.fullmatch(r"[0-5]?\d:[0-5]\d", duration))

root = tk.Tk()
root.title("Music Library Manager")
root.geometry("750x550")
root.resizable(False, False)

def show_about():
    messagebox.showinfo("About", "Music Library Manager\nBuilt with Tkinter")

def exit_app():
    root.quit()

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Clear All", command=lambda: clear_all())
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

heading = tk.Label(root, text="Music Library Manager", font=("Arial", 18, "bold"),
                    bg="#2c3e50", fg="white", pady=10)
heading.pack(side="top", fill="x")

form_frame = tk.Frame(root, pady=10)
form_frame.pack(side="top", fill="x", padx=20)

tk.Label(form_frame, text="Song Title:").grid(row=0, column=0, sticky="w", pady=5)
title_entry = tk.Entry(form_frame, width=30)
title_entry.grid(row=0, column=1, padx=10)

tk.Label(form_frame, text="Artist Name:").grid(row=1, column=0, sticky="w", pady=5)
artist_entry = tk.Entry(form_frame, width=30)
artist_entry.grid(row=1, column=1, padx=10)

tk.Label(form_frame, text="Duration (mm:ss):").grid(row=0, column=2, sticky="w", pady=5)
duration_entry = tk.Entry(form_frame, width=15)
duration_entry.grid(row=0, column=3, padx=10)

tk.Label(form_frame, text="Genre:").grid(row=1, column=2, sticky="w", pady=5)
genre_combo = ttk.Combobox(form_frame, width=13,
                            values=["Pop", "Rock", "Hip-Hop", "Classical", "Jazz", "EDM"])
genre_combo.grid(row=1, column=3, padx=10)
genre_combo.current(0)

# Checkbutton and Radiobuttons (additional widgets)
favorite_var = tk.IntVar()
tk.Checkbutton(form_frame, text="Mark as Favorite", variable=favorite_var).grid(
    row=2, column=0, columnspan=2, sticky="w", pady=5)

explicit_var = tk.StringVar(value="No")
tk.Label(form_frame, text="Explicit:").grid(row=2, column=2, sticky="w")
explicit_frame = tk.Frame(form_frame)
explicit_frame.grid(row=2, column=3, sticky="w")
tk.Radiobutton(explicit_frame, text="Yes", variable=explicit_var, value="Yes").pack(side="left")
tk.Radiobutton(explicit_frame, text="No", variable=explicit_var, value="No").pack(side="left")

def clear_fields():
    title_entry.delete(0, tk.END)
    artist_entry.delete(0, tk.END)
    duration_entry.delete(0, tk.END)
    genre_combo.current(0)
    favorite_var.set(0)
    explicit_var.set("No")

def clear_all():
    songs.clear()
    refresh_listbox()
    update_stats()

def update_stats():
    total = len(songs)
    favs = sum(1 for s in songs if s["favorite"])
    stats_label.config(text=f"Total Songs: {total}   |   Favorites: {favs}")

def refresh_listbox(filtered=None):
    song_listbox.delete(0, tk.END)
    data = filtered if filtered is not None else songs
    for s in data:
        star = "★ " if s["favorite"] else ""
        song_listbox.insert(tk.END, f"{star}{s['title']} - {s['artist']} [{s['genre']}, {s['duration']}]")

def add_song():
    title = title_entry.get().strip()
    artist = artist_entry.get().strip()
    duration = duration_entry.get().strip()

    if not validate_title(title):
        messagebox.showerror("Invalid Input", "Song title is invalid.")
        return
    if not validate_artist(artist):
        messagebox.showerror("Invalid Input", "Artist name must be like 'John Doe'.")
        return
    if not validate_duration(duration):
        messagebox.showerror("Invalid Input", "Duration must be in mm:ss format.")
        return

    songs.append({
        "title": title,
        "artist": artist,
        "genre": genre_combo.get(),
        "duration": duration,
        "favorite": bool(favorite_var.get()),
        "explicit": explicit_var.get()
    })
    refresh_listbox()
    update_stats()
    clear_fields()
    messagebox.showinfo("Success", "Song added to the library.")

def delete_song():
    selection = song_listbox.curselection()
    if not selection:
        messagebox.showwarning("No Selection", "Select a song to delete.")
        return
    index = selection[0]
    del songs[index]
    refresh_listbox()
    update_stats()
    clear_fields()

button_frame = tk.Frame(root, pady=10)
button_frame.pack(side="top", fill="x", padx=20)

tk.Button(button_frame, text="Add Song", bg="#27ae60", fg="white", width=12,
          command=add_song).pack(side="left", padx=5)
tk.Button(button_frame, text="Delete Selected", bg="#c0392b", fg="white", width=14,
          command=delete_song).pack(side="left", padx=5)
tk.Button(button_frame, text="Clear Fields", bg="#7f8c8d", fg="white", width=12,
          command=clear_fields).pack(side="left", padx=5)


search_frame = tk.Frame(root, pady=5)
search_frame.pack(side="top", fill="x", padx=20)

tk.Label(search_frame, text="Search:").pack(side="left")
search_entry = tk.Entry(search_frame, width=40)
search_entry.pack(side="left", padx=10)

def live_search(event):
    query = search_entry.get().lower().strip()
    if query == "":
        refresh_listbox()
    else:
        filtered = [s for s in songs if query in s["title"].lower() or query in s["artist"].lower()]
        refresh_listbox(filtered)

search_entry.bind("<KeyRelease>", live_search)

list_frame = tk.Frame(root)
list_frame.pack(side="top", fill="both", expand=True, padx=20, pady=10)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

song_listbox = tk.Listbox(list_frame, width=90, height=12, yscrollcommand=scrollbar.set)
song_listbox.pack(side="left", fill="both", expand=True)
scrollbar.config(command=song_listbox.yview)

def load_selected(event):
    selection = song_listbox.curselection()
    if not selection:
        return
    song = songs[selection[0]]
    clear_fields()
    title_entry.insert(0, song["title"])
    artist_entry.insert(0, song["artist"])
    duration_entry.insert(0, song["duration"])
    genre_combo.set(song["genre"])
    favorite_var.set(1 if song["favorite"] else 0)
    explicit_var.set(song["explicit"])

def play_song(event):
    selection = song_listbox.curselection()
    if selection:
        song = songs[selection[0]]
        messagebox.showinfo("Now Playing", f"Playing '{song['title']}' by {song['artist']}")

song_listbox.bind("<<ListboxSelect>>", load_selected)
song_listbox.bind("<Double-Button-1>", play_song)

stats_label = tk.Label(root, text="Total Songs: 0   |   Favorites: 0",
                        font=("Arial", 10, "italic"), fg="#34495e")
stats_label.place(x=20, y=520)

root.mainloop()
