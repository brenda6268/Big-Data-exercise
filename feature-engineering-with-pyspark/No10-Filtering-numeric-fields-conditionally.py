#Filtering numeric fields conditionally
'''
Again, understanding the context of your data is extremely important. We want to understand what a normal range of houses sell for. Let's make sure we exclude any outlier homes that have sold for significantly more or less than the average. Here we will calculate the mean and standard deviation and use them to filer the near normal field log_SalesClosePrice.

Instructions
100 XP
Import mean() and stddev() from pyspark.sql.functions.
Use agg() to calculate the mean and standard deviation for 'log_SalesClosePrice' with the imported functions.
Create the upper and lower bounds by taking mean_val +/- 3 times stddev_val.
Create a where() filter for 'log_SalesClosePrice' using both low_bound and hi_bound.
'''
#code
from pyspark.sql.functions import mean, stddev

# Calculate values used for outlier filtering
mean_val = df.agg({'log_SalesClosePrice': 'mean'}).collect()[0][0]
stddev_val = df.agg({'log_SalesClosePrice': 'stddev'}).collect()[0][0]

# Create three standard deviation (μ ± 3σ) lower and upper bounds for data
low_bound = mean_val - (3 * stddev_val)
hi_bound = mean_val + (3 * stddev_val)

# Filter the data to fit between the lower and upper bounds
df = df.where((df['log_SalesClosePrice'] < hi_bound) & (df['log_SalesClosePrice'] > low_bound))

