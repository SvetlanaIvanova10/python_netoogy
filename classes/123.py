from python_netology.classes import Animals

сlass Birds(Animals):
    def __init__(self, eggs, name, weight, voices, food):
        super().__init__(name, weight, voices, food)
        self.eggs = eggs

    def collect_eggs(self):
        return "РЇРёС†Р° СЃРѕР±СЂР°РЅС‹" % self.eggs