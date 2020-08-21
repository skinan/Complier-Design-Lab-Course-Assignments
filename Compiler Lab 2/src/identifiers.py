
def is_identifier(word):
    if 48 <= ord(word[0]) <= 57:
        return False
    else:
        for char in word:
            char = ord(char)
            if char == 95 or (65 <= char <= 90) or (97 <= char <= 122) or (48 <= char <= 57):
                continue
            else:
                return False

    return True


if __name__ == '__main__':
    print("This is a module.")