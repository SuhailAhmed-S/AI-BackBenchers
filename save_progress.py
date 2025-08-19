# save_progress.py
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['gym_coach']
progress = db['user_progress']

# Insert a workout record
progress.insert_one({
    "username": "john",
    "exercise": "pushup",
    "reps": 15,
    "sets": 3
})

print("Data saved successfully!")
