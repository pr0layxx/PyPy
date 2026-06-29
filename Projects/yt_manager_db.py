import sqlite3

conn = sqlite3.connectoin("yt_manager.db")
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS videos(
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   time TEXT NOT NULL
                )
               
               """)

def main():
    while True:
        print("\n YT MANAGER || CHOOSE AN OPTION")
        print("1. List all youtube videos")
        print("2. Add a yt video")
        print("3. Update a yt video details")
        print("4. Delete a yt video")
        print("5. Exit the app")

if __name__ =="__main__":
    main()