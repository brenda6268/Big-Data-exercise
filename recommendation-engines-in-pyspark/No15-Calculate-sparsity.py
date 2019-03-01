#Calculate sparsity
'''
As you know, ALS works well with sparse datasets. Let's see how much of the ratings matrix is actually empty. Remember that sparsity is calculated by the number of cells in a matrix that contain a rating divided by the total number of values that matrix could hold given the number of users and items (movies). In other words, dividing the number of ratings present in the matrix by the product of users and movies in the matrix and subtracting that from 1 will give us the sparsity or the percentage of the ratings matrix that is empty.

Instructions
100 XP

Calculate numerator of the sparsity metric by counting the total number of ratings that are contained in the ratings matrix.
Calculate the number of distinct() userIds and distinct() movieIds in the ratings matrix.
Calculate the denominator of the sparsity metric by multiplying the number of users by the number of movies in the ratings matrix.
Calculate and print the sparsity by dividing the numerator by the denominator, subtracting from 1 and multiplying by 100. The 1.0 is added to ensure the sparsity is returned as a decimal and not an integer.
'''

# Code
# Count the total number of ratings in the dataset
numerator = ratings.select("rating").count()

# Count the number of distinct userIds and distinct movieIds.
num_users = ratings.select("userId").distinct().count()
num_movies = ratings.select("movieId").distinct().count()

# Set the denominator equal to the number of users multiplied by the number of movies
denominator = num_users * num_movies

# Divide the numerator by the denominator
sparsity = (1.0 - (numerator *1.0)/denominator)*100
print ("The ratings dataframe is ", "%.2f" % sparsity + "% empty.")

'''result
The ratings dataframe is  98.36% empty.


'''