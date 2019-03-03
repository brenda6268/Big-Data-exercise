#What are we predicting?
'''
Which of these fields (or columns) is the value we are trying to predict for?

TAXES
SALESCLOSEPRICE
DAYSONMARKET
LISTPRICE

Instructions
100 XP
From the listed columns above, identify which one we will use as our dependent variable $Y$.
Using the loaded data set df, filter it down to our dependent variable with select(). Store this dataframe in the variable Y_df.
Display summary statistics for the dependent variable using describe() on Y_df and calling show() to display it.
'''

# code
# Select our dependent variable
Y_df = df.select(['SALESCLOSEPRICE'])

# Display summary statistics
Y_df.describe().show()


'''result
<script.py> output:
    +-------+------------------+
    |summary|   SALESCLOSEPRICE|
    +-------+------------------+
    |  count|              5000|
    |   mean|       262804.4668|
    | stddev|140559.82591998563|
    |    min|             48000|
    |    max|           1700000|
    +-------+------------------+
'''