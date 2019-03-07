#Calculate Missing Percents
'''
Automation is the future of data science. Learning to automate some of your data preparation pays dividends. In this exercise, we will automate dropping columns if they are missing data beyond a specific threshold.

Instructions
100 XP
Define a function column_dropper() that takes the parameters df a dataframe and threshold a float between 0 and 1.
Calculate the percentage of values that are missing using where(), isNull() and count()
Check to see if the percentage of missing is higher than the threshold, if so, drop the column using drop()
Run column_dropper() on df with the threshold set to .6
'''

# Code


def column_dropper(df, threshold):
  # Takes a dataframe and threshold for missing values. Returns a dataframe.
  total_records = df.count()
  for col in df.columns:
    # Calculate the percentage of missing values
    missing = df.where(df[col].isNull()).count()
    missing_percent = missing / total_records
    # Drop column if percent of missing is more than threshold
    if missing_percent > threshold:
      df = df.drop(col)
  return df

# Drop columns that are more than 60% missing
df = column_dropper(df, .6)

