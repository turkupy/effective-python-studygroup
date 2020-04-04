from itertools import zip_longest

recipes = {
    'challah': {'prep_time': 90},
    'ice cream': {'prep_time': 120},
    'pancakes': {'prep_time': 30}
}

prep_times = [item['prep_time'] for name, item in recipes.items()]
dish_names = [name for name, item in recipes.items()]

print(prep_times, dish_names)

# Challenge: iterate over both new lists in parallel to get 'challah', 90 etc.
# for dish_name, prep_time in zip(dish_names, prep_times):
#     print(f"Making {dish_name} takes {prep_time} minutes.")


# Make the other list longer, zip will stop at the end of the shorter one
dish_names.append('banana split')

for dish_name, prep_time in zip(dish_names, prep_times):
    print(f"Making {dish_name} takes {prep_time} minutes.")

print("Itertools' ZIP LONGEST:")
for dish_name, prep_time in zip_longest(dish_names, prep_times):
    print(f"Making {dish_name} takes {prep_time} minutes.")
