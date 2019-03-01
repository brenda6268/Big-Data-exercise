#View Schema
'''
As you know from previous chapters, Spark's implementaiton of ALS requires that movieIds and userIds be provided as integer datatypes. Many datasets need to be prepared accordingly in order for them to function properly with Spark. A common issue is that Spark thinks numbers are strings, and vice versa. Here you'll use the .cast() method to address these types of problems. Let's take a look at the schema of the dataset to ensure it's in the correct format.

Instructions
100 XP

Use the .printSchema() method to check whether the ratings dataset contains the proper data types for ALS to function correctly. Are the userIds and movieIds provided as integer datatypes? Are the ratings in numeric format?
Ensure that the columns of the ratings dataframe are the correct data types. Call the cast method on each column and specify the userID and movieId columns to be of type "integer" and the rating column to be of type "double". (We don't need the timestamp column, so we can leave that out.)
Call the .printSchema() again on the ratings dataframe to confirm that the data types are now correct.
'''


# code
# Use the .printSchema() method to see the datatypes of the ratings dataset.
ratings.printSchema()

# Tell Spark to convert the columns to the proper data types.
ratings = ratings.select(ratings.userId.cast("integer"), ratings.movieId.cast("integer"), ratings.rating.cast("double"))

# Call .printSchema() again to confirm the columns are now in the correct format
ratings.printSchema()

'''result
root
 |-- userId: string (nullable = true)
 |-- movieId: string (nullable = true)
 |-- rating: string (nullable = true)
 |-- timestamp: string (nullable = true)

root
 |-- userId: integer (nullable = true)
 |-- movieId: integer (nullable = true)
 |-- rating: double (nullable = true)
'''