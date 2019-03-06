#Using Corr()
'''
The old adage 'Correlation does not imply Causation' is a cautionary tale. However, correlation does give us a good nudge to know where to start looking promising features to use in our models. Use this exercise to get a feel for searching through your data for the first time, trying to find patterns.

A list called columns containing column names has been created for you. In this exercise you will compute the correlation between those columns and 'SALESCLOSEPRICE', and find the maximum.

Instructions
100 XP

Use a for loop iterate through the columns.
In each loop cycle, compute the correlation between the current column and 'SALESCLOSEPRICE' using the corr() method.
Create logic to update the maximum observed correlation and with which column.
Print out the name of the column that has the maximum correlation with 'SALESCLOSEPRICE'.
'''

# Code
# Name and value of col with max corr
corr_max = 0
corr_max_col = columns[0]

# Loop to check all columns contained in list
for col in columns:
    # Check the correlation of a pair of columns
    corr_val = df.corr(col, 'SALESCLOSEPRICE')
    # Logic to compare corr_max with current corr_val
    if corr_val > corr_max:
        # Update the column name and corr value
        corr_max = corr_val
        corr_max_col = col

print(corr_max_col)


'''result
<script.py> output:
    LIVINGAREA
'''