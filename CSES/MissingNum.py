n = int(input())
main = input().split()

given_numbers = list(map(int,main))
expected_sum = n * (n+1) // 2
acc_sum = sum(given_numbers)

print(expected_sum - acc_sum)
        
        
    
    