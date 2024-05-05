class Score:
    def __init__(self):
        self.score = 0
        self.eggs = 0

    def increase_score(self):
        self.score += 1

    def increase_eggs(self):
        self.eggs += 1

    def get_score(self):
        return self.score

    def get_eggs(self):
        return self.eggs
