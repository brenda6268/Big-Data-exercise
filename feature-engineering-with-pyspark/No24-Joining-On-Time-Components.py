#Joining On Time Components
'''
Often times you will use date components to join in other sets of information. However, in this example, we need to use data that would have been available to those considering buying a house. This means we will need to use the previous year's reporting data for our analysis.

Instructions
100 XP
Extract the year from LISTDATE using year() and put it into a new column called list_year with withColumn()
Create another new column called report_year by subtracting 1 from the list_year
Create a join condition that matches df['CITY'] with price_df['City'] and df['report_year'] with price_df['year']
Perform a left join between df and price_df
'''

# Code
from pyspark.sql.functions import year

# Create year column
df = df.withColumn('list_year', year('LISTDATE'))

# Adjust year to match
df = df.withColumn('report_year', (df['list_year'] - 1))

# Create join condition
condition = [df['CITY'] == price_df['City'], df['report_year'] == price_df['year']]

# Join the dataframes together
df = df.join(price_df, on=condition, how='left')
# Inspect that new columns are available
df[['MedianHomeValue']].show()

'''result
<script.py> output:
    +---------------+
    |MedianHomeValue|
    +---------------+
    |         401000|
    |         401000|
    |         401000|
    |         401000|
    |         401000|
    |         401000|
    |         401000|
    |         401000|
    |         401000|
    |         401000|
    |         401000|
    |         401000|
    |         401000|
    |         401000|
    |         401000|
    |         401000|
    |         401000|
    |         401000|
    |         401000|
    |         401000|
    +---------------+
    only showing top 20 rows

'''