read = open("speeding.in")
write = open("speeding.out","w")
N,M = map(int, read.readline().split())
road = [0 for i in range(100)]
dist = 0 
current_idx = 0
penalty = 0


for _ in range(N):
    distance, speed = map(int,read.readline().split())
    for i in range(distance):
        road[current_idx] = speed
        current_idx += 1

travelled_idx = 0
for _ in range(M):
    travelled, speed_B = map(int,read.readline().split())
    for i in range(travelled):
        temp = speed_B - road[travelled_idx]
        if temp > penalty:
                penalty = temp
        else:
                pass
        travelled_idx += 1

write.write(str(penalty))