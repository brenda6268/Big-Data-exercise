#Loading CSV into DataFrame
'''
In the previous exercise, you have seen a method of creating DataFrame but generally, loading data from CSV file is the most common method of creating DataFrames. In this exercise, you'll create a PySpark DataFrame from a people.csv file that is already provided to you as a file_path and confirm the created object is a PySpark DataFrame.

Remember, you already have SparkSession spark and file_path variable (which is the path to the people.csv file) available in your workspace.

Instructions
100 XP
Create a DataFrame from file_path variable which is the path to the people.csv file.
Confirm the output as PySpark DataFrame.
'''

# Code
# Create an DataFrame from file_path
people_df = spark.read.csv(file_path, header=True, inferSchema=True)

# Check the type of people_df
print("The type of people_df is", type(people_df))

'''
The type of people_df is <class 'pyspark.sql.dataframe.DataFrame'>
'''