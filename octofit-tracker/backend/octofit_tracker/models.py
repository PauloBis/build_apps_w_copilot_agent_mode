from pymongo import MongoClient

# MongoDB client setup
client = MongoClient('localhost', 27017)
db = client['octofit_db']

# Example: Accessing collections
def get_users_collection():
    return db['users']

def get_teams_collection():
    return db['teams']

def get_activity_collection():
    return db['activity']

def get_leaderboard_collection():
    return db['leaderboard']

def get_workouts_collection():
    return db['workouts']
