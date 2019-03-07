#Ratios
'''
Ratios are all around us. Whether it's miles per gallon or click through rate, they are everywhere. In this exercise, we'll create some ratios by dividing out pairs of columns.

Instructions
100 XP
Create a new variable ASSESSED_TO_LIST by dividing ASSESSEDVALUATION by LISTPRICE to help us understand if the having a high or low assessment value impacts our price.
Create another new variable TAX_TO_LIST to help us understand the approximate tax rate by dividing TAXES by LISTPRICE.
Lastly create another variable BED_TO_BATHS to help us know how crowded our bathrooms might be by dividing BEDROOMS by BATHSTOTAL.
'''

# Code

# ASSESSED_TO_LIST
df = df.withColumn('ASSESSED_TO_LIST',df['ASSESSEDVALUATION'] / df['LISTPRICE'])
df[['ASSESSEDVALUATION', 'LISTPRICE', 'ASSESSED_TO_LIST']].show(5)
# TAX_TO_LIST
df = df.withColumn('TAX_TO_LIST', df['TAXES'] / df['LISTPRICE'])
df[['TAX_TO_LIST', 'TAXES', 'LISTPRICE']].show(5)
# BED_TO_BATHS
df = df.withColumn('BED_TO_BATHS', df['BEDROOMS'] / df['BATHSTOTAL'])
df[['BED_TO_BATHS', 'BEDROOMS', 'BATHSTOTAL']].show(5)

'''result
<script.py> output:
    +-----------------+---------+----------------+
    |ASSESSEDVALUATION|LISTPRICE|ASSESSED_TO_LIST|
    +-----------------+---------+----------------+
    |              0.0|   139900|             0.0|
    |              0.0|   210000|             0.0|
    |              0.0|   225000|             0.0|
    |              0.0|   230000|             0.0|
    |              0.0|   239900|             0.0|
    +-----------------+---------+----------------+
    only showing top 5 rows
    
    +--------------------+-----+---------+
    |         TAX_TO_LIST|TAXES|LISTPRICE|
    +--------------------+-----+---------+
    |0.013280914939242315| 1858|   139900|
    | 0.00780952380952381| 1640|   210000|
    |0.010622222222222222| 2390|   225000|
    |0.009330434782608695| 2146|   230000|
    |0.008378491037932471| 2010|   239900|
    +--------------------+-----+---------+
    only showing top 5 rows
    
    +------------------+--------+----------+
    |      BED_TO_BATHS|BEDROOMS|BATHSTOTAL|
    +------------------+--------+----------+
    |               1.5|       3|         2|
    |1.3333333333333333|       4|         3|
    |               2.0|       2|         1|
    |               1.0|       2|         2|
    |               1.5|       3|         2|
    +------------------+--------+----------+
    only showing top 5 rows

 we've created some great ratios to use in our model that 
 people looking at homes might be considering! Often times 
 rather than just hoping that features will be important and 
 trying them all brute force its more worthwhile to talk to 
 someone that knows the context to get ideas!
note:
'''