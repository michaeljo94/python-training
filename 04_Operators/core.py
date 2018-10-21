def main():
    pass


def arithmetic():
    a = 1 + 2           # addion
    b = 1 - 2           # subtraction
    c = a * b           # multipication
    d = c / b           # divison

    mudolus = d % c     # mudolus (divides d by c and reutrns the remainder)
    exp = b**a          # exp(b, a) multiplys b exp to a
    fldiv = a//2        # divides a by 2 and floors it


def comarison():
    if 1 == 1:                                  # ==  -> is eaual to
        print("true is always eaqual to true")
    if 2 != 1:                                  # !=  -> is not equal to
        print("cond is not false")
    if 1 < 2:                                   # <   -> less than
        print("1 is less than 2")
    if 2 > 1:                                   # >   -> more than
        print("2 is more than 1")
    if 2 <= 3:                                  # <=  -> more or eaqual than/to
        print("2 is less or eaqual to 3")
    if 4 >= 3:                                  # >=  -> less or eaqual then/to
        print("4 is more ore equal to 3")


def assignment_operators():
    a += 2          # a = a + 2
    b -= 2          # b = b - 2
    c *= 2          # c = c * 2
    d /= 2          # d = d / 2

    e %= 2          # e / 2 -> e = remainder
    f **= 2         # f = f-exp(2)
    g //= 2         # g = g // 2


if __name__ == '__main__':
    main()
