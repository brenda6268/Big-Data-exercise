#Visualizing Missing Data
'''
Being able to plot missing values is a great way to quickly understand how much of your data is missing. It can also help highlight when variables are missing in a pattern something that will need to be handled with care lest your model be biased.

Which variable has the most missing values? Run all lines of code except the last one to determine the answer. Once you're confident, and fill out the value and hit "Submit Answer".

Instructions
100 XP
Use select() to subset the dataframe df with the list of columns columns and Sample with the provided sample() function, and assign this dataframe to the variable sample_df.
Convert the Subset dataframe to a pandas dataframe pandas_df, and use pandas isnull() to convert it DataFrame into True/False. Store this result in tf_df.
Use seaborn's heatmap() to plot tf_df.
Hit "Run Code" to view the plot. Then assign the name of the variable with most missing values to answer.
'''

# Code

# Sample the dataframe and convert to Pandas
sample_df = df.select(columns).sample(False, 0.5, 42)
pandas_df = sample_df.toPandas()

# Convert all values to T/F
tf_df = pandas_df.isnull()

# Plot it
sns.heatmap(data=tf_df)
plt.xticks(rotation=30, fontsize=10)
plt.yticks(rotation=0, fontsize=10)
plt.show()

# Set the answer to the column with the most missing data
answer = '____'

'''result
answer = 'BACKONMARKETDATE'
my note: the white part means missing
'''
