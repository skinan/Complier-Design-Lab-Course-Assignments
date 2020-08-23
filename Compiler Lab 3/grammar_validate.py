def aStarbPlus(word):
    flag = 0
    for w in word:
        if w == "a":
            if flag == 0:
                continue
            else:
                return False
        elif w == "b":
            if flag == 0:
                flag = 1
            else:
                continue
        else:
            return False

    if flag == 0:
        return False
    else:
        return True


def aStar(word):
    for s in word:
        if s != 'a':
            return False
    return True


def main():
    user_input = input("Enter your regex:")
    case1 = aStarbPlus(user_input)
    case2 = aStar(user_input)
    if case1 and case2:
        print("Matching Under Regular Expression: a*b+ AND a*")
    elif case1:
        print("Matching Under Regular Expression: a*b+")
    elif case2:
        print("Matching Under Regular Expression: a*")
    else:
        print("Not matching on given rules")


if __name__ == '__main__':
    main()
