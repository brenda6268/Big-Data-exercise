#SQL queries for filtering Table
'''
In the previous exercise, you have run a simple SQL query on a DataFrame. There are more sophisticated queries you can construct to obtain the result that you want and use it for downstream analysis such as data visualization and Machine Learning. In this exercise, we will use the temporary table people that you created previously and filter out the rows where the "sex" is male and female and create two DataFrames.

Remember, you already have SparkSession spark and people temporary table available in your workspace.

Instructions
100 XP

Filter the people table to select all rows where sex is female into people_female_df DataFrame.
Filter the people table to select all rows where sex is male into people_male_df DataFrame.
Count the number of rows in both people_female and people_male DataFrames.
'''

# Code
# Filter the people table to select female sex 
people_female_df = spark.sql('SELECT * FROM people WHERE sex=="female"')

# Filter the people table DataFrame to select male sex
people_male_df = spark.sql('SELECT * FROM people WHERE sex=="male"')

# Count the number of rows in both DataFrames
print("There are {} rows in the people_female_df and {} rows in the people_male_df DataFrames".format(people_female_df.count(), people_male_df.count()))


'''
There are 49014 rows in the people_female_df and 49066 rows in the people_male_df DataFrames
'''
