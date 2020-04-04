original_numbers = [1, 2, 3, 4, 5, 6]

# List comprehension
doubled = [number * 2 for number in original_numbers]
print(doubled)

# Map with Lambda (map takes two params, the function for mapping and the original list)
tripled = map(lambda number: number * 3, original_numbers)
print(tripled, list(tripled))

# List comprehension with conditional
doubled_even_numbers = [number * 2 for number in original_numbers if number % 2 == 0]
print(doubled_even_numbers)

# Map with Lambda and filter
tripled_even_numbers = map(lambda number: number * 3, filter(lambda number: number % 2 == 0, original_numbers))


# Dictionaries and sets
hardware_skills = {
    'Mila': 10,
    'Magda': 3,
    'Mystery Friend': 7
}

# Convert the skill levels to be between 0-5
skill_levels = {name: level // 2 for name, level in hardware_skills.items()}
print(skill_levels)

# Just get a set of all ranks
ranks = {level for name, level in hardware_skills.items()}
print(ranks)




