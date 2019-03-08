#Dropping Columns with Low Observations
'''
After doing a lot of feature engineering it's a good idea to take a step back and look at what you've created. If you've used some automation techniques on your categorical features like exploding or OneHot Encoding you may find that you now have hundreds of new binary features. While the subject of feature selection is material for a whole other course but there are some quick steps you can take to reduce the dimensionality of your data set.

In this exercise, we are going to remove columns that have less than 30 observations. 30 is a common minimum number of observations for statistical significance. Any less than that and the relationships cause overfitting because of a sheer coincidence!

NOTE: The data is available in the dataframe, df.

Instructions
100 XP

Using the provided for loop that iterates through the list of binary columns, calculate the sum of the values in the column using the agg function. Use collect() to run the calculation immediately and save the results to obs_count.
Compare obs_count to obs_threshold, the if statement should be true if obs_count is less than or equal to obs_threshold.
Remove columns that have been appended to cols_to_remove list by using drop(). Recall that the * allows the list to be unpacked.
Print the starting and ending shape of the PySpark dataframes by using count() for number of records and len() on df.columns or new_df.columns to find the number of columns.
'''

# Code
obs_threshold = 30
cols_to_remove = list()
# Inspect first 10 binary columns in list
for col in binary_cols[0:10]:
  # Count the number of 1 values in the binary column
  obs_count = df.agg({col: 'sum'}).collect()[0][0]
  # If less than our observation threshold, remove
  if obs_count <= obs_threshold:
    cols_to_remove.append(col)
    
# Drop columns and print starting and ending dataframe shapes
new_df = df.drop(*cols_to_remove)

print('Rows: ' + str(df.count()) + ' Columns: ' + str(len(df.columns)))
print('Rows: ' + str(new_df.count()) + ' Columns: ' + str(len(new_df.columns)))

'''result
<script.py> output:
    Rows: 5000 Columns: 253
    Rows: 5000 Columns: 250

    note: Removing low observation features is 
    helpful in many ways. It can improve processing
     speed of model training, prevent overfitting by 
     coincidence and help interpretability by reducing
      the number of things to consider.
'''