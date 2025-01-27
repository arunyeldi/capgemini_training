import math

# function to check whether the given number is a prime or not
def check_prime(n):
    flag = True
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            flag = False
            break
    return flag
        
def main():
    prime_list = []
    input_range = int(input('Enthe the number (specify the range): '))
    for i in range(input_range + 1):
        if(check_prime(i)):
            prime_list.append(i)
    print(f"Smallest prime number in the range(1, {input_range}): {prime_list[0]}")
    print(f"Largest prime number in the range(1, {input_range}): {prime_list[len(prime_list) - 1]}")

main()