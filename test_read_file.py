import csv
import psycopg2
import psycopg2.extras



if __name__ == '__main__' :
    connection_string = "host= 'localhost' dbname='resort' user='resort' password='resort'"

    conn = psycopg2.connect(connection_string,cursor_factory=psycopg2.extras.DictCursor )


    ###this part is to drop the existed tables and the data we have already loaded, and reloaded
    with open('schema.sql','r') as setup:
        cursor = conn.cursor()
        setup_queries = setup.read()
        cursor.execute(setup_queries)
        conn.commit()
    ############################################################################################

    with open('data/Accessible_Outdoor_Recreation_Destinations.csv') as csv_file:
        # Region,County,Name,Feature,Description,Primitive Setting,Tent Site,Lean-to,Picnic Tables,Privy,Trails,Equestrian,Scenic Overlook,Interpretive Materials,Wildlife Viewing Platform,Hunting Blind,Fishing Pier,Boat Launch,Loading Dock,Hand Launch,Beach,Flush Toilet,Shower,URL,Data_Type,Land_Unit,Facility,Status,Setlmt,Inspected,Inspected By,Date Inspected,Pass Inspection,Accessible,Notes,Directions,KMLNOTES,POINT_X,POINT_Y,Location
        #   0   ,  1   , 2  , 3      ,4         ,5                , 6       ,7      ,8            , 9   , 10   , 11       , 12            , 13                   ,14                       , 15          , 16         , 17        , 18         , 19        , 20  ,21          ,22    ,23 , 24      , 25      , 26     , 27   , 28   ,29       ,30          , 31           , 32            ,33        , 34  , 35       , 36     ,37     , 38    ,39
        csv_reader = csv.reader(csv_file, delimiter = ',')
        line_count = 0

        for row_o in csv_reader:

            if line_count == 0 :
                line_count+=1
                continue

            line_count+= 1
            cursor = conn.cursor()

            row = list(row_o)

            for cnt in range(0, len(row) ):
                index = row[cnt].find("'")
                if index != -1:
                    row[cnt] = row[cnt][:index]+"\\"+row[cnt][:index]

            if row[4] != '' and row[35] != '' :
                insert = "INSERT INTO outdoor_recreation VALUES (%d,'%s', '%s', '%s' ,'%s', %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, '%s',%f,%f);"%(line_count,row[1],row[2],row[3],row[4],  row[5]=='Y',row[6]=='Y',row[8]=='Y',row[9]=='Y',row[10]=='Y',row[11]=='Y',row[12]=='Y',row[15]=='Y',row[16]=='Y',row[20]=='Y',row[21]=='Y',row[22]=='Y', row[35],float(row[37]) ,float(row[38]) )
            if row[4] == '':
                insert = "INSERT INTO outdoor_recreation VALUES (%d,'%s', '%s', '%s','%s', %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, '%s',%f,%f);"%(line_count,row[1],row[2],row[3],row[4],  row[5]=='Y',row[6]=='Y',row[8]=='Y',row[9]=='Y',row[10]=='Y',row[11]=='Y',row[12]=='Y',row[15]=='Y',row[16]=='Y',row[20]=='Y',row[21]=='Y',row[22]=='Y', row[35],float(row[37]) ,float(row[38]) )
            if row[35] =='':
                insert = "INSERT INTO outdoor_recreation VALUES (%d,'%s','%s', '%s','%s', %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, '%s',%f,%f);"%(line_count,row[1],row[2],row[3],row[4],  row[5]=='Y',row[6]=='Y',row[8]=='Y',row[9]=='Y',row[10]=='Y',row[11]=='Y',row[12]=='Y',row[15]=='Y',row[16]=='Y',row[20]=='Y',row[21]=='Y',row[22]=='Y', row[35],float(row[37]) ,float(row[38]) )
            if row[4]=='' and row[35] =='' :
                insert = "INSERT INTO outdoor_recreation VALUES (%d,'%s', '%s', '%s','%s', %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, '%s',%f,%f);"%(line_count,row[1],row[2],row[3],row[4],  row[5]=='Y',row[6]=='Y',row[8]=='Y',row[9]=='Y',row[10]=='Y',row[11]=='Y',row[12]=='Y',row[15]=='Y',row[16]=='Y',row[20]=='Y',row[21]=='Y',row[22]=='Y', row[35],float(row[37]) ,float(row[38]) )

            cursor.execute(insert)

            conn.commit()

# about national historic places##################################################################################################################################################################################################################################################################################################################################################
    with open('data/National_Register_of_Historic_Places.csv') as csv_file:
        # Region,County,Name,Feature,Description,Primitive Setting,Tent Site,Lean-to,Picnic Tables,Privy,Trails,Equestrian,Scenic Overlook,Interpretive Materials,Wildlife Viewing Platform,Hunting Blind,Fishing Pier,Boat Launch,Loading Dock,Hand Launch,Beach,Flush Toilet,Shower,URL,Data_Type,Land_Unit,Facility,Status,Setlmt,Inspected,Inspected By,Date Inspected,Pass Inspection,Accessible,Notes,Directions,KMLNOTES,POINT_X,POINT_Y,Location
        #   0   ,  1   , 2  , 3      ,4         ,5                , 6       ,7      ,8            , 9   , 10   , 11       , 12            , 13                   ,14                       , 15          , 16         , 17        , 18         , 19        , 20  ,21          ,22    ,23 , 24      , 25      , 26     , 27   , 28   ,29       ,30          , 31           , 32            ,33        , 34  , 35       , 36     ,37     , 38    ,39
        csv_reader = csv.reader(csv_file, delimiter = ',')
        line_count = 0

        for row_o in csv_reader:

            if line_count == 0 :
                line_count+=1
                continue

            line_count+= 1
            cursor = conn.cursor()

            row = list(row_o)

            for cnt in range(0, len(row) ):
                index = row[cnt].find("'")
                if index != -1:
                    row[cnt] = row[cnt][:index]+"\\"+row[cnt][:index]

            insert = "INSERT INTO historic_places VALUES (%d,'%s', '%s',%f,%f);"%(line_count-1,row[0],row[1],float(row[-3]),float(row[-2]) )
            cursor.execute(insert)
            conn.commit()














# ###########################################################################################################################################################################
