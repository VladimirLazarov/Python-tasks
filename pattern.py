pattern = "*"

for row in range(1, 10):

    if row <= 5:
        print(pattern * row)

    else:
        print(pattern * (10 - row))

        