#Dropping a list of columns
'''
Our data set is rich with a lot of features, but not all are valuable. We have many that are going to be hard to wrangle into anything useful. For now, let's remove any columns that aren't immediately useful by dropping them.

'STREETNUMBERNUMERIC': The postal address number on the home
'FIREPLACES': Number of Fireplaces in the home
'LOTSIZEDIMENSIONS': Free text describing the lot shape
'LISTTYPE': Set list of values of sale type
'ACRES': Numeric area of lot size
Instructions
100 XP
Read the list of column descriptions above and explore their top 30 values with show(), the dataframe is already filtered to the listed columns as df
Create a list of two columns to drop based on their lack of relevance to predicting house prices called cols_to_drop. Recall that computers only interpret numbers explicitly and don't understand context.
Use the drop() function to remove the columns in the list cols_to_drop from the dataframe df.
'''

#Code
# Show top 30 records
df.show(30)

# List of columns to remove from dataset
cols_to_drop = ['STREETNUMBERNUMERIC', 'LOTSIZEDIMENSIONS']

# Drop columns in list
df = df.drop(*cols_to_drop)

'''result
+-------------------+----------+--------------------+---------------+------------------+
|STREETNUMBERNUMERIC|FIREPLACES|   LOTSIZEDIMENSIONS|       LISTTYPE|             ACRES|
+-------------------+----------+--------------------+---------------+------------------+
|              11511|         0|             279X200|Exclusive Right|              1.28|
|              11200|         0|             100x140|Exclusive Right|              0.32|
|               8583|         0|             120x296|Exclusive Right|0.8220000000000001|
|               9350|         1|             208X208|Exclusive Right|              0.94|
|               2915|         1|             116x200|Exclusive Right|               0.0|
|               3604|         1|              50x150|Exclusive Right|             0.172|
|               9957|         0|              common|Exclusive Right|              0.05|
|               9934|         0|              common|Exclusive Right|              0.05|
|               9926|         0|              common|Exclusive Right|              0.05|
|               9928|         0|              common|Exclusive Right|              0.05|
|               9902|         0|              common|Exclusive Right|              0.05|
|               9904|         0|              common|Exclusive Right|              0.05|
|               9894|         0|              common|Exclusive Right|              0.05|
|               9892|         0|              COMMON|Exclusive Right|              0.05|
|               9295|         1|261 x 293 x 287 x...|Exclusive Right|             1.661|
|               9930|         0|               36X32|Exclusive Right|              0.05|
|               9898|         0|               36X32|Exclusive Right|              0.05|
|               9924|         0|              COMMON|Exclusive Right|              0.05|
|               9906|         0|              COMMON|Exclusive Right|              0.05|
|               9938|         0|              COMMON|Exclusive Right|              0.05|
|               9795|         1|               32X60|Exclusive Right|              0.04|
|               9797|         1|               32X60|Exclusive Right|              0.04|
|               8909|         2|             125x150|Exclusive Right|              0.43|
|               3597|         2|             100x250|Exclusive Right|             0.574|
|               8656|         1|     151x158x130x151|Exclusive Right|             0.498|
|               9775|         1|               36X32|Exclusive Right|              0.04|
|               8687|         2|                   -|Exclusive Right|              1.03|
|               8367|         0|             285x305|Exclusive Right|             1.995|
|               2866|         0|           Irregular|Exclusive Right|              0.72|
|               9793|         1|               42x60|Exclusive Right|              0.06|
+-------------------+----------+--------------------+---------------+------------------+
only showing top 30 rows

<script.py> output:
    +----------+---------------+------------------+
    |FIREPLACES|       LISTTYPE|             ACRES|
    +----------+---------------+------------------+
    |         0|Exclusive Right|              1.28|
    |         0|Exclusive Right|              0.32|
    |         0|Exclusive Right|0.8220000000000001|
    |         1|Exclusive Right|              0.94|
    |         1|Exclusive Right|               0.0|
    |         1|Exclusive Right|             0.172|
    |         0|Exclusive Right|              0.05|
    |         0|Exclusive Right|              0.05|
    |         0|Exclusive Right|              0.05|
    |         0|Exclusive Right|              0.05|
    |         0|Exclusive Right|              0.05|
    |         0|Exclusive Right|              0.05|
    |         0|Exclusive Right|              0.05|
    |         0|Exclusive Right|              0.05|
    |         1|Exclusive Right|             1.661|
    |         0|Exclusive Right|              0.05|
    |         0|Exclusive Right|              0.05|
    |         0|Exclusive Right|              0.05|
    |         0|Exclusive Right|              0.05|
    |         0|Exclusive Right|              0.05|
    |         1|Exclusive Right|              0.04|
    |         1|Exclusive Right|              0.04|
    |         2|Exclusive Right|              0.43|
    |         2|Exclusive Right|             0.574|
    |         1|Exclusive Right|             0.498|
    |         1|Exclusive Right|              0.04|
    |         2|Exclusive Right|              1.03|
    |         0|Exclusive Right|             1.995|
    |         0|Exclusive Right|              0.72|
    |         1|Exclusive Right|              0.06|
    +----------+---------------+------------------+
    only showing top 30 rows

'''