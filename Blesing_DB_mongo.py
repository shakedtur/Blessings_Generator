
from pymongo import MongoClient
from datetime import datetime
from Mongo import Access_keys

def save_text_in_mogoDB(text):
# Connect to MongoDB
    client= MongoClient(Access_keys.Mongo_secret)
    print(client)

    # Select database and collection
    db = client['mydatabase']  # Replace with your database name
    collection = db['blessings']  # Replace with your collection name


    # Your blessing text


    current_datetime = datetime.now()
    current_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    blessing = {
        "text": text,
        "author": "shaked",  # Optional: Add more fields
        "date": current_datetime    # Optional: Store the creation date
    }

    # Insert the blessing into the collection
    result = collection.insert_one(blessing)

    # Print the ID of the inserted document
    print(f"Blessing saved with ID: {result.inserted_id}")
