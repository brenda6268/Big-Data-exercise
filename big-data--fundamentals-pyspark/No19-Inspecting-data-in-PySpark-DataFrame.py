#Inspecting data in PySpark DataFrame
'''
Inspecting data is very crucial before performing analysis such as plotting, modeling, training etc., In this simple exercise, you'll inspect the data in the people_df DataFrame that you have created in the previous exercise using basic DataFrame operators.

Remember, you already have SparkSession spark and people_df DataFrame available in your workspace.

Instructions
100 XP
Print the first 10 observations in the people_df DataFrame.
Count the number of rows in the people_df DataFrame.
How many columns does people_df DataFrame have and what are their names?
'''

# Code
# Print the first 10 observations 
people_df.show(10)

# Count the number of rows 
print("There are {} rows in the people_df DataFrame.".format(people_df.count()))

# Count the number of columns and their names
print("There are {} columns in the people_df DataFrame and their names are {}".format(len(people_df.columns), people_df.columns))

'''
+---+---------+----------------+------+-------------+
only showing top 10 rows

There are 100000 rows in the people_df DataFrame.
There are 5 columns in the people_df DataFrame and their names are ['_c0', 'person_id', 'name', 'sex', 'date of birth']
'''