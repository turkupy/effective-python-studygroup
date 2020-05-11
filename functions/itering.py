class GeneratedNumbers:
    def __iter__(self):
        for i in range(1, 6):
            yield i


generated_numbers = GeneratedNumbers()


def percentages(numbers):
    if iter(numbers) is iter(numbers):
        raise TypeError('Must supply a container, got: ', numbers)

    total = sum(numbers)
    return [100 * value / total for value in numbers]


result_container = percentages(generated_numbers)
result_list = percentages([1, 2, 3, 4, 5])
my_generator = (number for number in range(1, 6))
# Errs
result_generator = percentages(my_generator)

print('Container: ', result_container)
print('List: ', result_list)
print('Generator: ', result_generator)


