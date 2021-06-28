# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def play_with_lists():
    mylist = [1, 2, 3, 4, 5, 6, 7, "osiem"]
    print("1:", mylist[:])
    print("2:", mylist[-1])
    print("3:", mylist[-4:-1])
    print("4:", mylist[1:])
    print("5:", mylist[1::2])

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    play_with_lists()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
