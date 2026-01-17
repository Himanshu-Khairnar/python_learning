import json

file_name = "youtube_videos.json"


def load_data():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open(file_name, "w") as file:
        json.dump(videos, file)


def list_all_youtube_videos(videos):
    print("\n")
    print("*" * 50)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name- {video['name']}, Duration- {video['time']}")
    print("*" * 50)


def add_new_youtube_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)


def update_youtube_video(videos):
    list_all_youtube_videos(videos)
    id = int(input("Enter the id of video:\n"))

    new_name = input(
        "Enter the new name of the video: (press enter if you don't wanna change the name) \n"
    )
    new_time = input(
        "Enter the new time of the video: (press enter if you don't wanna change the time) \n"
    )
    if id < 1 or id > len(videos):
        print("Invalid ID selected")
        return
    if new_name == "":
        new_name = videos[id - 1]["name"]
    if new_time == "":
        new_time = videos[id - 1]["time"]

    videos[id - 1] = {"name": new_name, "time": new_time}
    print("Video updated successfully!")
    save_data_helper(videos)


def delete_youtube_video(videos):
    list_all_youtube_videos(videos)
    id = int(input("Enter the id of video:\n"))
    if id < 1 or id > len(videos):
        print("Invalid ID selected")
        return

    videos.pop(id - 1)
    save_data_helper(videos)
    print("Video deleted successfully!")


def main():
    videos = load_data()
    while True:
        print("\n")
        print("-" * 50)
        print("Managing YouTube content...")
        print("1. List all youtube videos")
        print("2. Add a new youtube video")
        print("3. Update a youtube video")
        print("4. Delete a youtube video")
        print("5. Exit")
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                list_all_youtube_videos(videos)
            case "2":
                add_new_youtube_video(videos)
            case "3":
                update_youtube_video(videos)
            case "4":
                delete_youtube_video(videos)
            case "5":
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
