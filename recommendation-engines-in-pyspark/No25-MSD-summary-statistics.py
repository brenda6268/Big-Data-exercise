#MSD summary statistics
'''
Let's get familiar with the Million Songs Echo Nest Taste Profile data subset. For purposes of this course, we'll just call it the Million Songs dataset or msd. Let's get the number of users and the number of songs. Let's also see which songs have the most plays from this subset.

Instructions
100 XP
Use the .show() method to see what the data looks like.
Complete the code to count the number of distinct userIds. Select the userId column, call the .distinct() method and subsequently, the .count() method.
Now do the same thing for the songId's. Count the number of distinct songIds. Select the songId column and call the .distinct() method and the .count() method on it.
'''

# Code
# Look at the data
msd.show()

# Count the number of distinct userId's
user_count = msd.select("userId").distinct().count()
print("Number of users: ", user_count)

# Count the number of distinct songId's
song_count = msd.select("songId").distinct().count()
print("Number of songs: ", song_count)

'''result
<script.py> output:
    +------+------+---------+
    |userId|songId|num_plays|
    +------+------+---------+
    |   148|   148|        0|
    |   243|   496|        0|
    |    31|   471|        0|
    |   137|   463|        0|
    |   251|   623|        0|
    |    85|   392|        0|
    |    65|   540|        0|
    |   255|   243|        0|
    |    53|   516|        0|
    |   133|    31|        0|
    |   296|    85|        0|
    |    78|   451|        0|
    |   108|   580|        0|
    |   155|   137|        0|
    |   193|   251|        0|
    |   211|    65|        0|
    |    34|   458|        0|
    |   115|    53|        0|
    |   126|   255|        0|
    |   101|   588|        0|
    +------+------+---------+
    only showing top 20 rows
    
    Number of users:  321
    Number of songs:  729
'''