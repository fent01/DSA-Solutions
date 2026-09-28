inputed = input()
main = inputed.split()
Found = False
value = int(main[0])
while not Found:
    if str(value) in main:
        value = value - 1
    else:
        print(value)
        Found = True
        
        
    
    