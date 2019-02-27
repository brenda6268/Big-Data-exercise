#See the power of a recommendation engine
'''
Taylor and Jane both like watching movies. Taylor only likes dramas, comedies and romances. Jane likes only action, adventure and otherwise exciting films. One of the greatest benefits of ALS-based recommendation engines is that they can identify movies or items that users will like, even if they themselves think that they might not like them. Take a look at the movie ratings that Taylor and Jane have provided below. It would stand to reason that their different preferences would generate different recommendations.

Instructions
100 XP
Take a look at TJ_ratings using the .show() method and any other methods you prefer, to see how each of them rated the various movies they've seen.
Input user names into the get_ALS_recs function provided to see what movies ALS recommends for Jane and Taylor based on the ratings provided. Do the ratings make sense to you?
'''

# Code
# View TJ_ratings
TJ_ratings.show()

# Generate recommendations for users
get_ALS_recs(['Jane', 'Taylor']) 

'''
+---------+--------------------+------+
|user_name|          movie_name|rating|
+---------+--------------------+------+
|   Taylor|            Twilight|   4.9|
|   Taylor|  A Walk to Remember|   4.5|
|   Taylor|        The Notebook|   5.0|
|   Taylor|Raiders of the Lo...|   1.2|
|   Taylor|      The Terminator|   1.0|
|   Taylor|      Mrs. Doubtfire|   1.0|
|     Jane|            Iron Man|   4.8|
|     Jane|Raiders of the Lo...|   4.9|
|     Jane|      The Terminator|   4.6|
|     Jane|           Anchorman|   1.2|
|     Jane|        Pretty Woman|   1.0|
|     Jane|           Toy Story|   1.2|
+---------+--------------------+------+

    userId       ...                genres
0   Taylor       ...                 Drama
1   Taylor       ...                 Drama
2   Taylor       ...                Comedy
3   Taylor       ...        Comedy|Romance
4   Taylor       ...        Comedy|Romance
5   Taylor       ...        Comedy|Drama|R
6     Jane       ...              Thriller
7     Jane       ...        Adventure|Fant
8     Jane       ...        Adventure|Fant
9     Jane       ...                Action
10    Jane       ...        Action|Adventu
11    Jane       ...        Action|Drama|W
12    Jane       ...        Action|Sci-Fi|

[13 rows x 4 columns]
'''