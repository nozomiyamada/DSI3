# Project 2 - Bangkok Housing Price

data scraped from https://www.ddproperty.com/en/ 
## Data Dictionary

> `Bangkok_Housing_Price_train.json`

- 22,316 records

|**column**|**data type**|**description**|
|:-:|:-:|:-:|
|id|int|ID of selling item|
|province|string|province name: this dataset only includes **Bangkok**,**Samut Prakan** and **Nonthaburi** |
|district|string|district name|
|subdistrict|string|subdtistrict name|
|address|string|address e.g. Street name|
|property_type|string|type of the house: **Condo**, **Townhouse** or **Detached House**|
|total_units|float|the humber of rooms/houses that the condo/village has|
|bedrooms|int|the number of bedrooms|
|baths|int|the number of baths|
|floor_area|float|total area of inside floor [㎡]|
|floor_level|int|floor level of the room |
|land_area|float|total area of the land [㎡]|
|latitude|float|latitude of the house|
|longitude|float|longitude of the house|
|nearby_stations|int|the number of nearby stations (within 1km)|
|nearby_station_distance|list|list of (station name, distance[m]). Each station name consists of **station ID**, **station name**, and **Line** such as *"E4 Asok BTS"*|
|nearby_bus_stops|int|the number of nearby bus stops|
|nearby_supermarkets|int|the number of nearby supermarkets|
|nearby_shops|int|the number of nearby shops|
|year_built|int|year built|
|month_built|string|month built: January-December|
|price|float|**[TARGET VALUE]** selling price|

> `bangkok_district.csv`

- 331 rows
- in order to join with main table and to check whether (sub)district name is correct or not

|column|data type|description|
|:-:|:-:|:-:|
|province|string|province name (only 4 province around Bangkok)|
|district|string|district name (เขต / อำเภอ)|
|subdistrict|string|subdistrict name (แขวง / ตำบล)|

