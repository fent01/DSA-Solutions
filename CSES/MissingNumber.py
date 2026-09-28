inputed = sys.stdin.read
main = inputed.split()

if not main:
    print("empty D:")

n = int(main[0])
sum_acc = sum(map(int, main[1:]))
sum_exp = n* (n+1)//2
print(sum_exp - sum_acc)

        
        
    
    