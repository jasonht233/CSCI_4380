import psycopg2
import psycopg2.extras



if __name__ == '__main__' :
    connection_string = "host= 'localhost' dbname='resort' user='resort' password='resort'"

    conn = psycopg2.connect(connection_string,cursor_factory=psycopg2.extras.DictCursor )


    ###this part is to drop the existed tables and the data we have already loaded, and reloaded
   
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS fish')
    cursor.execute('DROP TABLE IF EXISTS liquor')
    cursor.execute('DROP TABLE IF EXISTS historic_Places')
    cursor.execute('DROP TABLE IF EXISTS Fishing_and_River')
    cursor.execute('DROP TABLE IF EXISTS outdoor_recreation')
    conn.commit()
