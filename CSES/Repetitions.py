read = input()
h_s = 1
temp = 1
temp_v = " "
for i in read:
   
    if temp_v != i:
        temp = 1 
        temp_v = i
        if temp > h_s:
            h_s = temp
            
    else:
        temp += 1
        if temp > h_s:
            h_s = temp
print(h_s)