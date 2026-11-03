for i in range(1, 4):
    for j in range(i):
        if i == 3:
            print(chr(98 - j), end="")
        else:
            print(chr(97 + j), end="")
    print()
