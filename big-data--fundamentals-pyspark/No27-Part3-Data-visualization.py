#Part 3: Data visualization
'''
Data visualization is important for exploratory data analysis (EDA). PySpark DataFrame is a perfect for data visualization compared to RDDs because of it's inherent structure and schema.

In this third part, you'll create a histogram of the ages of all the players from Germany from the DataFrame that you created in the previous exercise. For this, you'll first convert the PySpark DataFrame into Pandas DataFrame and use matplotlib's plot() function to create a density plot of ages of all players from Germany.

Remember, you already have SparkSession spark, fifa_df_table temporary table and fifa_df_germany_age DataFrame available in your workspace.

Instructions
100 XP
Convert fifa_df_germany_age to fifa_df_germany_age_pandas Pandas DataFrame.
Generate a density plot of the 'Age' column from the fifa_df_germany_age_pandas Pandas DataFrame.
'''

# Code
# Convert fifa_df to fifa_df_germany_age_pandas DataFrame
fifa_df_germany_age_pandas = fifa_df_germany_age.toPandas()

# Plot the 'Age' density of Germany Players
fifa_df_germany_age_pandas.plot(kind='density')
plt.show()

