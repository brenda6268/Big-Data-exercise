#The GroupBy and Filter Methods
'''
Now that we know a little more about the dataset, let's look at some general summary metrics of the ratings dataset and see how many ratings the movies have and how many ratings the users have provided. Two common methods that will be helpful to you as you perform summary statistics in Spark are the .filter() and the .groupBy() methods. The .filter() method allows you to filter out any data that doesn't meet your specified criteria.

Instructions
100 XP

Import col from the pyspark.sql.functions, and view the ratings dataset using the .show().
Apply the .filter() method on the ratings dataset with the following filter inside the parenthesis in order to include only userId's less than 100: col("userId") < 100.
Call the .groupBy() method on the ratings dataset to group the data by userId. Call the .count() method to see how many movies each userId has rated.
'''

# Code
# Import the requisite packages
from pyspark.sql.functions import col

# View the ratings dataset
ratings.show()

# Filter out all userIds greater than 100
ratings.filter(col("userId") < 100).show()
#If you want to apply two filters, you can do so like this: ratings.filter((col('userId') < 100) & (col('userId') > 50)).show()

# Group data by userId, count ratings
ratings.groupBy("userId").count().show()


'''result
+------+-------+------+----------+
|userId|movieId|rating| timestamp|
+------+-------+------+----------+
|     1|     31|   2.5|1260759144|
|     1|   1029|   3.0|1260759179|
|     1|   1061|   3.0|1260759182|
|     1|   1129|   2.0|1260759185|
|     1|   1172|   4.0|1260759205|
|     1|   1263|   2.0|1260759151|
|     1|   1287|   2.0|1260759187|
|     1|   1293|   2.0|1260759148|
|     1|   1339|   3.5|1260759125|
|     1|   1343|   2.0|1260759131|
|     1|   1371|   2.5|1260759135|
|     1|   1405|   1.0|1260759203|
|     1|   1953|   4.0|1260759191|
|     1|   2105|   4.0|1260759139|
|     1|   2150|   3.0|1260759194|
|     1|   2193|   2.0|1260759198|
|     1|   2294|   2.0|1260759108|
|     1|   2455|   2.5|1260759113|
|     1|   2968|   1.0|1260759200|
|     1|   3671|   3.0|1260759117|
+------+-------+------+----------+
only showing top 20 rows

+------+-------+------+----------+
|userId|movieId|rating| timestamp|
+------+-------+------+----------+
|     1|     31|   2.5|1260759144|
|     1|   1029|   3.0|1260759179|
|     1|   1061|   3.0|1260759182|
|     1|   1129|   2.0|1260759185|
|     1|   1172|   4.0|1260759205|
|     1|   1263|   2.0|1260759151|
|     1|   1287|   2.0|1260759187|
|     1|   1293|   2.0|1260759148|
|     1|   1339|   3.5|1260759125|
|     1|   1343|   2.0|1260759131|
|     1|   1371|   2.5|1260759135|
|     1|   1405|   1.0|1260759203|
|     1|   1953|   4.0|1260759191|
|     1|   2105|   4.0|1260759139|
|     1|   2150|   3.0|1260759194|
|     1|   2193|   2.0|1260759198|
|     1|   2294|   2.0|1260759108|
|     1|   2455|   2.5|1260759113|
|     1|   2968|   1.0|1260759200|
|     1|   3671|   3.0|1260759117|
+------+-------+------+----------+
only showing top 20 rows

+------+-----+
|userId|count|
+------+-----+
|   296|   20|
|   467|   64|
|   125|  210|
|   451|   52|
|   666|   40|
|     7|   88|
|    51|   31|
|   124|   85|
|   447|   87|
|   591|   30|
|   307|   72|
|   475|  655|
|   574|  342|
|   613|   53|
|   169|  113|
|   205|  206|
|   334|   34|
|   544|  268|
|   577|  279|
|   581|   49|
+------+-----+
only showing top 20 rows


'''