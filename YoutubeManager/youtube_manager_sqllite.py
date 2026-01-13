import sqlite3

conn = sqlite3.connect("youtube_videos.db")
cur = conn.cursor()

cur.execute(
    """
        CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
        )               
"""
)


def list_all_youtube_videos():
    cur.execute("SELECT * FROM videos")
    for row in cur.fetchall():
        print(f"{row[0]}. Name- {row[1]}, Duration- {row[2]}")


def add_youtube_video(name, time):
    cur.execute("INSERT INTO videos (name,time) VALUES (?,?)", (name, time))
    conn.commit()


def update_youtube_video(video_id, name, time):
    cur.execute("UPDATE videos SET name=?, time=? WHERE id = ?", (name, time, video_id))
    conn.commit()


def delete_youtube_video(video_id):
    cur.execute("DELETE FROM videos  WHERE id = ?", (video_id,))
    conn.commit()


def main():
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
                list_all_youtube_videos()
            case "2":
                name = input("Enter video name: ")
                time = input("Enter video time: ")
                add_youtube_video(name, time)

            case "3":
                id = input("Enter video Id to update: ")
                name = input("Enter video name: ")
                time = input("Enter video time: ")
                update_youtube_video(id, name, time)
            case "4":
                id = input("Enter video Id to delete: ")
                delete_youtube_video(id)
            case "5":
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Please try again.")
    conn.close()


if __name__ == "__main__":
    main()
