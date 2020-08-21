def main():
    token_list = list(map(str, input().split(" ")))
    symbols = {"+", "-", "*", "/", "="}
    syntax_tree = []
    for index, element in enumerate(token_list):
        if element in symbols:
            syntax_tree.append([token_list[index - 1], token_list[index + 1], element])

    for _ in syntax_tree:
        for v in _:
            print(v, end=" ")
        print()


if __name__ == "__main__":
    main()
