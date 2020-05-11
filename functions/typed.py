# Type hints are available in python > 3.5


def generate_name(name: str, town: str) -> str:
    return f'The Great {name} of {town}!'


print(generate_name('Mila', 'Turku'))


# Explicitly state return type None
def print_greeting(name: str) -> None:
    print(f'Hello, {name}!!!')


print_greeting('Magda')
