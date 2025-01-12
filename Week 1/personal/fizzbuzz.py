# program details:
# divisible by 3, print Fizz
# divisible by 5, print Buzz
# divisible by both 3 and 5, FizzBuzz
# if divisible by none, print the number as it is

#solution:
# 1. for number, we use for loop.
# 2. 4 conditional statement for checking divisiblity.

for i in range(1, 100):
    # modulo operator (%) -> remainder
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    