import random
from typing import Callable

# Functions are first-class objects in Python -->


def random_color() -> str:
    color_choices = ['red', 'orange', 'green', 'cyan']
    return random.choice(color_choices)


# You can assign functions to variables
picker = random_color
print(picker())


# You can pass functions as arguments
def print_return_value(func: Callable[[str], str]):
    print(f'{func} returns {func()}')


print_return_value(random_color)


# You can return functions from functions
def create_name_maker(prefix: str) -> Callable[[str], str]:
    def name_maker(name: str): return f'{prefix}-{name}'
    return name_maker


my_name_maker = create_name_maker('silly')
my_name = my_name_maker('Magda')

print(my_name)
