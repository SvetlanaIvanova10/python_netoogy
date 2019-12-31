class Animal:
    def __init__(self, name, weight, voice):
        self.name = name
        self.weight = weight
        self.voice = voice

    def feed(self):
        return "покормили"

    def distinguish_by_voice(self):
        return f'услышали {self.voice}'


class Sheep(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight, 'бе-бе')

    def wool(self):
        return "остригли"


class Goat(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight, 'ме-ме')

    def milk(self):
        return "подоили"

class Cow(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight, 'му-му')

    def milk(self):
        return "подоили"

class Birds(Animal):

    def __init__(self, name, weight, voice):
        super().__init__(name, weight, voice)

    def collect_eggs(self):
        return "собрали яйца"


class Chicken(Birds):
    def __init__(self, name, weight):
        super().__init__(name, weight, "ко-ко-ко")

class Duck(Birds):
    def __init__(self, name, weight):
        super().__init__(name, weight, 'кря-кря')




class Goose(Birds):
    def __init__(self, name, weight):
        super().__init__(name, weight, 'га-га-га')

