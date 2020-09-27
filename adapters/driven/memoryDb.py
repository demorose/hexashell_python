class MemoryDb():
    db = {}

    def get_user(self, id):
        return self.db[id]

