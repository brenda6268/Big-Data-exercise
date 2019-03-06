#Using text filters to remove records
'''
It pays to have to ask your clients lots of questions and take time to understand your variables. You find out that Assumable mortgage is an unusual occurrence in the real estate industry and your client suggests you exclude them. In this exercise we will use isin() which is similar to like() but allows us to pass a list of values to use as a filter rather than a single one.

Instructions
0 XP

Use select() and show() to inspect the distinct values in the column 'ASSUMABLEMORTGAGE' and create the list yes_values for all the values containing the string 'Yes'.
Use ~df['ASSUMABLEMORTGAGE'], isin(), and .isNull() to create a NOT filter to remove records containing corresponding values in the list yes_values and to keep records with null values. Store this filter in the variable text_filter.
Use where() to apply the text_filter to df.
Print out the number of records remaining in df.
'''

# Code
# Inspect unique values in the column 'ASSUMABLEMORTGAGE'
df.select(['ASSUMABLEMORTGAGE']).distinct().show()

# List of possible values containing 'yes'
yes_values = ['Yes w/ Qualifying', 'Yes w/No Qualifying']  #copy this line from solution. still cannot understand why 

# Filter the text values out of df but keep null values
text_filter = ~df['ASSUMABLEMORTGAGE'].isin(yes_values) | df['ASSUMABLEMORTGAGE'].isNull()
df = df.where(text_filter)

# print count of remaining records
print(df.count())

'''result
<script.py> output:
    +------------------+
    | ASSUMABLEMORTGAGE|
    +------------------+
    |Information Coming|
    |              null|
    |     Not Assumable|
    +------------------+
    
    4976

'''