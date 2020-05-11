from collections import defaultdict


# Count stuff when called
class CountMissing(object):
    def __init__(self):
        self.added = 0

    def __call__(self, *args, **kwargs):
        self.added += 1
        print("Adding one!")
        return 0


count_missing = CountMissing()
current = {'red': 9, 'green': 8}
increments = [
    ('red', 5),
    ('green', 17),
    ('blue', 9),
]

# Defaultdict allows you to define a function that is called each time a missing key is added
result = defaultdict(count_missing, current)
print('Before', dict(result))
for key, amount in increments:
    result[key] += amount
print('After', dict(result))

assert count_missing.added == 1
