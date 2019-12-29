class Animals:
    def __init__(self, name, weight, voices, food):
        self.name = name
        self.weight = weight
        self.voices = voices
        self.food = food

    def feed(self):
        """
        РљРѕСЂРјРёС‚СЊ Р¶РёРІРѕС‚РЅС‹С…
        """
        return "РЇ РїРѕРєРѕСЂРјР»РµРЅ" % self.food

    def distinguish_by_voice(self):
        """
        Р Р°Р·Р»РёС‡РёРµ РїРѕ РіРѕР»РѕСЃР°Рј
        """

        return "РЇ " % self.name


class Birds(Animals):

    def __init__(self, eggs, name, weight, voices, food):
        super().__init__(name, weight, voices, food)
        self.eggs = eggs

    def collect_eggs(self):
        return "РЇРёС†Р° СЃРѕР±СЂР°РЅС‹" % self.eggs