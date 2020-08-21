def main():
    productions_list = []
    with open("input", "r") as f:
        lines = f.readlines()
        for l in lines:
            productions_list.append(l.strip("\n"))

    # print(productions_list)

    non_terminals = []

    productions_dict = dict()

    for production in productions_list:
        nt = production.split("=")[0].strip(" ")
        non_terminals.append(nt)
        productions_dict[nt] = (production.split("=")[1].strip(" ")).split("|")

    for key, value in productions_dict.items():
        for index, string in enumerate(value):
            value[index] = string.strip(" ").split(" ")

    find_first = input("FIND FIRST OF: ").strip(" ")
    ans = set()
    check = True
    while check:
        for p in productions_dict[find_first]:
            if p[0] in non_terminals:
                find_first = p[0]
            else:
                ans.add(p[0])
                check = False

    print(ans)


if __name__ == "__main__":
    main()
