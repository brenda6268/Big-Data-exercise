#Correcting Right Skew Data
'''
In the slides we showed how you might use log transforms to fix positively skewed data (data whose distribution is mostly to the left). To correct negative skew (data mostly to the right) you need to take an extra step called "reflecting" before you can apply the inverse of loglog, written as (1/loglog) to make the data look more like normal a normal distribution. Reflecting data uses the following formula to reflect each value: (xmax+1)–x(xmax+1)–x.

Instructions
100 XP
Use the aggregate function skewness() to verify that 'YEARBUILT' has negative skew.
Use the withColumn() to create a new column 'Reflect_YearBuilt' and reflect the values of 'YEARBUILT'.
Using 'Reflect_YearBuilt' column, create another column 'adj_yearbuilt' by taking 1/log() of the values.
'''

# Code
from pyspark.sql.functions import log

# Compute the skewness
print(df.agg({'YEARBUILT': 'skewness'}).collect())

# Calculate the max year
max_year = df.agg({'YEARBUILT': 'max'}).collect()[0][0]

# Create a new column of reflected data
df = df.withColumn('Reflect_YearBuilt', (max_year + 1) - df['YEARBUILT'])

# Create a new column based reflected data
df = df.withColumn('adj_yearbuilt', 1 / log(df['Reflect_YearBuilt']))

'''result
<script.py> output:
    [Row(skewness(YEARBUILT)=-0.2455425013492729)]

note:Adjusting variables is a complex task.
 What you've seen here are only a few of the ways 
 that you might try to make your data fit a normal distribution.
'''