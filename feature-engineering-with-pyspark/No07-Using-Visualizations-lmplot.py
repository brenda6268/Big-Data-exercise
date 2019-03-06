#Using Visualizations: lmplot
'''
Creating linear model plots helps us visualize if variables have relationships with the dependent variable. If they do they are good candidates to include in our analysis. If they don't it doesn't mean that we should throw them out, it means we may have to process or wrangle them before they can be used.

seaborn is available in your workspace with the customary alias sns.

Instructions
100 XP

Using the loaded data set df filter it down to the columns 'SALESCLOSEPRICE' and 'LIVINGAREA' with select().
Sample 50% of the dataframe with sample() making sure to not use replacement and setting the random seed to 42.
Convert the Spark DataFrame to a pandas.DataFrame() with toPandas().
Using 'SALESCLOSEPRICE' as your dependent variable and 'LIVINGAREA' as your independent, plot a linear model plot using seaborn lmplot().
'''

# Code
# Select a the relevant columns and sample
sample_df = df.select(['SALESCLOSEPRICE','LIVINGAREA']).sample(False, 0.5, 42)

# Convert to pandas dataframe
pandas_df = sample_df.toPandas()

# Linear model plot of pandas_df
sns.lmplot(x='LIVINGAREA', y='SALESCLOSEPRICE', data=pandas_df)
plt.show()

