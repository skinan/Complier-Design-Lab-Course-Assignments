
def is_keyword(word):
    keyword_list = set()
    try:
        with open("/home/inan/PycharmProjects/Compiler Lab 2/kewords_list.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                keyword_list.add(line.strip("\n"))
    except FileNotFoundError:
        print("File Not Found!")
    if word in keyword_list:
        return True
    else:
        return False


if __name__ == '__main__':
    print("This is a module")
