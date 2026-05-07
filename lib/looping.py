def happy_new_year():
    """
    Count down from 10 to 1 using a while loop, then print "Happy New Year!"
    """
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")


def square_integers(int_list):
    """
    Return a new list with each integer squared.
    
    Args:
        int_list (list): A list of integers
    
    Returns:
        list: A new list with squared values
    """
    # Using list comprehension (preferred method)
    return [num ** 2 for num in int_list]
    
    # Alternative using a for loop:
    # squared_list = []
    # for num in int_list:
    #     squared_list.append(num ** 2)
    # return squared_list


def fizzbuzz():
    """
    Print numbers from 1 to 100 with FizzBuzz rules:
    - Multiples of 3: print "Fizz"
    - Multiples of 5: print "Buzz"  
    - Multiples of both 3 and 5: print "FizzBuzz"
    - Otherwise: print the number
    """
    for i in range(1, 101):  # range(1, 101) gives numbers 1 through 100
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)