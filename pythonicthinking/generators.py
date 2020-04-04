# Creating a generator expression
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
double_generator = (number * 2 for number in numbers)  # Use () to make a generator
print(double_generator)

# You can advance it one step at a time, only the current value is held in memory
# HOX these are stateful
# If looking at large inputs, generator expressions could be the way to go!
print(next(double_generator))
print(next(double_generator))

# You can also use a generator as an input in a generator expression
# (notice how the stateful double_generator now is at step 3!)
half_generator = (number // 2 for number in double_generator)  # Use () to make a generator
print(next(half_generator))

