#Write your code below this line 👇

import time

def prime_checker(number):
    primes = [2]
    if number < 0:
        print('Please only provide positive number')
    if number % 2 != 0:
        for num in range(3,number+1,2):
            for prime in primes:
                check = True
                if num % prime == 0:
                    check = False
                    break
            if check:
                primes.append(num)
                if number % num == 0:
                    break
    if number in primes:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
    print(max(primes))

#Write your code above this line 👆
    
#Do NOT change any of the code below👇


n = int(input("Check this number: "))
t0 = time.perf_counter()
prime_checker(number=n)
t1 = time.perf_counter()
print('Time required ',t1 - t0)