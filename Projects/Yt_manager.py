import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test = json.load(file)
            print(test)
            print(type(test))
            return test
    except FileNotFoundError:
        print("File not found")
        return []

    
    
def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)

def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video["name"]}, Duration: {video["time"]}")
 
def update_video(videos):
     list_all_videos(videos)
     index= int((input("Index of the video , want to update: ")))
     if 1 <= index <= len(videos):        
        name = input("Enter the video name: ")
        time = input("Enter the video duration: ")
        videos[index -1 ] = {'name': name, 'time': time}
        save_data_helper(videos)
     else:
        print("Invalid index selected!")
        
     
def add_video(videos):
    name = input("Enter the name: ")
    time = input("Enter the time")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)


def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | choose option.")
        print("1. List all youtube videos")
        print("2. Add a yt video")
        print("3. Update a yt video details")
        print("4. Delete a yt video")
        print("5. Exit the app")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(video)
            case '5':
                break
            case _:
                print("Invalid choice")
if __name__ == "__main__":
    main()