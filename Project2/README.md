# Project 2 - Bangkok Housing Price

data scraped from https://www.ddproperty.com/en/ 

# Files
- `train.json` - the training set **WITH** target value `price`
- `test.json` - the test set **WITHOUT** target value `price`
- `bangkok_district.csv` - supplemental data
- `sample_submission.csv` - a sample submission file in the correct format
- `sample_code.ipynb` - a sample code of EDA and Modelling
- `validate.py` - to check whether your submission file is written in the correct form or not 

# Data Dictionary

> `train.json`

- you can open this data with the method `pd.read_json("train.json")`
- 14,271 records x 23 columns

|column|data type|description|
|---|---|---|
|`id`|int|ID of selling item|
|`province`|string|province name: this dataset only includes **Bangkok**,**Samut Prakan** and **Nonthaburi** |
|`district`|string|district name|
|`subdistrict`|string|subdtistrict name|
|`address`|string|address e.g. street name, area name, soi number|
|`property_type`|string|type of the house: **Condo**, **Townhouse** or **Detached House**|
|`total_units`|float|the number of rooms/houses that the condo/village has|
|`bedrooms`|int|the number of bedrooms|
|`baths`|int|the number of baths|
|`floor_area`|float|total area of inside floor [㎡]|
|`floor_level`|int|floor level of the room |
|`land_area`|float|total area of the land [㎡]|
|`latitude`|float|latitude of the house|
|`longitude`|float|longitude of the house|
|`nearby_stations`|int|the number of nearby stations (within 1km)|
|`nearby_station_distance`|list|list of (station name, distance[m]). Each station name consists of **station ID**, **station name**, and **Line** such as *"E4 Asok BTS"*|
|`nearby_bus_stops`|int|the number of nearby bus stops|
|`nearby_supermarkets`|int|the number of nearby supermarkets|
|`nearby_shops`|int|the number of nearby shops|
|`year_built`|int|year built|
|`month_built`|string|month built: January-December|
|`price`|float|**[TARGET VALUE]** selling price|

> `test.json`

- 2,500 records x 22 columns

> `bangkok_district.csv`

- 331 rows, 6 columns
- you can use this file to join with main table and to check whether (sub)district names are correct or not

|column|data type|description|
|---|---|---|
|`province`|string|province name (only 4 province around Bangkok)|
|`province_th`|string|province name in Thai|
|`district`|string|district name (เขต / อำเภอ)|
|`district_th`|string|district name in Thai|
|`subdistrict`|string|subdistrict name (แขวง / ตำบล)|
|`subdistrict_th`|string|subdistrict name in Thai|
