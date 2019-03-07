#Custom Percentage Scaling
'''
In the slides we showed how to scale the data between 0 and 1. Sometimes you may wish to scale things differently for modeling or display purposes.

Instructions
100 XP
Calculate the max and min and put them into variables max_days and min_days, don't forget to use collect() on agg().
Using withColumn() create a new column called 'percentagescaleddays' based on DAYSONMARKET.
percentage_scaled_days should be a column of integers ranging from 0 to 100, use round() to get integers.
Print the max() and min() for the new column percentage_scaled_days.

'''

# Code
# Define max and min values and collect them
max_days = df.agg({'DAYSONMARKET': 'max'}).collect()[0][0]
min_days = df.agg({'DAYSONMARKET': 'min'}).collect()[0][0]

# Create a new column based off the scaled data
df = df.withColumn('percentagescaleddays', 
                  round((df['DAYSONMARKET'] - min_days) / (max_days - min_days)) * 100)

# Calc max and min for new column
print(df.agg({'percentagescaleddays': 'max'}).show())
print(df.agg({'percentagescaleddays': 'min'}).show())

'''result

'''