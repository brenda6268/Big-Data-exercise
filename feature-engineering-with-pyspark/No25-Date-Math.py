#Date Math
'''
In this example, we'll look at verifying the frequency of our data. The Mortgage dataset is supposed to have weekly data but let's make sure by lagging the report date and then taking the difference of the dates.

Recall that to create a lagged feature we will need to create a window(). window() allows you to return a value for each record based off some calculation against a group of records, in this case, the previous period's mortgage rate.

Instructions
100 XP

Cast mort_df['DATE'] to date type with to_date()
Create a window with the Window() function and use orderBy() to sort by mort_df[DATE]
Create a new column DATE-1 using withColumn() by lagging the DATE column with lag() and window it using over(w)
Calculate the difference between DATE and DATE-1 using datediff() and name it Days_Between_Report
'''

# Code
from pyspark.sql.functions import lag, datediff, to_date
from pyspark.sql.window import Window

# Cast data type
mort_df = mort_df.withColumn('DATE', to_date('DATE'))

# Create window
w = Window().orderBy(mort_df['DATE'])
# Create lag column
mort_df = mort_df.withColumn('DATE-1', lag('DATE', count=1).over(w))

# Calculate difference between date columns
mort_df = mort_df.withColumn('Days_Between_Report', datediff('DATE', 'DATE-1'))
# Print results
mort_df.select('Days_Between_Report').distinct().show()

'''result
<script.py> output:
    +-------------------+
    |Days_Between_Report|
    +-------------------+
    |               null|
    |                  7|
    |                  6|
    |                  8|
    +-------------------+
'''