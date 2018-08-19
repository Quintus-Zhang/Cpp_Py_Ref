def syntax_var_assign():
    """
        Variable Assignment
        In python, when we assign a value to a variable, we say the variable refers to the value(object).
        e.g. variable name 'a' refers to a string object 'Hello', or, we can say, name 'a' is bind to a string object
             'Hello'
             when we assign 'a' to "World", the string object containing 'hello' is unaffected. We just change the
             binding of the name 'a'.
    """
    a = 'Hello'
    print(f'{a} is stored at {hex(id(a))}')
    a = "World"
    print(f'{a} is stored at {hex(id(a))}')

    ## Output
    # Hello is stored at 0x10d251340
    # World is stored at 0x10d251378

    ## Notes
    # id()
    # Return the “identity” of an object. This is an integer (or long integer) which is guaranteed
    # to be unique and constant for this object during its lifetime.


def syntax_print():
    """
        Print
    """
    print("Hello, World!")

    # Output
    # Hello, World!


def syntax_for():
    """
        For-loop to print the number in the range
    """
    for i in range(5):
        print(i)

    ## Output
    # 0
    # 1
    # 2
    # 3
    # 4

    ## Notes
    # range()
    # Rather than being a function, range is actually an immutable sequence type.
    # The range type represents an immutable sequence of numbers and is commonly used for
    # looping a specific number of times in for loops.


def syntax_for_continue():
    """
        For loop to print the number in the range, using continue statement to skip the odd numbers
    """

    for i in range(5):
        if i % 2 == 1:
            continue
        print(i)

    ## Output
    # 0
    # 2
    # 4


def syntax_for_break():
    """
        For loop to print the number in the range, using break statement to terminate the loop
    """
    for i in range(5):
        if i >= 3:
            break
        print(i)

    ## Output
    # 0
    # 1
    # 2


def syntax_while():
    """
        While loop to print the number from 0 to 4
    """
    i = 0
    while i < 5:
        print(i)
        i += 1

    ## Output
    # 0
    # 1
    # 2
    # 3
    # 4


def syntax_while_continue():
    """
        While loop to print the number from 0 to 4, using continue statement to skip the odd numbers
    """
    i = 0
    while i < 5:
        if i % 2 == 1:
            i += 1
            continue
        print(i)
        i += 1

    ## Output
    # 0
    # 2
    # 4


def syntax_while_break():
    """
        While loop to print the number from 0 to 4, using break statement to terminate the loop
    """
    i = 0
    while i < 5:
        if i >= 3:
            break
        print(i)
        i += 1

    ## Output
    # 0
    # 1
    # 2


def syntax_if_else():
    """
        If-else statement
    """
    s = 1
    if s:
        print(s)
    else:
        print(s)

    ## Output
    # 1


def syntax_if_elif_else():
    """
        If-elif-else statement
        There is no switch-case statement in python, use if-elif-else instead
    """
    s = 0.1
    if s < 0:
        print("s is smaller than 0")
    elif s > 1:
        print("s is greater than 1")
    else:
        print("s is between 0 and 1")

    ## Output
    # s is between 0 and 1


def syntax_logical_op(s, t):
    """
        Logical operators
        1. and: logical and
        2. or: logical or
        3. not: logical not
    """
    if s and t:
        print(f's = {s}, t = {t}, s and t = {s and t}')
    elif s or t:
        print(f's = {s}, t = {t}, s or t = {s or t}')
    else:
        print(f's = {s}, t = {t}, not s = {not s}, not t = {not t}')

    # when s = 1, t = 0
    ## Output
    # s = 1, t = 0, s or t = 1


def ds_list():
    """
        List Methods
        1. append(): Adds an element at the end of the list
        2. pop(idx): Removes the element at the specified position 'idx', If no index is specified, a.pop() removes and
                     returns the last item in the list.
        3. insert(idx, x): Adds an element 'x' at the specified position 'idx'
        4. remove(x): Remove the first item from the list whose value is x.
        5. clear(): Removes all the elements from the list
    """
    a = []

    print('empty list --> ', end='')
    for i in range(5):
        a.append(i)
    print(a)

    print('           --> ', end='')
    a.pop()
    print(a)

    print('           --> ', end='')
    a.insert(0, 9)
    print(a)

    print('           --> ', end='')
    a.remove(9)  # a.pop(0)
    print(a)

    print('           --> ', end='')
    a.clear()
    print(a)

    ## Output
    # empty list --> [0, 1, 2, 3, 4]
    #            --> [0, 1, 2, 3]
    #            --> [9, 0, 1, 2, 3]
    #            --> [0, 1, 2, 3]
    #            --> []


def ds_list_extend():
    """
        List Method
        extend(): Extend the list by appending all the items from the iterable.
    """
    a = [1, 2, 3, 4, 5]
    b = [2, 3, 4]

    print(f"a: {a}")
    print(f"b: {b}")
    a.extend(b)
    print(f"a: {a}")

    ## Output
    # a: [1, 2, 3, 4, 5]
    # b: [2, 3, 4]
    # a: [1, 2, 3, 4, 5, 2, 3, 4]


def ds_list_index():
    """
        List Method
        index(x): Return zero-based index in the list of the first item whose value is 'x'.
    """
    a = [1, 2, 3, 4, 5, 2, 3, 4]
    print(a)
    print(f"The first occurrence of 2 is at {a.index(2)}")

    ## Output
    # [1, 2, 3, 4, 5, 2, 3, 4]
    # The first occurrence of 2 is at 1


def ds_list_count():
    """
        List Method
        count(x): Return the number of times 'x' appears in the list.
    """
    a = [1, 2, 3, 4, 5, 2, 3, 4]
    print(a)
    print(f"# of 3 in the list is {a.count(3)}")

    ## Output
    # [1, 2, 3, 4, 5, 2, 3, 4]
    # # of 3 in the list is 2


def ds_list_sort():
    """
        List Method
        sort(): Sorts the list inplace
    """
    a = [1, 2, 3, 4, 5, 2, 3, 4]
    print(a)
    a.sort()
    print(a)

    ## Output
    # [1, 2, 3, 4, 5, 2, 3, 4]
    # [1, 2, 2, 3, 3, 4, 4, 5]


def ds_dict():
    """
        Dict Methods
        1. get(key[, default]): Return the value for key if key is in the dictionary, else default. If default is not
                                given, it defaults to None, so that this method never raises a KeyError.
        2. in operator: Return True if dict has a specified key, else False.
        3. update(): Update the dictionary with the key/value pairs from other, overwriting existing keys. Return None.
        4. search: use in operator with [] operator, or just use get() method
    """
    print('Dict initialization: ', end='')
    a_dict = {'a': 1, 'b': 3, 'c': 5, 'd': 7}  # or a_map = dict(a=1, b=3, c=5, d=7)
    print(a_dict, '\n')

    print("get method: ", end='')
    print(f"a_dict.get('a') returns {a_dict.get('a')}\n")

    print(f"in: ", end='')
    print(f"'d' in a_dict returns {'d' in a_dict}", end=', ')
    print(f"'e' in a_dict returns {'e' in a_dict}\n")

    print("update method: ", end='')
    a_dict.update({'x': 9})
    print(f'updated dict is {a_dict}\n')

    print("search: ", end='')
    k = 'b'
    if k in a_dict:
        print(a_dict[k])

    ## Output
    # Dict initialization: {'a': 1, 'b': 3, 'c': 5, 'd': 7}
    #
    # get method: a_dict.get('a') returns 1
    #
    # in: 'd' in a_dict returns True, 'e' in a_dict returns False
    #
    # update method: updated dict is {'a': 1, 'b': 3, 'c': 5, 'd': 7, 'x': 9}
    #
    # search: 3


def ds_dict_keys_values_items():
    """
        Dict Method
        1. keys(): Returns an iterable view of keys
        2. values(): Returns an iterable view of values
        3. items(): Returns an iterable view of key-value pair
    """
    a_dict = {'a': 1, 'b': 3, 'c': 5, 'd': 7}
    print(a_dict.keys())
    print(a_dict.values())
    print(a_dict.items())

    ## Output
    # dict_keys(['a', 'b', 'c', 'd'])
    # dict_values([1, 3, 5, 7])
    # dict_items([('a', 1), ('b', 3), ('c', 5), ('d', 7)])

    ## Notes
    # view object
    # it is dynamic, if you drop one of your keys, the view does change as well.


def ds_dict_sort_by_key():
    """
        Dict Method
        Sort dict by key
    """
    mydict = {'carl': 40, 'alan': 2, 'bob': 1, 'danny': 3}
    print(mydict)

    for key in sorted(mydict.keys()):
        print(key, mydict[key])

    ## Output
    # {'carl': 40, 'alan': 2, 'bob': 1, 'danny': 3}
    # alan 2
    # bob 1
    # carl 40
    # danny 3


def str_concatenate():
    """
        String Manipulation
        '+' operator: concatenate two string objects
    """
    s1 = 'Hello'
    s2 = 'World'
    s3 = s1 + s2
    print(f"s3 = s1 + s2 = {s3}")
    print(f"length of s3 = {len(s3)}")

    ## Output
    # s3 = s1 + s2 = HelloWorld
    # length of s3 = 10


def str_find_substr():
    """
        String Manipulation
        find(str, beg=0, end=len(string)): Return index of the first occurrence if found, -1 otherwise
    """
    s = "Hello World! \nHaHa \tNaNa"
    print(s.find('or'))
    print(s.find('\n'))
    print(s.find('\t'))
    print(s.find('z'))

    ## Output
    # 7
    # 13
    # 19
    # -1


def str_substr():
    """
        String Manipulation
        [] operator: To access substrings, use the square brackets for slicing along with the index to obtain your
                     substring.
    """
    #
    s = "Hello, World!"
    print(s[:5])

    ## Output
    # Hello


def str_num_format():
    """
        String Manipulation
        format specifiers: width.precision
    """
    n = 3.1415926
    print(f'{n:10.5f}')

    ## Output
    #    3.14159


def iter_py():
    """
        normally, we do not use iter to traverse over container
    """
    s = "Hello, World!"
    it = iter(s)
    while True:
        try:
            print(next(it))
        except:
            break

    ## Output
    # H
    # e
    # l
    # l
    # o
    # ,
    #
    # W
    # o
    # r
    # l
    # d
    # !


def add_b(a, b):
    """
        function: pass-a-"immutable"-object
        in the function scope, a refers to int object 15
        in the outer scope, a refers to 10
    """
    a = a + b
    return a

    ## Output
    # 10
    # 15
    # 10


def foo(bar):
    """
        function: pass-a-mutable-object
    """
    bar.append(42)
    print(bar)

    ## Output
    # []
    # [42]
    # [42]


def import_package():
    import numpy as np
    print(np.pi)

    ## Output
    # 3.141592653589793

    # Notes
    # np.pi returns the pi constant


def io_write_read_1dlist_txt():
    """
        Text File I/O
        write and read 1 dimension list to text file
    """
    a = [1, 2, 3, 4, 5]
    with open('1d.txt', 'w') as f:
        for item in a:
            f.write(f'{item}\t')

    with open('1d.txt', 'r') as f:
        line = f.readline()
        b = line.strip().split('\t')
        b = [int(item) for item in b]
    print(b)

    ## Output
    # [1, 2, 3, 4, 5]

    ## Notes
    # with statement
    # a convenient method for indicating a particular operation has some cleanup associated with it,
    # and to guarantee that cleanup happens, no matter what

    # list comprehension
    # List comprehensions provide a concise way to create lists.


def io_write_read_2dlist_txt():
    """
        Text File I/O
        write and read 2 dimension list to text file
    """
    a_2d = [["ab", "cd", "ef", "gh", "ij"]] * 3
    with open('2d.txt', 'w') as f:
        for a in a_2d:
            for item in a:
                f.write(f'{item}\t')
            f.write('\n')

    b_2d = []
    with open('2d.txt', 'r') as f:
        for line in f:
            b = line.strip().split('\t')
            b_2d.append(b)
    print(b_2d)

    ## Output
    # [['ab', 'cd', 'ef', 'gh', 'ij'], ['ab', 'cd', 'ef', 'gh', 'ij'], ['ab', 'cd', 'ef', 'gh', 'ij']]

    ## Notes
    # strip([chars])
    # Returns a copy of the string with the leading and trailing characters removed.
    # If [chars] omitted or None, the chars argument defaults to removing whitespace.

    # split([str])
    # returns a list of all the words in the string, using [str] as the separator


class Shape(object):
    def __init__(self, a=0, b=0):
        print("Object is being created")
        self.width = a
        self.height = b

    def area(self):
        print(f"Shape area: width is {self.width}, height is {self.height}")

    ## Output
    # Object is being created
    # Shape area: width is 0, height is 0


class Rectangle(Shape):
    def __init__(self, a=0, b=0):
        super().__init__(a, b)

    def area(self):
        print(f"Rectangle area: {self.width * self.height}")

    def give_me_rec(self, x):
        print(f"give me {x} rectangle")
        print(f"Area: {x} * {self.width * self.height} = {x*self.width * self.height}")


    ## Output - class: inheritance
    # Object is being created
    # Rectangle area: 12

    ## Output - class: function overloading
    # Object is being created
    # give me 3 rectangle
    # Area: 3 * 1 = 3
    # give me 3.5 rectangle
    # Area: 3.5 * 1 = 3.5


class Triangle(Shape):
    def __init__(self, a=0, b=0):
        super().__init__(a, b)

    def area(self):
        print(f"Triangle area: {0.5 * self.width * self.height}")

    ## Output - class: polymorphism
    # Object is being created
    # Object is being created
    # Rectangle area: 12
    # Triangle area: 25.0


# TODO:
#   1. after calling `print()` it automatically goes to a newline
#   2. print double quote and single quote at the same time
#   3. list comprehension
#   4. map
#   5. reduce
#   6. [5] * 3
#   7. various ways to traverse over container: for, zip, range, ...
#   8. try-except
#   9. tuple, set


# run the module directly, the code in the if-block will be executed
# import the module in another file, the code in the if-block will not be executed
# Use: put your test code in the if-block / main program
if __name__ == '__main__':

    # syntax: variable assignment
    syntax_var_assign()

    # syntax: print
    syntax_print()

    # syntax: for-loop
    syntax_for()

    # syntax: for-loop & continue
    syntax_for_continue()

    # syntax: for-loop & break
    syntax_for_break()

    # syntax: while-loop
    syntax_while()

    # syntax: while-loop & continue
    syntax_while_continue()

    # syntax: while-loop & break
    syntax_while_break()

    # syntax: if-else
    syntax_if_else()

    # syntax: if-elif-else
    syntax_if_elif_else()

    # syntax: logical operators
    syntax_logical_op(1, 0)

    # data structure: list
    ds_list()
    ds_list_extend()
    ds_list_index()
    ds_list_count()
    ds_list_sort()

    # data structure: dict
    ds_dict()
    ds_dict_keys_values_items()
    ds_dict_sort_by_key()

    # string manipulation
    str_concatenate()
    str_find_substr()
    str_substr()
    str_num_format()
    iter_py()

    # function: pass-a-"immutable"-object
    a = 10
    b = 5
    print(a)
    print(add_b(a, b))
    print(a)

    # function: pass-a-mutable-object
    answer_list = []
    print(answer_list)
    foo(answer_list)
    print(answer_list)

    # write and read text file
    io_write_read_1dlist_txt()
    io_write_read_2dlist_txt()

    # import package
    import_package()

    # class: declaration & constructor
    ape = Shape(0, 0)
    ape.area()

    # class: inheritance
    rec = Rectangle(3, 4)
    rec.area()

    # class: function overloading
    rec = Rectangle(1, 1)
    rec.give_me_rec(3)
    rec.give_me_rec(3.5)

    # class: polymorphism
    shapes = [Rectangle(3, 4), Triangle(10, 5)]
    for shape in shapes:
        shape.area()
