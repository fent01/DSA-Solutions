read = open("lowcow.in")
write = open("lowcow.out")

X,Y = map(int,read.readline().split())
step = 1
multi = 1 
count = 0
current_pos = X
while True:
    next_pos = X + (step*multi)
    if min(next_pos,current_pos) <= Y <= max(next_pos,current_pos):
        count += abs(Y - current_pos)
        break
    else:
        count += abs(next_pos - current_pos)
        multi = multi * 2
        step = step * -1
        current_pos = next_pos 
print(count)
