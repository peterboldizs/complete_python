import fnmatch
import os


def list_all_songs(root):
    for path, dirs, files in os.walk(root, topdown=True):
        if files:
            print(path)
            first_split = os.path.split(path)
            print(first_split)
            second_split = os.path.split(first_split[0])
            print(second_split)
            for f in files:
                song_details = f.strip('.emp3').split(' - ')
                print(song_details)


def find_albums(root, artist_name):
    for path, dirs, files in os.walk(root):
        for artist in fnmatch.filter(dirs, artist_name):
            subdir = os.path.join(path, artist)
            # print(subdir)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album


def find_songs(albums):
    for album in albums:
        for song in os.listdir(album[0]):
            yield song


def find_music(start, extension):
    for path, dirs, files in os.walk(start):
        for file in fnmatch.filter(files, "*.{}".format(extension)):
            abs_path = os.path.abspath(path)
            yield os.path.join(abs_path, file)


print("list all Doors songs")
list_all_songs("music/Doors")
print("-" * 40)
print("find all U2 albums")
alb_list = find_albums("music", "u2*")
song_list = find_songs(alb_list)
for s in song_list:
    print(s)
print("=" * 40)
print("list all Beatles emp3 files - absolute paths")
for f in find_music("music/Beatles", "emp3"):
    print(f)
