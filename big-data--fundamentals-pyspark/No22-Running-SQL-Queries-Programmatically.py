#Running SQL Queries Programmatically
'''
DataFrames can easily be manipulated using SQL queries in PySpark. The sql() function on a SparkSession enables applications to run SQL queries programmatically and returns the result as another DataFrame. In this exercise, you'll create a temporary table of the people_df DataFrame that you created previously, then construct a query to select the names of the people from the temporary table and assign the result to a new DataFrame.

Remember, you already have SparkSession spark and people_df DataFrame available in your workspace.

Instructions
100 XP
Create a temporary table people that's a pointer to the people_df DataFrame.
Construct a query to select the names of the people.
Assign the result of Spark's query to a new DataFrame - people_df_names.
Print the top 10 names of the people from people_df_names DataFrame.
'''

# Code
# Create a temporary table "people"
people_df.createOrReplaceTempView("people")

# Construct a "query" to select the names of the people
query = '''SELECT name FROM people'''

# Assign the result of Spark's query to people_df_names
people_df_names = spark.sql(query)

# Print the top 10 names of the people
people_df_names.show(10)

'''
+----------------+
|            name|
+----------------+
|  Penelope Lewis|
|   David Anthony|
|       Ida Shipp|
|    Joanna Moore|
|  Lisandra Ortiz|
|   David Simmons|
|   Edward Hudson|
|    Albert Jones|
|Leonard Cavender|
|  Everett Vadala|
+----------------+
only showing top 10 rows

'''