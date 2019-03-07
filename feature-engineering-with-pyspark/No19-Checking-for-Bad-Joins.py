#Checking for Bad Joins
'''
Joins can go bad silently if we are careful, meaning they will not error out but instead return mangled data with more or less data than you'd intended. Let's take a look at a couple ways that joining incorrectly can change your data set for the worse.

In this example we will look at what happens if you join two dataframes together when the join keys are not the same precision and compare the record counts between the correct join and the incorrect one.

Instructions
100 XP

Create a join between df_orig, the dataframe before its precision was corrected, and walk_df that matches on longitude and latitude.
Count the number of missing values with where() isNull() on df['walkscore'] and correct_join['walkscore']. You should notice that there are many missing values because our datatypes and precision do not match.
Create a join between df and walk_df that only matches on longitude
Count the number of records with count() bad_df and correct_join. You should notice that there are many more values as we have not constrained our matching correctly.
'''

# Code
# Join on mismatched keys precision 
wrong_prec_cond = [df_orig['longitude'] == walk_df['longitude'], df_orig['latitude'] == walk_df['latitude']]
wrong_prec_df = df_orig.join(walk_df, on=wrong_prec_cond, how='left')

# Compare bad join to the correct one
print(wrong_prec_df.where(wrong_prec_df['walkscore'].isNull()).count())
print(correct_join_df.where(correct_join_df['walkscore'].isNull()).count())

# Create a join on too few keys
few_keys_cond = [df['longitude'] == walk_df['longitude']]
few_keys_df = df.join(walk_df, on=few_keys_cond, how='left')

# Compare bad join to the correct one
print("Record Count of the Too Few Keys Join Example: " + str(few_keys_df.count()))
print("Record Count of the Correct Join Example: " + str(correct_join_df.count()))

'''result
<script.py> output:
    4999
    151
    Record Count of the Too Few Keys Join Example: 6152
    Record Count of the Correct Join Example: 5000
'''