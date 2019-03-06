#Verifying DataTypes
'''
In the age of data we have access to more attributes than we ever had before. To handle all of them we will build a lot of automation but at a minimum requires that their datatypes be correct. In this exercise we will validate a dictionary of attributes and their datatypes to see if they are correct. This dictionary is stored in the variable validation_dict and is available in your workspace.

Instructions
100 XP
Using df create a list of attribute and datatype tuples with dtypes called actual_dtypes_list.
Iterate through actual_dtypes_list, checking if the column names exist in the dictionary of expected dtypes validation_dict.
For the keys that exist in the dictionary, check their dtypes and print those that match.
'''

#Code
# create list of actual dtypes to check
actual_dtypes_list = df.dtypes
print(actual_dtypes_list)

# Iterate through the list of actual dtypes tuples
for attribute_tuple in actual_dtypes_list:
  
  # Check if column name is dictionary of expected dtypes
  col_name = attribute_tuple[0]
  if col_name in validation_dict:

    # Compare attribute types
    col_type = attribute_tuple[1]
    if col_type == validation_dict[col_name]:
      print(col_name + ' has expected dtype.')


'''result
[('No.', 'bigint'), ('MLSID', 'string'), ('StreetNumberNumeric', 'bigint'), ('streetaddress', 'string'), ('STREETNAME', 'string'), ('PostalCode', 'bigint'), ('StateOrProvince', 'string'), ('City', 'string'), ('SalesClosePrice', 'bigint'), ('LISTDATE', 'string'), ('LISTPRICE', 'bigint'), ('LISTTYPE', 'string'), ('OriginalListPrice', 'bigint'), ('PricePerTSFT', 'double'), ('FOUNDATIONSIZE', 'bigint'), ('FENCE', 'string'), ('MapLetter', 'string'), ('LotSizeDimensions', 'string'), ('SchoolDistrictNumber', 'string'), ('DAYSONMARKET', 'bigint'), ('offmarketdate', 'string'), ('Fireplaces', 'bigint'), ('RoomArea4', 'string'), ('roomtype', 'string'), ('ROOF', 'string'), ('RoomFloor4', 'string'), ('PotentialShortSale', 'string'), ('PoolDescription', 'string'), ('PDOM', 'bigint'), ('GarageDescription', 'string'), ('SQFTABOVEGROUND', 'bigint'), ('Taxes', 'bigint'), ('RoomFloor1', 'string'), ('RoomArea1', 'string'), ('TAXWITHASSESSMENTS', 'double'), ('TAXYEAR', 'bigint'), ('LivingArea', 'bigint'), ('UNITNUMBER', 'string'), ('YEARBUILT', 'bigint'), ('ZONING', 'string'), ('STYLE', 'string'), ('ACRES', 'double'), ('CoolingDescription', 'string'), ('APPLIANCES', 'string'), ('backonmarketdate', 'double'), ('ROOMFAMILYCHAR', 'string'), ('RoomArea3', 'string'), ('EXTERIOR', 'string'), ('RoomFloor3', 'string'), ('RoomFloor2', 'string'), ('RoomArea2', 'string'), ('DiningRoomDescription', 'string'), ('BASEMENT', 'string'), ('BathsFull', 'bigint'), ('BathsHalf', 'bigint'), ('BATHQUARTER', 'bigint'), ('BATHSTHREEQUARTER', 'double'), ('Class', 'string'), ('BATHSTOTAL', 'bigint'), ('BATHDESC', 'string'), ('RoomArea5', 'string'), ('RoomFloor5', 'string'), ('RoomArea6', 'string'), ('RoomFloor6', 'string'), ('RoomArea7', 'string'), ('RoomFloor7', 'string'), ('RoomArea8', 'string'), ('RoomFloor8', 'string'), ('Bedrooms', 'bigint'), ('SQFTBELOWGROUND', 'bigint'), ('AssumableMortgage', 'string'), ('AssociationFee', 'bigint'), ('ASSESSMENTPENDING', 'string'), ('AssessedValuation', 'double')]
SQFTBELOWGROUND has expected dtype.
AssumableMortgage has expected dtype.
AssociationFee has expected dtype.
ASSESSMENTPENDING has expected dtype.
AssessedValuation has expected dtype.


'''