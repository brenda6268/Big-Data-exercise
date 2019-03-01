#Recommendations From Binary Data
'''
So you see from the ROEM, these models can still generate meaningful test predictions. Let's look at the actual recommendations now. The col function from the pyspark.sql.functions class has been imported for you.

Instructions
100 XP
The dataframe original_ratings is provided for you. It contains the original ratings that users provided. Use the .filter() method to examine user 26's original ratings.
The dataframe binary_recs is also provided. It contains the recommendations for each user. Use the .filter() method to examine userId == 26 recommendations. Do they seem consistent with the recommendations the model provided?
Do the same thing with user 99. Feel free to examine other users.
'''

# Code
# View user 26's original ratings
print ("User 26 Original Ratings:")
original_ratings.filter(col("userId") == 26).show()

# View user 26's recommendations
print ("User 26 Recommendations:")
binary_recs.filter(col("userId") == 26).show()

# View user 99's original ratings
print ("User 99 Original Ratings:")
original_ratings.filter(col("userId") == 99).show()

# View user 99's recommendations
print ("User 99 Recommendations:")
binary_recs.filter(col("userId") == 99).show()

'''result
note:ALS seems to have picked up on the fact that user 26 likes thrillers, crime movies, 
action and adventure, and that user 99 likes dramas and romances.
<script.py> output:
    User 26 Original Ratings:
    +------+-------+------+--------------------+--------------------+
    |userId|movieId|rating|               title|              genres|
    +------+-------+------+--------------------+--------------------+
    |    26|      1|     5|      ToyStory(1995)|Adventure|Animati...|
    |    26|   2542|     5|LockStock&TwoSmok...|Comedy|Crime|Thri...|
    |    26|   2571|     5|     MatrixThe(1999)|Action|Sci-Fi|Thr...|
    |    26|   4011|     5|        Snatch(2000)|Comedy|Crime|Thri...|
    |    26|   6016|     5|CityofGod(Cidaded...|Action|Adventure|...|
    |    26|   8798|     5|    Collateral(2004)|Action|Crime|Dram...|
    |    26|  27831|     5|     LayerCake(2004)|Crime|Drama|Thriller|
    |    26|  44191|     5|  VforVendetta(2006)|Action|Sci-Fi|Thr...|
    |    26|  44195|     5|ThankYouforSmokin...|        Comedy|Drama|
    |    26|  50872|     5|   Ratatouille(2007)|Animation|Childre...|
    |    26|  54286|     5|BourneUltimatumTh...|Action|Crime|Thri...|
    |    26|  58559|     5| DarkKnightThe(2008)|Action|Crime|Dram...|
    |    26|  59369|     5|         Taken(2008)|Action|Crime|Dram...|
    |    26|  59784|     5|   KungFuPanda(2008)|Action|Animation|...|
    |    26|  60684|     5|      Watchmen(2009)|Action|Drama|Myst...|
    |    26|  65514|     5|         IpMan(2008)|    Action|Drama|War|
    |    26|     32|     4|TwelveMonkeys(a.k...|Mystery|Sci-Fi|Th...|
    |    26|     47|     4|Seven(a.k.a.Se7en...|    Mystery|Thriller|
    |    26|     50|     4|UsualSuspectsThe(...|Crime|Mystery|Thr...|
    |    26|     69|     4|        Friday(1995)|              Comedy|
    +------+-------+------+--------------------+--------------------+
    only showing top 20 rows
    
    User 26 Recommendations:
    +------+-------+----------+--------------------+--------------------+
    |userId|movieId|prediction|               title|              genres|
    +------+-------+----------+--------------------+--------------------+
    |    26|  30707| 1.1401137|Million Dollar Ba...|               Drama|
    |    26|    293| 1.1154407|Léon: The Profess...|Action|Crime|Dram...|
    |    26|    111| 1.0985317|  Taxi Driver (1976)|Crime|Drama|Thriller|
    |    26|  81845| 1.0974996|King's Speech, Th...|               Drama|
    |    26|   5971| 1.0956558|My Neighbor Totor...|Animation|Childre...|
    |    26|  70286| 1.0950022|   District 9 (2009)|Mystery|Sci-Fi|Th...|
    |    26|  48394| 1.0917767|Pan's Labyrinth (...|Drama|Fantasy|Thr...|
    |    26|  46578| 1.0879191|Little Miss Sunsh...|Adventure|Comedy|...|
    +------+-------+----------+--------------------+--------------------+
    
    User 99 Original Ratings:
    +------+-------+------+--------------------+--------------------+
    |userId|movieId|rating|               title|              genres|
    +------+-------+------+--------------------+--------------------+
    |    99|    318|     5|ShawshankRedempti...|         Crime|Drama|
    |    99|    356|     5|   ForrestGump(1994)|Comedy|Drama|Roma...|
    |    99|    357|     5|FourWeddingsandaF...|      Comedy|Romance|
    |    99|    509|     5|      PianoThe(1993)|       Drama|Romance|
    |    99|    595|     5|BeautyandtheBeast...|Animation|Childre...|
    |    99|    608|     5|         Fargo(1996)|Comedy|Crime|Dram...|
    |    99|    720|     5|Wallace&Gromit:Th...|Adventure|Animati...|
    |    99|    903|     5|       Vertigo(1958)|Drama|Mystery|Rom...|
    |    99|    912|     5|    Casablanca(1942)|       Drama|Romance|
    |    99|    918|     5|MeetMeinSt.Louis(...|             Musical|
    |    99|    953|     5|It'saWonderfulLif...|Children|Drama|Fa...|
    |    99|    969|     5|AfricanQueenThe(1...|Adventure|Comedy|...|
    |    99|   1028|     5|   MaryPoppins(1964)|Children|Comedy|F...|
    |    99|   1204|     5|LawrenceofArabia(...| Adventure|Drama|War|
    |    99|   1233|     5|BootDas(BoatThe)(...|    Action|Drama|War|
    |    99|   1304|     5|ButchCassidyandth...|      Action|Western|
    |    99|   1617|     5|L.A.Confidential(...|Crime|Film-Noir|M...|
    |    99|   1619|     5|SevenYearsinTibet...| Adventure|Drama|War|
    |    99|   1721|     5|       Titanic(1997)|       Drama|Romance|
    |    99|   2067|     5| DoctorZhivago(1965)|   Drama|Romance|War|
    +------+-------+------+--------------------+--------------------+
    only showing top 20 rows
    
    User 99 Recommendations:
    +------+-------+------------------+--------------------+--------------------+
    |userId|movieId|        prediction|               title|              genres|
    +------+-------+------------------+--------------------+--------------------+
    |    99|   3148|         1.1828514|Cider House Rules...|               Drama|
    |    99|    111|1.1700658000000002|  Taxi Driver (1976)|Crime|Drama|Thriller|
    |    99|    920|         1.1438243|Gone with the Win...|   Drama|Romance|War|
    |    99|    265|         1.1368732|Like Water for Ch...|Drama|Fantasy|Rom...|
    |    99|   1959|         1.1332427|Out of Africa (1985)|       Drama|Romance|
    |    99|   1188|         1.1314342|Strictly Ballroom...|      Comedy|Romance|
    |    99|     34|         1.1144139|         Babe (1995)|      Children|Drama|
    |    99|    910|         1.1108267|Some Like It Hot ...|        Comedy|Crime|
    |    99|    589|          1.096542|Terminator 2: Jud...|       Action|Sci-Fi|
    |    99|   1225|1.0958363000000002|      Amadeus (1984)|               Drama|
    +------+-------+------------------+--------------------+--------------------+
'''