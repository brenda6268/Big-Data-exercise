#Bucketing
'''
If you are a homeowner its very important if a house has 1, 2, 3 or 4 bedrooms. But like bathrooms, once you hit a certain point you don't really care whether the house has 7 or 8. This example we'll look at how to figure out where are some good value points to bucket.

Instructions
100 XP

Plot a distribution plot of the pandas dataframe sample_df using Seaborn distplot().
Given it looks like there is a long tail of infrequent values after 5, create the bucket splits of 1, 2, 3, 4, 5+
Create the transformer buck by instantiating Bucketizer() with the splits for setting the buckets, then set the input column as BEDROOMS and output column as bedrooms.
Apply the Bucketizer transformation on df using transform() and verify the results with show()
'''

# Code
from pyspark.ml.feature import Bucketizer

# Plot distribution of sample_df
sns.distplot(sample_df, axlabel='BEDROOMS')
plt.show()

# Create the bucket splits and bucketizer
splits = [0,1, 2, 3, 4, 5, float('Inf')]  #I lost 0 at first try
buck = Bucketizer(splits=splits, inputCol='BEDROOMS', outputCol='bedrooms')

# Apply the transformation to df
df = buck.transform(df)

# Display results
df[['BEDROOMS', 'bedrooms']].show()

'''result
<script.py> output:
    +--------+--------+
    |BEDROOMS|bedrooms|
    +--------+--------+
    |     3.0|     3.0|
    |     4.0|     4.0|
    |     2.0|     2.0|
    |     2.0|     2.0|
    |     3.0|     3.0|
    |     3.0|     3.0|
    |     3.0|     3.0|
    |     3.0|     3.0|
    |     3.0|     3.0|
    |     3.0|     3.0|
    |     3.0|     3.0|
    |     3.0|     3.0|
    |     3.0|     3.0|
    |     3.0|     3.0|
    |     2.0|     2.0|
    |     3.0|     3.0|
    |     3.0|     3.0|
    |     3.0|     3.0|
    |     3.0|     3.0|
    |     3.0|     3.0|
    +--------+--------+
    only showing top 20 rows

'''