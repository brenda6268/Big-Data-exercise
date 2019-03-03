#Verifying Data Load
'''
Let's suppose each month you get a new file. You know to expect a certain number of records and columns. In this exercise we will create a function that will validate the file loaded.

Instructions
100 XP
Create a data validation function check_load() with parameters df a dataframe, num_records as the number of records and num_columns the number of columns.
Using num_records create a check to see if the input dataframe df has the same amount with count().
Compare input number of columns the input dataframe has withnum_columns by using len() on columns.
If both of these return True, then print Validation Passed
'''

# Code
def check_load(df, num_records, num_columns):
  # Takes a dataframe and compares record and column counts to input
  # Message to return if the critera below aren't met
  message = 'Validation Failed'
  # Check number of records
  if num_records == df.count():
    # Check number of columns
    if num_columns == len(df.columns):
      # Success message
      message = 'Validation Passed'
  return message

# Print the data validation message
print(check_load(df, 5000, 74))

'''result
Validation Passed
'''