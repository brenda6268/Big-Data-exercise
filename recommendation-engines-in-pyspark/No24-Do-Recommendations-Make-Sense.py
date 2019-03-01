#Do Recommendations Make Sense
'''
Now that we have an understanding of how well our model performed, and can take some confidence that it will provide recommendations that are relevant to users, let's actually look at recommendations made to a user and see if they make sense.

The original ratings data is provided here as original_ratings. Take a look at user 60 and user 63's original ratings, and compare them to what ALS recommended for him/her. In your opinion, are the recommendations consistent with his/her original preferences?

Instructions
100 XP

Use the .filter() on the original_ratings dataframe to ensure that col("userId") equals 60 to look at user 60's original ratings. Call the .sort() method to sort the output by rating and set the ascending argument to False to see the highest ratings first.
Use the .filter() and .show() methods on the recommendations dataset to look at user 60's ratings. Note that when ALS generates recommendations, they are provided in descending order by userId, so there's no need to sort the dataframe.
Do the same thing for user 63.
Do the recommendation genres have some consistency with each user's original ratings?
'''

# Code
# Look at user 60's ratings
print ("User 60's Ratings:")
original_ratings.filter(col("userId") == 60).sort("rating", ascending = False).show()

# Look at the movies recommended to user 60
print ("User 60s Recommendations:")
recommendations.filter(col("userId") == 60).show()

# Look at user 63's ratings
print ("User 63's Ratings:")
original_ratings.filter(col("userId") == 63).sort("rating", ascending = False).show()

# Look at the movies recommended to user 63
print ("User 63's Recommendations:")
recommendations.filter(col("userId") == 63).show()

'''result
User 60's Ratings:
+------+-------+------+--------------------+--------------------+
|userId|movieId|rating|               title|              genres|
+------+-------+------+--------------------+--------------------+
|    60|    858|     5|  GodfatherThe(1972)|         Crime|Drama|
|    60|    235|     5|        EdWood(1994)|        Comedy|Drama|
|    60|   1732|     5|BigLebowskiThe(1998)|        Comedy|Crime|
|    60|   2324|     5|LifeIsBeautiful(L...|Comedy|Drama|Roma...|
|    60|   3949|     5|RequiemforaDream(...|               Drama|
|    60|    541|     5|   BladeRunner(1982)|Action|Sci-Fi|Thr...|
|    60|   5995|     5|    PianistThe(2002)|           Drama|War|
|    60|   6350|     5|Laputa:Castleinth...|Action|Adventure|...|
|    60|   7361|     5|EternalSunshineof...|Drama|Romance|Sci-Fi|
|    60|   8638|     5|  BeforeSunset(2004)|       Drama|Romance|
|    60|   8981|     5|        Closer(2004)|       Drama|Romance|
|    60|  27803|     5|SeaInsideThe(Mara...|               Drama|
|    60|  30749|     5|   HotelRwanda(2004)|           Drama|War|
|    60|   5060|     5|M*A*S*H(a.k.a.MAS...|    Comedy|Drama|War|
|    60|   1221|     5|Godfather:PartIIT...|         Crime|Drama|
|    60|   5690|     5|GraveoftheFirefli...| Animation|Drama|War|
|    60|   1653|     5|       Gattaca(1997)|Drama|Sci-Fi|Thri...|
|    60|     16|   4.5|        Casino(1995)|         Crime|Drama|
|    60|    111|   4.5|    TaxiDriver(1976)|Crime|Drama|Thriller|
|    60|   1080|   4.5|MontyPython'sLife...|              Comedy|
+------+-------+------+--------------------+--------------------+
only showing top 20 rows

User 60s Recommendations:
+------+-------+----------+--------------------+--------------------+
|userId|movieId|prediction|               title|              genres|
+------+-------+----------+--------------------+--------------------+
|    60|  83318|  5.810963|       GoatThe(1921)|              Comedy|
|    60|  83411|  5.810963|          Cops(1922)|              Comedy|
|    60|  73344|  5.315315|ProphetA(UnProphÃ...|         Crime|Drama|
|    60|   3309| 5.2298656|    Dog'sLifeA(1918)|              Comedy|
|    60|   8609| 5.2298656|OurHospitality(1923)|              Comedy|
|    60|  72647| 5.2298656|   Zorn'sLemma(1970)|               Drama|
|    60|   5059| 5.2298656|LittleDieterNeeds...|         Documentary|
|    60|   8797| 5.2298656|      Salesman(1969)|         Documentary|
|    60|  25764| 5.2298656|  CameramanThe(1928)|Comedy|Drama|Romance|
|    60|   7074| 5.2298656|  NavigatorThe(1924)|              Comedy|
|    60|  31547| 5.2298656|LessonsofDarkness...|     Documentary|War|
|    60|   4405| 5.2298656|LastLaughThe(Letz...|               Drama|
|    60|  26400| 5.2298656| GatesofHeaven(1978)|         Documentary|
|    60|  80599| 5.2298656|BusterKeaton:AHar...|         Documentary|
|    60|  92494| 5.1418443|DylanMoran:Monste...|  Comedy|Documentary|
|    60|   3216| 5.1418443|VampyrosLesbos(Va...|Fantasy|Horror|Th...|
|    60|   6918| 5.1184077|UnvanquishedThe(A...|               Drama|
|    60|  40412| 5.0673676|DeadMan'sShoes(2004)|      Crime|Thriller|
|    60|  52767|  5.043912|          21Up(1977)|         Documentary|
|    60|   8955| 5.0317564|      Undertow(2004)|Crime|Drama|Thriller|
+------+-------+----------+--------------------+--------------------+

User 63's Ratings:
+------+-------+------+--------------------+--------------------+
|userId|movieId|rating|               title|              genres|
+------+-------+------+--------------------+--------------------+
|    63|      1|     5|      ToyStory(1995)|Adventure|Animati...|
|    63|     16|     5|        Casino(1995)|         Crime|Drama|
|    63|    260|     5|StarWars:EpisodeI...|Action|Adventure|...|
|    63|    318|     5|ShawshankRedempti...|         Crime|Drama|
|    63|    592|     5|        Batman(1989)|Action|Crime|Thri...|
|    63|   1193|     5|OneFlewOvertheCuc...|               Drama|
|    63|   1198|     5|RaidersoftheLostA...|    Action|Adventure|
|    63|   1214|     5|         Alien(1979)|       Horror|Sci-Fi|
|    63|   1221|     5|Godfather:PartIIT...|         Crime|Drama|
|    63|   1259|     5|     StandbyMe(1986)|     Adventure|Drama|
|    63|   1356|     5|StarTrek:FirstCon...|Action|Adventure|...|
|    63|   1639|     5|    ChasingAmy(1997)|Comedy|Drama|Romance|
|    63|   2797|     5|           Big(1988)|Comedy|Drama|Fant...|
|    63|   2858|     5|AmericanBeauty(1999)|       Drama|Romance|
|    63|   2918|     5|FerrisBueller'sDa...|              Comedy|
|    63|   3114|     5|     ToyStory2(1999)|Adventure|Animati...|
|    63|   3176|     5|TalentedMr.Ripley...|Drama|Mystery|Thr...|
|    63|   3481|     5|  HighFidelity(2000)|Comedy|Drama|Romance|
|    63|   3578|     5|     Gladiator(2000)|Action|Adventure|...|
|    63|   4306|     5|         Shrek(2001)|Adventure|Animati...|
+------+-------+------+--------------------+--------------------+
only showing top 20 rows

User 63's Recommendations:
+------+-------+----------+--------------------+--------------------+
|userId|movieId|prediction|               title|              genres|
+------+-------+----------+--------------------+--------------------+
|    63|  92210| 4.8674645|DisappearanceofHa...|Adventure|Animati...|
|    63| 110873| 4.8674645|CentenarianWhoCli...|Adventure|Comedy|...|
|    63|   9010| 4.8588977|LoveMeIfYouDare(J...|       Drama|Romance|
|    63| 108583|  4.836118|FawltyTowers(1975...|              Comedy|
|    63|   8530| 4.8189244|   DearFrankie(2004)|       Drama|Romance|
|    63|  83318|  4.813581|       GoatThe(1921)|              Comedy|
|    63|  83411|  4.813581|          Cops(1922)|              Comedy|
|    63|  65037| 4.7906556|          BenX(2007)|               Drama|
|    63|  54328|  4.688013|MyBestFriend(Monm...|              Comedy|
|    63|   3437|  4.678849|     CoolasIce(1991)|               Drama|
|    63|   2924|  4.675808|DrunkenMaster(Jui...|       Action|Comedy|
|    63|   1196| 4.6633716|StarWars:EpisodeV...|Action|Adventure|...|
|    63|  27156| 4.6382804|NeonGenesisEvange...|Action|Animation|...|
|    63|  26865| 4.6308517|FistofLegend(Jing...|        Action|Drama|
|    63|   5244| 4.6302986|ShogunAssassin(1980)|    Action|Adventure|
|    63|  93320| 4.6302986|TrailerParkBoys(1...|        Comedy|Crime|
|    63|  50641| 4.6302986|  House(Hausu)(1977)|Comedy|Fantasy|Ho...|
|    63|   6598|  4.624031|StepIntoLiquid(2002)|         Documentary|
|    63|   7502| 4.6232696|BandofBrothers(2001)|    Action|Drama|War|
|    63|  73344|  4.609774|ProphetA(UnProphÃ...|         Crime|Drama|
+------+-------+----------+--------------------+--------------------+
'''