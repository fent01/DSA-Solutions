m, n, k = input().split()

for _ in range(int(m)):
    scaled_row = ""
    row = input()
    scaled_row = scaled_row.join(char*int(k) for char in row)

    for i in range(int(k)):
        print(scaled_row)

