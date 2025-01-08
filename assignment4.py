def sum_of_even_numbers(n):
    if n < 1:
        return 0  
    total_sum = 0
    for i in range(2, n + 1, 2):  
        total_sum += i
    return total_sum
try:
    n = int(input("Enter a positive integer: "))
    if n <= 0:
        print("Please enter a positive integer greater than 0.")
    else:
        result = sum_of_even_numbers(n)
        print(f"The sum of all even numbers between 1 and {n} is: {result}")
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")
