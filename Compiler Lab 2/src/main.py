from keywords import is_keyword
from identifiers import is_identifier
from symbols import is_symbol


def main():
    user_input = input().strip(" ")
    # print(user_input)
    tokens_list = []
    temp = ""
    for word in user_input:
        if word == " ":
            tokens_list.append(temp)
            temp = ""
        elif is_symbol(word):
            tokens_list.append(temp)
            tokens_list.append(word)
            temp = ""
        else:
            temp += word

    tokens_dict = dict()

    for word in tokens_list:
        if word:
            if is_keyword(word):
                tokens_dict[word] = "Keyword"
            elif is_identifier(word):
                tokens_dict[word] = "Identifier"
            elif len(word) == 1:
                if is_symbol(word):
                    tokens_dict[word] = "Symbol"
            else:
                tokens_dict[word] = "Constant"

    print(tokens_dict)


if __name__ == '__main__':
    main()
