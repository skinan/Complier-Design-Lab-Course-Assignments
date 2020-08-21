
def aStarbPlus(word):
    index = 0
    while index < len(word):
        if word[index] == 'a':
            index += 1
        elif word[index] == 'b':
            while index < len(word):
                if word[index] != 'b':
                    return False
                index += 1
            return True
        else:
            return False
    return False


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
