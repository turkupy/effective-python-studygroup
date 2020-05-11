# Simple coroutine example by Jason McDonald
# in https://dev.to/codemouse92/dead-simple-python-generators-and-coroutines-21ll

# Param is the array to which the results will be appended
def count_common_letters(results):
    letters = {}

    while True:
        word = yield
        print('After yield!', len(results))
        word = word.lower()
        for c in word:
            if c.isalpha():
                if c not in letters:
                    letters[c] = 0
                letters[c] += 1

        counted = sorted(letters.items(), key=lambda kv: kv[1]) # Sort by the tuples [1]th value, i.e. count of letter
        print('Counted: ', counted)
        #counted = counted[::-1] This just sorts them in descending rather than ascending order

        results.clear()
        for item in counted:
            results.append(item)


names = ['Skimpole', 'Sloppy', 'Wopsle', 'Toodle', 'Squeers',
         'Honeythunder', 'Tulkinghorn', 'Bumble', 'Wegg',
         'Swiveller', 'Sweedlepipe', 'Jellyby', 'Smike', 'Heep',
         'Sowerberry', 'Pumblechook', 'Podsnap', 'Tox', 'Wackles',
         'Scrooge', 'Snodgrass', 'Winkle', 'Pickwick']

results = []
counter = count_common_letters(results)
counter.send(None)  # prime the coroutine

for name in names:
    counter.send(name)  # send data to the coroutine

counter.close()  # manually end the coroutine

for letter, count in results:
    print(f'{letter} appears {count} times.')