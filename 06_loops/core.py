def main():
    for_loops()
    while_loops()


def for_loops():
    tmp = 0
    tmp_list = ["Hallo", "World"]

    for l in range(0, 2000, 1):
        tmp += l

    # Nested for-loop
    for i in tmp_list:
        for j in i:
            print(j)


def while_loops():
    Jesus_is_alive = False
    you_are_beliver = False

    while not Jesus_is_alive:
        print("Ahmen")
        if you_are_beliver:
            Jesus_is_alive = True
        you_are_beliver = True

if __name__ == '__main__':
    main()
