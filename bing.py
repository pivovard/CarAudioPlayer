import pygame
import os

def play_music(music_file):
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    try:
        pygame.mixer.music.load(music_file)
        print("Music file {} loaded!".format(music_file))
    except pygame.error:
        print("File {} not found! ({})".format(music_file, pygame.get_error()))
        return
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        clock.tick(30)

def main():
    folder = '.'
    while True:
        print(f"\nCurrent folder: {os.path.abspath(folder)}")
        files = os.listdir(folder)
        files.sort()
        for i, file in enumerate(files):
            if os.path.isdir(os.path.join(folder, file)):
                print(f"  {i+1}. {file}/")
            else:
                print(f"  {i+1}. {file}")
        print("\nPress left arrow to go up one level.")
        print("Press right arrow to play/pause or enter a subfolder.")
        print("Press up/down arrow to navigate in the current folder.")
        choice = input("Enter your choice: ")
        if choice == 'q':
            break
        elif choice == 'left':
            folder = os.path.dirname(folder)
            continue
        elif choice == 'right':
            if os.path.isdir(os.path.join(folder, files[int(choice)-1])):
                folder = os.path.join(folder, files[int(choice)-1])
                continue
            else:
                music_file = os.path.join(folder, files[int(choice)-1])
                play_music(music_file)
                continue
        elif choice.isdigit() and int(choice) <= len(files):
            if os.path.isdir(os.path.join(folder, files[int(choice)-1])):
                folder = os.path.join(folder, files[int(choice)-1])
                continue
            else:
                music_file = os.path.join(folder, files[int(choice)-1])
                play_music(music_file)
                continue

if __name__ == '__main__':
    main()
