Solved = False
n = int(input())
while not Solved:
    print(n)
    if n % 2 == 0:
        n = n//2
    elif n == 1:
        Solved = True
    else:
        n = (n * 3)+1
    
