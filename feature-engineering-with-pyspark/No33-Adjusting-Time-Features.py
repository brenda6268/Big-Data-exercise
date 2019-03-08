#Adjusting Time Features
'''
We have mentioned throughout this course some of the dangers of leaking information to your model during training. Data leakage will cause your model to have very optimistic metrics for accuracy but once real data is run through it the results are often very disappointing.

In this exercise, we are going to ensure that DAYSONMARKET only reflects what information we have at the time of predicting the value. I.e., if the house is still on the market, we don't know how many more days it will stay on the market. We need to adjust our test_df to reflect what information we currently have as of 2017-12-10.

NOTE: This example will use the lit() function. This function is used to allow single values where an entire column is expected in a function call.

Instructions
100 XP

Import the following functions from pyspark.sql.functions to use later on: datediff(), to_date(), lit().
Convert the date string '2017-12-10' to a pyspark date by first calling the literal function, lit() on it and then to_date()
Create test_df by filtering OFFMKTDATE greater than or equal to the split_date and LISTDATE less than or equal to the split_date using where().
Replace DAYSONMARKET by calculating a new column called DAYSONMARKET, the new column should be the difference between split_date and LISTDATE use datediff() to perform the date calculation. Inspect the new column and the original using the code provided.
'''

# Code
from pyspark.sql.functions import datediff,to_date,lit

split_date = to_date(lit('2017-12-10'))
# Create Sequential Test set
test_df = df.where(df['OFFMKTDATE'] >= split_date).where(df['LISTDATE'] <= split_date)

# Create a copy of DAYSONMARKET to review later
test_df = test_df.withColumn('DAYSONMARKET_Original', test_df['DAYSONMARKET'])

# Recalculate DAYSONMARKET from what we know on our split date
test_df = test_df.withColumn('DAYSONMARKET', datediff(split_date, 'LISTDATE'))

# Review the difference
test_df[['LISTDATE', 'OFFMKTDATE', 'DAYSONMARKET_Original', 'DAYSONMARKET']].show()

'''result

<script.py> output:
    +-------------------+-------------------+---------------------+------------+
    |           LISTDATE|         OFFMKTDATE|DAYSONMARKET_Original|DAYSONMARKET|
    +-------------------+-------------------+---------------------+------------+
    |2017-10-06 00:00:00|2018-01-24 00:00:00|                  110|          65|
    |2017-09-18 00:00:00|2017-12-12 00:00:00|                   82|          83|
    |2017-11-07 00:00:00|2017-12-12 00:00:00|                   35|          33|
    |2017-10-30 00:00:00|2017-12-11 00:00:00|                   42|          41|
    |2017-07-14 00:00:00|2017-12-19 00:00:00|                  158|         149|
    |2017-10-25 00:00:00|2017-12-20 00:00:00|                   45|          46|
    |2017-12-07 00:00:00|2017-12-23 00:00:00|                   16|           3|
    |2017-11-22 00:00:00|2017-12-16 00:00:00|                   24|          18|
    |2017-10-27 00:00:00|2017-12-13 00:00:00|                   47|          44|
    |2017-09-29 00:00:00|2017-12-12 00:00:00|                   12|          72|
    |2017-11-28 00:00:00|2017-12-11 00:00:00|                   13|          12|
    |2017-09-09 00:00:00|2018-01-17 00:00:00|                  119|          92|
    |2017-11-18 00:00:00|2017-12-15 00:00:00|                   26|          22|
    |2017-12-07 00:00:00|2017-12-18 00:00:00|                   11|           3|
    |2017-11-25 00:00:00|2018-01-02 00:00:00|                   38|          15|
    |2017-11-09 00:00:00|2018-01-03 00:00:00|                   55|          31|
    |2017-10-18 00:00:00|2017-12-26 00:00:00|                   69|          53|
    |2017-10-03 00:00:00|2017-12-15 00:00:00|                   40|          68|
    |2017-10-16 00:00:00|2017-12-15 00:00:00|                   60|          55|
    |2017-11-18 00:00:00|2017-12-28 00:00:00|                   40|          22|
    +-------------------+-------------------+---------------------+------------+
    only showing top 20 rows

'''