read = open("cowsignal.in","r")
write = open("cowsignal.out","w")
M,N,K = map(int,read.readline().split())

for _ in range(M):
    sig = ""
    line = read.readline().strip()
    for char in line:
        sig = sig + (char * K)

    for multi in range(K):
        write.write(sig+"\n")



