class Humanoid: #То есть здесь я определяю общий набор характеристик который будет присвоен всем гуманоидам(человек,зомби,соладт,рабочий)
    def __init__(self, hp: int, speed: int):
        self.hp = hp  #то есть пока хп (числовое значение)
        self.speed = speed #скорость

class Building: #Тут набор характеристик, которые будет иметь строения
    def __init__(self, strength: int, price: int):
        self.strength = strength #прочность (значение измеряется до 100 единиц)
        self.price = price #стоимость (значения измеряется в числах)

class Resource:
    def __init__(self, weight: int):
        self.weight = weight




