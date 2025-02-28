#Let's print the first n positive integers using recursion
def recursive_method(n):
    if n < 1:
        pass
    else:
        recursive_method(n-1)
        print(n)
print("First 5 positive integers :")
recursive_method(5)

#Now Let's create a recursion function to find the factorial of n numbers
def factorial(n:int):
    assert n>=0 and int(n)==n, 'The number must be positive integers only'
    if n<=1:
        return 1
    else:
        return n * factorial(n-1)
print("Factorial of 3: ",factorial(3))
