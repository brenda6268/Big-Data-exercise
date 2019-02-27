#PySpark DataFrame visualization
'''
Graphical representations or visualization of data is imperative for understanding as well as interpreting the data. In this simple data visualization exercise, you'll first print the column names of names_df DataFrame that you created earlier, then convert the names_df to Pandas DataFrame and finally plot the contents as horizontal bar plot with names of the people on the x-axis and their age on the y-axis.

Remember, you already have SparkSession spark and names_df DataFrame available in your workspace.

Instructions
100 XP
Print the names of the columns in names_df DataFrame.
Convert names_df DataFrame to df_pandas Pandas DataFrame.
Use matplotlib's plot() method to create a horizontal bar plot with 'Name' on x-axis and 'Age' on y-axis.
'''

# Code
# Check the column names of names_df
print("The column names of names_df are", names_df.columns)

# Convert to Pandas DataFrame  
df_pandas = names_df.toPandas()

# Create a horizontal bar plot
df_pandas.plot(kind='barh', x='Name', y='Age', colormap='winter_r')
plt.show()

'''
The column names of names_df are ['Name', 'Age']
'''