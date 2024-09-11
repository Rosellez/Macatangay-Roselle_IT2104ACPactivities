def inverted_half_pyramid(rows):
    for i in range(rows, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

inverted_half_pyramid(5)
