songs = []
playlist = []

while True:
    print("\n1-Add 2-Show 3-Search 4-Sort 5-Add to playlist 6-Show playlist 7-Remove from playlist 8-Exit")
    choice = input("Choose: ")

    match choice:
        case "1":
            name = input("Song name: ")
            singer = input("Singer: ")
            songs.append(name + " - " + singer)
            print("Song added!")

        case "2":
            for i in range(len(songs)):
                print(i + 1, "-", songs[i])
            if len(songs) == 0:
                print("No songs yet")

        case "3":
            word = input("Search: ")
            found = False
            for song in songs:
                if word.lower() in song.lower():
                    print(song)
                    found = True
            if found == False:
                print("Not found")

        case "4":
            songs.sort()
            print("Sorted by name!")

        case "5":
            n = int(input("Song number: "))
            if n < 1 or n > len(songs):
                print("Invalid number")
            else:
                playlist.append(songs[n - 1])
                print("Added to playlist!")

        case "6":
            for i in range(len(playlist)):
                print(i + 1, "-", playlist[i])
            if len(playlist) == 0:
                print("Playlist is empty")

        case "7":
            n = int(input("Playlist number: "))
            if n < 1 or n > len(playlist):
                print("Invalid number")
            else:
                playlist.pop(n - 1)
                print("Removed!")

        case "8":
            break

        case _:
            print("Invalid option")
