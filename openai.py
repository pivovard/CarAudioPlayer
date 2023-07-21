import os

def list_files_in_folder(folder_path):
    files = os.listdir(folder_path)
    mp3_files = [f for f in files if f.endswith('.mp3')]
    subfolders = [f for f in files if os.path.isdir(os.path.join(folder_path, f))]
    return mp3_files, subfolders

def print_player_state(current_folder, prev_item, current_item, next_item):
    print("Current Folder:", current_folder)
    print("Previous:", prev_item)
    print("Current:", current_item)
    print("Next:", next_item)

def main():
    current_path = os.getcwd()
    current_folder = current_path
    mp3_files, subfolders = list_files_in_folder(current_folder)
    current_index = 0

    while True:
        current_item = mp3_files[current_index] if mp3_files else None

        print_player_state(current_folder, mp3_files[current_index - 1] if current_index > 0 else None, 
                           current_item, mp3_files[current_index + 1] if current_index < len(mp3_files) - 1 else None)

        user_input = input("Enter command (Right/Left/Up/Down): ").lower()

        if user_input == "right":
            if current_item:
                # Implement the logic for playing the current MP3 file here.
                print("Playing:", current_item)
            elif subfolders:
                folder_choice = None
                while folder_choice not in range(len(subfolders)):
                    print("Subfolders:")
                    for i, folder in enumerate(subfolders):
                        print(f"{i}: {folder}")
                    folder_choice = int(input("Enter the folder number: "))
                current_folder = os.path.join(current_folder, subfolders[folder_choice])
                mp3_files, subfolders = list_files_in_folder(current_folder)
                current_index = 0

        elif user_input == "left":
            if current_folder != current_path:
                current_folder = os.path.dirname(current_folder)
                mp3_files, subfolders = list_files_in_folder(current_folder)
                current_index = 0

        elif user_input == "up":
            current_index = max(0, current_index - 1)

        elif user_input == "down":
            current_index = min(len(mp3_files) - 1, current_index + 1)

        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
