def main():
    cond = True
    if cond is True:                 # the code is documentation enougth
        print("cond is true")

    if cond is not False:
        print("cond is not false")
    else:
        print("cond must be false")

    if cond not True and not False:
        print("cond must be None")
    elif cond is True:    # if the first statement is false it tests if this is true
        print("cond is true")
    else:
        print("cond is false")

if __name__ == '__main__':
    main()
