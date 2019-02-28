#Correct format and distinct users
'''
Take a look at the R dataframe. Notice that it is in conventional or "wide" format with a different movie in each column. Also notice that the User's and movie names are not in integer format. Follow the steps to properly prepare this data for ALS.

Instructions
100 XP
Instructions
100 XP
Import the monotonically_increasing_id package from pyspark.sql.functions and view the R dataframe using the .show() method.
Use the to_long() function to convert the R dataframe into a "long" data frame. Call the new dataframe ratings.
Create a dataframe called users that contains all the .distinct() users from the dataframe and repartition the dataframe into one partition using the .coalesce(1) method.
Use the monotonically_increasing_id() method to create a new column in the users dataframe that contains a unique integer for each user. Call this column userId. Be sure to call the .persist() method on the final dataframe to ensure the new integer id's persist.
'''

# Code
from pyspark.sql.functions import monotonically_increasing_id
R.show()

# Use the to_long() function to convert the dataframe to the "long" format.
ratings = to_long(R)
ratings.show()

# Get unique users and repartition to 1 partition
users = ratings.select("User").distinct().coalesce(1)

# Create a new column of unique integers called "userId" in the users dataframe.
users = users.withColumn("userId", monotonically_increasing_id()).persist()
users.show()

'''result

+----------------+-----+----+----------+--------+
|            User|Shrek|Coco|Swing Kids|Sneakers|
+----------------+-----+----+----------+--------+
|    James Alking|    3|   4|         4|       3|
|Elvira Marroquin|    4|   5|      null|       2|
|      Jack Bauer| null|   2|         2|       5|
|     Julia James|    5|null|         2|       2|
+----------------+-----+----+----------+--------+

+----------------+----------+------+
|            User|     Movie|Rating|
+----------------+----------+------+
|    James Alking|     Shrek|     3|
|    James Alking|      Coco|     4|
|    James Alking|Swing Kids|     4|
|    James Alking|  Sneakers|     3|
|Elvira Marroquin|     Shrek|     4|
|Elvira Marroquin|      Coco|     5|
|Elvira Marroquin|  Sneakers|     2|
|      Jack Bauer|      Coco|     2|
|      Jack Bauer|Swing Kids|     2|
|      Jack Bauer|  Sneakers|     5|
|     Julia James|     Shrek|     5|
|     Julia James|Swing Kids|     2|
|     Julia James|  Sneakers|     2|
+----------------+----------+------+

+----------------+------+
|            User|userId|
+----------------+------+
|Elvira Marroquin|     0|
|      Jack Bauer|     1|
|    James Alking|     2|
|     Julia James|     3|
+----------------+------+

'''