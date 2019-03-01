#Add Zeros
'''
Many recommendation engines use implicit ratings. In many cases these datasets don't include behavior counts for items that a user has never purchased. In these cases, you'll need to add them and include zeros. The dataframe Z is provided for you. It contains userId's, productId's and num_purchases which is the number of times a user has purchased a specific product.

Instructions
100 XP

Take a look at the dataframe Z using the .show() method.
Extract the distinct userId's and productId's from Z using the .distinct() method. Call the result users and products respectively.
Perform a .crossJoin() on the users and products dataframes. Call the result cj.
"left" join cj to the original ratings dataframe Z on ["userId", "productId"]. Call the .fillna(0) method on the result to fill in the blanks with zeros. Call the result Z_expanded.
'''

# Code
# View the data
Z.show()

# Extract distinct userIds and productIds
users = Z.select("userId").distinct()
products = Z.select("productId").distinct()

# Cross join users and products
cj = users.crossJoin(products)

# Join cj and Z
Z_expanded = cj.join(Z, ["userId", "productId"], "left").fillna(0)

# View Z_expanded
Z_expanded.show()


'''result
<script.py> output:
    +------+---------+-------------+
    |userId|productId|num_purchases|
    +------+---------+-------------+
    |  2112|      777|            1|
    |     7|       44|           23|
    |  1132|      227|            9|
    |   686|     1981|            2|
    |    42|     2390|            5|
    |    13|     1662|           21|
    |  2112|     1492|            8|
    |    22|     1811|           96|
    +------+---------+-------------+
    
    +------+---------+-------------+
    |userId|productId|num_purchases|
    +------+---------+-------------+
    |    22|       44|            0|
    |    22|      777|            0|
    |    22|     1811|           96|
    |    22|      227|            0|
    |    22|     1662|            0|
    |    22|     1492|            0|
    |    22|     2390|            0|
    |    22|     1981|            0|
    |   686|       44|            0|
    |   686|      777|            0|
    |   686|     1811|            0|
    |   686|      227|            0|
    |   686|     1662|            0|
    |   686|     1492|            0|
    |   686|     2390|            0|
    |   686|     1981|            2|
    |    13|       44|            0|
    |    13|      777|            0|
    |    13|     1811|            0|
    |    13|      227|            0|
    +------+---------+-------------+
    only showing top 20 rows

In [1]: Z.show()
+------+---------+-------------+
|userId|productId|num_purchases|
+------+---------+-------------+
|  2112|      777|            1|
|     7|       44|           23|
|  1132|      227|            9|
|   686|     1981|            2|
|    42|     2390|            5|
|    13|     1662|           21|
|  2112|     1492|            8|
|    22|     1811|           96|
+------+---------+-------------+

In [4]: cj.show()
+------+---------+
|userId|productId|
+------+---------+
|    22|       44|
|    22|      777|
|    22|     1811|
|    22|      227|
|    22|     1662|
|    22|     1492|
|    22|     2390|
|    22|     1981|
|   686|       44|
|   686|      777|
|   686|     1811|
|   686|      227|
|   686|     1662|
|   686|     1492|
|   686|     2390|
|   686|     1981|
|    13|       44|
|    13|      777|
|    13|     1811|
|    13|      227|
+------+---------+
only showing top 20 rows

'''