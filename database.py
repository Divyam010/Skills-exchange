class SkillDatabase:
    def __init__(self):
        self.listings = {}  # username: skill

    def add_listing(self, username, skill):
        self.listings[username] = skill

    def get_all_listings(self):
        return self.listings