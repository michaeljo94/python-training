def main():
    # Basic variables
    a = 1  # this is a integer (int)
    b = 1.0  # this is a floating point (float)
    c = "one"  # this is a string (str)
    d = True  # this is a boolean (bool)

    print(a)
    print(b)
    print(c)
    print(d)

    del a, b, c, d  # this removes the variables a, b, c amd d

    # Multiple Assignment

    a, b, c = 1, 1.0, "one"

    # Strings (str)

    str = 'Hello World!'

    print(str)  # prints complete string
    print(str[0])  # prints first character of the string
    print(str[2:5])  # prints characters starting from 3rd to 5th
    print(str[2:])  # prints string starting from 3rd character
    print(str * 2)  # prints string two times
    print(str + "test")  # prints concatenated string

    # Lists (list)

    list = ['abcd', 786, 2.23, 'john', 70.2]
    tinylist = [123, 'john']

    print(list)  # Prints complete list
    print(list[0])  # Prints first element of the list
    print(list[1:3])  # Prints elements starting from 2nd till 3rd
    print(list[2:])  # Prints elements starting from 3rd element
    print(tinylist * 2)  # Prints list two times
    print(list + tinylist)  # Prints concatenated lists

    # Tuple (tuple)

    tuple = ('abcd', 786, 2.23, 'john', 70.2)
    tinytuple = (123, 'john')

    print(tuple)  # Prints complete tuple
    print(tuple[0])  # Prints first element of the tuple
    print(tuple[1:3])  # Prints elements starting from 2nd till 3rd
    print(tuple[2:])  # Prints elements starting from 3rd element
    print(tinytuple * 2)  # Prints tuple two times
    print(tuple + tinytuple)  # Prints concatenated tuple

    tuple = ('abcd', 786, 2.23, 'john', 70.2)
    list = ['abcd', 786, 2.23, 'john', 70.2]
    # tuple[2] = 1000    # Invalid syntax with tuple
    list[2] = 1000  # Valid syntax with list

    # Dictionary (dict)
    dictionary = dict()  # explicit
    dictionary = {}  # implicit
    dictionary['one'] = "This is one"
    dictionary[2] = "This is two"

    tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

    print(dictionary['one'])  # Prints value for 'one' key
    print(dictionary[2])  # Prints value for 2 key
    print(tinydict)  # Prints complete dictionary
    print(tinydict.keys())  # Prints all the keys
    print(tinydict.values())  # Prints all the values


if __name__ == '__main__':
    main()
