#PySpark DataFrame subsetting and cleaning
'''
After data inspection, it is often necessary to clean the data which mainly involves subsetting, renaming the columns, removing duplicated rows etc., PySpark DataFrame API provides several operators to do this. In this exercise, your job is to subset 'name', 'sex' and 'date of birth' columns from people_df DataFrame, remove any duplicate rows from that dataset and count the number of rows before and after duplicates removal step.

Remember, you already have SparkSession spark and people_df DataFrames available in your workspace.

Instructions
100 XP

Select 'name', 'sex' and 'date of birth' columns from people_df and create people_df_sub DataFrame.
Print the first 10 observations in the people_df DataFrame.
Remove duplicate entries from people_df_sub DataFrame and create peopledfsub_nodup DataFrame.
How many rows are there before and after duplicates are removed?
'''

# Code
# Select name, sex and date of birth columns
people_df_sub = people_df.select('name',  'sex' ,'date of birth')

# Print the first 10 observations from people_df_sub
people_df_sub.show(10)

# Remove duplicate entries from people_df_sub
people_df_sub_nodup = people_df_sub.dropDuplicates()

# Count the number of rows
print("There were {} rows before removing duplicates, and {} rows after removing duplicates".format(people_df_sub.count(), people_df_sub_nodup.count()))

'''
<script.py> output:
    +----------------+------+-------------+
    |            name|   sex|date of birth|
    +----------------+------+-------------+
    |  Penelope Lewis|female|   1990-08-31|
    |   David Anthony|  male|   1971-10-14|
    |       Ida Shipp|female|   1962-05-24|
    |    Joanna Moore|female|   2017-03-10|
    |  Lisandra Ortiz|female|   2020-08-05|
    |   David Simmons|  male|   1999-12-30|
    |   Edward Hudson|  male|   1983-05-09|
    |    Albert Jones|  male|   1990-09-13|
    |Leonard Cavender|  male|   1958-08-08|
    |  Everett Vadala|  male|   2005-05-24|
    +----------------+------+-------------+
    only showing top 10 rows
    
    There were 100000 rows before removing duplicates, and 99998 rows after removing duplicates
'''