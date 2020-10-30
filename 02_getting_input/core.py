
#function main
def main():

    # input(x: str) grabs a string from std:in
    # and returns the entered input.
    name = input("Who are you, dude?\n")

    # concats the string literal with the
    # contents of the name variable above
    print("hi there, " + name)

# ifmain entrypoint
if __name__ == '__main__':
    # calls function main()
    main()
