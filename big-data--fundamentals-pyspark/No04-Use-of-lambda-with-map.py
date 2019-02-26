#Use of lambda() with map()
'''
The map() function in Python returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.). The general syntax of map() function is map(fun, iter). We can also use lambda functions with map(). The general syntax of map() function with lambda() is map(lambda <agument>:<expression>, iter). Refer to slide 5 of video 1.7 for general help of map() function with lambda().

In this exercise, you'll be using lambda function inside the map() built-in function to square all numbers in the list.


Print my_list which is available in your environment.
Square each item in my_list using map() and lambda().
Print the result of map function.
'''

#code
# Print my_list in the console
print("Input list is", my_list)

# Square all numbers in my_list
squared_list_lambda = list(map(lambda x: x**2, my_list))

# Print the result of the map function
print("The squared numbers are", squared_list_lambda)

'''result
Input list is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
The squared numbers are [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
'''