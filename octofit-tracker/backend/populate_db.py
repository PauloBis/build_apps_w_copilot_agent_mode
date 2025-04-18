from pymongo import MongoClient

# Connect to the MongoDB instance
client = MongoClient('localhost', 27017)
db = client['octofit_db']

# Insert test data into the users collection
db.users.insert_many([
    {"username": "john_doe", "email": "john@example.com", "password": "password123"},
    {"username": "jane_doe", "email": "jane@example.com", "password": "password456"}
])

# Insert test data into the teams collection
db.teams.insert_many([
    {"name": "Team Alpha", "members": []},
    {"name": "Team Beta", "members": []}
])

# Insert test data into the activity collection
db.activity.insert_many([
    {"user": "john_doe", "activity_type": "Running", "duration": "00:30:00"},
    {"user": "jane_doe", "activity_type": "Cycling", "duration": "01:00:00"}
])

# Insert test data into the leaderboard collection
db.leaderboard.insert_many([
    {"user": "john_doe", "score": 100},
    {"user": "jane_doe", "score": 150}
])

# Insert test data into the workouts collection
db.workouts.insert_many([
    {"name": "Push-ups", "description": "Do 20 push-ups"},
    {"name": "Sit-ups", "description": "Do 30 sit-ups"}
])

print("Test data inserted successfully!")
