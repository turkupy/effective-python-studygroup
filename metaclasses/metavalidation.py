class ValidateAnimal(type):
    def __new__(meta, name, bases, class_dict):
        print((meta, name, bases, class_dict))
        if class_dict['feet'] and class_dict['feet'] < 0:
            raise ValueError("Cannot have negative amout of feet!")
        return type.__new__(meta, name, bases, class_dict)


class Cat(object, metaclass=ValidateAnimal):
    feet = 4
    sound = "Purrr"

    def purr(self):
        print(self.sound)


class Snail(object, metaclass=ValidateAnimal):
    feet = -1
