import math

# function to check whether the given number is a prime or not
def check_prime(n):
    flag = True
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            flag = False
            break
    return flag

    # below is the sieve algorithm llogic (used when the iterations are more than 10 ^ 8)

    # arr = [True for i in range(n + 1)]
    # arr[0] = False
    # arr[1] = False
    # k = 2
    # while(k * k <= n):
    #     if(arr[k] == True):
    #         for i in range(k * k, n + 1, k):
    #             arr[i] = False
    #     k += 1
    # for i in range(n + 1):
    #     if(arr[i]):
    #         print(i)
        
def main():
    input_range = int(input('Enthe the number (specify the range): '))
    prime = 0
    for i in range(2, input_range + 1):
        if(check_prime(i)):
            prime = prime + 1
            if(i == 2):
                print(f"The number {i} is a least prime number")
            else:
                print(f"The number {i} is a prime number")
        else:
            print(f"The number {i} is not a prime number")
    print(f"Number of primes between the given range are: {prime}")


main()