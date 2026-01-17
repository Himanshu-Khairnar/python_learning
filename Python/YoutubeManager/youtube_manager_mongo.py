from pymongo.mongo_client import MongoClient
uri = "mongodb+srv"
from bson import ObjectId

# Create a new client and connect to the server
client = MongoClient(uri,tlsAllowInvalidCertificates=True)
db = client["youtube_manager"]
videos_collection = db["videos"]



def list_all_youtube_videos():
    for video in videos_collection.find():
        print(f"{video['_id']}. Name- {video['name']}, Duration- {video['time']}")
    


def add_youtube_video(name, time):
    videos_collection.insert_one({"name": name, "time": time})  

def update_youtube_video(video_id, name, time):
    up = videos_collection.update_one({"_id": ObjectId(video_id)}, {"$set": {"name": name, "time": time}})
    if up.modified_count > 0:
        print("Video updated successfully!")
    else:
        print("Video not found.")
def delete_youtube_video(video_id):
    videos_collection.delete_one({"_id": ObjectId(video_id)})


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
if __name__ == "__main__":
    main()
