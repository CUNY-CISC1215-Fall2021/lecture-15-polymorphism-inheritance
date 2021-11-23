# Coding exercise conducted as part of Lecture 15
# demonstrating the value of polymorphism
#
# Task: Create a list containing an empty list, empty tuple,
# and empty string. Then write a function that appends a
# given object to every object in the list.
my_list = [
    [],
    tuple(),
    "",
]


def append_all(lst, val):
    # Because lists, tuples, and strings all have different interfaces,
    # we have to write code like this to make the function work.
    # This is not good (and part of the reason we like lists containing
    # objects of the same type).
    for i in range(len(lst)):
        if isinstance(lst[i], list):
            lst[i] = lst[i] + [val]
        elif isinstance(lst[i], tuple):
            lst[i] = lst[i] + (val,)
        elif isinstance(lst[i], str):
            lst[i] = lst[i] + val


print(my_list)
append_all(my_list, "a")
print(my_list)