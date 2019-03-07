#A Dangerous Join
'''
In this exercise, we will be joining on Latitude and Longitude to bring in another dataset that measures how walk-friendly a neighborhood is. We'll need to be careful to make sure our joining columns are the same data type and ensure we are joining on the same precision (number of digits after the decimal) or our join won't work!

Below you will find that df['latitude'] and df['longitude'] are at a higher precision than walk_df['longitude'] and walk_df['latitude'] we'll need to round them to the same precision so the join will work correctly.

Instructions
100 XP

Convert walk_df['latitude'] and walk_df['longitude'] to type double by using cast('double') on the column and replacing the column in place withColumn().
Round the columns in place with withColumn() and round('latitude', 5) and round('longitude', 5).
Create the join condition of walk_df['latitude'] matching df['latitude'] and walk_df['longitude'] matching df['longitude'].
Join df and walk_df together with join(), using the condition above and the left join type. Save the joined dataframe as join_df.
'''

# Code
# Cast data types
walk_df = walk_df.withColumn('longitude', walk_df['longitude'].cast('double'))
walk_df = walk_df.withColumn('latitude', walk_df['latitude'].cast('double'))

# Round precision
df = df.withColumn('longitude', round('longitude', 5))
df = df.withColumn('latitude', round('latitude', 5))

# Create join condition
condition = [walk_df['latitude'] == df['latitude'], walk_df['longitude'] == df['longitude']]

# Join the dataframes together
join_df = df.join(walk_df, on=condition, how='left')
# Count non-null records from new field
print(join_df.where(~join_df['walkscore'].isNull()).count())

'''result
<script.py> output:
    4849

note:taking steps make sure that your 
join keys are in the same format and precision is important 
if you hope to get the most out of the new data set!
'''