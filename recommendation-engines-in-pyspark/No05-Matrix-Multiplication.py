#Matrix Multiplication
'''
To understand matrix multiplication more directly, let's do some matrix operations manually.

Instructions
100 XP
Matrices a and b are Pandas dataframes. Use the .head() method on each of them to view them.
Work out the product of these two matrices on your own.
Enter the values of the product of these two matrices into the product array
Use the validation on the last line of code to evaluate your estimate. The .dot() method multiplies two matrices together.
'''

# Code
# Use the .head() method to view the contents of matrices a and b
print("Matrix A: ")
print (a.head())

print("Matrix B: ")
print (b.head())

# Complete the matrix called "product" with the product of matrices a and b.
product = np.array([[10,12], [15,18]])

# Run this validation to see how your estimate performs
product == np.dot(a,b)

'''
<script.py> output:
    Matrix A: 
         0  1
    One  2  2
    Two  3  3
    Matrix B: 
         0  1
    One  1  2
    Two  4  4

'''