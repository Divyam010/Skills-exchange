import json
import os

class AuthManager:
    def __init__(self, filepath="users.json"):
        self.filepath = filepath
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as f:
                self.users = json.load(f)
        else:
            self.users = {}

    def save_users(self):
        with open(self.filepath, "w") as f:
            json.dump(self.users, f)

    def signup(self, username, password):
        if username in self.users:
            return False
        self.users[username] = password
        self.save_users()
        return True

    def login(self, username, password):
        return self.users.get(username) == password

