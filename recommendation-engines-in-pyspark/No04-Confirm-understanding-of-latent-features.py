#Confirm understanding of latent features
'''
Matrix P is provided here. It's columns represent movies and it's rows represent several latent features. Use your understanding of Spark commands to view matrix P, and see if you can determine what some of the latent features might represent. After examining the matrix, look at the dataframe Pi which contains a rough approximation of what these latent features could represent. See if you weren't far off.

Instructions
100 XP
Examine matrix P using the .show() method
Examine matrix Pi using the .show() method
'''

# Code
# Examine matrix P using the .show() method
P.show()

# Examine matrix Pi using the .show() method
Pi.show()

'''
+--------+------------+--------+---------+------------+------+----------+
|Iron Man|Finding Nemo|Avengers|Toy Story|Forrest Gump|Wall-E|Green Mile|
+--------+------------+--------+---------+------------+------+----------+
|     0.2|         2.4|     0.1|      2.4|           0|   2.5|         0|
|     1.5|         1.4|     1.4|      1.3|         1.8|   1.8|       2.5|
|     2.5|         1.1|     2.4|      0.9|         0.2|   0.9|      0.09|
|     1.9|           2|     1.5|      2.2|         1.2|   0.3|      0.01|
|       0|           0|       0|      2.3|         2.2|     0|       2.5|
+--------+------------+--------+---------+------------+------+----------+

+---------+--------+------------+--------+---------+------------+------+----------+
| Lat Feat|Iron Man|Finding Nemo|Avengers|Toy Story|Forrest Gump|Wall-E|Green Mile|
+---------+--------+------------+--------+---------+------------+------+----------+
| Animated|     0.2|         2.4|     0.1|      2.4|           0|   2.5|         0|
|    Drama|     1.5|         1.4|     1.4|      1.3|         1.8|   1.8|       2.5|
|Superhero|     2.5|         1.1|     2.4|      0.9|         0.2|   0.9|      0.09|
|   Comedy|     1.9|           2|     1.5|      2.2|         1.2|   0.3|      0.01|
|Tom Hanks|       0|           0|       0|      1.8|         2.2|     0|       2.5|
+---------+--------+------------+--------+---------+------------+------+----------+


'''