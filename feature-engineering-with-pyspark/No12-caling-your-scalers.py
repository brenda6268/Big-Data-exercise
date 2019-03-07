#Scaling your scalers
'''
In the previous exercise, we minmax scaled a single variable. Suppose you have a LOT of variables to scale, you don't want hundreds of lines to code for each. Let's expand on the previous exercise and make it a function.

Instructions
100 XP
Define a function called min_max_scaler that takes parameters df a dataframe and cols_to_scale the list of columns to scale.
Use a for loop to iterate through each column in the list and minmax scale them.
Return the dataframe df with the new columns added.
Apply the function min_max_scaler() on df and the list of columns cols_to_scale.\
'''

# Code
def min_max_scaler(df, cols_to_scale):
  # Takes a dataframe and list of columns to minmax scale. Returns a dataframe.
  for col in cols_to_scale:
    # Define min and max values and collect them
    max_days = df.agg({col: 'max'}).collect()[0][0]
    min_days = df.agg({col: 'min'}).collect()[0][0]
    new_column_name = 'scaled_' + col
    # Create a new column based off the scaled data
    df = df.withColumn(new_column_name, 
                      (df[col] - min_days) / (max_days - min_days))
  return df
  
df = min_max_scaler(df, cols_to_scale)
# Show that our data is now between 0 and 1
df[['DAYSONMARKET', 'scaled_DAYSONMARKET']].show()

'''result
<script.py> output:
    +------------+--------------------+
    |DAYSONMARKET| scaled_DAYSONMARKET|
    +------------+--------------------+
    |          10|0.044444444444444446|
    |           4|0.017777777777777778|
    |          28| 0.12444444444444444|
    |          19| 0.08444444444444445|
    |          21| 0.09333333333333334|
    |          17| 0.07555555555555556|
    |          32| 0.14222222222222222|
    |           5|0.022222222222222223|
    |          23| 0.10222222222222223|
    |          73|  0.3244444444444444|
    |          80| 0.35555555555555557|
    |          79|  0.3511111111111111|
    |          12| 0.05333333333333334|
    |           1|0.004444444444444...|
    |          18|                0.08|
    |           2|0.008888888888888889|
    |          12| 0.05333333333333334|
    |          45|                 0.2|
    |          31| 0.13777777777777778|
    |          16| 0.07111111111111111|
    +------------+--------------------+
    only showing top 20 rows

'''