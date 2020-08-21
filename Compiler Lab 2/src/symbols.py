# 36 - 47
# 91 - 96
# 123 -126
# 58 - 63


def is_symbol(word):
    if (36 <= ord(word) <= 47) or (91 <= ord(word) <= 96) or (123 <= ord(word) <= 126) or (58 <= ord(word) <= 63):
        return True
    else:
        return False


if __name__ == '__main__':
    print("It is a module.")