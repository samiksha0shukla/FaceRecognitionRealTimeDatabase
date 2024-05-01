import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://faceattendancerealtime-f13b4-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "0225CS211129":
        {
            "name": "Sagar Yadav",
            "major": "Computer Science",
            "starting_year":2021,
            "total_attendance":70,
            "standing": "A+",
            "year":3,
            "last_attendance_time": "2024-04-22 02:14:04"
        },

    "0225CS211136":
        {
            "name": "Samiksha Shukla",
            "major": "Computer Vision",
            "starting_year":2021,
            "total_attendance":60,
            "standing": "A",
            "year":3,
            "last_attendance_time": "2024-04-22 02:14:04"
        },

    "0225CS211137":
        {
            "name": "Khan Sir",
            "major": "Robotics",
            "starting_year": 2020,
            "total_attendance": 40,
            "standing": "B",
            "year":4,
            "last_attendance_time": "2024-04-22 02:14:04"
        },

    "0225CS211138":
        {
            "name": "Emily Blunt",
            "major": "Arts",
            "starting_year": 2022,
            "total_attendance": 15,
            "standing": "C",
            "year": 2,
            "last_attendance_time": "2024-04-22 02:14:04"
        },

    "0225CS211139":
        {
            "name": "Alon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 30,
            "standing": "B+",
            "year": 4,
            "last_attendance_time": "2024-04-22 02:14:04"
        }
}

for key, value in data.items():
    ref.child(key).set(value)