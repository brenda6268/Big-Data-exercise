#Imputing Missing Data
'''
Missing data happens. If we make the assumption that our data is missing completely at random, we are making the assumption that what data we do have, is a good representation of the population. If we have a few values we could remove them or we could use the mean or median as a replacement. In this exercise, we will look at 'PDOM': Days on Market at Current Price.

Instructions
100 XP
Get a count of the missing values in the column 'PDOM' using where(), isNull() and count().
Calculate the mean value of 'PDOM' using the aggregate function mean().
Use fillna() with the value set to the 'PDOM' mean value and only apply it to the column 'PDOM' using the subset parameter.
'''

# Code
# Count missing rows
missing = df.where(df['PDOM'].isNull()).count()

# Calculate the mean value
col_mean = df.agg({'PDOM': 'mean'}).collect()[0][0]

# Replacing with the mean value for that column
df.fillna(col_mean, subset=['PDOM'])

'''result
DataFrame[NO: int, STREETADDRESS: string, POSTALCODE: int, STATEORPROVINCE: string, CITY: string, SALESCLOSEPRICE: int, LISTDATE: string, LISTPRICE: int, LISTTYPE: string, ORIGINALLISTPRICE: int, PRICEPERTSFT: double, FOUNDATIONSIZE: int, FENCE: string, SCHOOLDISTRICTNUMBER: string, DAYSONMARKET: int, OFFMKTDATE: string, FIREPLACES: int, ROOMTYPE: string, ROOF: string, POTENTIALSHORTSALE: string, POOLDESCRIPTION: string, PDOM: int, GARAGEDESCRIPTION: string, SQFTABOVEGROUND: int, TAXES: int, TAXWITHASSESSMENTS: double, TAXYEAR: int, LIVINGAREA: int, UNITNUMBER: string, YEARBUILT: int, ZONING: string, STYLE: string, ACRES: double, COOLINGDESCRIPTION: string, APPLIANCES: string, BACKONMARKETDATE: string, EXTERIOR: string, DININGROOMDESCRIPTION: string, BASEMENT: string, BATHSFULL: int, BATHSHALF: int, BATHQUARTER: int, BATHSTHREEQUARTER: int, CLASS: string, BATHSTOTAL: int, BATHDESC: string, BEDROOMS: int, SQFTBELOWGROUND: int, ASSUMABLEMORTGAGE: string, ASSOCIATIONFEE: int, ASSESSMENTPENDING: string, ASSESSEDVALUATION: double]

'''