# While the number is 20 or below this will run infinitly
n = 0
while n <= 20:
    n = n + 1
    if n % 3 == 0:
        if n % 5 == 0:
            print("Fizzbuzz")
        else:
            print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

#---------------------------
#  made by 404Mate with <3  
#--------------------------- 