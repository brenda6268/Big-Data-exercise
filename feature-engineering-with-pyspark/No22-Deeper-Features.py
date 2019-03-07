#Deeper Features
'''
In previous exercises we showed how combining two features together can create good additional features for a predictive model. In this exercise, you will generate 'deeper' features by combining the effects of three variables into one. Then you will check to see if deeper and more complicated features always make for better predictors.

Instructions
100 XP

Create a new feature by adding SQFTBELOWGROUND and SQFTABOVEGROUND and creating a new column Total_SQFT
Using Total_SQFT, create yet another feature called BATHS_PER_1000SQFT with BATHSTOTAL. Be sure to scale Total_SQFT to 1000's
Use describe() to inspect the new min, max and mean of our newest feature BATHS_PER_1000SQFT. Notice anything strange?
Create two jointplots()s with Total_SQFT and BATHS_PER_1000SQFT as the xx values and SALESCLOSEPRICE as the yy value to see which has the better R**2 fit. Does this more complicated feature have a stronger relationship with SALESCLOSEPRICE?
'''

# Code
# Create new feature by adding two features together
df = df.withColumn('Total_SQFT', df['SQFTBELOWGROUND'] + df['SQFTABOVEGROUND'])

# Create additional new feature using previously created feature
df = df.withColumn('BATHS_PER_1000SQFT', df['BATHSTOTAL'] / (df['Total_SQFT'] / 1000))
df[['BATHS_PER_1000SQFT']].describe().show()

# Sample and create pandas dataframe
pandas_df = df.sample(False, 0.5, 0).toPandas()

# Linear model plots
sns.jointplot(x='Total_SQFT', y='SALESCLOSEPRICE', data=pandas_df, kind="reg", stat_func=r2)
plt.show()
sns.jointplot(x='BATHS_PER_1000SQFT', y='SALESCLOSEPRICE', data=pandas_df, kind="reg", stat_func=r2)
plt.show()

'''result
<script.py> output:
    +-------+-------------------+
    |summary| BATHS_PER_1000SQFT|
    +-------+-------------------+
    |  count|               5000|
    |   mean| 1.4302617483739894|
    | stddev|  14.12890410245937|
    |    min|0.39123630672926446|
    |    max|             1000.0|
    +-------+-------------------+

note : Using the describe() function you could have seen there was a max of 
1000 bathrooms per 1000sqft, which is almost for sure an issue with our data
 since no sane person would need a bathroom for square foot! If you really 
 wanted to use this feature you'd have to filter that outlier out or overwrite 
 it to NULL with when(). After plotting the jointplots()s you should have seen
  that the less complicated feature Total_SQFT had a much better R**2 of .67 vs BATHS_PER_1000SQFT's .02'. 
  Often simplier is better!
'''