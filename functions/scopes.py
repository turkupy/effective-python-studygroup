def do_stuff():
    my_number = 5

    # Inner scope
    def do_inner_stuff():
        # See pylint warning!
        my_number = 10
        print('Inner scope ', my_number)

    do_inner_stuff()

    print('Outer scope ', my_number)

do_stuff()