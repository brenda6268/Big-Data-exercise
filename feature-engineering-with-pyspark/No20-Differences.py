#Differences
'''
Let's explore generating features using existing ones. In the midwest of the U.S. many single family homes have extra land around them for green space. In this example you will create a new feature called 'YARD_SIZE', and then see if the new feature is correlated with our outcome variable.

Instructions
100 XP
Create a new column using withColumn() called LOT_SIZE_SQFT and convert ACRES to square feet by multiplying by acres_to_sqfeet the conversion factor.
Create another new column called YARD_SIZE by subtracting FOUNDATIONSIZE from LOT_SIZE_SQFT.
Run corr() on each of the independent variables YARD_SIZE, FOUNDATIONSIZE, LOT_SIZE_SQFT against the dependent variable SALESCLOSEPRICE. Does new feature show a stronger correlation than either of its components?
'''

# Code

# Lot size in square feet
acres_to_sqfeet = 43560
df = df.withColumn('LOT_SIZE_SQFT', df['ACRES'] * acres_to_sqfeet)

# Create new column YARD_SIZE
df = df.withColumn('YARD_SIZE', df['LOT_SIZE_SQFT'] - df['FOUNDATIONSIZE'])

# Corr of ACRES vs SALESCLOSEPRICE
print("Corr of ACRES vs SALESCLOSEPRICE: " + str(df.corr('SALESCLOSEPRICE', 'ACRES')))
# Corr of FOUNDATIONSIZE vs SALESCLOSEPRICE
print("Corr of FOUNDATIONSIZE vs SALESCLOSEPRICE: " + str(df.corr('SALESCLOSEPRICE', 'FOUNDATIONSIZE')))
# Corr of YARD_SIZE vs SALESCLOSEPRICE
print("Corr of YARD_SIZE vs SALESCLOSEPRICE: " + str(df.corr('SALESCLOSEPRICE', 'YARD_SIZE')))

'''result
<script.py> output:
    Corr of ACRES vs SALESCLOSEPRICE: 0.2206061258893533
    Corr of FOUNDATIONSIZE vs SALESCLOSEPRICE: 0.6152231695664402
    Corr of YARD_SIZE vs SALESCLOSEPRICE: 0.20714585430854268
note:Not all generated features are worthwhile, many are not but 
its still worth doing! Most likely this is because there isn't a 
lot of variation in lot sizes in the neighborhoods we are looking 
at to create a strong feature. In addition if we look at our data,
some of the homes have 0 ACRES if we really wanted to handle
 this correctly we could have to set the minimum YARD_SIZE to 0.

'''