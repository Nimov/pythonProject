# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def play_with_lists():
    mylist = [1, 2, 3, 4, 5, 6, 7, "osiem"]
    print("1:", mylist[:])
    print("2:", mylist[-1])
    print("3:", mylist[-4:-1])
    print("4:", mylist[1:])
    print("5:", mylist[1::2])


def play_with_strings():
    print("Name: %s\nNumber: %s\nString: %s" % ("Nimov", 3, 3 * "-"))

    # WARNING: Watch out for the trailing s in "%(key)s".
    print("This %(verb)s a %(noun)s." % {"noun": "test", "verb": "is"})

    name = "Nimov"
    "Hello, {}!".format(name)
    print(f"Hello, {name}!")


def play_with_loops():
    print(range(10))
    rangelist = list(range(10))
    print(rangelist)

    for number in range(10):
        # Check if number is one of
        # the numbers in the tuple.
        if number in (3, 4, 7, 9):
            # "Break" terminates a for without
            # executing the "else" clause.
            print("Just before a break")
            break
        else:
            # "Continue" starts the next iteration
            # of the loop. It's rather useless here,
            # as it's the last statement of the loop.
            print("No break here")
            continue
    else:
        # The "else" clause is optional and is
        # executed only if the loop didn't "break".
        print("Do nothing")
        pass  # Do nothing

    if rangelist[1] == 1:
        print("The second item (lists are 0-based) is 1")
    elif rangelist[1] == 3:
        print("The second item (lists are 0-based) is 3")
    else:
        print("Dunno")

#    while rangelist[1] == 1:
#        print("We are trapped in an infinite loop!")


# Same as def funcvar(x): return x + 1
funcvar = lambda x: x + 1


def passing_example(a_list, an_int=2, a_string="A default string"):
    a_list.append("A new item")
    an_int = 4
    return a_list, an_int, a_string


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    play_with_lists()
    play_with_strings()
    play_with_loops()
    # playing with functions
    print(funcvar(4))
    my_list = [1, 2, 3]
    my_int = 10
    print(passing_example(my_list, my_int))
    print(my_list)
    print(my_int)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
