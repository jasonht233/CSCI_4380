   Recommended Fishing Rivers And Streams (River_data)
    https://data.ny.gov/Recreation/Recommended-Fishing-Rivers-And-Streams/jcxg-7gnm

    Accessible Outdoor Recreation Destinations
    https://data.ny.gov/Recreation/Accessible-Outdoor-Recreation-Destinations/pt2v-9a3h

    Liquor Authority Quarterly List of Active linceses

    https://data.ny.gov/Economic-Development/Liquor-Authority-Quarterly-List-of-Active-Licenses/hrvs-fxs2


    National Register of Historic Places
    https://data.ny.gov/Recreation/National-Register-of-Historic-Places/iisn-hnyv

    Sprint Trout 
    https://data.ny.gov/Recreation/Current-Season-Spring-Trout-Stocking-Data-Lens/bexs-funz

for our load_data:
    1. For our data, we at first have the check whether the data is setup or not (including the number of tables and the number of rows in one table).
    2. We need use the schema.sql to set up the table and schema(include in the python code)
    3. Then it would load Five files separately.

for our main.py:
    In our main.py, it would run the load_data.py first.
    Then it would have the location setting up. [our core information to connect the user and data set]


General interface:
    #just a infinite loop to continue

    menu:
        at first, we would ask the user to write the location
        
        then get into the manu:
            1. Historic , outdoor, liquor, outdoor-fishing, fishing, find-trout: find out the closest place to your location 

                for the historic , outdoor , liquor fishing. They are all about the calculation between users and one table. 

                for outdoor-fishing and find-trout. We are setting join two different tables together to give us one general answer based on the two data set. 


            2. A B function 
            A B  is in the list[historic , outdoor , liquor ]
                For the this function which is different for the last one. It can take two interested places which the user pick and use the sql to combine these two places and give the ans or suggestion to user to recommand the great way to enjoy their day. 


commands:

Set up the data and operate our application(don't need to run the load_data.py ):

>>> python3 main.py 

Choose to locate your location or Not 

>>> Y
    ^ which would set the location for your current location 
>>> N
    ^ you can set up by yourselves 

>>> Quit 
    ^ quit the application 


memebers:

    Bohan Wu (wub4)
    Haotian Zhang (zhangh20)
    Ruoyan Wu(wur7）
    Shenjin Li (lis17)
    
                  
                
