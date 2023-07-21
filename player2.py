from pygame import mixer
import os
import json

root = '.'


def print_directory(list):
    for item in list:
        print(item)

def print_song():
    pass

def print_error(msg):
    print("Error: " + msg)

def main():
    folder = root
    song_id = 0
    
    if os.path.isfile(f'{root}/player.config'):
        f = open("player.config", "r")
        data=json.load(f)
        folder = data["folder"]
        song_id = int(data["song_id"])
        f.close()

    files = os.listdir(folder)
    print_directory(files)

if __name__ == '__main__':
    main()