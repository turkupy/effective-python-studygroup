# In this example grade implements the descriptor protocol
class Grade(object):
    def __init__(self):
        self._value = 0

    # Descriptors that only define get are known as non-data descriptors
    def __get__(self, instance, instance_type):
        return self._value

    # If an object implements set (or delete) it is considered a data descriptor
    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._value = value


class Exam(object):
    # Class attributes
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()

