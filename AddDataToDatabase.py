import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://attendencerecognition-default-rtdb.firebaseio.com/"
})

ref = db.reference('Employees')

data = {
    "202301":
        {
            "name": "Akshay Patil",
            "major": "Backend Developer",
            "starting_year": 2023,
            "total_attendance": 9,
            "standing": "G",
            "year": 1,
            "last_attandence_time": "2023-07-01 09:30:34"
        },
    "202302":
        {
            "name": "Bhavyashree",
            "major": "Manager",
            "starting_year": 2023,
            "total_attendance": 10,
            "standing": "G",
            "year": 1,
            "last_attandence_time": "2023-07-01 10:01:34"
        },
    "202303":
        {
            "name": "Harish Poojari",
            "major": "Founder",
            "starting_year": 2022,
            "total_attendance": 0,
            "standing": "G",
            "year": 2,
            "last_attandence_time": "2023-07-01 10:01:34"
        },
    "202304":
            {
                "name": "Latha",
                "major": "Trainer",
                "starting_year": 2022,
                "total_attendance": 0,
                "standing": "G",
                "year": 2,
                "last_attandence_time": "2023-07-01 10:01:34"
            }
}

for key, value in data.items():
    ref.child(key).set(value)
