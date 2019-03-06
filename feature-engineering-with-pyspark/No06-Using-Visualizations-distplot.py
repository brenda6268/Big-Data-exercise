#Using Visualizations: distplot
'''
Understanding the distribution of our dependent variable is very important and can impact the type of model or preprocessing we do. A great way to do this is to plot it, however plotting is not a built in function in PySpark, we will need to take some intermediary steps to make sure it works correctly. In this exercise you will visualize the variable the 'LISTPRICE' variable, and you will gain more insights on its distribution by computing the skewness.

The matplotlib.pyplot and seaborn packages have been imported for you with aliases plt and sns.

Instructions
100 XP

Sample 50% of the dataframe df with sample() making sure to not use replacement and setting the random seed to 42.
Convert the Spark DataFrame to a pandas.DataFrame() with toPandas().
Plot a distribution plot using seaborn's distplot() method.
Import the skewness() function from pyspark.sql.functions and compute it on the aggregate of the 'LISTPRICE' column with the agg() method. Remember to collect() your result to evaluate the computation.
'''

# Code
# Select a single column and sample and convert to pandas
sample_df = df.select(['LISTPRICE']).sample(False, 0.5, 42)
pandas_df = sample_df.toPandas()

# Plot distribution of pandas_df and display plot
sns.distplot(pandas_df)
plt.show()

# Import skewness function
from pyspark.sql.functions import skewness

# Compute and print skewness of LISTPRICE
print(df.agg({'LISTPRICE': 'skewness'}).collect())

'''result
[Row(skewness(LISTPRICE)=2.790448093916559)]

note:checking the distribution visually is a great way to get an idea of 
what steps will need to be taken before applying a model. We can see the 
'ListPrice' is mostly pushed to the left, which means its skewed. We can
 use the skewness function to verify this numerically rather than visually.
'''