class Topscore:
    def __init__(self, x):
        self.high_score = x

    def top_score(self, score):
        if score > self.high_score:
            self.high_score = score
        return self.high_score
