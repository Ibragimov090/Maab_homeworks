#001
import math
number = int(input("Enter the number: "))
num = int(math.sqrt(number)) + 1

if number <= 1:
    print("It is not prime number!")
else:
    is_prime = True  #
    for i in range(2, num):
        if number % i == 0:
            is_prime = False
            break    
    if is_prime:
        print("It is prime!")
    else:
        print("It is not prime!")
#002
k = int(input(": "))
c = 0
while k > 0:
    c += k % 10 
    k = k // 10  
print(c)  
#003
n=10
while 2**k<n:
    print(2**k)
    k+=1
