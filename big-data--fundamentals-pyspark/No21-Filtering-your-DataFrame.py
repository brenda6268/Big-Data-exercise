#Filtering your DataFrame
'''
In the previous exercise, you have subset the data using select() operator which is mainly used to subset the DataFrame column-wise. What if you want to subset the DataFrame based on a condition (for example, select all rows where the sex is Female). In this exercise, you will filter the rows in the people_df DataFrame in which 'sex' is female and male and create two different datasets. Finally, you'll count the number of rows in each of those datasets.

Remember, you already have SparkSession spark and people_df DataFrame available in your workspace.

Instructions
100 XP
Filter the people_df DataFrame to select all rows where sex is female into people_df_female DataFrame.
Filter the people_df DataFrame to select all rows where sex is male into people_df_male DataFrame.
Count the number of rows in people_df_female and people_df_male DataFrames.
'''

# Code
# Filter people_df to select females 
people_df_female = people_df.filter(people_df.sex == "female")

# Filter people_df to select males
people_df_male = people_df.filter(people_df.sex == "male")

# Count the number of rows 
print("There are {} rows in the people_df_female DataFrame and {} rows in the people_df_male DataFrame".format(people_df_female.count(), people_df_male.count()))

'''
<script.py> output:
    There are 49014 rows in the people_df_female DataFrame and 49066 rows in the people_df_male DataFrame
'''