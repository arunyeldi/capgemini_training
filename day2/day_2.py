# # def display(data):
# #     print(f"The area is {data}")

# # def get_input():
# #     length = int(input("Length: "))
# #     width = int(input("Width: "))

# #     return (length, width)

# # #calculatiing the area of rectangle
# # def calculate_area(length, width):
# #     return length * width

# # def main():
# #     (len, wid) = get_input()
# #     area = calculate_area(len, wid)
# #     display(area)

# # main()


# #Average of four numbers

# # def get_input_sum(n):
# #     sum = 0
# #     for i in range(n):
# #         sum += int(input(f"Enther the number {i + 1}: "))
# #     return sum

# # def calculate_avg(input_sum, n):
# #     return (input_sum) / n

# # def display(avg, n):
# #     print(f"Avg of {n} numbers is: {avg}")

# # def main():
# #     print(f"Program to calculate the avg of given numbers")
# #     print("Enter the number: ", end = "")
# #     n = int(input())
# #     input_sum = get_input_sum(n)
# #     avg = calculate_avg(input_sum, n)
# #     display(avg, n)

# # main()

# #Greatest among three numbers

# # def display(result, ans):
# #     print(f"The greatest among given three numbers is: {result}-{ans}")

# # def get_greatest(a, b, c):
# #     ans = 0
# #     if a > b and a > c:
# #         ans = a
# #         largegst_number = 'a'
# #     elif b > c:
# #         ans = b
# #         largegst_number = 'b'
# #     else:
# #         ans = c
# #         largegst_number = 'c'
# #     return largegst_number, ans
    
# # def get_input():
# #     a = int(input("Enter the value of a: "))
# #     b = int(input("Enter the value of b: "))
# #     c = int(input("Enter the value of c: "))
# #     return (a, b, c)

# # def main():
# #     print("Program to find the largest among the given three numbers")
# #     (a, b, c) = get_input()
# #     (result, ans) = get_greatest(a, b, c)
# #     display(result, ans)

# # main()


# # dis assembler
# # multiplication of two numbers
# # import dis
# # a = 0
# # def add():
# #     for i in range(3):
# #         a += i
# # dis.dis(add)

# import math
# def check_prime(n):
#     # flag = True
#     # for i in range(2, int(math.sqrt(n) + 1)):
#     #     if n % i == 0:
#     #         flag = False
#     #         break
#     # return flag

#     i = 2
#     flag = True
#     while(i < math.sqrt(n) + 1):
#         if n % i == 0:
#             flag = False
#             break
#         i = i + 1
#     return flag

#     #sieve algorithm
#     # arr = [True for i in range(n + 1)]
#     # arr[0] = False
#     # arr[1] = False
#     # k = 2
#     # while(k * k <= n):
#     #     if(arr[k] == True):
#     #         for i in range(k * k, n + 1, k):
#     #             arr[i] = False
#     #     k += 1
#     # for i in range(n + 1):
#     #     if(arr[i]):
#     #         print(i)
        

# def main():
#     for i in range(1, 100):
#         if(check_prime(i)):
#             print(f"The number {i} is a prime number")
#         else:
#             print(f"The number {i} is not a prime number")
# main()