class Animals:
    def __init__(self, name, weight, voices, food):
        self.name = name
        self.weight = weight
        self.voices = voices
        self.food = food

    def feed(self):

        return "Меня покормили" % self.food

    def distinguish_by_voice(self):
        return "РЇ " % self.name